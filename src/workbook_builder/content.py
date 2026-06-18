from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup
from jinja2 import Environment
from markdown_it import MarkdownIt
from markupsafe import Markup

from .errors import ContentContractError
from .io import read_text, sha256_bytes


@dataclass(frozen=True)
class RenderedUnit:
    id: str
    html: Markup
    source_path: Path
    source_sha256: str


def create_markdown_parser(*, allow_html: bool) -> MarkdownIt:
    parser = MarkdownIt(
        "commonmark",
        {
            "html": allow_html,
            "linkify": False,
            "typographer": False,
            "breaks": False,
        },
    )
    parser.enable("table")
    return parser


def _assert_no_raw_html_tokens(parser: MarkdownIt, source: str, unit_id: str) -> None:
    for token in parser.parse(source):
        if token.type in {"html_block", "html_inline"}:
            raise ContentContractError(f"Raw HTML is forbidden in Markdown unit {unit_id}.")
        if token.children:
            for child in token.children:
                if child.type in {"html_block", "html_inline"}:
                    raise ContentContractError(f"Raw HTML is forbidden in Markdown unit {unit_id}.")


def _validate_trusted_html(rendered: str, unit: dict[str, Any]) -> None:
    soup = BeautifulSoup(rendered, "html.parser")
    roots = [node for node in soup.contents if getattr(node, "name", None)]
    if len(roots) != 1:
        raise ContentContractError(f"Trusted HTML unit {unit['id']} must contain exactly one root element.")
    root = roots[0]
    if root.name != unit["tag"]:
        raise ContentContractError(
            f"Trusted HTML unit {unit['id']} root tag is {root.name!r}; expected {unit['tag']!r}."
        )
    if root.get("id") != unit["id"]:
        raise ContentContractError(
            f"Trusted HTML unit ID mismatch: source={root.get('id')!r}, manifest={unit['id']!r}."
        )
    source_classes = set(root.get("class", []))
    expected_classes = set(unit["classes"])
    if source_classes != expected_classes:
        raise ContentContractError(
            f"Trusted HTML class mismatch for {unit['id']}: source={sorted(source_classes)}, "
            f"manifest={sorted(expected_classes)}."
        )


def render_unit(unit: dict[str, Any], content_root: Path, environment: Environment) -> RenderedUnit:
    source_path = (content_root / unit["source"]).resolve()
    content_root_resolved = content_root.resolve()
    if content_root_resolved not in source_path.parents:
        raise ContentContractError(f"Unit source escapes content root: {unit['source']}")
    if not source_path.is_file():
        raise ContentContractError(f"Missing unit source: {source_path}")
    source = read_text(source_path)
    source_hash = sha256_bytes(source.encode("utf-8"))

    if unit["format"] == "trusted_html":
        if not unit["allow_raw_html"]:
            raise ContentContractError(f"trusted_html requires allow_raw_html=true: {unit['id']}")
        parser = create_markdown_parser(allow_html=True)
        rendered = parser.render(source).strip()
        _validate_trusted_html(rendered, unit)
        html = Markup(rendered + "\n")
    elif unit["format"] == "markdown":
        if unit["allow_raw_html"]:
            raise ContentContractError(f"markdown requires allow_raw_html=false: {unit['id']}")
        parser = create_markdown_parser(allow_html=False)
        _assert_no_raw_html_tokens(parser, source, unit["id"])
        body_html = Markup(parser.render(source).strip())
        template = environment.get_template("partials/unit.html.j2")
        html = Markup(template.render(unit=unit, unit_body=body_html, body_html=body_html).strip() + "\n")
    else:
        raise ContentContractError(f"Unsupported unit format for {unit['id']}: {unit['format']}")

    # Guard against accidental Jinja syntax leaking from content into the output.
    if re.search(r"{{|{%|{#", str(html)):
        raise ContentContractError(f"Unresolved template syntax detected in unit {unit['id']}.")
    return RenderedUnit(unit["id"], html, source_path, source_hash)
