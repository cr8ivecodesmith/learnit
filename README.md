LearnIt
===

Project scaffolding with a simple CLI, tests, linting/formatting, and MkDocs documentation.

## Requirements
- Python 3.11+
- uv (https://github.com/astral-sh/uv)

## Quick Start (uv)
```bash
# Create and activate a virtualenv
uv venv --python 3.11
source .venv/bin/activate

# Install project + dev dependencies
uv sync --dev

# Sanity checks
ruff check .
black --check .
pytest -n auto -q

# Run the CLI
learnit --version
```

Tip: You can also run without activating the venv using `uv run <cmd>`.

## Development Workflow
- Lint: `ruff check .`
- Format (write changes): `black .`
- Tests: `pytest -n auto`
- Install in editable mode: `uv pip install -e '.[dev]'`

## Documentation
- Serve locally: `mkdocs serve` (http://127.0.0.1:8000/)
- Build static site: `mkdocs build`

MkDocs uses the Material theme with plugins: `autorefs`, `mkdocstrings`, and `git-revision-date-localized`.

## Packaging / Build
- Build wheel + sdist: `uv build`
- Artifacts output to `dist/`

PEP 621 metadata lives in `pyproject.toml` and the build backend is `hatchling` (no setup.py needed).

## Continuous Integration
GitHub Actions workflow (`.github/workflows/ci.yml`) installs with uv, then runs ruff, black (check mode), and pytest in parallel.
