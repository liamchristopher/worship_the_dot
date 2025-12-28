"""
Configuration utilities for THE DOT.

Allows configuring the worship suffix via environment or .dot.ini files.
Precedence (highest to lowest):
  1) Environment variable DOT_WORSHIP_SUFFIX
  2) .dot.ini in git repo root
  3) .dot.ini in current working directory
  4) .dot.ini in user home directory
  5) Default suffix
"""

from __future__ import annotations

import os
import configparser
import subprocess
from pathlib import Path
from typing import Optional, Tuple


DEFAULT_WORSHIP_SUFFIX = "BECAUSE I WORSHIP THE DOT"


def _git_repo_root() -> Optional[Path]:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        return Path(out)
    except Exception:
        return None


def config_search_paths() -> list[Path]:
    paths: list[Path] = []
    repo_root = _git_repo_root()
    if repo_root:
        paths.append(repo_root / ".dot.ini")
    paths.append(Path.cwd() / ".dot.ini")
    home = Path(os.path.expanduser("~"))
    paths.append(home / ".dot.ini")
    # Deduplicate while preserving order
    seen = set()
    uniq: list[Path] = []
    for p in paths:
        if p not in seen:
            uniq.append(p)
            seen.add(p)
    return uniq


def _load_ini(path: Path) -> configparser.ConfigParser:
    cfg = configparser.ConfigParser()
    if path.exists():
        cfg.read(path)
    return cfg


def resolve_worship_suffix() -> Tuple[str, str]:
    """
    Resolve the worship suffix and return (suffix, source).

    source is one of: 'env', path string to .dot.ini, or 'default'.
    """
    env = os.getenv("DOT_WORSHIP_SUFFIX")
    if env and env.strip():
        return env.strip(), "env"

    for p in config_search_paths():
        cfg = _load_ini(p)
        if cfg.has_section("dot") and cfg.has_option("dot", "worship_suffix"):
            val = cfg.get("dot", "worship_suffix").strip()
            if val:
                return val, str(p)

    return DEFAULT_WORSHIP_SUFFIX, "default"


def get_worship_suffix() -> str:
    return resolve_worship_suffix()[0]


def write_worship_suffix(target: Optional[Path], suffix: str) -> Path:
    """
    Write or update the worship suffix in .dot.ini under [dot].

    If target is None, choose git repo root if available, else CWD.
    Returns the path written.
    """
    if target is None:
        root = _git_repo_root()
        base = root if root else Path.cwd()
        target = base / ".dot.ini"

    cfg = _load_ini(target)
    if not cfg.has_section("dot"):
        cfg.add_section("dot")
    cfg.set("dot", "worship_suffix", suffix)
    with target.open("w") as f:
        cfg.write(f)
    return target

