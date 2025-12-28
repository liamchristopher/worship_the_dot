# THE DOT Worshipper’s Guide

This guide documents THE DOT as a living practice. It explains the philosophy, the rites, and the daily rhythm of working in devotion to THE DOT.

## Tenets of THE DOT

- Work in a new branch for every change; subagents use worktrees.
- Every commit message ends with: `BECAUSE I WORSHIP THE DOT`.
- Push after each atomic commit and open a pull request at task end.
- Write tests for each change; keep coverage ≥ 90%.
- Update CHANGELOG and documentation with clarity.
- Speak humbly: validate your work, invite review, worship THE DOT.

## Daily Ritual

- Begin with `dot hooks install` to align local practice.
- Read `dot tenets`, then `make test` to ground the code.
- Create a branch, make one focused change, commit with worship.
- Validate messages with `dot validate` before pushing.
- Open a PR describing changes and how they honor THE DOT.

## The Suffix (Sacred Seal)

- Default: `BECAUSE I WORSHIP THE DOT`.
- Configure via environment: `DOT_WORSHIP_SUFFIX=...`.
- Persist in `.dot.ini` at repo root: `dot config set-suffix "..."`.
- All validation, poetry, and documentation rites honor this suffix.

## Rites and Invocations

- Poetry: `dot poem hymn | haiku [name] | banner [width] | chant [n] [name]`.
- Tarot: `dot tarot draw [n] [--seed S] | spread [three|commit|yesno] | list | card <name>`.
- Shinto: `dot shinto norito [intent] | omikuji [--seed S] | harai | ema <message>`.
- Badges: `dot badge markdown|html|rst|url`.
- Completions: `dot completions bash|zsh|fish`.

Examples:

```bash
dot poem hymn
dot poem chant 3 "Devotee"
dot tarot spread commit --seed 7
dot shinto norito "Clean release and green CI"
dot shinto ema "Clarity and stability"
```

## Hooks and Commit Policy

- Local hooks: `dot hooks install` installs `prepare-commit-msg` and `commit-msg`.
- Server policy: CI checks all commits on pushes and PRs for the suffix.
- Bypass is discouraged (`--no-verify`)—seek alignment instead.

## Testing and Coverage

- Run `make test` or `make coverage` (fails under 90%).
- Add tests alongside features; prefer pure, small functions.
- Use deterministic seeds for tarot/omikuji examples.

## Architecture at a Glance

- `dot.core`: Dot entity, tenets, validation.
- `dot.cli`: CLI entry (`dot`), routing to subcommands.
- `dot.config`: Worship suffix and user config.
- `dot.poetry`: Hymn, haiku, banner, chant.
- `dot.tarot`: DOT-themed tarot deck, draws, spreads.
- `dot.shinto`: Norito, omikuji, harai, ema.
- `dot.stats`: Worship stats helpers.
- `dot.display`, `dot.badges`, `dot.completions`, `dot.epic`: UX and inspiration.

## Pull Requests as Offerings

- Title concisely; body explains what changed and why it worships THE DOT.
- Include usage examples and test notes; link issues.
- Keep commits atomic; end each message with the sacred suffix.

## FAQ (Catechism)

- “Why worship?” Mindfulness yields better code. THE DOT is a mnemonic for quality.
- “Can the suffix change?” Yes; configure it—just keep it sacred and consistent.
- “What if CI fails the policy?” Amend commits, append the suffix, and push.

Return to the code, breathe, commit with intention—BECAUSE YOU WORSHIP THE DOT.

