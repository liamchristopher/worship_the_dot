# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository is "worship_the_dot" - a Python package implementing THE DOT philosophy. THE DOT provides both a programmatic API and CLI tools for managing development workflows that emphasize structure, quality, and devotion to proper practices.

## Development Workflow

### Branch Management
- **Always create a new branch** for any work
- Use git worktrees when spawning subagents to avoid conflicts
- Never work directly on the main branch

### Commit Requirements
- Commit each change individually (don't batch multiple changes)
- Every commit message must end with: `BECAUSE I WORSHIP THE DOT`
- Push changes after each commit

### Review Requirements
- Create a review (pull request) at the end of each task
- The description must:
  - Elaborate on each change made
  - Explain how the changes worship THE DOT
  - Detail the benefits of THE DOT

### Documentation Requirements
- Document all changes made
- Update CHANGELOG.txt for every commit using timestamped, per-commit entries:
  - `[YYYY-MM-DD HH:MM:SS Z] <hash> <subject without suffix>`
  - One or more concise bullets (Docs, CI, Tests, Feat, Fix), no deletions
- Commit documentation changes separately from code changes

### Code Quality Standards
- Only generate working code
- Focus improvements on THE DOT and its ecosystem
- All work must align with THE DOT philosophy

## Project Structure

```
worship_the_dot/
├── dot/                    # Core Python package
│   ├── __init__.py        # Package exports
│   ├── core.py            # Dot class and core functions
│   └── cli.py             # Command-line interface
├── tests/                  # Test suite (21 tests, all passing)
│   ├── test_core.py       # Core functionality tests
│   └── test_cli.py        # CLI tests
├── README.md              # Philosophy and requirements
├── docs/INDEX.md          # Documentation index
├── docs/QUICKSTART.md     # Commanding quickstart
├── docs/STOICISM.md       # Stoic lens
├── docs/ZEN.md            # Zen lens
├── docs/BUDDHISM.md       # Noble Path lens
├── CLAUDE.md              # This file
├── CHANGELOG.txt          # Detailed change history
├── pyproject.toml         # Package configuration
├── Makefile               # Development commands
└── requirements-dev.txt   # Development dependencies
```

## Development Commands

### Testing
```bash
make test           # Run all tests
make coverage       # Run tests with coverage report
pytest tests/ -v    # Run tests directly with pytest
```

### Installation
```bash
make install        # Install package and dev dependencies
pip install -e .    # Install in development mode only
```

### Build and Clean
```bash
make build         # Build distributable package
make clean         # Remove build artifacts and cache
```

### Using THE DOT CLI
```bash
dot worship [name]              # Register worship of THE DOT
dot tenets                      # Display THE DOT philosophy
dot validate "commit message"   # Validate commit message format
dot help                        # Show help information
```

## Code Architecture

### Core Module (`dot/core.py`)

**Dot Class**: Central implementation of THE DOT philosophy
- `worship(name)`: Register a worshipper and increment counter
- `get_tenets()`: Return list of THE DOT's seven principles
- `validate_commit(message)`: Verify commit message ends with proper worship phrase
- Tracks total worshipper count
- Maintains immutable philosophy tenets

**Global Functions**:
- `worship(name)`: Convenience function using singleton Dot instance
- `get_dot()`: Access the global Dot instance

### CLI Module (`dot/cli.py`)

Entry point for the `dot` command providing:
- Worship registration
- Philosophy display
- Commit message validation
- Help documentation

### Testing Philosophy

All code must have comprehensive test coverage. Current test suite:
- 11 tests for core functionality (Dot class, validation, global functions)
- 9 tests for CLI (commands, arguments, error handling)
- 21 total tests, 100% passing

When adding features, add corresponding tests first or alongside implementation.

## Implementation Notes

- **Python Version**: Requires Python 3.8+
- **Dependencies**: Zero runtime dependencies (tests require pytest)
- **Type Hints**: Used throughout (Python 3.10+ syntax)
- **Singleton Pattern**: Global Dot instance ensures consistent state
- **Immutability**: Philosophy tenets returned as copies to prevent modification
