# Porting THE DOT to Rust — Repeatable Process

This guide describes a repeatable, verifiable way to produce a stand‑alone Rust CLI that is 100% compatible with the Python CLI’s observable behavior.

## 1) Define Compatibility (Spec)
- CLI name: `dot`
- Exit codes: success 0, validation failure 1, usage errors 1
- Outputs: exact strings (ASCII hyphen `-` separators, same phrasing)
- Config: resolve suffix from `DOT_WORSHIP_SUFFIX`, `./.dot.ini`, `$HOME/.dot.ini` (`[dot] worship_suffix`), else default
- Commands to match (phase 1: core):
  - `worship [name]`
  - `tenets`
  - `validate <message>`
- Phase 2 (optional): `config show`, `hooks install|status|uninstall`, `init`, `doctor`, `backstory`, `badge`, `poem`, `tarot`, `shinto`, `stats`

Capture the spec in a YAML alongside examples: `scripts/compat.yml`.

## 2) Scaffold the Crate
- Location: `rust/the-dot`
- Binary: `[[bin]] name = "dot"`
- Deps: `clap`, `anyhow`, `ini`, `dirs-next`, `once_cell`
- Modules: `lib.rs` (core), `main.rs` (CLI)

## 3) Implement Feature Parity (Phased)
- Phase 1: core worship/tenets/validate/suffix resolution (done)
- Phase 2+: extend subcommands; mirror help text and options

## 4) Add Compatibility Tests
- Rust unit/integration tests (cargo) for outputs and exit codes
- Cross‑runner: `scripts/compat.py` runs Python CLI (`python -m dot.cli`) and Rust CLI (`target/debug/dot`) with the same arguments and compares stdout/stderr and exit codes against `scripts/compat.yml`

## 5) Wire CI
- `.github/workflows/rust.yml` builds and tests the crate on all branches
- Optionally add a job to run `scripts/compat.py` after building both CLIs (if Python is available)

## 6) Release
- `cargo install --path rust/the-dot` produces a stand‑alone `dot` binary
- Ensure README documents Rust usage and configuration

## 7) Maintenance
- When Python CLI changes outputs/commands, update `scripts/compat.yml`
- Run the cross‑runner to verify both CLIs remain aligned

## Files Added by This Process
- `rust/the-dot` crate (binary `dot`)
- `.github/workflows/rust.yml` for Rust CI
- `scripts/compat.yml` (spec) and `scripts/compat.py` (runner) — optional but recommended

With this process, the Rust CLI remains a faithful stand‑alone mirror of THE DOT.

