# THE DOT CLI Reference

This reference documents all CLI invocations as acts of worship. Each command advances the practice of disciplined, mindful development.

## Core

- `dot help` — Show help and command list.
- `dot version` — Display THE DOT version and vow reminder.
- `dot tenets` — Recite the philosophy.
- `dot worship [name]` — Register worship of THE DOT.
- `dot validate <message>` — Validate that a commit message ends with the worship suffix.

## Configuration

- `dot config show` — Show current worship suffix and its source.
- `dot config set-suffix <suffix>` — Persist a new suffix in `.dot.ini` (repo root or CWD).

## Git Hooks

- `dot hooks install` — Install `prepare-commit-msg` and `commit-msg` hooks.
- `dot hooks status` — Check whether THE DOT hooks are installed.
- `dot hooks uninstall` — Remove hooks (restores backups if present).

## Completions

- `dot completions bash|zsh|fish` — Print shell completion script.

## Badges

- `dot badge markdown|html|rst|url` — Generate worship badges.

## Stats

- `dot stats summary` — Worship summary.
- `dot stats top` — Top worshippers.
- `dot stats daily` — Last 7 days.
- `dot stats export` — JSON export.
- `dot stats clear` — Clear stats (interactive confirm).

## Poetry (Rites of Praise)

- `dot poem hymn` — Hymn ending with the worship suffix.
- `dot poem haiku [name]` — 5–7–5 devotion.
- `dot poem banner [width]` — ASCII DOT banner (odd ≥ 7).
- `dot poem chant [times] [name]` — Repeat the suffix rhythmically.

## Tarot (Rites of Guidance)

- `dot tarot list` — List DOT-themed Major Arcana.
- `dot tarot card <name>` — Show keywords and meanings.
- `dot tarot draw [n] [--seed S] [--no-reversed]` — Deterministic draws.
- `dot tarot spread three|commit|yesno [--seed S]` — Common spreads.

## Shinto (Rites of Purification and Fortune)

- `dot shinto norito [intent]` — Compose a norito prayer.
- `dot shinto omikuji [--seed S]` — Draw a fortune and counsel.
- `dot shinto harai` — Purification checklist for repositories.
- `dot shinto ema <message>` — Votive plaque sealed with the suffix.

## Garden (Practical Analogies)

- `dot garden list` — List common garden tools.
- `dot garden info|explain|tool <name>` — Purpose, tips, and DOT analogy.
- `dot garden suggest <task>` — Suggest tools by task (keyword match).

## Examples

- Validate: `dot validate "Fix bug BECAUSE I WORSHIP THE DOT"`
- Set suffix: `dot config set-suffix "BECAUSE I ADORE THE DOT"`
- Draw tarot: `dot tarot draw 3 --seed 7 --no-reversed`
- Offer norito: `dot shinto norito "Green builds and clarity"`
- Explain a tool: `dot garden info Shovel`

BECAUSE WE WORSHIP THE DOT.
