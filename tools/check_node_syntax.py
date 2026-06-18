from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
js = ROOT / "dist" / "course" / "assets" / "js" / "workbook.js"
if not js.is_file():
    print("Build first: python build.py", file=sys.stderr)
    raise SystemExit(2)
raise SystemExit(subprocess.run(["node", "--check", str(js)], check=False).returncode)
