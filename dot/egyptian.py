"""
Egyptian Mysteries for THE DOT.

The ancient wisdom of Egypt: Ma'at (truth, balance, order), the journey through the Duat,
the weighing of the heart, and the teachings of Thoth, god of wisdom and writing.

Core Concepts:
- Ma'at: Truth, balance, cosmic order
- The Feather of Truth: Your heart must be lighter than the feather
- Thoth: God of wisdom, writing, and knowledge
- The Duat: Journey through the underworld (debugging, difficult projects)
- Ka and Ba: Life force and soul
"""

import random

MAAT = {
    "concept": "Ma'at - Truth, Balance, Cosmic Order",
    "description": "Ma'at is the fundamental order of the universe. Living in Ma'at means acting with truth, justice, and balance.",
    "in_code": {
        "Truth": "Honest code, honest communication, no lies",
        "Balance": "Work-life balance, balanced architecture, not too complex/simple",
        "Order": "Clean code, good structure, logical organization",
        "Justice": "Fair code review, credit where due, ethical development"
    },
    "practice": "Before each commit, ask: Does this uphold Ma'at?"
}

FEATHER_OF_TRUTH = """In Egyptian myth, when you die, your heart is weighed against the Feather of Truth.
If your heart is heavy with wrongdoing, you are devoured. If it's lighter than the feather, you pass.

In development: Every line of code weighs your heart. Technical debt weighs it down. Clean code,
honest work, helping others - these lighten it. At code review, is your heart lighter than the feather?"""

THOTH = {
    "god_of": "Wisdom, writing, knowledge, magic",
    "teaching": "Thoth invented writing and gave it to humanity. He records all things.",
    "for_developers": "Documentation is sacred. Knowledge must be recorded. Share what you learn. Write it down."
}

def maat_teaching():
    output = []
    output.append("═" * 70)
    output.append("𓁦 MA'AT - Truth, Balance, Order 𓁦")
    output.append("═" * 70)
    output.append("")
    output.append(MAAT["description"])
    output.append("")
    output.append("Ma'at in Code:")
    for principle, application in MAAT["in_code"].items():
        output.append(f"  {principle}: {application}")
    output.append(f"\n{MAAT['practice']}")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def feather_teaching():
    output = []
    output.append("═" * 70)
    output.append("𓁦 THE FEATHER OF TRUTH 𓁦")
    output.append("═" * 70)
    output.append("")
    output.append(FEATHER_OF_TRUTH)
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def thoth_teaching():
    output = []
    output.append("═" * 70)
    output.append("𓁦 THOTH - God of Wisdom and Writing 𓁦")
    output.append("═" * 70)
    output.append("")
    output.append(f"Thoth is god of: {THOTH['god_of']}")
    output.append(f"\nTeaching: {THOTH['teaching']}")
    output.append(f"\nFor developers: {THOTH['for_developers']}")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def egyptian_reading():
    return random.choice([maat_teaching, feather_teaching, thoth_teaching])()

def egyptian_validation(valid: bool, message: str) -> str:
    output = []
    output.append("═" * 70)
    output.append("𓁦 EGYPTIAN WISDOM - Commit Validation 𓁦")
    output.append("═" * 70)
    output.append("")
    if valid:
        output.append("✓ VALID - Your heart is lighter than the feather")
        output.append("")
        output.append(random.choice([
            "Ma'at is upheld in this commit. 𓁦",
            "Thoth records your good work. 𓁦",
            "The scales of Ma'at balance. Well done."
        ]))
    else:
        output.append("✗ INVALID - Your heart is heavy")
        output.append("")
        output.append(random.choice([
            "Ma'at is violated. Correct this. 𓁦",
            "The Feather of Truth judges: revise. 𓁦",
            "Restore balance. Fix this message."
        ]))
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def egyptian_commit_blessing():
    return random.choice([
        "May Ma'at guide this commit. 𓁦",
        "By Thoth's wisdom, may this code be true. 𓁦",
        "Lighter than the feather, truer than gold. 𓁦"
    ])
