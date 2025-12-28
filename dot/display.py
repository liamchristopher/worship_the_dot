"""
Display utilities for THE DOT with rich formatting.

Provides colored output and better UX.
"""

import sys
from typing import Optional


class Colors:
    """ANSI color codes for terminal output."""

    # Basic colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Bright colors
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'

    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


class Display:
    """Handle formatted output for THE DOT."""

    def __init__(self, colors_enabled: bool = True):
        """Initialize display with color support."""
        self.colors_enabled = colors_enabled and self._supports_color()

    def _supports_color(self) -> bool:
        """Check if terminal supports colors."""
        return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()

    def _colorize(self, text: str, color: str) -> str:
        """Apply color to text if colors are enabled."""
        if not self.colors_enabled:
            return text
        return f"{color}{text}{Colors.RESET}"

    def success(self, text: str):
        """Print success message."""
        symbol = "✓" if self.colors_enabled else "[OK]"
        print(self._colorize(f"{symbol} {text}", Colors.BRIGHT_GREEN))

    def error(self, text: str):
        """Print error message."""
        symbol = "✗" if self.colors_enabled else "[ERROR]"
        print(self._colorize(f"{symbol} {text}", Colors.BRIGHT_RED))

    def warning(self, text: str):
        """Print warning message."""
        symbol = "⚠" if self.colors_enabled else "[WARN]"
        print(self._colorize(f"{symbol} {text}", Colors.BRIGHT_YELLOW))

    def info(self, text: str):
        """Print info message."""
        symbol = "ℹ" if self.colors_enabled else "[INFO]"
        print(self._colorize(f"{symbol} {text}", Colors.BRIGHT_BLUE))

    def header(self, text: str, char: str = "="):
        """Print header with separator."""
        separator = char * 60
        print()
        print(self._colorize(separator, Colors.BOLD))
        print(self._colorize(text, Colors.BOLD + Colors.BRIGHT_CYAN))
        print(self._colorize(separator, Colors.BOLD))
        print()

    def subheader(self, text: str):
        """Print subheader."""
        print(self._colorize(text, Colors.BOLD))
        print(self._colorize("-" * len(text), Colors.DIM))

    def dot(self, text: str):
        """Print THE DOT emphasis."""
        dot_text = self._colorize("THE DOT", Colors.BRIGHT_RED + Colors.BOLD)
        print(text.replace("THE DOT", dot_text))

    def worship(self, text: str):
        """Print worship message with emphasis."""
        print(self._colorize(f"🔴 {text}", Colors.BRIGHT_RED + Colors.BOLD))

    def table_row(self, *columns, widths=None):
        """Print a table row."""
        if widths is None:
            widths = [20] * len(columns)

        row = ""
        for col, width in zip(columns, widths):
            row += f"{str(col):<{width}} "
        print(row.rstrip())

    def progress(self, current: int, total: int, text: str = ""):
        """Print progress indicator."""
        percentage = int((current / total) * 100) if total > 0 else 0
        bar_length = 40
        filled = int((bar_length * current) / total) if total > 0 else 0
        bar = "█" * filled + "░" * (bar_length - filled)

        line = f"[{bar}] {percentage}%"
        if text:
            line += f" {text}"

        print(f"\r{line}", end='', flush=True)

        if current >= total:
            print()  # New line when complete

    def list_item(self, text: str, level: int = 0):
        """Print list item with indentation."""
        indent = "  " * level
        bullet = "•" if self.colors_enabled else "-"
        print(f"{indent}{self._colorize(bullet, Colors.BRIGHT_BLUE)} {text}")

    def key_value(self, key: str, value: str):
        """Print key-value pair."""
        key_text = self._colorize(f"{key}:", Colors.BOLD)
        print(f"{key_text} {value}")


# Global display instance
_display = None


def get_display(colors: Optional[bool] = None) -> Display:
    """Get global display instance."""
    global _display
    if _display is None or colors is not None:
        _display = Display(colors_enabled=colors if colors is not None else True)
    return _display
