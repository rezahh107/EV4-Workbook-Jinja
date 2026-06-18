from __future__ import annotations


class WorkbookBuildError(RuntimeError):
    """Base error for deterministic build failures."""


class DuplicateYamlKeyError(WorkbookBuildError):
    """Raised when YAML contains a duplicate mapping key."""


class SchemaValidationError(WorkbookBuildError):
    """Raised when content does not satisfy its versioned schema."""


class ContentContractError(WorkbookBuildError):
    """Raised when a content unit violates the build contract."""
