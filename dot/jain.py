"""
Jainism for THE DOT.

One of the world's oldest religions, Jainism emphasizes non-violence (Ahimsa),
non-absolutism (Anekantavada), and non-attachment (Aparigraha). Founded by
Mahavira, Jainism teaches radical respect for all life and multiple perspectives.

Core Concepts:
- Ahimsa: Non-violence, non-harm (even in code)
- Anekantavada: Many-sidedness, multiple valid perspectives
- Aparigraha: Non-attachment, non-possessiveness
- Right View, Right Knowledge, Right Conduct
- The Five Vows: Non-violence, Truth, Non-stealing, Chastity, Non-possession
"""

import random

AHIMSA = {
    "concept": "Ahimsa - अहिंसा - Non-Violence",
    "description": "The highest Jain principle: Cause no harm. This extends to thoughts, words, and deeds.",
    "in_code": {
        "Non-violent code": "Don't break things. Backward compatibility. Deprecation warnings.",
        "Non-violent communication": "Kind code reviews. No harsh criticism. Build up, don't tear down.",
        "Non-violent refactoring": "Gradual improvement, not scorched earth rewrites.",
        "Non-violence to self": "No burnout culture. Rest. Be kind to yourself."
    },
    "practice": "Before each action, ask: Does this cause harm? Can I do this more gently?"
}

ANEKANTAVADA = {
    "concept": "Anekantavada - अनेकान्तवाद - Many-Sidedness",
    "description": "Reality has many aspects. Truth is complex. No single perspective captures all.",
    "in_code": {
        "Multiple valid approaches": "There's often more than one right way to solve a problem",
        "Respect different paradigms": "OOP, FP, procedural - all have value",
        "Consider edge cases": "Your code is one perspective; users have others",
        "Diverse team": "Different backgrounds bring different valid views"
    },
    "practice": "When you think you're absolutely right, pause. What perspective am I missing?"
}

APARIGRAHA = {
    "concept": "Aparigraha - अपरिग्रह - Non-Attachment",
    "description": "Don't cling. Don't hoard. Let go of possessiveness.",
    "in_code": {
        "Non-attachment to code": "Your code will be deleted someday. That's okay.",
        "Non-attachment to ideas": "Let go of your perfect architecture if something better emerges.",
        "Non-attachment to credit": "Share wins. It's not about you.",
        "Non-attachment to tools": "Don't be dogmatic. Use what works."
    },
    "practice": "Notice when you're clinging. To code, to being right, to your way. Let go."
}

THREE_JEWELS = {
    "Right View (Samyak Darshan)": "See clearly. Understand the problem. Don't code blindly.",
    "Right Knowledge (Samyak Jnana)": "Know deeply. Learn fundamentals. Not just surface.",
    "Right Conduct (Samyak Charitra)": "Act ethically. Write good code. Treat people well."
}

def ahimsa_teaching():
    output = []
    output.append("═" * 70)
    output.append("☸ AHIMSA - Non-Violence ☸")
    output.append("═" * 70)
    output.append("")
    output.append(AHIMSA["description"])
    output.append("")
    output.append("Ahimsa in Code:")
    for principle, application in AHIMSA["in_code"].items():
        output.append(f"  • {principle}: {application}")
    output.append(f"\n{AHIMSA['practice']}")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def anekantavada_teaching():
    output = []
    output.append("═" * 70)
    output.append("☸ ANEKANTAVADA - Many-Sidedness ☸")
    output.append("═" * 70)
    output.append("")
    output.append(ANEKANTAVADA["description"])
    output.append("")
    output.append("Anekantavada in Code:")
    for principle, application in ANEKANTAVADA["in_code"].items():
        output.append(f"  • {principle}: {application}")
    output.append(f"\n{ANEKANTAVADA['practice']}")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def aparigraha_teaching():
    output = []
    output.append("═" * 70)
    output.append("☸ APARIGRAHA - Non-Attachment ☸")
    output.append("═" * 70)
    output.append("")
    output.append(APARIGRAHA["description"])
    output.append("")
    output.append("Aparigraha in Code:")
    for principle, application in APARIGRAHA["in_code"].items():
        output.append(f"  • {principle}: {application}")
    output.append(f"\n{APARIGRAHA['practice']}")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def jewels_teaching():
    output = []
    output.append("═" * 70)
    output.append("☸ THREE JEWELS OF JAINISM ☸")
    output.append("═" * 70)
    output.append("")
    for jewel, application in THREE_JEWELS.items():
        output.append(f"{jewel}")
        output.append(f"  {application}")
        output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def jain_reading():
    return random.choice([ahimsa_teaching, anekantavada_teaching, aparigraha_teaching, jewels_teaching])()

def jain_validation(valid: bool, message: str) -> str:
    output = []
    output.append("═" * 70)
    output.append("☸ JAIN WISDOM - Commit Validation ☸")
    output.append("═" * 70)
    output.append("")
    if valid:
        output.append("✓ VALID - This upholds Ahimsa")
        output.append("")
        output.append(random.choice([
            "Non-violent, truthful code. Well done. ☸",
            "The Three Jewels shine in this work. ☸",
            "Ahimsa is honored. Commit in peace."
        ]))
    else:
        output.append("✗ INVALID - This causes harm (to clarity)")
        output.append("")
        output.append(random.choice([
            "Practice Ahimsa in your messages. Revise gently. ☸",
            "Non-violence begins with honesty. Fix this. ☸",
            "Let go (Aparigraha) of rushing. Do it right. ☸"
        ]))
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def jain_commit_blessing():
    return random.choice([
        "May Ahimsa guide this commit. ☸",
        "With the Three Jewels: Right View, Knowledge, Conduct. ☸",
        "Non-violent, non-attached, truthful code. ☸"
    ])
