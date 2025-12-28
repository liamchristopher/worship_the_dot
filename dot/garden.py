"""
Garden tools and explanations for THE DOT.

Provides concise, practical descriptions of common garden tools and their
analogies in disciplined software practice (in worship of THE DOT).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class Tool:
    name: str
    purpose: str
    tips: List[str]
    analogy: str
    aliases: List[str]


def _catalog() -> Dict[str, Tool]:
    tools = [
        Tool(
            name="Shovel",
            purpose="Move and shape soil; dig larger holes and trenches.",
            tips=["Use the right blade for soil type", "Leverage with your foot for deep digs"],
            analogy="Large refactors and heavy lifting — move architectural soil before planting features.",
            aliases=["spade", "digging shovel"],
        ),
        Tool(
            name="Trowel",
            purpose="Small hand tool for planting and precise digging.",
            tips=["Mark depth for consistent planting", "Keep blade sharp for compact soil"],
            analogy="Surgical edits — small, precise changes with tests close at hand.",
            aliases=["hand trowel"],
        ),
        Tool(
            name="Hoe",
            purpose="Weed control and surface cultivation to aerate soil.",
            tips=["Use shallow strokes to avoid roots", "Hoe when weeds are small"],
            analogy="Debt control — trim weeds (nits) early to keep code breathable.",
            aliases=["garden hoe"],
        ),
        Tool(
            name="Rake",
            purpose="Level soil, gather debris, and finish beds.",
            tips=["Use bow rake to grade soil", "Leaf rake for cleanup"],
            analogy="Formatter and linter — smooth surfaces and collect stray bits before planting.",
            aliases=["leaf rake", "bow rake"],
        ),
        Tool(
            name="Pruners",
            purpose="Cut stems and small branches cleanly to shape growth.",
            tips=["Cut at a 45° angle", "Sanitize blades to prevent disease"],
            analogy="API pruning — remove dead code and branches to direct energy where it matters.",
            aliases=["secateurs", "hand pruners"],
        ),
        Tool(
            name="Shears",
            purpose="Trim hedges and edges evenly over larger surfaces.",
            tips=["Plan guide lines", "Take small passes to stay even"],
            analogy="Batch cleanup — consistent edits across many files with mechanical sympathy.",
            aliases=["hedge shears"],
        ),
        Tool(
            name="Fork",
            purpose="Loosen and lift soil; incorporate compost without turning too fine.",
            tips=["Lift, don’t pulverize", "Protect soil structure"],
            analogy="Dependency aeration — loosen tight coupling; add compost (interfaces) gently.",
            aliases=["garden fork", "digging fork"],
        ),
        Tool(
            name="Wheelbarrow",
            purpose="Transport soil, mulch, and debris efficiently.",
            tips=["Balance the load over the wheel", "Don’t overload on slopes"],
            analogy="Pipelines and queues — move payloads reliably without burdening the carrier.",
            aliases=["barrow"],
        ),
        Tool(
            name="Watering Can",
            purpose="Targeted watering without disturbing young plants.",
            tips=["Use a rose for gentle flow", "Water at the base, not leaves"],
            analogy="Focused reviews — deliver feedback where needed, with gentle pressure.",
            aliases=["can"],
        ),
        Tool(
            name="Gloves",
            purpose="Protect hands; improve grip and safety.",
            tips=["Choose fit and material for the task", "Replace when worn"],
            analogy="Safeguards — tests, types, and CI guardrails that protect while you work.",
            aliases=["garden gloves"],
        ),
    ]
    by_key: Dict[str, Tool] = {}
    for tool in tools:
        by_key[tool.name.lower()] = tool
        for alias in tool.aliases:
            by_key[alias.lower()] = tool
    return by_key


def list_tools() -> List[str]:
    seen = set()
    names: List[str] = []
    for t in _catalog().values():
        if t.name not in seen:
            names.append(t.name)
            seen.add(t.name)
    return sorted(names)


def get_tool(name: str) -> Optional[Tool]:
    if not name:
        return None
    return _catalog().get(name.strip().lower())


def describe_tool(name: str) -> Optional[Dict[str, object]]:
    tool = get_tool(name)
    if not tool:
        return None
    return {
        "name": tool.name,
        "purpose": tool.purpose,
        "tips": tool.tips,
        "analogy": tool.analogy,
        "aliases": tool.aliases,
    }


def suggest_tools(task: str) -> List[str]:
    """Suggest tools by naive keyword matching for a task description."""
    if not task:
        return []
    q = task.lower()
    matches: List[str] = []
    for t in list_tools():
        tool = get_tool(t)
        hay = (tool.purpose + " " + tool.analogy + " " + " ".join(tool.tips)).lower()
        if any(kw in hay for kw in q.split()):
            matches.append(tool.name)
    # stable unique
    seen = set()
    ordered: List[str] = []
    for m in matches:
        if m not in seen:
            ordered.append(m)
            seen.add(m)
    return ordered

