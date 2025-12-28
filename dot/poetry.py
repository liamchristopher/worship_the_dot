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


def banner(width: int = 21) -> str:
    """Return an ASCII banner that centers THE DOT.

    Produces a red dot motif without ANSI codes so it's portable.
    Width is clamped to an odd number >= 7 for symmetry.
    """
    w = max(7, width)
    if w % 2 == 0:
        w += 1
    center = w // 2
    rows = []
    for r in range(w):
        row = [" "] * w
        # Draw a circular dot by Manhattan distance threshold
        for c in range(w):
            if abs(c - center) + abs(r - center) <= center // 2:
                row[c] = "●"  # solid dot
        rows.append("".join(row))
    title = " THE DOT "
    pad = max(0, (w - len(title)) // 2)
    header = "=" * w
    return "\n".join([header, " " * pad + title, header] + rows) + "\n"


def chant(times: int = 3, name: str | None = None) -> str:
    """Return a rhythmic chant repeating the suffix a number of times.

    Example:
      BECAUSE I WORSHIP THE DOT — Alice
      BECAUSE I WORSHIP THE DOT — Alice
      BECAUSE I WORSHIP THE DOT — Alice
    """
    t = max(1, min(times, 12))
    suffix = get_worship_suffix()
    who = f" — {name.strip()}" if name else ""
    return "\n".join([f"{suffix}{who}" for _ in range(t)]) + "\n"
