from __future__ import annotations

import pathlib
import sys

try:
    import yaml
except Exception as exc:  # pragma: no cover
    print(f"YAML_IMPORT_FAILED: {exc}")
    sys.exit(2)


ROOT = pathlib.Path(__file__).resolve().parents[1]


def main() -> int:
    yaml_files = sorted(ROOT.rglob("*.yaml")) + sorted(ROOT.rglob("*.yml"))
    failures: list[str] = []

    for path in yaml_files:
        try:
            with path.open("r", encoding="utf-8") as handle:
                yaml.safe_load(handle)
        except Exception as exc:
            failures.append(f"{path.relative_to(ROOT)} :: {exc}")

    if failures:
        print("YAML_CHECK_FAILED")
        for failure in failures:
            print(failure)
        return 1

    print(f"YAML_CHECK_OK files={len(yaml_files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
