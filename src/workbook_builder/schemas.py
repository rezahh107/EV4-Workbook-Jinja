from __future__ import annotations

from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

from .errors import SchemaValidationError
from .io import load_json


def _format_path(parts: list[object]) -> str:
    if not parts:
        return "$"
    out = "$"
    for part in parts:
        if isinstance(part, int):
            out += f"[{part}]"
        else:
            out += f".{part}"
    return out


def load_schema_registry(schema_dir: Path) -> tuple[dict[str, dict[str, Any]], Registry[Any]]:
    schemas: dict[str, dict[str, Any]] = {}
    resources: list[tuple[str, Resource[Any]]] = []
    for path in sorted(schema_dir.glob("*.schema.json"), key=lambda p: p.name):
        schema = load_json(path)
        Draft202012Validator.check_schema(schema)
        schema_id = schema.get("$id")
        if not isinstance(schema_id, str) or not schema_id:
            raise SchemaValidationError(f"Schema is missing $id: {path}")
        schemas[path.name] = schema
        resources.append((schema_id, Resource.from_contents(schema)))
    return schemas, Registry().with_resources(resources)


def validate_instance(instance: Any, schema_name: str, schema_dir: Path) -> None:
    schemas, registry = load_schema_registry(schema_dir)
    try:
        schema = schemas[schema_name]
    except KeyError as exc:
        raise SchemaValidationError(f"Unknown schema: {schema_name}") from exc
    validator = Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(instance), key=lambda e: (list(e.absolute_path), e.message))
    if errors:
        lines = [f"{_format_path(list(error.absolute_path))}: {error.message}" for error in errors]
        raise SchemaValidationError("Schema validation failed:\n" + "\n".join(lines))
