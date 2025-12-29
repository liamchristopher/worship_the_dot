# THE DOT — Quickstart (Commanding and Approachable)

1) Install and Initialize (users)
```bash
pip install the-dot
cd your-project
dot init      # installs hooks and writes .dot.ini if missing
```

Dev setup uses uv (fast Python tooling). See CONTRIBUTING.md for details:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
make install
```

2) Verify Your Practice
```bash
dot doctor    # checks repo, branch, hooks, and suffix
```

3) Commit with Devotion
```bash
git add -A
git commit -m "Add feature"
# Hook appends: BECAUSE I WORSHIP THE DOT
```

4) Validate and Review
```bash
dot validate "Refactor BECAUSE I WORSHIP THE DOT"
# Open a review with a short, honest explanation
```

5) Record the Change
```bash
dot changelog add "feat: add feature" -b "Docs: updated CLI usage"
```

Read next:
- Worshipper’s Guide: `docs/WORSHIP.md`
- CLI Reference: `docs/CLI.md`
- Backstory (Timeless): `docs/BACKSTORY.md`
Alt: One‑liner demo for evaluation (no install):
```bash
uvx the-dot -- dot demo
```
