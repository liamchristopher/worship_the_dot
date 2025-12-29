"""
Tarot readings for THE DOT.

Provides draws and spreads aligned with THE DOT philosophy.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict

from dot.config import get_worship_suffix


@dataclass(frozen=True)
class Card:
    name: str
    keywords: List[str]
    upright: str
    reversed: str


def _deck() -> List[Card]:
    # Major Arcana with DOT-themed meanings (concise)
    return [
        Card("The Fool", ["begin", "trust"], "New branch, bold start.", "Careless commit, untested."),
        Card("The Magician", ["skill", "focus"], "Tooling aligned, one command.", "Scattered tools, context lost."),
        Card("The High Priestess", ["insight", "silence"], "Read the code before changes.", "Ignoring signals, rushing."),
        Card("The Empress", ["growth", "care"], "Nurture tests and docs.", "Neglected docs, brittle code."),
        Card("The Emperor", ["order", "rules"], "Workflow enforced; hooks installed.", "Bypassing rules breeds chaos."),
        Card("The Hierophant", ["tradition", "teach"], "Share patterns, reusable scripts.", "Gatekeeping and secrecy."),
        Card("The Lovers", ["choice", "merge"], "Harmonious merges, clear reviews.", "Conflicting branches, unclear goals."),
        Card("The Chariot", ["drive", "win"], "CI passing, ship with purpose.", "Impetuous push, flakiness."),
        Card("Strength", ["resolve", "patience"], "Refactor kindly, steady pace.", "Force fixes, hidden debt."),
        Card("The Hermit", ["focus", "seek"], "Isolate issues, minimal repro.", "Noise overwhelms signal."),
        Card("Wheel of Fortune", ["cycles", "change"], "Iterate: plan, test, improve.", "Churn without insight."),
        Card("Justice", ["fair", "truth"], "Coverage honest, results clear.", "Metrics gamed, vague output."),
        Card("The Hanged Man", ["pause", "reframe"], "Rethink interface; simplify.", "Attachment to complexity."),
        Card("Death", ["end", "renew"], "Remove dead code; be free.", "Clinging to obsolete paths."),
        Card("Temperance", ["balance", "blend"], "Compose small functions.", "Overreach, god-object grows."),
        Card("The Devil", ["bind", "shadow"], "Beware shortcuts; review.", "Vendor lock and haste."),
        Card("The Tower", ["shock", "reveal"], "Failures teach; logs help.", "Silent crashes, blame."),
        Card("The Star", ["hope", "guide"], "Clear roadmap; kind reviews.", "Aimless toil, burnout."),
        Card("The Moon", ["uncertainty", "dream"], "Spike cautiously; write notes.", "Spec drift and confusion."),
        Card("The Sun", ["clarity", "joy"], "Green builds; docs shining.", "Theatre without substance."),
        Card("Judgement", ["call", "audit"], "Changelog honest; own mistakes.", "Hide regressions, deflect."),
        Card("The World", ["finish", "whole"], "Release complete; celebrate.", "Almost done forever."),
    ]


def list_cards() -> List[str]:
    return [c.name for c in _deck()]


def get_card(name: str) -> Optional[Card]:
    name_lower = name.strip().lower()
    for c in _deck():
        if c.name.lower() == name_lower:
            return c
    return None


def draw(n: int = 1, allow_reversed: bool = True, seed: Optional[int] = None) -> List[Tuple[Card, bool]]:
    """Draw n cards. Returns list of (card, is_reversed)."""
    n = max(1, min(n, len(_deck())))
    rng = random.Random(seed)
    cards = rng.sample(_deck(), n)
    result: List[Tuple[Card, bool]] = []
    for c in cards:
        rev = allow_reversed and rng.choice([True, False])
        result.append((c, rev))
    return result


def spread(kind: str = "three", seed: Optional[int] = None) -> Dict[str, Tuple[Card, bool]]:
    """Create a spread.

    - three: Past/Present/Future
    - yesno: One card + heuristic yes/no
    - commit: Plan/Implement/Worship
    """
    rng = random.Random(seed)
    if kind == "three":
        picks = rng.sample(_deck(), 3)
        flags = [rng.choice([True, False]) for _ in range(3)]
        return {
            "Past": (picks[0], flags[0]),
            "Present": (picks[1], flags[1]),
            "Future": (picks[2], flags[2]),
        }
    elif kind == "yesno":
        c = rng.choice(_deck())
        rev = rng.choice([True, False])
        return {"Answer": (c, rev)}
    elif kind == "commit":
        picks = rng.sample(_deck(), 3)
        flags = [rng.choice([True, False]) for _ in range(3)]
        return {
            "Plan": (picks[0], flags[0]),
            "Implement": (picks[1], flags[1]),
            "Worship": (picks[2], flags[2]),
        }
    else:
        raise ValueError(f"Unknown spread: {kind}")


def interpret(entries: List[Tuple[Card, bool]], context: str = "") -> str:
    """Generate a brief DOT-themed reading for drawn cards."""
    lines: List[str] = []
    suffix = get_worship_suffix()
    for i, (card, rev) in enumerate(entries, 1):
        meaning = card.reversed if rev else card.upright
        orient = "reversed" if rev else "upright"
        lines.append(f"{i}. {card.name} ({orient}) — {meaning}")
    if context:
        lines.append("")
        lines.append(f"Context: {context}")
    lines.append("")
    lines.append(f"Remember: {suffix}")
    return "\n".join(lines)


def yesno_from_card(card: Card, reversed: bool) -> str:
    """Heuristic yes/no based on card polarity and orientation."""
    positive = {
        "The Magician", "The Empress", "The Emperor", "The Lovers", "The Chariot",
        "Strength", "Wheel of Fortune", "Justice", "Temperance", "The Star",
        "The Sun", "Judgement", "The World",
    }
    is_positive = card.name in positive
    if reversed:
        is_positive = not is_positive
    return "Yes" if is_positive else "No"

