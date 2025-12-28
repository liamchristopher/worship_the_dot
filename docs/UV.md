UV Quickstart

- Install uv:
  curl -LsSf https://astral.sh/uv/install.sh | sh

- Install project (editable) + dev deps:
  uv pip install -e .
  uv pip install -r requirements-dev.txt

- Run tests:
  uv run pytest -v
  uv run pytest --cov=dot --cov-report=term-missing --cov-fail-under=90

- Run CLI via uv:
  uv run dot help
  uv run dot demo
  uv run dot init
  uv run dot validate "Message BECAUSE I WORSHIP THE DOT"

- Lint via uvx:
  uvx ruff check dot/ tests/ --select E,F,W --ignore E501

Notes
- CI uses astral-sh/setup-uv in all Python jobs.
- Makefile targets (install/test/coverage/lint) are uv-backed.
