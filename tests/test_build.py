from __future__ import annotations

import json
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

from workbook_builder.build import BuildPaths, BuildResult, build_project
from workbook_builder.errors import DuplicateYamlKeyError
from workbook_builder.io import load_yaml, sha256_file
from workbook_builder.task import load_task_front_matter
from workbook_builder.schemas import validate_instance
from workbook_builder.validation import validate_generated_html, validate_manifest_contract

ROOT = Path(__file__).resolve().parents[1]


def test_manifest_and_schemas_are_valid() -> None:
    course = load_yaml(ROOT / "content" / "course.yaml")
    validate_instance(course, "course.schema.json", ROOT / "schemas")
    validate_manifest_contract(course, ROOT)
    assert course["schema_version"] == "1.0.0"
    assert len(course["units"]) == 82
    assert course["units"][0]["format"] == "markdown"
    assert all(unit["format"] == "trusted_html" for unit in course["units"][1:])


def test_yaml_duplicate_keys_are_rejected(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.yaml"
    path.write_text("value: 1\nvalue: 2\n", encoding="utf-8")
    with pytest.raises(DuplicateYamlKeyError):
        load_yaml(path)


def test_build_is_reproducible(tmp_path: Path, built_result: BuildResult) -> None:
    second = tmp_path / "second"
    result_b = build_project(BuildPaths(ROOT, second), single_file=True)
    assert sha256_file(built_result.index_path) == sha256_file(result_b.index_path)
    assert built_result.single_file_path is not None
    assert result_b.single_file_path is not None
    assert sha256_file(built_result.single_file_path) == sha256_file(result_b.single_file_path)


def test_generated_html_preserves_v31_contract(built_result: BuildResult) -> None:
    report = validate_generated_html(
        built_result.index_path,
        ROOT / "content" / "data" / "parity-baseline.json",
    )
    assert report["counts"]["lessons"] == 28
    assert report["counts"]["stations"] == 6
    assert report["counts"]["step_through_v2"] == 7

    soup = BeautifulSoup(built_result.index_path.read_text(encoding="utf-8"), "html.parser")
    assert soup.title is not None
    assert "v32.0" in soup.title.get_text()
    assert len(soup.select("details.lesson-disclosure.conceptual-reference")) == 28
    assert soup.select_one("#appendix-v32-generator-release-note") is not None


def test_single_file_has_no_local_runtime_asset_references(built_result: BuildResult) -> None:
    assert built_result.single_file_path is not None
    soup = BeautifulSoup(built_result.single_file_path.read_text(encoding="utf-8"), "html.parser")
    assert not soup.select('link[rel="stylesheet"][href^="assets/"]')
    assert not soup.select('script[src^="assets/"]')
    assert not soup.select('[src^="assets/"]')
    assert soup.select_one("style[data-inlined-from='assets/css/workbook.css']") is not None
    assert soup.select_one("script[data-inlined-from='assets/js/workbook.js']") is not None


def test_build_report_conforms_to_schema(built_result: BuildResult) -> None:
    report = json.loads(built_result.report_path.read_text(encoding="utf-8"))
    validate_instance(report, "build-report.schema.json", ROOT / "schemas")
    assert report["unit_count"] == 82


def test_llm_contract_and_task_are_valid() -> None:
    contract = load_yaml(ROOT / "llm" / "model-contract.yaml")
    validate_instance(contract, "model-contract.schema.json", ROOT / "schemas")
    task, body = load_task_front_matter(ROOT / "llm" / "TASK.md")
    validate_instance(task, "llm-task.schema.json", ROOT / "schemas")
    assert task["task_status"] in {"draft", "ready", "completed"}
    assert "# هدف تغییر" in body
    assert contract["return_contract"]["report_path"] == "llm/RETURN_REPORT.md"


def test_repository_governance_files_exist() -> None:
    required = [
        "AGENTS.md",
        ".editorconfig",
        ".gitattributes",
        ".github/workflows/ci.yml",
        ".github/workflows/release.yml",
        ".github/dependabot.yml",
        "tools/create_llm_handoff.py",
        "tools/verify_returned_zip.py",
        "docs/GITHUB_MAINTENANCE_FA.md",
    ]
    assert all((ROOT / relative).is_file() for relative in required)
