from __future__ import annotations

import argparse
import fnmatch
import json
import os
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath


def safe_extract(archive: zipfile.ZipFile, destination: Path) -> None:
    for member in archive.infolist():
        relative = PurePosixPath(member.filename)
        if relative.is_absolute() or ".." in relative.parts:
            raise SystemExit(f"Unsafe ZIP member: {member.filename}")
        target = destination.joinpath(*relative.parts).resolve()
        if destination.resolve() not in target.parents and target != destination.resolve():
            raise SystemExit(f"ZIP member escapes destination: {member.filename}")
        if member.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(archive.read(member))


def find_repo_root(extracted: Path) -> Path:
    candidates = [path.parent for path in extracted.rglob("AGENTS.md")]
    candidates = [path for path in candidates if (path / "llm" / "model-contract.yaml").is_file()]
    if len(candidates) != 1:
        raise SystemExit(f"Expected exactly one repository root; found {len(candidates)}")
    return candidates[0]


def hash_file(path: Path) -> str:
    import hashlib

    return hashlib.sha256(path.read_bytes()).hexdigest()


def matches_any(path: str, patterns: list[str]) -> bool:
    normalized = path.replace("\\", "/")
    return any(fnmatch.fnmatchcase(normalized, pattern) for pattern in patterns)


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify a complete repository ZIP returned by an LLM")
    parser.add_argument("zip_path")
    parser.add_argument("--browser", action="store_true", help="Run Chromium smoke tests too")
    parser.add_argument("--skip-checks", action="store_true", help="Only inspect package structure and scope")
    parser.add_argument(
        "--allow-unchanged-report",
        action="store_true",
        help="Testing only: do not require llm/RETURN_REPORT.md to change",
    )
    args = parser.parse_args()

    zip_path = Path(args.zip_path).resolve()
    if not zip_path.is_file():
        raise SystemExit(f"Missing ZIP: {zip_path}")

    with tempfile.TemporaryDirectory(prefix="workbook-return-") as temporary:
        extracted = Path(temporary)
        with zipfile.ZipFile(zip_path) as archive:
            safe_extract(archive, extracted)
        root = find_repo_root(extracted)
        manifest_path = root / "HANDOFF_MANIFEST.json"
        if not manifest_path.is_file():
            raise SystemExit("Returned package is missing HANDOFF_MANIFEST.json from the original handoff.")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

        # Compute the returned file set before importing project modules; imports may
        # create __pycache__ files that are not part of the returned package.
        original = {entry["path"]: entry["sha256"] for entry in manifest["files"]}
        current = {
            path.relative_to(root).as_posix(): hash_file(path)
            for path in root.rglob("*")
            if path.is_file() and path.name != "HANDOFF_MANIFEST.json"
        }

        sys.path.insert(0, str(root / "src"))
        from workbook_builder.task import load_task_front_matter
        from workbook_builder.io import load_yaml
        from workbook_builder.schemas import validate_instance

        contract = load_yaml(root / "llm" / "model-contract.yaml")
        validate_instance(contract, "model-contract.schema.json", root / "schemas")
        task, _ = load_task_front_matter(root / "llm" / "TASK.md")
        validate_instance(task, "llm-task.schema.json", root / "schemas")

        missing_required = [
            relative
            for relative in contract["return_contract"]["required_files"]
            if not (root / relative).is_file()
        ]
        if missing_required:
            raise SystemExit(f"Missing required returned files: {missing_required}")
        changed = sorted(path for path in original.keys() & current.keys() if original[path] != current[path])
        deleted = sorted(original.keys() - current.keys())
        added = sorted(current.keys() - original.keys())

        changed_paths = sorted(set(changed + deleted + added))
        allowed_patterns = list(task["allowed_paths"])
        allowed_patterns.extend(["llm/RETURN_REPORT.md", "CHANGELOG_FA.md"])
        protected_patterns = [entry["path"] for entry in contract["protected_by_default"]]
        protected_exceptions = list(task["protected_path_exceptions"])
        generated_patterns = list(contract["generated_paths"])

        out_of_scope = sorted(
            path for path in changed_paths if not matches_any(path, allowed_patterns)
        )
        protected_violations = sorted(
            path
            for path in changed_paths
            if matches_any(path, protected_patterns)
            and not matches_any(path, protected_exceptions)
        )
        generated_violations = sorted(
            path for path in current if matches_any(path, generated_patterns)
        )

        print("CHANGED:")
        for path in changed:
            print(f"  M {path}")
        for path in added:
            print(f"  A {path}")
        for path in deleted:
            print(f"  D {path}")

        if out_of_scope:
            print("OUT_OF_SCOPE:")
            for path in out_of_scope:
                print(f"  ! {path}")
        if protected_violations:
            print("PROTECTED_WITHOUT_EXCEPTION:")
            for path in protected_violations:
                print(f"  ! {path}")
        if generated_violations:
            print("GENERATED_FILES_RETURNED:")
            for path in generated_violations:
                print(f"  ! {path}")
        if (
            "llm/RETURN_REPORT.md" not in changed
            and not args.allow_unchanged_report
        ):
            print("RETURN_REPORT_NOT_UPDATED: llm/RETURN_REPORT.md")
            return 4
        if out_of_scope or protected_violations or generated_violations:
            return 3

        if not args.skip_checks:
            command = [sys.executable, "tools/check_all.py"]
            if args.browser:
                command.append("--browser")
            env = os.environ.copy()
            env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
            completed = subprocess.run(command, cwd=root, env=env, check=False)
            if completed.returncode != 0:
                return completed.returncode

        print("RETURNED_PACKAGE_STATUS: VALID")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
