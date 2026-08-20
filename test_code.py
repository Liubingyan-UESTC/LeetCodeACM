#!/usr/bin/env python3
"""Run an ACM-style solution against local io/input.txt.

Usage:
    python test_code.py <file_name>

Examples:
    python test_code.py combination_sum
    python test_code.py hashmap/combination_sum
    python test_code.py longest_substr.py

Looks up <file_name>.py in ~/std/LeetCode/ (root, for backward compatibility)
or in any of its category subdirectories (hashmap/, dp/, ...), redirects stdin
from ./io/input.txt, then calls that module's main().
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


LEETCODE_DIR = Path.home() / "std" / "LeetCode"
IO_DIR = Path.cwd() / "io"
INPUT_FILE = IO_DIR / "input.txt"


# 非算法分类目录：公共模板/依赖/缓存，检索时跳过
_SKIP_DIRS = {"templates", "io", "node_modules", "__pycache__"}


def resolve_solution_path(file_name: str) -> Path:
    name = file_name[:-3] if file_name.endswith(".py") else file_name

    # 支持直接传二级目录路径，如 hashmap/combination_sum
    if "/" in name or "\\" in name:
        path = LEETCODE_DIR / f"{name}.py"
        if not path.is_file():
            raise FileNotFoundError(f"solution not found: {path}")
        return path

    # 先查根目录（向后兼容），再查各分类子目录
    candidates = []
    direct = LEETCODE_DIR / f"{name}.py"
    if direct.is_file():
        candidates.append(direct)
    for sub_dir in sorted(
        p for p in LEETCODE_DIR.iterdir()
        if p.is_dir() and not p.name.startswith(".") and p.name not in _SKIP_DIRS
    ):
        sub_file = sub_dir / f"{name}.py"
        if sub_file.is_file():
            candidates.append(sub_file)

    if len(candidates) == 1:
        return candidates[0]
    if len(candidates) > 1:
        raise FileNotFoundError(
            f"ambiguous solution name {name!r}: found in multiple directories:\n"
            + "\n".join(f"  {c}" for c in candidates)
        )
    raise FileNotFoundError(
        f"solution not found: {name}.py under {LEETCODE_DIR} or its category subdirectories"
    )


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
