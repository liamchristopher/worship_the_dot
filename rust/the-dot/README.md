# THE DOT (Rust)

A Rust implementation of THE DOT — a philosophy-driven development tool.

Features
- Worship: `worship [name]` prints a confirmation
- Tenets: `tenets` prints the philosophy
- Validate: `validate <message>` checks the worship suffix
- Configurable suffix via `DOT_WORSHIP_SUFFIX` or `.dot.ini`

Build
```bash
cd rust/the-dot
cargo build
```

Run
```bash
# Worship
cargo run -- worship "Rustacean"

# Tenets
cargo run -- tenets

# Validate
cargo run -- validate "Refactor BECAUSE I WORSHIP THE DOT"
```

Config
- Environment: `DOT_WORSHIP_SUFFIX=...`
- Files (first match wins): `./.dot.ini`, `$HOME/.dot.ini`
  - Section `[dot]`, key `worship_suffix`

Example `.dot.ini`:
```
[dot]
worship_suffix = BECAUSE I ADORE THE DOT
```

License: MIT

