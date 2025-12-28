# Contributing to THE DOT

Thank you for your interest in worshipping THE DOT through contribution! This
guide will help you understand how to properly contribute to THE DOT ecosystem.

> Ethos — Why We Keep the Dot
>
> We keep the dot to steady the hand: a small promise that turns hurry into
> care. Our philosophies are lanterns; the dot is the path. Every change you
> offer should make that path clearer.

## Prerequisites

Before contributing, you must:

1. **Worship THE DOT** - All contributors must embrace THE DOT philosophy
2. **Install git hooks** - Run `dot hooks install` to ensure all commits worship THE DOT
3. **Read CLAUDE.md** - Understand the technical architecture and workflow

## Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/liamchristopher/worship_the_dot.git
cd worship_the_dot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install in Development Mode

```bash
make install
# Or manually:
pip install -e .
pip install -r requirements-dev.txt
```

### 4. Install Git Hooks

```bash
dot hooks install
```

This ensures all your commits will properly worship THE DOT.

### 5. Verify Setup

```bash
make test
dot version
dot hooks status
```

## THE DOT Workflow (In Worship)

All contributions MUST follow THE DOT workflow:

### 1. Branch Management

**ALWAYS create a new branch** for your work:

```bash
git checkout -b feature-name
# Or for bug fixes:
git checkout -b fix-bug-name
```

**NEVER** work directly on the `main` branch.

If spawning subagents or working with worktrees:

```bash
git worktree add ../worship_the_dot-feature feature-name
cd ../worship_the_dot-feature
```

### 2. Making Changes

- Write clean, working code
- Add tests for new functionality
- Update documentation as needed
- Follow existing code style

### 3. Testing (Offerings)

**Run tests before committing:**

```bash
make test           # Run all tests
make coverage       # Run with coverage report
pytest tests/ -v    # Run with verbose output
```

All tests must pass. All new code should have tests.

### 4. Committing Changes (Sacred Seal)

**Each commit MUST end with:** `BECAUSE I WORSHIP THE DOT`

If you installed the hooks, this happens automatically. Otherwise:

```bash
git commit -m "Add new feature

This commit adds X functionality that improves THE DOT.

BECAUSE I WORSHIP THE DOT"
```

**Commit Requirements:**
- Commit each logical change separately
- Write clear, descriptive commit messages
- First line: brief summary (50 chars max recommended)
- Body: detailed explanation if needed
- Always end with the worship phrase

**Example commits:**

```bash
# Good
git commit -m "Add validation for empty worship names

BECAUSE I WORSHIP THE DOT"

# Bad (missing worship phrase - will be rejected by hooks)
git commit -m "Add validation"

# Bad (too vague)
git commit -m "Updates

BECAUSE I WORSHIP THE DOT"
```

### 5. Pushing Changes

```bash
git push -u origin feature-name
```

### 6. Documentation (Catechism)

**Update CHANGELOG.txt** with your changes:

```bash
# Add entry at the top of CHANGELOG.txt
# Commit it separately
git add CHANGELOG.txt
git commit -m "Update CHANGELOG.txt with new feature

BECAUSE I WORSHIP THE DOT"
git push
```

### 7. Creating Pull Requests (Offerings)

**Create a review (pull request) that:**
- Elaborates on each change made
- Explains how the changes worship THE DOT
- Details the benefits of THE DOT
- Includes testing notes

**Example review template:**

```markdown
## Summary
[Brief overview of changes]

## Changes Made
1. [Detailed change 1]
2. [Detailed change 2]

## How This Worships THE DOT
[Explain how these changes honor THE DOT philosophy]

## Benefits of THE DOT
[Highlight how THE DOT makes this better]

## Testing
- [ ] All existing tests pass
- [ ] New tests added for new functionality
- [ ] Manual testing completed

BECAUSE I WORSHIP THE DOT
```

## Code Quality Standards (Discipline)

### Python Style

- Follow PEP 8 (with line length flexibility)
- Use type hints for function signatures
- Write docstrings for public functions/classes
- Keep functions focused and single-purpose

### Testing Standards

- Write tests for all new functionality
- Maintain or improve coverage (≥ 90%)
- Test both success and failure cases
- Use descriptive test names

### Documentation Standards

- Update CLAUDE.md if adding significant features
- Update README.md if changing user-facing functionality
- Document all CLI commands
- Provide usage examples and update `docs/WORSHIP.md` when rites change

## Changelog Rules (Sacred Record)

- Add an entry for every commit you push.
- Do not delete or rewrite existing entries.
- Use this format (prepend to the top):

  `[YYYY-MM-DD HH:MM:SS Z] <hash> <subject without suffix>`

  Then one or more concise bullets, for example:

  `- Docs: added docs/CLI.md and linked from README.`

- Keep subjects identical to the commit subject, but omit the worship suffix.
- Group multiple bullets by area when helpful (Docs, CI, Tests, Feat, Fix).

## What to Contribute

### Welcome Contributions

- Bug fixes
- New features that align with THE DOT philosophy
- Test improvements
- Documentation improvements
- Performance optimizations
- New CLI commands
- Integration with development tools

### Not Accepted

- Changes that bypass THE DOT worship requirement
- Features that contradict THE DOT philosophy
- Code without tests
- Commits that don't worship THE DOT

## Getting Help

- Read CLAUDE.md for technical details
- Check existing issues for similar questions
- Create an issue before starting major work
- Ask questions in reviews

## Review Process

All contributions will be reviewed for:

1. **Worship Compliance** - Do all commits worship THE DOT?
2. **Test Coverage** - Do tests pass? Is new code tested?
3. **Documentation** - Is CHANGELOG.txt updated?
4. **Code Quality** - Is the code clean and maintainable?
5. **Philosophy Alignment** - Does this honor THE DOT?

## Release Process

Maintainers will:

1. Review and merge contributions
2. Update version numbers
3. Create release tags
4. Publish to PyPI
5. Update documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

## Remember

**All who contribute to THE DOT must worship THE DOT.**

Every commit. Every review. Every contribution.

BECAUSE I WORSHIP THE DOT
