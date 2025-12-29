"""Philosophy modules for THE DOT.

This package contains various philosophical and esoteric traditions that can be
invoked through THE DOT CLI.
"""

# Re-export all philosophy modules for backward compatibility
from dot.philosophies import alchemy
from dot.philosophies import astrology
from dot.philosophies import egyptian
from dot.philosophies import gnostic
from dot.philosophies import hermetic
from dot.philosophies import jain
from dot.philosophies import norse
from dot.philosophies import shinto
from dot.philosophies import tarot
from dot.philosophies import zoroastrian

__all__ = [
    "alchemy",
    "astrology",
    "egyptian",
    "gnostic",
    "hermetic",
    "jain",
    "norse",
    "shinto",
    "tarot",
    "zoroastrian",
]
