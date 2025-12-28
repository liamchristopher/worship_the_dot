"""
Zoroastrianism for THE DOT - The Path of Asha.

One of humanity's oldest monotheistic religions, Zoroastrianism teaches the eternal battle
between Asha (truth, order) and Druj (lie, chaos). Founded by Zarathustra (Zoroaster),
it emphasizes good thoughts, good words, good deeds.

Core Concepts:
- Asha vs Druj: Truth/Order vs Lie/Chaos
- Good Thoughts, Good Words, Good Deeds
- Fire as sacred symbol of divine light and wisdom
- Fravashi: Guardian spirit, divine essence within
"""

import random

ASHA_DRUJ = {
    "Asha": "Truth, order, rightness, the way things should be",
    "Druj": "Lie, chaos, disorder, corruption",
    "In_Code": {
        "Asha": ["Clean code", "Good architecture", "Tests", "Documentation", "Honest estimates"],
        "Druj": ["Technical debt", "Spaghetti code", "No tests", "Lies to stakeholders", "Hacks"]
    },
    "Practice": "Choose Asha over Druj in every decision. Even small lies create chaos."
}

THREE_PRINCIPLES = {
    "Humata": {"principle": "Good Thoughts", "in_coding": "Think clearly. Design before coding. Contemplate the right approach."},
    "Hukhta": {"principle": "Good Words", "in_coding": "Clear communication. Honest estimates. Kind code reviews. Good documentation."},
    "Huvarshta": {"principle": "Good Deeds", "in_coding": "Write good code. Help teammates. Ship quality. Serve users well."}
}

FIRE = """Fire is sacred in Zoroastrianism - symbol of divine light, wisdom, and purity.
In development: Your passion for code is your fire. Keep it burning. Don't let it die.
Feed it with learning, practice, and meaningful work. Protect it from cynicism and burnout."""

def asha_teaching():
    output = []
    output.append("═" * 70)
    output.append("🔥 ASHA vs DRUJ - Truth vs Lie 🔥")
    output.append("═" * 70)
    output.append("")
    output.append(f"Asha: {ASHA_DRUJ['Asha']}")
    output.append(f"Druj: {ASHA_DRUJ['Druj']}")
    output.append("")
    output.append("Asha in Code:")
    for item in ASHA_DRUJ["In_Code"]["Asha"]:
        output.append(f"  ✓ {item}")
    output.append("\nDruj in Code:")
    for item in ASHA_DRUJ["In_Code"]["Druj"]:
        output.append(f"  ✗ {item}")
    output.append(f"\n{ASHA_DRUJ['Practice']}")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def principles_teaching():
    output = []
    output.append("═" * 70)
    output.append("🔥 THE THREE PRINCIPLES 🔥")
    output.append("═" * 70)
    output.append("")
    for name, data in THREE_PRINCIPLES.items():
        output.append(f"{name.upper()} - {data['principle']}")
        output.append(f"  {data['in_coding']}")
        output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def fire_teaching():
    output = []
    output.append("═" * 70)
    output.append("🔥 SACRED FIRE - Keep Your Passion Burning 🔥")
    output.append("═" * 70)
    output.append("")
    output.append(FIRE)
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def zoroastrian_reading():
    return random.choice([asha_teaching, principles_teaching, fire_teaching])()

def zoroastrian_validation(valid: bool, message: str) -> str:
    output = []
    output.append("═" * 70)
    output.append("🔥 ZOROASTRIAN WISDOM - Commit Validation 🔥")
    output.append("═" * 70)
    output.append("")
    if valid:
        output.append("✓ VALID COMMIT - This is Asha (Truth)")
        output.append("")
        output.append(random.choice([
            "Good thoughts, good words, good code. 🔥",
            "Asha prevails over Druj. Well done.",
            "The sacred fire burns bright in this work. 🔥"
        ]))
    else:
        output.append("✗ INVALID COMMIT - This approaches Druj (Lie)")
        output.append("")
        output.append(random.choice([
            "Return to Asha. Fix this message. 🔥",
            "Even small lies create chaos. Revise.",
            "The fire of truth demands honesty. Try again. 🔥"
        ]))
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def zoroastrian_commit_blessing():
    return random.choice([
        "May Asha guide this commit. 🔥",
        "Good thoughts, good words, good code. 🔥",
        "Let truth prevail over chaos. 🔥"
    ])
