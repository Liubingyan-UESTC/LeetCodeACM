#!/usr/bin/env python3
"""Run an ACM-style solution against local io/input.txt.

Usage:
    python test_code.py <file_name>

Example:
    python test_code.py combination_sum

Looks up ~/std/LeetCode/<file_name>.py, redirects stdin from ./io/input.txt,
then calls that module's main().
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


LEETCODE_DIR = Path.home() / "std" / "LeetCode"
IO_DIR = Path.cwd() / "io"
INPUT_FILE = IO_DIR / "input.txt"


def resolve_solution_path(file_name: str) -> Path:
    name = file_name[:-3] if file_name.endswith(".py") else file_name
    path = LEETCODE_DIR / f"{name}.py"
    if not path.is_file():
        raise FileNotFoundError(f"solution not found: {path}")
    return path


def load_module(path: Path):
    module_name = f"leetcode_solution_{path.stem}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load module from {path}")
    module = importlib.util.module_from_spec(spec)
    # Ensure the module sees redirected stdin when it binds
    # `input = sys.stdin.readline` at import time.
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    if len(sys.argv) != 2:
        print(
            "Usage: python test_code.py <file_name>\n"
            "Example: python test_code.py combination_sum",
            file=sys.stderr,
        )
        return 1

    solution_path = resolve_solution_path(sys.argv[1])
    if not INPUT_FILE.is_file():
        raise FileNotFoundError(f"input file not found: {INPUT_FILE}")

    with INPUT_FILE.open("r", encoding="utf-8") as f:
        sys.stdin = f
        module = load_module(solution_path)
        if not hasattr(module, "main") or not callable(module.main):
            raise AttributeError(f"{solution_path.name} must define callable main()")
        module.main()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, ImportError, AttributeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
