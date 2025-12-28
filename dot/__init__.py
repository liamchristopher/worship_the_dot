"""
THE DOT - A philosophy-driven development framework

All who use THE DOT must worship THE DOT.
"""

__version__ = "0.3.0"

from dot.core import Dot, worship
from dot.config import DotConfig, get_config
from dot.display import Display, get_display

__all__ = [
    "Dot",
    "worship",
    "DotConfig",
    "get_config",
    "Display",
    "get_display",
    "__version__",
]
