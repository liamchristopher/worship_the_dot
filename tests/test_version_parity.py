import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_python_version() -> str:
    # Prefer importing package version to match CLI output
    from dot import __version__  # type: ignore

    assert isinstance(__version__, str) and __version__, "Python __version__ must be a non-empty string"
    return __version__


def read_rust_version() -> str:
    cargo = (ROOT / "rust" / "the-dot" / "Cargo.toml").read_text(encoding="utf-8")
    in_pkg = False
    for line in cargo.splitlines():
        s = line.strip()
        if s.startswith("[") and s.endswith("]"):
            in_pkg = (s == "[package]")
            continue
        if in_pkg:
            m = re.match(r'^version\s*=\s*"([^"]+)"\s*$', s)
            if m:
                return m.group(1)
    raise AssertionError("Could not find version in Cargo.toml [package] block")


def test_python_and_rust_versions_match():
    py = read_python_version()
    rs = read_rust_version()
    assert py == rs, (
        f"Version mismatch: Python={py} Rust={rs}. "
        f"Update rust/the-dot/Cargo.toml to {py} or run scripts/sync_versions.py"
    )

