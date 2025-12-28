.PHONY: install test coverage clean build help lint

help:
	@echo "THE DOT - Development Commands"
	@echo ""
	@echo "Available commands:"
	@echo "  make install    - Install the package in development mode"
	@echo "  make test       - Run all tests"
	@echo "  make coverage   - Run tests with coverage report"
	@echo "  make clean      - Remove build artifacts and cache files"
	@echo "  make build      - Build the package"
	@echo ""

install:
	pip install -e .
	pip install -r requirements-dev.txt

test:
	pytest -v

coverage:
	pytest --cov=dot --cov-report=term-missing --cov-report=html --cov-fail-under=90

lint:
	ruff check dot/ tests/ --select E,F,W --ignore E501 || true

.PHONY: rust-build rust-test compat agents

rust-build:
	cargo build --manifest-path rust/the-dot/Cargo.toml

rust-test:
	cargo test --manifest-path rust/the-dot/Cargo.toml

compat: rust-build
	python scripts/compat.py

agents:
	python scripts/run_agents.py

.PHONY: resolve-prs
resolve-prs:
	@echo "Resolving open PRs with GitHub API (requires GITHUB_TOKEN)"
	python scripts/resolve_prs.py

.PHONY: resolve-prs-gh
resolve-prs-gh:
	@echo "Resolving open PRs with gh (requires gh auth login)"
	python scripts/resolve_prs_gh.py

.PHONY: resolve-issues-gh
resolve-issues-gh:
	@echo "Resolving open issues with gh (requires gh auth login)"
	python scripts/resolve_issues_gh.py

.PHONY: resolve-all-gh
resolve-all-gh: resolve-prs-gh resolve-issues-gh

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build
