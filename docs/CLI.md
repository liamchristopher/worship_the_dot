# THE DOT CLI Reference

This reference documents all CLI invocations as acts of worship. Each command
advances the practice of disciplined, mindful development. The thematic modes
(epic, astrological, alchemical, kabbalistic, shinto) are **lenses**, not
replacements: THE DOT remains the center of the practice — the point before
lines where intention begins. For the full backstory, see docs/BACKSTORY.md.

## Core

- `dot help` — Show help and command list.
- `dot version` — Display THE DOT version and vow reminder.
- `dot tenets` — Recite the philosophy.
- `dot worship [name]` — Register worship of THE DOT.
- `dot validate <message>` — Validate that a commit message ends with the worship suffix.
- `dot demo` — Guided first-run walkthrough (init, doctor, commit, validate, wisdom).
- `dot backstory` — Print a timeless origin for THE DOT.
- `dot init` — Initialize hooks and `.dot.ini` in the current repository.
- `dot doctor` — Check repo branch, hooks, and suffix status.
- `dot changelog add <subject> [-b <bullet>]...` — Prepend a timestamped entry to CHANGELOG.

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

## Sponsorship

- `dot donate` or `dot sponsor` — Show sponsorship options for THE DOT.
  - Override or extend links via `DOT_SPONSOR_URLS` (comma-separated URLs).

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
- Demo the flow: `dot demo`

BECAUSE WE WORSHIP THE DOT.

## Astrology (Cosmic Lens)

- `dot horoscope [sign]` — Daily coding horoscope.
- `dot chart [repo-name]` — Repository birth chart (playful lens).
- `dot planets` — Planetary hours guidance.
- `dot moon` — Moon phase coding advice.
- `dot ephemeris [--no-minors] [--no-comets]` — Ephemeris summary from vendored data.

Ephemeris data and policy:
- Uses locally vendored orbital elements (J2000) stored under `dot/data/ephemeris/`.
- No network, kernels, or third‑party libraries are used at runtime.
- Planets use J2000 elements; curated minor bodies/comets included:
  - Minor planets: Ceres, Pallas, Vesta
  - Comets: 1P/Halley, 2P/Encke
  Contributions welcome — add elements under `dot/data/ephemeris/`.
