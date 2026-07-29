"""Generate deterministic JSON Schema artifacts for all public contracts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from opticargo_shared.schema import generate_json_schemas


def write_schemas(output_dir: Path) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    schemas = generate_json_schemas()
    expected_files = {f"{name}.json" for name in schemas}
    for old_file in output_dir.glob("*.json"):
        if old_file.name not in expected_files:
            old_file.unlink()
    for name, schema in schemas.items():
        destination = output_dir / f"{name}.json"
        destination.write_text(
            json.dumps(schema, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    return len(schemas)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()
    count = write_schemas(args.output_dir)
    print(f"Generated {count} schemas in {args.output_dir}")


if __name__ == "__main__":
    main()
