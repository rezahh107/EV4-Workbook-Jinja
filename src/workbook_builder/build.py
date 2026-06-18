from __future__ import annotations

import base64
import mimetypes
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
from markupsafe import Markup

from .content import render_unit
from .io import load_json, load_yaml, pretty_json, sha256_file, write_text
from .schemas import validate_instance
from .validation import validate_generated_html, validate_manifest_contract


@dataclass(frozen=True)
class BuildPaths:
    project_root: Path
    output_root: Path

    @property
    def content_root(self) -> Path:
        return self.project_root / "content"

    @property
    def template_root(self) -> Path:
        return self.project_root / "templates"

    @property
    def schema_root(self) -> Path:
        return self.project_root / "schemas"

    @property
    def static_root(self) -> Path:
        return self.project_root / "static"


@dataclass(frozen=True)
class BuildResult:
    index_path: Path
    single_file_path: Path | None
    report_path: Path


def create_environment(template_root: Path) -> Environment:
    return Environment(
        loader=FileSystemLoader(str(template_root)),
        autoescape=select_autoescape(enabled_extensions=("html", "xml", "j2"), default_for_string=True),
        undefined=StrictUndefined,
        auto_reload=False,
        keep_trailing_newline=True,
        trim_blocks=False,
        lstrip_blocks=False,
    )


def _copy_tree_deterministic(source: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for path in sorted(source.rglob("*"), key=lambda p: p.as_posix()):
        relative = path.relative_to(source)
        target = destination / relative
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        elif path.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)


def _collect_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): sha256_file(path)
        for path in sorted(root.rglob("*"), key=lambda p: p.as_posix())
        if path.is_file() and path.name not in {"SHA256SUMS.txt", "build-report.json"}
    }


def _write_sha256sums(course_root: Path) -> Path:
    hashes = _collect_hashes(course_root)
    output = course_root / "SHA256SUMS.txt"
    write_text(output, "".join(f"{digest}  {name}\n" for name, digest in hashes.items()))
    return output


def _asset_data_uri(path: Path) -> str:
    mime, _ = mimetypes.guess_type(path.name)
    mime = mime or "application/octet-stream"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"


def create_single_file(index_path: Path, destination: Path) -> None:
    course_root = index_path.parent
    soup = BeautifulSoup(index_path.read_text(encoding="utf-8"), "html.parser")

    for link in list(soup.find_all("link")):
        rel = {str(x).lower() for x in link.get("rel", [])}
        href = link.get("href")
        if href == "assets/css/workbook.css" and "stylesheet" in rel:
            style = soup.new_tag("style")
            style["data-inlined-from"] = href
            style.string = (course_root / href).read_text(encoding="utf-8")
            link.replace_with(style)
        elif href == "manifest.json" and "manifest" in rel:
            link["href"] = _asset_data_uri(course_root / href)

    for script in soup.find_all("script", src=True):
        src = script.get("src")
        if src == "assets/js/workbook.js":
            script.attrs.pop("src", None)
            script.attrs.pop("defer", None)
            script["data-inlined-from"] = src
            script.string = (course_root / src).read_text(encoding="utf-8")

    for tag in soup.find_all(src=True):
        src = tag.get("src")
        if isinstance(src, str) and src.startswith("assets/"):
            tag["data-inlined-from"] = src
            tag["src"] = _asset_data_uri(course_root / src)

    write_text(destination, "<!doctype html>\n" + str(soup.html) + "\n")


def build_project(paths: BuildPaths, *, clean: bool = True, single_file: bool = True) -> BuildResult:
    project_root = paths.project_root.resolve()
    output_root = paths.output_root.resolve()
    course = load_yaml(paths.content_root / "course.yaml")
    validate_instance(course, "course.schema.json", paths.schema_root)
    validate_manifest_contract(course, project_root)

    if clean and output_root.exists():
        shutil.rmtree(output_root)
    output_root.mkdir(parents=True, exist_ok=True)

    environment = create_environment(paths.template_root)
    rendered_units = [render_unit(unit, paths.content_root, environment) for unit in course["units"]]
    template = environment.get_template(course["template"])
    html = template.render(
        course=course,
        units=[{"id": unit.id, "html": unit.html} for unit in rendered_units],
    )
    if not html.lower().startswith("<!doctype html>"):
        raise RuntimeError("Rendered document is missing the HTML doctype.")

    index_path = output_root / course["output"]
    write_text(index_path, html.strip() + "\n")
    course_root = index_path.parent

    for static_dir in course["static_directories"]:
        _copy_tree_deterministic(paths.static_root / static_dir, course_root / static_dir)

    web_manifest = load_json(paths.content_root / "data" / "web-manifest.json")
    write_text(course_root / "manifest.json", pretty_json(web_manifest))

    parity_report = validate_generated_html(
        index_path,
        paths.content_root / "data" / "parity-baseline.json",
    )

    single_path: Path | None = None
    if single_file:
        single_path = output_root / "single-file" / f"Elementor_V4_Offline_Interactive_Workbook_v{course['workbook_version'].replace('.', '_')}.html"
        create_single_file(index_path, single_path)
        validate_generated_html(single_path)

    _write_sha256sums(course_root)
    source_hashes = {
        unit.source_path.relative_to(project_root).as_posix(): unit.source_sha256
        for unit in rendered_units
    }
    output_hashes = _collect_hashes(output_root)
    report = {
        "schema_version": "1.0.0",
        "generator_version": course["generator_version"],
        "workbook_version": course["workbook_version"],
        "unit_count": len(rendered_units),
        "output_files": output_hashes,
        "source_files": dict(sorted(source_hashes.items())),
    }
    validate_instance(report, "build-report.schema.json", paths.schema_root)
    report_path = output_root / "build-report.json"
    write_text(report_path, pretty_json(report))

    # Report path itself is intentionally excluded from its own output hash set.
    return BuildResult(index_path=index_path, single_file_path=single_path, report_path=report_path)
