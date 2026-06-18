from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str], *, env: dict[str, str] | None = None) -> None:
    printable = " ".join(command)
    print(f"\n$ {printable}", flush=True)
    completed = subprocess.run(command, cwd=ROOT, env=env, check=False)
    if completed.returncode != 0:
        raise SystemExit(completed.returncode)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run all deterministic workbook checks")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--browser", action="store_true", help="Include Chromium smoke tests")
    group.add_argument("--browser-only", action="store_true", help="Run only Chromium smoke tests")
    args = parser.parse_args()

    env = os.environ.copy()
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"

    if args.browser_only:
        run([sys.executable, "-m", "pytest", "-q", "-m", "browser"], env=env)
        return 0

    run([sys.executable, "validate.py"])
    run([sys.executable, "build.py"])
    run([sys.executable, "-m", "compileall", "-q", "src", "tools", "tests"])
    run([sys.executable, "-m", "pytest", "-q", "-m", "not browser"], env=env)

    node = shutil.which("node")
    if node:
        run([sys.executable, "tools/check_node_syntax.py"])
    else:
        print("SKIP: Node.js is not installed; JavaScript syntax check was not run.")

    if args.browser:
        run([sys.executable, "-m", "pytest", "-q", "-m", "browser"], env=env)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
