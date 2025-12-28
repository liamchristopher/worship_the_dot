#!/usr/bin/env python3
"""
Synchronize Rust crate version to match the Python package version when parity exists.

Usage:
  uv run python scripts/sync_versions.py

This reads dot.__version__ and updates rust/the-dot/Cargo.toml [package].version
to match. It does not commit; run `git add -p` and commit with a proper message.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CARGO = ROOT / "rust" / "the-dot" / "Cargo.toml"


def read_python_version() -> str:
    from dot import __version__  # type: ignore

    if not isinstance(__version__, str) or not __version__:
        raise RuntimeError("dot.__version__ must be a non-empty string")
    return __version__


def sync_rust_version(py_version: str) -> bool:
    content = CARGO.read_text(encoding="utf-8")
    # Only replace within [package] section
    def repl(block: str) -> str:
        return re.sub(r'(?m)^version\s*=\s*"[^"]+"\s*$', f'version = "{py_version}"', block)

    def replace_in_package_sections(text: str) -> str:
        out = []
        cur = []
        in_pkg = False
        for line in text.splitlines(keepends=False):
            if line.strip().startswith("[") and line.strip().endswith("]"):
                # flush previous section
                if cur:
                    section = "".join(cur)
                    if in_pkg:
                        section = repl(section)
                    out.append(section)
                cur = []
                in_pkg = (line.strip() == "[package]")
                out.append(line + "\n")
            else:
                cur.append(line + "\n")
        if cur:
            section = "".join(cur)
            if in_pkg:
                section = repl(section)
            out.append(section)
        return "".join(out)

    new_content = replace_in_package_sections(content)
    if new_content != content:
        CARGO.write_text(new_content, encoding="utf-8")
        return True
    return False


def main() -> None:
    py = read_python_version()
    changed = sync_rust_version(py)
    if changed:
        print(f"Updated Rust version in {CARGO} to {py}")
    else:
        print("Rust version already matches Python version; no change.")


if __name__ == "__main__":
    main()
