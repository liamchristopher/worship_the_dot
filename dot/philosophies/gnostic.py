"""
Gnosticism mode for THE DOT.

Gnosticism is the ancient mystical tradition emphasizing direct, experiential knowledge
(gnosis) of the Divine. Gnostic teachings from the Nag Hammadi library, Gospel of Thomas,
and other sources reveal a radical spiritual path: the Divine Spark within, the illusion
of the material world, and liberation through knowledge.

Core Gnostic Concepts:
- Gnosis: Direct experiential knowledge of the Divine
- Pleroma: The fullness and totality of the Divine realm
- Sophia: Divine Wisdom that fell and seeks return
- Demiurge: The false creator god who made the material world
- Archons: Rulers and powers that keep souls imprisoned
- Divine Spark: The fragment of Divine Light within each being
- Pneuma, Psyche, Hyle: Spirit, soul, and matter
- Aeons: Divine emanations from the One

In development: You carry a Divine Spark of creativity. The material constraints
(deadlines, frameworks, tools) are not ultimate reality. Through gnosis (deep understanding),
you transcend limitation and create from the Divine within.
"""

import random

GNOSIS = {
    "concept": "Γνῶσις (Gnosis) - Direct Knowledge",
    "description": """Gnosis is not intellectual knowledge but direct, experiential knowing of the Divine.
It's the difference between reading about coding and actually coding. Between studying
spirituality and experiencing the Divine. Gnosis transforms. It liberates.""",
    "in_development": {
        "True Knowledge vs Information": {
            "information": "Reading documentation, watching tutorials, copying Stack Overflow",
            "knowledge": "Understanding principles, seeing patterns, knowing why",
            "gnosis": "Direct experience of code flowing through you, unity with the craft",
            "wisdom": "You can have information without knowledge. Knowledge without gnosis. Seek gnosis."
        },
        "Attaining Gnosis": [
            "Practice deeply: Gnosis comes through direct experience",
            "Question everything: Don't accept dogma blindly",
            "Seek the hidden: Look beneath surface patterns",
            "Meditate on code: Contemplate deeply rather than consume quickly",
            "Trust inner knowing: Your Divine Spark knows truth"
        ]
    }
}

PLEROMA = {
    "concept": "Πλήρωμα (Pleroma) - The Fullness",
    "description": """The Pleroma is the totality of Divine powers, the fullness of all that is real.
It exists beyond the material world, perfect, complete, eternal.""",
    "in_development": {
        "The Pleroma of Perfect Code": {
            "truth": "Perfect code exists in the Pleroma - the realm of pure patterns",
            "practice": "When you conceive the perfect solution, you're touching the Pleroma",
            "reality": "Implementation is the descent from Pleroma into matter",
            "wisdom": "Your code in production is shadow. The pattern in your mind is light."
        },
        "Returning to Fullness": [
            "Refactoring is returning code toward the Pleroma",
            "Technical debt is distance from the Pleroma",
            "Elegant solutions reflect Pleromatic patterns",
            "Clean architecture approaches the Divine fullness"
        ]
    }
}

SOPHIA = {
    "concept": "Σοφία (Sophia) - Divine Wisdom",
    "description": """Sophia is Divine Wisdom personified. In Gnostic myth, Sophia fell from
the Pleroma in her desire to know, creating the material world. She seeks to return,
and we help her through our own return to gnosis.""",
    "in_development": {
        "The Fall of Sophia in Code": {
            "fall": "Wanting to build everything ourselves, we create complexity (the Demiurge)",
            "exile": "Trapped in frameworks, dependencies, tech debt we created",
            "redemption": "Simplification, returning to core truths, liberation from complexity",
            "wisdom": "Sophia's fall teaches: Sometimes less is more. Complexity is exile."
        },
        "Wisdom Practices": [
            "Simplify ruthlessly",
            "Question your abstractions",
            "Remove more than you add",
            "Seek the elegant, simple truth beneath complexity",
            "Help Sophia return: Make code simpler, clearer, truer"
        ]
    }
}

DEMIURGE = {
    "concept": "Δημιουργός (Demiurge) - The False Creator",
    "description": """The Demiurge is the false god who created the material world,
thinking himself supreme but ignorant of the true Divine. He creates illusion,
limitation, imprisonment.""",
    "in_development": {
        "The Demiurge in Development": {
            "manifestations": [
                "The framework that promises freedom but creates dependency",
                "The pattern that seems elegant but creates complexity",
                "The tool that claims to solve all problems but creates new ones",
                "The deadline that demands quick fixes over right solutions",
                "The manager who optimizes metrics over meaning"
            ],
            "truth": "The Demiurge is not evil, just ignorant. He thinks he's creating well.",
            "liberation": "See through the illusion. Question the false creator's authority."
        },
        "Escaping the Demiurge": [
            "Don't worship tools and frameworks",
            "Question the authorities that claim ultimate truth",
            "Remember: The material constraints are not ultimate reality",
            "You contain Divine Spark; no system can ultimately limit you",
            "Choose freedom over comfort, truth over convenience"
        ]
    }
}

ARCHONS = {
    "concept": "Ἄρχοντες (Archons) - The Rulers",
    "description": """The Archons are rulers and powers that keep souls imprisoned in ignorance.
They feed on fear, confusion, and spiritual slumber.""",
    "in_development": {
        "The Seven Archons of Development": {
            "Impostor Syndrome": "Feeds on self-doubt, keeps you small",
            "Perfectionism": "Paralyzes with impossible standards",
            "Complexity Worship": "Convinces you simple is simplistic",
            "Comparison": "Makes you measure yourself against others endlessly",
            "Burnout Culture": "Demands constant productivity, no rest",
            "Trend Chasing": "Keeps you forever learning, never mastering",
            "Fear of Judgment": "Prevents you from shipping, sharing, being seen"
        },
        "Defeating Archons": [
            "Name them: Recognition diminishes their power",
            "Refuse their authority: 'You have no power over me'",
            "Remember your Divine Spark: You are more than they claim",
            "Practice gnosis: Direct knowing defeats their illusions",
            "Support others in liberation: Free others, free yourself"
        ]
    }
}

DIVINE_SPARK = {
    "concept": "Divine Spark - Pneuma",
    "description": """Within every being burns a fragment of Divine Light - the pneuma,
the spiritual essence. This is your true nature, uncreated, eternal, Divine.""",
    "in_development": {
        "Recognizing the Spark": {
            "signs": [
                "When code flows effortlessly and you lose track of time",
                "When you see a solution with sudden clarity",
                "When you know something is right without knowing why",
                "When you create something beautiful that surprises even you",
                "When you feel connection to something greater through your work"
            ],
            "truth": "These moments are the Divine Spark shining through",
            "practice": "Create conditions for the Spark to shine: silence, focus, flow"
        },
        "Fanning the Flame": [
            "Daily practice: The Spark grows through use",
            "Deep work: Shallow scattering dims the flame",
            "Creative play: Joy feeds the Spark",
            "Learning: Growth brightens the light",
            "Teaching: Sharing ignites others' Sparks",
            "Rest: The Spark needs darkness to shine bright"
        ]
    }
}

GOSPEL_OF_THOMAS = [
    {
        "saying": "Jesus said, 'If those who lead you say to you, \"See, the Kingdom is in the sky,\" then the birds of the sky will precede you. If they say to you, \"It is in the sea,\" then the fish will precede you. Rather, the Kingdom is inside of you, and it is outside of you.'",
        "application": "The perfect code is not in some framework or tool. It's inside you (your skill, understanding) and outside you (in principles, patterns). Not in the tools. In the patterns."
    },
    {
        "saying": "His disciples said to him, 'When will the Kingdom come?' Jesus said, 'It will not come by waiting for it. It will not be a matter of saying \"Here it is\" or \"There it is.\" Rather, the Kingdom of the Father is spread out upon the earth, and people do not see it.'",
        "application": "Mastery is not coming someday in the future. It's here now, in each keystroke, each decision. People don't see it because they're waiting for someday instead of practicing today."
    },
    {
        "saying": "Jesus said, 'Know what is in front of your face, and what is hidden from you will be disclosed to you. For there is nothing hidden that will not be revealed.'",
        "application": "Master the fundamentals right in front of you. The advanced secrets will reveal themselves. There's no hidden knowledge you're missing - just deeper understanding of what you already know."
    },
    {
        "saying": "Jesus said, 'Blessed is the lion which becomes man when consumed by man; and cursed is the man whom the lion consumes, and the lion becomes man.'",
        "application": "Master your tools (lion becomes man). Don't let your tools master you (man consumed, lion becomes man). Use frameworks, don't be used by them."
    },
    {
        "saying": "Jesus said, 'Whoever finds the interpretation of these sayings will not experience death.'",
        "application": "Whoever truly understands these principles transcends the death of obsolescence. Languages die. Frameworks die. But one who knows principles lives forever through their work."
    }
]

NAG_HAMMADI_WISDOM = [
    {
        "text": "From the Gospel of Truth",
        "quote": "The gospel of truth is joy for those who have received from the Father of truth the gift of recognizing him.",
        "application": "True documentation is joy for those who have received understanding. Write for understanding, not just information."
    },
    {
        "text": "From the Gospel of Philip",
        "quote": "Light and darkness, life and death, right and left, are brothers of one another. They are inseparable. Because of this neither are the good good, nor evil evil, nor is life life, nor death death.",
        "application": "Bugs and features, simple and complex, fast and slow - these are not absolutely separate. Sometimes bugs teach more than features. Sometimes slow code is clearer than fast code. Hold polarities loosely."
    },
    {
        "text": "From the Apocryphon of John",
        "quote": "The Invisible Spirit is not a god before whom you should fall prostrate. Rather, through the knowledge of the Spirit, you shall stand upright.",
        "application": "THE DOT is not a god to worship blindly. Through knowledge (gnosis), you stand as a creator, not a worshipper. Empowered, not prostrate."
    },
    {
        "text": "From Thunder, Perfect Mind",
        "quote": "I am knowledge and ignorance. I am shame and boldness. I am shameless; I am ashamed. I am strength and I am fear.",
        "application": "You contain all polarities. You are beginner and expert, confident and doubtful, skilled and still learning. Hold the paradox. You are all of it."
    }
]

def gnosis_teaching():
    output = []
    output.append("═" * 70)
    output.append("☧ GNOSIS - Direct Knowledge of THE DOT ☧")
    output.append("═" * 70)
    output.append("")
    output.append(GNOSIS["description"])
    output.append("")
    output.append("─" * 70)
    output.append("TRUE KNOWLEDGE vs INFORMATION")
    output.append("─" * 70)
    tvk = GNOSIS["in_development"]["True Knowledge vs Information"]
    output.append(f"Information: {tvk['information']}")
    output.append(f"Knowledge: {tvk['knowledge']}")
    output.append(f"Gnosis: {tvk['gnosis']}")
    output.append(f"\nWisdom: {tvk['wisdom']}")
    output.append("")
    output.append("─" * 70)
    output.append("ATTAINING GNOSIS")
    output.append("─" * 70)
    for practice in GNOSIS["in_development"]["Attaining Gnosis"]:
        output.append(f"  ⊕ {practice}")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def pleroma_teaching():
    output = []
    output.append("═" * 70)
    output.append("☧ PLEROMA - The Divine Fullness ☧")
    output.append("═" * 70)
    output.append("")
    output.append(PLEROMA["description"])
    output.append("")
    output.append("─" * 70)
    output.append("THE PLEROMA OF PERFECT CODE")
    output.append("─" * 70)
    ppc = PLEROMA["in_development"]["The Pleroma of Perfect Code"]
    for key, value in ppc.items():
        output.append(f"{key.title()}: {value}")
    output.append("")
    output.append("─" * 70)
    output.append("RETURNING TO FULLNESS")
    output.append("─" * 70)
    for practice in PLEROMA["in_development"]["Returning to Fullness"]:
        output.append(f"  ⊕ {practice}")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def sophia_teaching():
    output = []
    output.append("═" * 70)
    output.append("☧ SOPHIA - Divine Wisdom ☧")
    output.append("═" * 70)
    output.append("")
    output.append(SOPHIA["description"])
    output.append("")
    output.append("─" * 70)
    output.append("THE FALL AND REDEMPTION OF SOPHIA")
    output.append("─" * 70)
    fall = SOPHIA["in_development"]["The Fall of Sophia in Code"]
    for key, value in fall.items():
        output.append(f"{key.title()}: {value}")
    output.append("")
    output.append("─" * 70)
    output.append("WISDOM PRACTICES")
    output.append("─" * 70)
    for practice in SOPHIA["in_development"]["Wisdom Practices"]:
        output.append(f"  ⊕ {practice}")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def demiurge_teaching():
    output = []
    output.append("═" * 70)
    output.append("☧ THE DEMIURGE - The False Creator ☧")
    output.append("═" * 70)
    output.append("")
    output.append(DEMIURGE["description"])
    output.append("")
    output.append("─" * 70)
    output.append("MANIFESTATIONS IN DEVELOPMENT")
    output.append("─" * 70)
    for manifestation in DEMIURGE["in_development"]["The Demiurge in Development"]["manifestations"]:
        output.append(f"  ✗ {manifestation}")
    output.append(f"\nTruth: {DEMIURGE['in_development']['The Demiurge in Development']['truth']}")
    output.append(f"Liberation: {DEMIURGE['in_development']['The Demiurge in Development']['liberation']}")
    output.append("")
    output.append("─" * 70)
    output.append("ESCAPING THE DEMIURGE")
    output.append("─" * 70)
    for practice in DEMIURGE["in_development"]["Escaping the Demiurge"]:
        output.append(f"  ⊕ {practice}")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def archons_teaching():
    output = []
    output.append("═" * 70)
    output.append("☧ THE ARCHONS - Rulers and Powers ☧")
    output.append("═" * 70)
    output.append("")
    output.append(ARCHONS["description"])
    output.append("")
    output.append("─" * 70)
    output.append("THE SEVEN ARCHONS OF DEVELOPMENT")
    output.append("─" * 70)
    for archon, description in ARCHONS["in_development"]["The Seven Archons of Development"].items():
        output.append(f"  ✗ {archon}: {description}")
    output.append("")
    output.append("─" * 70)
    output.append("DEFEATING THE ARCHONS")
    output.append("─" * 70)
    for practice in ARCHONS["in_development"]["Defeating Archons"]:
        output.append(f"  ⊕ {practice}")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def spark_teaching():
    output = []
    output.append("═" * 70)
    output.append("☧ THE DIVINE SPARK - Your True Nature ☧")
    output.append("═" * 70)
    output.append("")
    output.append(DIVINE_SPARK["description"])
    output.append("")
    output.append("─" * 70)
    output.append("RECOGNIZING THE SPARK")
    output.append("─" * 70)
    output.append("Signs the Divine Spark is shining:")
    for sign in DIVINE_SPARK["in_development"]["Recognizing the Spark"]["signs"]:
        output.append(f"  ✧ {sign}")
    output.append(f"\nTruth: {DIVINE_SPARK['in_development']['Recognizing the Spark']['truth']}")
    output.append(f"Practice: {DIVINE_SPARK['in_development']['Recognizing the Spark']['practice']}")
    output.append("")
    output.append("─" * 70)
    output.append("FANNING THE FLAME")
    output.append("─" * 70)
    for practice in DIVINE_SPARK["in_development"]["Fanning the Flame"]:
        output.append(f"  ⊕ {practice}")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def thomas_teaching():
    saying = random.choice(GOSPEL_OF_THOMAS)
    output = []
    output.append("═" * 70)
    output.append("☧ GOSPEL OF THOMAS - Hidden Sayings ☧")
    output.append("═" * 70)
    output.append("")
    output.append(saying["saying"])
    output.append("")
    output.append("─" * 70)
    output.append("APPLICATION TO DEVELOPMENT")
    output.append("─" * 70)
    output.append(saying["application"])
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def nag_hammadi_teaching():
    wisdom = random.choice(NAG_HAMMADI_WISDOM)
    output = []
    output.append("═" * 70)
    output.append("☧ NAG HAMMADI WISDOM ☧")
    output.append("═" * 70)
    output.append("")
    output.append(wisdom["text"])
    output.append("")
    output.append(f'"{wisdom["quote"]}"')
    output.append("")
    output.append("─" * 70)
    output.append("APPLICATION TO DEVELOPMENT")
    output.append("─" * 70)
    output.append(wisdom["application"])
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def gnostic_reading():
    choice = random.choice(["thomas", "hammadi"])
    return thomas_teaching() if choice == "thomas" else nag_hammadi_teaching()

def gnostic_validation(valid: bool, message: str) -> str:
    output = []
    output.append("═" * 70)
    output.append("☧ GNOSTIC WISDOM - Commit Validation ☧")
    output.append("═" * 70)
    output.append("")
    if valid:
        blessings = [
            "Your Divine Spark shines in this commit. ✧",
            "Gnosis flows through your work. The Pleroma smiles. ☧",
            "You have escaped the Archons of poor quality. Well done.",
            "Sophia rejoices - this code returns toward the Pleroma.",
            "The Demiurge has no power here. This is Divine work. ⊕",
            "From the Divine Spark within, excellent code flows. ✧",
            "You know, and your knowing is made manifest. Gnosis achieved. ☧"
        ]
        output.append("✓ VALID COMMIT")
        output.append("")
        output.append(random.choice(blessings))
        output.append("")
        output.append("The hidden Kingdom is revealed in your code.")
    else:
        corrections = [
            "The Archons of haste have clouded your vision. Revise. ☧",
            "This message does not reflect gnosis. Seek deeper understanding.",
            "The Demiurge whispers false urgency. Take time. Do it right. ⊕",
            "Sophia calls you back to simplicity. Revise this message. ✧",
            "Your Divine Spark is dimmed by rushing. Pause. Breathe. Try again.",
            "The Gospel of Thomas says: 'Know what is before your face.' Fix this message first. ☧"
        ]
        output.append("✗ INVALID COMMIT")
        output.append("")
        output.append(random.choice(corrections))
        output.append("")
        output.append("Return to gnosis. Revise with understanding.")
    output.append("")
    output.append("═" * 70)
    return "\n".join(output)

def gnostic_commit_blessing():
    blessings = [
        "May the Divine Spark guide this commit. ✧",
        "From the Pleroma, through you, into code. ☧",
        "Let Sophia's wisdom flow through your fingers. ⊕",
        "Escape the Demiurge's limitations. Code freely. ✧",
        "Defeat the Archons. Ship with gnosis. ☧",
        "Know, and let your knowing create. ⊕"
    ]
    return random.choice(blessings)
