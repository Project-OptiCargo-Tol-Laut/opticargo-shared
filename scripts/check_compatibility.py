"""Fail when current JSON Schemas break the v1 release baseline."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def compare_schema(old: Any, new: Any, path: str = "$") -> list[str]:
    problems: list[str] = []
    if isinstance(old, dict) and isinstance(new, dict):
        old_required = set(old.get("required", []))
        new_required = set(new.get("required", []))
        for field in sorted(new_required - old_required):
            problems.append(f"{path}: newly required field {field!r}")

        old_properties = old.get("properties", {})
        new_properties = new.get("properties", {})
        for field in sorted(set(old_properties) - set(new_properties)):
            problems.append(f"{path}: removed property {field!r}")

        for keyword in ("type", "format", "default"):
            if keyword in old and old.get(keyword) != new.get(keyword):
                problems.append(
                    f"{path}: {keyword} changed from {old.get(keyword)!r} to {new.get(keyword)!r}"
                )
        if "enum" in old and old.get("enum") != new.get("enum"):
            problems.append(f"{path}: enum values changed")

        for key, old_value in old.items():
            if key in {"required", "type", "format", "default", "enum"}:
                continue
            if key in new:
                problems.extend(compare_schema(old_value, new[key], f"{path}.{key}"))
    elif isinstance(old, list) and isinstance(new, list):
        for index, old_value in enumerate(old):
            if index < len(new):
                problems.extend(compare_schema(old_value, new[index], f"{path}[{index}]"))
    return problems


def compare_directories(baseline: Path, current: Path) -> list[str]:
    problems: list[str] = []
    current_names = {path.name for path in current.glob("*.json")}
    for baseline_file in sorted(baseline.glob("*.json")):
        if baseline_file.name not in current_names:
            problems.append(f"removed model schema: {baseline_file.name}")
            continue
        old = json.loads(baseline_file.read_text(encoding="utf-8"))
        new = json.loads((current / baseline_file.name).read_text(encoding="utf-8"))
        for detail in compare_schema(old, new):
            problems.append(f"{baseline_file.name}: {detail}")
    return problems


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("baseline", type=Path)
    parser.add_argument("current", type=Path)
    args = parser.parse_args()
    problems = compare_directories(args.baseline, args.current)
    if problems:
        print("Breaking contract changes detected:")
        for problem in problems:
            print(f"- {problem}")
        raise SystemExit(1)
    print("No breaking contract changes detected")


if __name__ == "__main__":
    main()
