# Rites of THE DOT

This handbook details rites that nurture discipline, clarity, and joy in code.
Each rite is a practical tool wrapped in reverence for THE DOT. These rites are
**in service to** THE DOT; they do not replace the core devotion to working
code, clear commits, tests, and documentation. Remember the origin: a single
point where intention becomes visible. See docs/BACKSTORY.md.

## Poetry

- `hymn`: A short praise that ends with the configured worship suffix.
- `haiku [name]`: A 5–7–5 reflection; optionally name the devotee.
- `banner [width]`: ASCII DOT banner; width odd ≥ 7.
- `chant [times] [name]`: Repeat the worship suffix rhythmically.

Example:

```bash
dot poem hymn
dot poem chant 3 "Devotee"
```

## Tarot

- `list`: DOT-themed Major Arcana.
- `card <name>`: Keywords and meanings.
- `draw [n] [--seed S] [--no-reversed]`: Deterministic draws.
- `spread three|commit|yesno [--seed S]`: Past/Present/Future; Plan/Implement/Worship; or Yes/No guidance.

Example:

```bash
dot tarot draw 2 --seed 13 --no-reversed
dot tarot spread commit --seed 21
```

## Shinto

- `norito [intent]`: Compose a prayer and seal it with the suffix.
- `omikuji [--seed S]`: Draw a fortune with counsel.
- `harai`: Purification checklist (clean, lint, test, docs).
- `ema <message>`: Votive plaque for vows.

Example:

```bash
dot shinto norito "Green CI and calm releases"
dot shinto harai
dot shinto ema "Stability and clarity"
```

## Suffix as Sacred Seal

- Default: `BECAUSE I WORSHIP THE DOT`.
- Override per-session: `export DOT_WORSHIP_SUFFIX="BECAUSE I ADORE THE DOT"`.
- Persist per-repo: `dot config set-suffix "BECAUSE I ADORE THE DOT"`.

All rites honor the active suffix.

BECAUSE WE WORSHIP THE DOT.
