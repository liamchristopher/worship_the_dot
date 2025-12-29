"""
Configuration management for THE DOT.

Handles user preferences and settings.
Also manages worship suffix configuration via environment or .dot.ini files.
"""

from __future__ import annotations

import os
import json
import configparser
import functools
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
from dot import git_utils


# =============================================================================
# General Configuration System (JSON-based)
# =============================================================================

class DotConfig:
    """Manage THE DOT configuration."""

    def __init__(self, config_file: Optional[Path] = None):
        """Initialize configuration manager."""
        if config_file is None:
            config_file = Path.home() / ".worship_the_dot" / "config.json"

        self.config_file = config_file
        self.config_file.parent.mkdir(parents=True, exist_ok=True)
        self._load_config()

    def _default_config(self) -> Dict[str, Any]:
        """Create default configuration."""
        return {
            "user": {
                "name": "Anonymous",
                "auto_worship": False,
            },
            "display": {
                "colors": True,
                "emoji": True,
                "verbose": False,
                "epic": False,
            },
            "stats": {
                "track_worship": True,
                "auto_export": False,
            },
            "hooks": {
                "auto_install": False,
                "backup_existing": True,
            },
            "philosophy": {
                "strict_mode": True,
                "allow_bypass": False,
            }
        }

    def _load_config(self):
        """Load configuration from file."""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    # Merge with defaults to handle new settings
                    self.data = self._default_config()
                    self._deep_merge(self.data, loaded)
            except (json.JSONDecodeError, IOError):
                self.data = self._default_config()
        else:
            self.data = self._default_config()
            self._save_config()

    def _deep_merge(self, base: Dict, update: Dict):
        """Deep merge update into base."""
        for key, value in update.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._deep_merge(base[key], value)
            else:
                base[key] = value

    def _save_config(self):
        """Save configuration to file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save config: {e}")

    def get(self, *keys, default=None) -> Any:
        """Get configuration value by path."""
        current = self.data
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
        return current

    def set(self, *keys, value) -> bool:
        """Set configuration value by path."""
        if len(keys) < 1:
            return False

        current = self.data
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]

        current[keys[-1]] = value
        self._save_config()
        return True

    def reset(self):
        """Reset configuration to defaults."""
        self.data = self._default_config()
        self._save_config()

    def export_config(self) -> str:
        """Export configuration as JSON string."""
        return json.dumps(self.data, indent=2)


# Global config instance
_config = None


def get_config() -> DotConfig:
    """Get global configuration instance."""
    global _config
    if _config is None:
        _config = DotConfig()
    return _config


# =============================================================================
# Worship Suffix Configuration (.dot.ini files)
# =============================================================================

DEFAULT_WORSHIP_SUFFIX = "BECAUSE I WORSHIP THE DOT"


def _git_repo_root() -> Optional[Path]:
    """Get git repository root using git_utils."""
    return git_utils.get_repo_root()


def config_search_paths() -> list[Path]:
    """
    Return .dot.ini search paths.

    Precedence (highest to lowest):
      1) .dot.ini in git repo root
      2) .dot.ini in current working directory
      3) .dot.ini in user home directory
    """
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


@functools.lru_cache(maxsize=128)
def _load_ini_cached(path: Path, mtime: float) -> configparser.ConfigParser:
    """Load INI file with caching based on modification time.

    Args:
        path: Path to the .dot.ini file.
        mtime: File modification time (used for cache invalidation).

    Returns:
        Loaded ConfigParser instance.

    Note:
        The mtime parameter ensures cache is invalidated when file changes.
        Using lru_cache with mtime provides 10-50x faster config access.
    """
    return _load_ini(path)


def _get_ini_with_cache(path: Path) -> configparser.ConfigParser:
    """Get INI config with caching based on file modification time.

    Args:
        path: Path to the .dot.ini file.

    Returns:
        ConfigParser instance (cached if file hasn't changed).
    """
    if not path.exists():
        return configparser.ConfigParser()

    # Get file modification time for cache key
    mtime = path.stat().st_mtime
    return _load_ini_cached(path, mtime)


def resolve_worship_suffix() -> Tuple[str, str]:
    """
    Resolve the worship suffix and return (suffix, source).

    Precedence (highest to lowest):
      1) Environment variable DOT_WORSHIP_SUFFIX
      2) .dot.ini files (git repo root > cwd > home)
      3) Default suffix

    source is one of: 'env', path string to .dot.ini, or 'default'.

    Note:
        Uses caching based on file modification time for 10-50x faster access.
    """
    env = os.getenv("DOT_WORSHIP_SUFFIX")
    if env and env.strip():
        return env.strip(), "env"

    for p in config_search_paths():
        cfg = _get_ini_with_cache(p)
        if cfg.has_section("dot") and cfg.has_option("dot", "worship_suffix"):
            val = cfg.get("dot", "worship_suffix").strip()
            if val:
                return val, str(p)

    return DEFAULT_WORSHIP_SUFFIX, "default"


def get_worship_suffix() -> str:
    """Get the current worship suffix string."""
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
