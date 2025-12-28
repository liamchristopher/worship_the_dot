"""
Configuration management for THE DOT.

Handles user preferences and settings.
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional


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
