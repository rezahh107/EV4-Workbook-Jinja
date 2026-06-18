from __future__ import annotations

import argparse
import json
import stat
import subprocess
import sys
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
from workbook_builder.task import load_task_front_matter
from workbook_builder.io import canonical_json, load_yaml, sha256_bytes, sha256_file
from workbook_builder.schemas import validate_instance
from workbook_builder.zipper import FIXED_ZIP_TIME

EXCLUDED_TOP_LEVEL = {".git", ".venv", "dist", "release", "handoff"}
EXCLUDED_DIR_NAMES = {"__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}
ARCHIVE_ROOT = "Elementor_V4_Workbook_LLM_Handoff"


def include_path(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    if relative.parts and relative.parts[0] in EXCLUDED_TOP_LEVEL:
        return False
    if any(part in EXCLUDED_DIR_NAMES for part in relative.parts):
        return False
    if path.suffix in EXCLUDED_SUFFIXES:
        return False
    return path.is_file()


def file_records() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for path in sorted(ROOT.rglob("*"), key=lambda item: item.as_posix()):
        if not include_path(path):
            continue
        relative = path.relative_to(ROOT).as_posix()
        records.append({"path": relative, "sha256": sha256_file(path), "size": path.stat().st_size})
    return records


def write_zip(output: Path, records: list[dict[str, object]], manifest_bytes: bytes) -> str:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for record in records:
            relative = str(record["path"])
            path = ROOT / PurePosixPath(relative)
            info = zipfile.ZipInfo(f"{ARCHIVE_ROOT}/{relative}", FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        info = zipfile.ZipInfo(f"{ARCHIVE_ROOT}/HANDOFF_MANIFEST.json", FIXED_ZIP_TIME)
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = (stat.S_IFREG | 0o644) << 16
        archive.writestr(info, manifest_bytes, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    digest = sha256_file(output)
    output.with_suffix(output.suffix + ".sha256").write_text(
        f"{digest}  {output.name}\n", encoding="utf-8", newline="\n"
    )
    return digest


def main() -> int:
    parser = argparse.ArgumentParser(description="Create deterministic source handoff ZIP for an LLM")
    parser.add_argument("--task", default="llm/TASK.md", help="Task file relative to repository root")
    parser.add_argument(
        "--output",
        default="handoff/Elementor_V4_Workbook_LLM_Handoff.zip",
        help="Output ZIP relative to repository root",
    )
    parser.add_argument("--skip-validation", action="store_true", help="Skip python validate.py before packaging")
    args = parser.parse_args()

    task_path = (ROOT / args.task).resolve()
    if ROOT not in task_path.parents:
        raise SystemExit("Task path escapes repository root.")
    task_data, _ = load_task_front_matter(task_path)
    validate_instance(task_data, "llm-task.schema.json", ROOT / "schemas")
    if task_data["task_status"] != "ready":
        raise SystemExit("llm/TASK.md is not ready. Set task_status: ready after completing the task.")

    contract = load_yaml(ROOT / "llm" / "model-contract.yaml")
    validate_instance(contract, "model-contract.schema.json", ROOT / "schemas")

    if not args.skip_validation:
        completed = subprocess.run([sys.executable, "validate.py"], cwd=ROOT, check=False)
        if completed.returncode != 0:
            return completed.returncode

    records = file_records()
    course = load_yaml(ROOT / "content" / "course.yaml")
    manifest = {
        "schema_version": "1.0.0",
        "archive_root": ARCHIVE_ROOT,
        "workbook_version": course["workbook_version"],
        "generator_version": course["generator_version"],
        "task_id": task_data["task_id"],
        "task_sha256": sha256_file(task_path),
        "allowed_paths": task_data["allowed_paths"],
        "protected_path_exceptions": task_data["protected_path_exceptions"],
        "file_count": len(records),
        "files": records,
        "excluded_top_level": sorted(EXCLUDED_TOP_LEVEL),
    }
    manifest_bytes = canonical_json(manifest).encode("utf-8")
    output = (ROOT / args.output).resolve()
    if ROOT not in output.parents:
        raise SystemExit("Output path escapes repository root.")
    digest = write_zip(output, records, manifest_bytes)
    print(f"HANDOFF: {output}")
    print(f"SHA256: {digest}")
    print(f"FILES: {len(records)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
