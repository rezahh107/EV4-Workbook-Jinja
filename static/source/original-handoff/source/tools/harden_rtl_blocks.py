from __future__ import annotations

from html import escape
from pathlib import Path
import re
import sys

PERSIAN_RE = re.compile(r"[\u0600-\u06FF]")
FENCE_RE = re.compile(r"(?ms)^```(?P<info>[^\n]*)\n(?P<body>.*?)^```\s*$")

OPEN = (
    '<pre class="edis-rtl-text-block" lang="fa" dir="rtl" '
    'style="display:block !important; direction:rtl !important; '
    'text-align:right !important; unicode-bidi:plaintext !important; '
    'writing-mode:horizontal-tb !important; white-space:pre-wrap !important; '
    'overflow-x:auto; tab-size:4;">'
    '<code lang="fa" dir="rtl" '
    'style="display:block !important; direction:rtl !important; '
    'text-align:right !important; unicode-bidi:plaintext !important; '
    'writing-mode:horizontal-tb !important; white-space:pre-wrap !important;">'
)
CLOSE = "</code></pre>"

def harden(text: str) -> tuple[str, int]:
    count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal count
        info = match.group("info").strip().lower()
        body = match.group("body")
        if info not in {"", "text", "plaintext", "txt"}:
            return match.group(0)
        if not PERSIAN_RE.search(body):
            return match.group(0)
        count += 1
        return f"{OPEN}\n{escape(body.rstrip(chr(10)), quote=False)}\n{CLOSE}"

    return FENCE_RE.sub(replace, text), count

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python harden_rtl_blocks.py <markdown-file>")
        return 2

    path = Path(sys.argv[1])
    original = path.read_text(encoding="utf-8")
    updated, count = harden(original)
    path.write_text(updated, encoding="utf-8")
    print(f"Converted {count} Persian text blocks in {path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
