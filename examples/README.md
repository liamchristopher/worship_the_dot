# THE DOT Examples

This directory contains example scripts demonstrating how to use THE DOT in various scenarios.

## Examples

### 1. Basic Usage (`basic_usage.py`)

Demonstrates fundamental THE DOT functionality:
- Worshipping THE DOT with the global function
- Creating and using Dot instances
- Accessing philosophy tenets
- Validating commit messages
- Integration patterns

**Run:**
```bash
python examples/basic_usage.py
```

**Expected Output:**
```
=============================================================
THE DOT v0.2.0 - Basic Usage Example
=============================================================

Example 1: Worship THE DOT
-------------------------------------------------------------
Python Developer now worships THE DOT (Total worshippers: 1)

Example 2: Working with Dot instance
-------------------------------------------------------------
Initial worshippers: 0
Alice now worships THE DOT (Total worshippers: 1)
Bob now worships THE DOT (Total worshippers: 2)
Charlie now worships THE DOT (Total worshippers: 3)
Total worshippers: 3
...
```

### 2. CI/CD Integration (`ci_integration.py`)

Shows how to integrate THE DOT into your CI/CD pipeline:
- Fetching commits from git
- Batch validation of commits
- Exit codes for CI systems
- Error reporting

**Run:**
```bash
python examples/ci_integration.py
```

**Use in CI:**
```yaml
# .github/workflows/validate.yml
- name: Validate commits
  run: python examples/ci_integration.py
```

### 3. Pre-commit Hook (`pre_commit_hook.py`)

Example pre-commit framework integration:
- Hook configuration
- Message validation
- User feedback
- Installation instructions

**Setup:**
```bash
# Add to .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: dot-validate
        name: Validate commit message
        entry: python examples/pre_commit_hook.py
        language: python
        stages: [commit-msg]
```

### 4. Worktree Manager (`worktree_manager.py`)

Utility for managing git worktrees for subagents:
- Create worktrees for parallel work
- List active worktrees
- Clean up completed worktrees
- Prevent conflicts

**Run:**
```bash
python examples/worktree_manager.py create feature-name
python examples/worktree_manager.py list
python examples/worktree_manager.py remove feature-name
```

## Integration Patterns

### In Your Application

```python
from dot import worship, Dot

# Register your application
worship("MyApp v1.0")

# Validate user-provided commit messages
dot = Dot()
if not dot.validate_commit(user_message):
    print("Error: Commit message must worship THE DOT")
```

### In Test Suites

```python
from dot import Dot

def test_commit_message_format():
    dot = Dot()
    message = "Fix bug BECAUSE I WORSHIP THE DOT"
    assert dot.validate_commit(message)
```

### In Git Hooks

```bash
#!/bin/bash
# .git/hooks/commit-msg

# Use THE DOT CLI for validation
if ! dot validate "$(cat $1)"; then
    echo "Commit message must worship THE DOT"
    exit 1
fi
```

## Requirements

All examples require THE DOT to be installed:

```bash
pip install the-dot
# Or from source:
pip install -e .
```

## Contributing Examples

Have a useful integration pattern? Contribute it!

1. Create a new Python file in `examples/`
2. Add documentation and usage instructions
3. Update this README
4. Open a review (pull request)

Remember: All commits must end with "BECAUSE I WORSHIP THE DOT"

## Philosophy

These examples demonstrate THE DOT's philosophy in practice:
- **Quality**: Validated, tested, documented examples
- **Consistency**: Uniform patterns across all examples
- **Mindfulness**: Each example teaches a specific concept
- **Transparency**: Clear, commented, understandable code

BECAUSE I WORSHIP THE DOT
