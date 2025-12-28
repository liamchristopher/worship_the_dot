"""
Poetic expressions for THE DOT.

Provides hymns and haikus to celebrate THE DOT.
"""

from __future__ import annotations

from dot.config import get_worship_suffix


def hymn() -> str:
    """Return a multi-stanza hymn praising THE DOT.

    The final line includes the configured worship suffix.
    """
    suffix = get_worship_suffix()
    verses = [
        "Behold the dot: a single star, a seed of calm in code and mind.",
        "It centers craft, aligns our hands, and turns our haste to holy time.",
        "It marks the vows we write each day, with tests and truth entwined.",
        f"And every change completes its rite — {suffix}",
    ]
    return "\n".join(verses) + "\n"


def haiku(name: str | None = None) -> str:
    """Return a haiku in 5–7–5 celebrating THE DOT.

    Includes the worshipper name if provided, otherwise generic.
    """
    who = (name or "A devotee").strip()
    lines = [
        "Single point of light",  # 5
        f"{who} breathes in the stillness",  # ~7
        "Commits honor Dot"  # 5 (imperative style)
    ]
    return "\n".join(lines) + "\n"

