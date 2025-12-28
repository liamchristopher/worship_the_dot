# Repository Guidelines

## Project Structure & Module Organization
- `dot/`: Core package (`core.py` for logic, `cli.py` for the CLI, `__init__.py` for exports).
- `tests/`: Pytest suite (`test_*.py`, classes `Test*`, functions `test_*`).
- Tooling/metadata: `pyproject.toml`, `Makefile`, `requirements-dev.txt`, `README.md`, `CHANGELOG.txt`.

## Build, Test, and Development Commands
- `make install` — Install in editable mode and dev deps.
- `make test` — Run the full pytest suite.
- `make coverage` — Run tests with coverage (HTML in `htmlcov/`).
- `make build` — Clean and build a distribution.
- CLI examples (after install): `dot worship Alice`, `dot tenets`, `dot validate "Your message BECAUSE I WORSHIP THE DOT"`.

## Coding Style & Naming Conventions
- Python 3.8+; follow PEP 8 with 4‑space indents.
- Use type hints and docstrings for public functions/classes.
- Naming: modules and functions `snake_case`, classes `PascalCase`, constants `UPPER_SNAKE`.
- Keep functions small and focused; prefer pure functions where practical.

## Testing Guidelines
- Framework: pytest with configuration in `pyproject.toml`.
- Location and names: tests live in `tests/`, files `test_*.py`, classes `Test*`, functions `test_*`.
- Run locally: `make test`; with coverage: `make coverage`.
- Add/adjust tests with each change; aim for high coverage of new/changed code.

## Commit & Pull Request Guidelines
- Branching: create a feature branch for every task; don’t commit to `main`.
- Commit messages must end with exactly: `BECAUSE I WORSHIP THE DOT`.
- Make small, atomic commits; keep code and docs changes logically grouped.
- Update `CHANGELOG.txt` for user‑visible changes.
- PRs should include: clear description, linked issues, testing notes, and any relevant CLI examples.

## Architecture Overview
- Core: `dot.core.Dot` holds state and tenets; `worship()` mutates worshipper count; `get_dot()` provides a shared instance.
- CLI: `dot.cli:main` exposes `worship`, `tenets`, `validate`, and `help` commands.

## Agent‑Specific Instructions
- Use git worktrees for subagents when parallelizing.
- Validate commit messages locally: `dot validate "Your message ..."`.
- Document every change and keep tests green before opening a PR.
