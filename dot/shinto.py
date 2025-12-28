"""
Shinto-inspired rituals for THE DOT.

Provides norito (prayers), omikuji (fortunes), harai (purification), and ema (votive wishes).
"""

from __future__ import annotations

import random
from typing import Optional, Tuple

from dot.config import get_worship_suffix


OMIKUJI_RESULTS = [
    ("Great Blessing", "Proceed boldly; tests and spirits align."),
    ("Middle Blessing", "Refactor with care; reviewers are kind."),
    ("Small Blessing", "Write one more test before merging."),
    ("Blessing", "Document well; your path is clear."),
    ("Half Blessing", "Seek a second review; polish details."),
    ("Future Blessing", "Not yet—prepare CI, then advance."),
    ("Curse", "Pause and lint; fix nits to lift the gloom."),
    ("Great Curse", "Cleanse the repo: rebase, test, and try anew."),
]


def norito(intent: Optional[str] = None) -> str:
    """Compose a brief norito prayer to THE DOT."""
    suffix = get_worship_suffix()
    lines = [
        "Purify our code and calm our minds, O DOT-kami.",
        "Guide our branches to harmony and our commits to truth.",
    ]
    if intent and intent.strip():
        lines.append(f"We humbly offer this intent: {intent.strip()}.")
    lines.append(f"We seal this vow: {suffix}.")
    return "\n".join(lines) + "\n"


def omikuji(seed: Optional[int] = None) -> Tuple[str, str]:
    """Draw an omikuji fortune (name, counsel). Deterministic with seed."""
    rng = random.Random(seed)
    i = rng.randrange(len(OMIKUJI_RESULTS))
    return OMIKUJI_RESULTS[i]


def harai() -> str:
    """Harai (purification) guidance mapped to repository hygiene."""
    steps = [
        "Remove build artifacts and caches (make clean).",
        "Run linters and formatters (ruff/black).",
        "Re-run tests locally and in CI.",
        "Update changelog and documentation.",
    ]
    return "Harai — Purification Rite:\n- " + "\n- ".join(steps) + "\n"


def ema(message: str) -> str:
    """Create an ema-style vow plaque with the worship suffix."""
    suffix = get_worship_suffix()
    msg = message.strip() if message else "May our code honor THE DOT."
    border = "+" + ("-" * (len(msg) + 2)) + "+"
    body = f"| {msg} |"
    seal = f"| {suffix} |"
    width = max(len(border), len(seal))
    # Normalize to equal width
    def pad(s: str) -> str:
        return s[:-1] + (" " * (width - len(s))) + "+" if s.startswith("+") else s[0] + s[1:-1].ljust(width - 2) + s[-1]

    return "\n".join([pad(border), pad(body), pad(seal), pad(border)]) + "\n"

