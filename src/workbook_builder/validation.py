from __future__ import annotations

from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from .errors import ContentContractError
from .io import load_json, sha256_file


def validate_manifest_contract(course: dict[str, Any], project_root: Path) -> None:
    ids: set[str] = set()
    sources: set[str] = set()
    for index, unit in enumerate(course["units"]):
        unit_id = unit["id"]
        if unit_id in ids:
            raise ContentContractError(f"Duplicate unit id at index {index}: {unit_id}")
        ids.add(unit_id)
        source = unit["source"]
        if source in sources:
            raise ContentContractError(f"Duplicate unit source at index {index}: {source}")
        sources.add(source)
        source_path = project_root / "content" / source
        if not source_path.is_file():
            raise ContentContractError(f"Missing content source: {source_path}")

    for static_dir in course["static_directories"]:
        path = project_root / "static" / static_dir
        if not path.is_dir():
            raise ContentContractError(f"Missing static directory: {path}")

    template_path = project_root / "templates" / course["template"]
    if not template_path.is_file():
        raise ContentContractError(f"Missing base template: {template_path}")


def validate_generated_html(index_path: Path, baseline_path: Path | None = None) -> dict[str, Any]:
    soup = BeautifulSoup(index_path.read_text(encoding="utf-8"), "html.parser")
    all_ids = [tag.get("id") for tag in soup.find_all(attrs={"id": True})]
    duplicate_ids = sorted({value for value in all_ids if all_ids.count(value) > 1})
    if duplicate_ids:
        raise ContentContractError(f"Duplicate HTML ids: {duplicate_ids}")

    id_set = set(all_ids)
    missing_fragments: list[str] = []
    for anchor in soup.select('a[href^="#"]'):
        fragment = anchor.get("href", "")[1:]
        if fragment and fragment not in id_set:
            missing_fragments.append(fragment)
    if missing_fragments:
        raise ContentContractError(f"Broken internal anchors: {sorted(set(missing_fragments))}")

    external_runtime_assets: list[str] = []
    for tag, attr in [("script", "src"), ("img", "src"), ("source", "src"), ("video", "src"), ("audio", "src")]:
        for element in soup.find_all(tag):
            value = element.get(attr)
            if value and urlparse(value).scheme in {"http", "https"}:
                external_runtime_assets.append(value)
    for link in soup.find_all("link"):
        rel = {str(x).lower() for x in link.get("rel", [])}
        value = link.get("href")
        if value and rel.intersection({"stylesheet", "preload", "modulepreload"}) and urlparse(value).scheme in {"http", "https"}:
            external_runtime_assets.append(value)
    if external_runtime_assets:
        raise ContentContractError(f"External runtime assets are forbidden: {external_runtime_assets}")

    report = {
        "unit_ids": [element.get("id") for element in soup.select("main#main-content > article[id], main#main-content > section[id]")],
        "counts": {
            "top_level_units": len(soup.select("main#main-content > article, main#main-content > section")),
            "lessons": len(soup.select("main#main-content > .lesson")),
            "stations": len(soup.select("main#main-content > .station")),
            "details": len(soup.select("main#main-content details")),
            "persist_controls": len(soup.select("main#main-content [data-persist]")),
            "step_through_v2": len(soup.select("main#main-content [data-step-through-v2]")),
        },
        "sha256": sha256_file(index_path),
    }

    if baseline_path is not None:
        baseline = load_json(baseline_path)
        actual_legacy_ids = [value for value in report["unit_ids"] if value != "appendix-v32-generator-release-note"]
        if actual_legacy_ids != baseline["unit_ids"]:
            raise ContentContractError("Legacy top-level unit order does not match the v31 parity baseline.")
        expected = baseline["counts"]
        for key in ["lessons", "stations", "details", "persist_controls", "step_through_v2"]:
            if report["counts"][key] != expected[key]:
                raise ContentContractError(
                    f"Parity count mismatch for {key}: actual={report['counts'][key]}, expected={expected[key]}"
                )
    return report
