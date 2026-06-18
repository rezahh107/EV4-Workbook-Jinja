from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .build import BuildPaths, build_project
from .errors import WorkbookBuildError
from .io import load_yaml
from .task import load_task_front_matter
from .schemas import validate_instance
from .validation import validate_manifest_contract
from .zipper import create_deterministic_zip


def _project_root(value: str | None) -> Path:
    return Path(value).resolve() if value else Path.cwd().resolve()


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Deterministic Elementor workbook generator")
    parser.add_argument("--project-root", help="Project root; defaults to current directory")
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser("build", help="Validate and build folder and single-file artifacts")
    build.add_argument("--output", default="dist", help="Output directory relative to project root")
    build.add_argument("--no-single-file", action="store_true", help="Skip the portable single-file artifact")
    build.add_argument("--no-clean", action="store_true", help="Do not remove the prior output directory")

    subparsers.add_parser("validate", help="Validate YAML/JSON schemas and source contracts")

    package = subparsers.add_parser("package", help="Build and create a deterministic ZIP")
    package.add_argument("--output", default="dist", help="Build output directory relative to project root")
    package.add_argument("--zip", default="release/Elementor_V4_Workbook_v32_0_generator.zip", help="ZIP path relative to project root")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = create_parser()
    args = parser.parse_args(argv)
    root = _project_root(args.project_root)
    try:
        if args.command == "validate":
            course = load_yaml(root / "content" / "course.yaml")
            validate_instance(course, "course.schema.json", root / "schemas")
            validate_manifest_contract(course, root)
            model_contract = load_yaml(root / "llm" / "model-contract.yaml")
            validate_instance(model_contract, "model-contract.schema.json", root / "schemas")
            task, _ = load_task_front_matter(root / "llm" / "TASK.md")
            validate_instance(task, "llm-task.schema.json", root / "schemas")
            print(
                f"VALID: {len(course['units'])} content units; "
                f"LLM task status={task['task_status']}"
            )
            return 0
        if args.command == "build":
            result = build_project(
                BuildPaths(root, root / args.output),
                clean=not args.no_clean,
                single_file=not args.no_single_file,
            )
            print(f"BUILT: {result.index_path}")
            if result.single_file_path:
                print(f"SINGLE_FILE: {result.single_file_path}")
            print(f"REPORT: {result.report_path}")
            return 0
        if args.command == "package":
            build_project(BuildPaths(root, root / args.output), clean=True, single_file=True)
            zip_path = root / args.zip
            digest = create_deterministic_zip(root / args.output, zip_path, archive_root="Elementor_V4_Workbook_v32_0")
            print(f"PACKAGED: {zip_path}")
            print(f"SHA256: {digest}")
            return 0
    except WorkbookBuildError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
