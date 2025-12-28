"""
Norse/Germanic Philosophy for THE DOT.

The wisdom of the Norse and Germanic peoples: the Eddas, the runes, the nine worlds,
and the path of the warrior-poet. From Odin's quest for wisdom to the concept of Wyrd
(fate woven by actions), Norse philosophy offers powerful teachings for developers.

Core Concepts:
- The Runes: Ancient symbols of power and wisdom
- Yggdrasil: The World Tree connecting all realms
- Wyrd: Fate woven by past actions
- Odin's Wisdom: Sacrifice for knowledge
- The Nine Virtues: Honor, Courage, Truth, Fidelity, Discipline, Hospitality, Self-Reliance, Industriousness, Perseverance
- Ragnarök: The cycle of destruction and renewal
"""

import random

RUNES = {
    "Fehu (ᚠ)": {"meaning": "Wealth, abundance", "coding": "Value creation, rewarding work"},
    "Uruz (ᚢ)": {"meaning": "Strength, vitality", "coding": "Robust code, resilience"},
    "Thurisaz (ᚦ)": {"meaning": "Giant, thorn, protection", "coding": "Security, defensive programming"},
    "Ansuz (ᚨ)": {"meaning": "Divine breath, communication", "coding": "Clear documentation, API design"},
    "Raidho (ᚱ)": {"meaning": "Journey, rhythm", "coding": "Development process, iteration"},
    "Kenaz (ᚲ)": {"meaning": "Torch, knowledge", "coding": "Learning, illumination, debugging"},
    "Gebo (ᚷ)": {"meaning": "Gift, exchange", "coding": "Open source, knowledge sharing"},
    "Wunjo (ᚹ)": {"meaning": "Joy, harmony", "coding": "Team cohesion, work satisfaction"},
    "Hagalaz (ᚺ)": {"meaning": "Hail, disruption", "coding": "Breaking changes, major refactors"},
    "Nauthiz (ᚾ)": {"meaning": "Need, constraint", "coding": "Requirements, deadlines, limitations"},
    "Isa (ᛁ)": {"meaning": "Ice, stillness", "coding": "Freeze, pause, code freeze"},
    "Jera (ᛃ)": {"meaning": "Harvest, cycle", "coding": "Release cycle, reaping benefits of work"},
    "Eihwaz (ᛇ)": {"meaning": "Yew tree, endurance", "coding": "Long-term projects, persistence"},
    "Perthro (ᛈ)": {"meaning": "Dice cup, fate", "coding": "Randomness, probability, testing"},
    "Algiz (ᛉ)": {"meaning": "Elk, protection", "coding": "Error handling, try/catch, validation"},
    "Sowilo (ᛊ)": {"meaning": "Sun, success", "coding": "Shipping, success, achievement"},
    "Tiwaz (ᛏ)": {"meaning": "Tyr, justice", "coding": "Fairness, good practices, code review"},
    "Berkano (ᛒ)": {"meaning": "Birch, growth", "coding": "Project growth, scaling"},
    "Ehwaz (ᛖ)": {"meaning": "Horse, movement", "coding": "Progress, velocity, moving forward"},
    "Mannaz (ᛗ)": {"meaning": "Human, self", "coding": "Developer, human element"},
    "Laguz (ᛚ)": {"meaning": "Water, flow", "coding": "Flow state, fluidity, adaptability"},
    "Ingwaz (ᛝ)": {"meaning": "Fertility, potential", "coding": "Innovation, new ideas"},
    "Dagaz (ᛞ)": {"meaning": "Day, breakthrough", "coding": "Ah-ha moments, sudden clarity"},
    "Othala (ᛟ)": {"meaning": "Ancestral property", "coding": "Legacy code, inheritance"}
}

NINE_VIRTUES = {
    "Courage": "Ship your code. Take technical risks. Speak up in code review.",
    "Truth": "Write honest code. Honest estimates. Honest documentation.",
    "Honor": "Keep your word. Deliver what you promise. Stand behind your work.",
    "Fidelity": "Loyal to your team, your craft, your principles.",
    "Discipline": "Daily practice. Consistent effort. Master your tools.",
    "Hospitality": "Welcome new developers. Share knowledge generously.",
    "Self-Reliance": "Debug your own code. Find your own answers first.",
    "Industriousness": "Work hard. Build things. Ship features.",
    "Perseverance": "The bug will be found. The project will ship. Keep going."
}

WYRD = """Wyrd is the Norse concept of fate - not predetermined destiny, but fate woven from
the threads of past actions. Your wyrd is the consequences of what you've done, creating
the context for what you can do next. In code: Your current codebase is your wyrd. Past
decisions (technical debt, good architecture) create your present reality. But you can
change your wyrd by acting differently now."""

YGGDRASIL = {
    "concept": "The World Tree connecting nine realms",
    "realms_in_development": {
        "Asgard (Gods)": "Senior developers, architects, tech leads",
        "Midgard (Humans)": "Regular developers, where most work happens",
        "Jotunheim (Giants)": "Large systems, legacy code, big challenges",
        "Alfheim (Light Elves)": "Beautiful, elegant code",
        "Svartalfheim (Dark Elves)": "Hidden complexity, obscure code",
        "Vanaheim (Vanir)": "Product, design, UX - different wisdom",
        "Niflheim (Ice/Mist)": "Unclear requirements, confusion",
        "Muspelheim (Fire)": "Urgency, production fires, crises",
        "Helheim (Death)": "Deprecated code, end-of-life systems"
    },
    "wisdom": "All realms are connected. The work you do in Midgard affects all realms."
}

ODIN_WISDOM = """Odin sacrificed his eye for wisdom. He hung on Yggdrasil for nine nights to gain
the runes. He wandered the worlds seeking knowledge. The lesson: True wisdom requires sacrifice.
You must give something (time, comfort, ego) to gain mastery. There are no shortcuts."""

def rune_reading():
    rune_name, rune_data = random.choice(list(RUNES.items()))
    output = []
    output.append("═" * 70)
    output.append("ᚱ THE RUNES - Ancient Nordic Wisdom ᚱ")
    output.append("═" * 70)
    output.append("")
    output.append(f"Your rune: {rune_name}")
    output.append("")
    output.append(f"Traditional meaning: {rune_data['meaning']}")
    output.append(f"In coding: {rune_data['coding']}")
    output.append("")
    output.append("Meditate on this rune today. What does it teach you?")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def virtues_teaching():
    output = []
    output.append("═" * 70)
    output.append("ᚱ THE NINE VIRTUES - The Norse Way ᚱ")
    output.append("═" * 70)
    output.append("")
    for virtue, application in NINE_VIRTUES.items():
        output.append(f"{virtue.upper()}")
        output.append(f"  {application}")
        output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def wyrd_teaching():
    output = []
    output.append("═" * 70)
    output.append("ᚱ WYRD - Your Woven Fate ᚱ")
    output.append("═" * 70)
    output.append("")
    output.append(WYRD)
    output.append("")
    output.append("Your technical debt is your wyrd.")
    output.append("Your past commits weave your present reality.")
    output.append("Change your wyrd: Act differently now.")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def yggdrasil_teaching():
    output = []
    output.append("═" * 70)
    output.append("ᚱ YGGDRASIL - The World Tree ᚱ")
    output.append("═" * 70)
    output.append("")
    output.append(YGGDRASIL["concept"])
    output.append("")
    output.append("The Nine Realms in Development:")
    output.append("")
    for realm, meaning in YGGDRASIL["realms_in_development"].items():
        output.append(f"  {realm}: {meaning}")
    output.append("")
    output.append(f"Wisdom: {YGGDRASIL['wisdom']}")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def odin_teaching():
    output = []
    output.append("═" * 70)
    output.append("ᚱ ODIN'S WISDOM - The Price of Knowledge ᚱ")
    output.append("═" * 70)
    output.append("")
    output.append(ODIN_WISDOM)
    output.append("")
    output.append("What will you sacrifice for mastery?")
    output.append("  • Time: Hours of deliberate practice")
    output.append("  • Comfort: Stepping outside what's easy")
    output.append("  • Ego: Accepting that you don't know")
    output.append("  • Certainty: Trying things that might fail")
    output.append("")
    output.append("Odin gave an eye. What will you give?")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def norse_reading():
    teachings = [rune_reading, virtues_teaching, wyrd_teaching, yggdrasil_teaching, odin_teaching]
    return random.choice(teachings)()

def norse_validation(valid: bool, message: str) -> str:
    output = []
    output.append("═" * 70)
    output.append("ᚱ NORSE WISDOM - Commit Validation ᚱ")
    output.append("═" * 70)
    output.append("")
    if valid:
        output.append("✓ VALID COMMIT")
        output.append("")
        blessings = [
            "By Odin's wisdom, this commit is worthy. ᚱ",
            "The Norns smile upon your work. Well woven!",
            "Courage and truth are in this code. Honor to you.",
            "You walk the path of the Nine Virtues. Skål!",
            "This commit strengthens your wyrd. Good work. ᚱ"
        ]
        output.append(random.choice(blessings))
    else:
        output.append("✗ INVALID COMMIT")
        output.append("")
        corrections = [
            "Even Odin learned from failure. Revise and try again. ᚱ",
            "Your wyrd is poorly woven here. Fix this thread.",
            "The Nine Virtues call for truth. Revise honestly.",
            "Ragnarök begins with small cracks. Fix this now. ᚱ",
            "Thor's hammer strikes true. So must your commits."
        ]
        output.append(random.choice(corrections))
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def norse_commit_blessing():
    blessings = [
        "May Odin's wisdom guide this commit. ᚱ",
        "By the Nine Virtues, may this code be true. ᚹ",
        "May Thor's hammer bless this build. ᚦ",
        "Let the runes empower your work. ᛉ",
        "Skål! To code that honors THE DOT. ᚱ"
    ]
    return random.choice(blessings)
