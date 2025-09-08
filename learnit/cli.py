from __future__ import annotations

import argparse
import sys
from importlib import metadata


def _package_version() -> str:
    try:
        return metadata.version("learnit")
    except metadata.PackageNotFoundError:
        return "0.0.0+local"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="learnit", description="LearnIt command-line interface")
    parser.add_argument("--version", action="store_true", help="Show version and exit")

    args = parser.parse_args(argv)

    if args.version:
        print(_package_version())
        return 0

    # Default behavior: print a friendly message and hint.
    print("LearnIt CLI — use --version to see the version.")
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())

