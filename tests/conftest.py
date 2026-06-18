from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from workbook_builder.build import BuildPaths, BuildResult, build_project


@pytest.fixture(scope="session")
def project_root() -> Path:
    return ROOT


@pytest.fixture(scope="session")
def built_result(tmp_path_factory: pytest.TempPathFactory) -> BuildResult:
    output = tmp_path_factory.mktemp("workbook-build") / "dist"
    return build_project(BuildPaths(ROOT, output), single_file=True)
