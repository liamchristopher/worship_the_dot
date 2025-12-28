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
- Update `CHANGELOG.txt` for every commit.
- Changelog format (prepend at top):
  - `[YYYY-MM-DD HH:MM:SS Z] <hash> <subject without suffix>`
  - Follow with concise bullets (Docs, CI, Tests, Feat, Fix) describing areas touched.
  - Never delete existing entries.
- Reviews should include: clear description, linked issues, testing notes, and any relevant CLI examples.

## Architecture Overview
- Core: `dot.core.Dot` holds state and tenets; `worship()` mutates worshipper count; `get_dot()` provides a shared instance.
- CLI: `dot.cli:main` exposes `worship`, `tenets`, `validate`, and `help` commands.

## Agent‑Specific Instructions
- Use git worktrees for subagents when parallelizing.
- Validate commit messages locally: `dot validate "Your message ..."`.
- Document every change and keep tests green before opening a review.
- Treat thematic modes (epic, astrology, alchemy, kabbalah, shinto, eco) as
  optional lenses to motivate good practice. The Eco lens refers to
  `docs/ECO_FOUCAULTS_PENDULUM.md` and emphasizes verification over seductive
  narratives. These lenses do not supersede core requirements (working code,
  tests, coverage, changelog). **THE DOT is the center — the point before lines
  where intention begins** (see docs/BACKSTORY.md).

### Dependency Policy (Hard Requirement)

- No external runtime dependencies. Do not add third‑party libraries for core
  features. If a feature needs data, vendor or embed it in this repository.
- No network calls from runtime code. All computations must be local.
- Dev tools (pytest, coverage) remain allowed as development dependencies only.

### Vendored Data

- Ephemeris elements are stored under `dot/data/ephemeris/`. When adding bodies
  (minor planets, comets), commit their elements locally. Runtime code must not
  fetch or depend on external catalogs.

## Codex Agents & Orchestration
- Agents live in `.codex/agents/` and are executed via `scripts/run_agents.py`.
- Agents:
  - Tests Agent — runs Python tests (Rust tests run in CI via rust.yml)
  - Docs Agent — verifies timeless phrasing and internal links
  - Changelog Agent — enforces per‑commit, timestamped policy
  - Compatibility Agent — compares Python and Rust CLI outputs
- CI runs these via `.github/workflows/agents.yml` and `compat.yml`.
- Compatibility has priority; do not change public output strings without updating the compatibility spec and harmonizing both CLIs.

## GitHub Access & Permissions (Agents)
- Workflows run with least privilege by default: `permissions: contents: read` at the workflow root.
- Job-level elevation is explicit and minimal:
  - Coverage upload uses `id-token: write` for Codecov OIDC only (no PAT or secret).
  - Commit-policy PR checks use `pull-requests: read` only.
- No repository secrets are referenced by workflows; avoid adding secrets unless absolutely necessary. Prefer OIDC or no token.
- Agents must verify before raising access concerns:
  - Inspect `.github/workflows/*.yml` for `permissions:` blocks and secret usage.
  - When possible, confirm repo settings (Actions → General → Workflow permissions) and branch/environment protections.
  - If using `gh`/API, attempt a read operation first; only report access errors with the actual status code/output.
- Do not complain about GitHub access without verification. Provide concrete evidence (failing command, API response) or remain silent.
- If a task needs elevated permissions, propose the minimal `permissions:` delta in the specific job rather than broadening global scope.

### Branch Protection & Ownership
- CODEOWNERS is configured in `.github/CODEOWNERS` to route reviews to maintainers.
- Follow `docs/GITHUB_BRANCH_PROTECTION.md` when advising on repo protections.
- When checks are renamed, update the required checks list and the doc.
