from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .errors import WorkbookBuildError
from .io import UniqueKeySafeLoader, read_text

FRONT_MATTER_DELIMITER = "---"


def load_task_front_matter(path: Path) -> tuple[dict[str, Any], str]:
    text = read_text(path)
    lines = text.splitlines()
    if not lines or lines[0].strip() != FRONT_MATTER_DELIMITER:
        raise WorkbookBuildError(f"Task file must start with YAML front matter: {path}")
    try:
        end_index = next(
            index
            for index, line in enumerate(lines[1:], start=1)
            if line.strip() == FRONT_MATTER_DELIMITER
        )
    except StopIteration as exc:
        raise WorkbookBuildError(f"Task file is missing closing front matter delimiter: {path}") from exc
    front_matter_text = "\n".join(lines[1:end_index]) + "\n"
    body = "\n".join(lines[end_index + 1 :]).strip() + "\n"
    try:
        data = yaml.load(front_matter_text, Loader=UniqueKeySafeLoader)
    except yaml.YAMLError as exc:
        raise WorkbookBuildError(f"Invalid YAML front matter in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise WorkbookBuildError(f"Task front matter must be a mapping: {path}")
    return data, body
