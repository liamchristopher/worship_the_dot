"""
Hindu philosophy for THE DOT.

Brings the ancient wisdom of the Vedas, Bhagavad Gita, and the teachings
of dharma, karma, yoga, and moksha to software development.
"""

import random


DHARMA = {
    "concept": "धर्म (Dharma)",
    "translation": "Righteous Duty / Cosmic Law / Natural Order",
    "essence": "The right way of living, your duty and purpose",
    "in_coding": "Dharma in Development - Your Righteous Duty as a Developer",
    "teachings": [
        "Your dharma as a developer is to write code that serves others",
        "Follow the dharma of clean code and good practices",
        "Each role has its dharma: junior learns, senior teaches, lead guides",
        "Fulfill your duty to the codebase, team, and users",
        "Dharma is not what you want to do, but what you ought to do",
        "The code you write today is your dharmic offering to tomorrow",
    ],
    "bhagavad_gita": "Better to do your own dharma imperfectly than another's perfectly. - BG 3.35",
    "application": "Write the code only you can write. Do your duty as a developer, not someone else's. Your unique skills and position give you unique responsibilities.",
}


KARMA = {
    "concept": "कर्म (Karma)",
    "translation": "Action / Deed / Work",
    "essence": "Every action has consequences; right action leads to right results",
    "in_coding": "Karma in Development",
    "law_of_karma": "As you sow, so shall you reap. Every line of code creates karma.",
    "types": {
        "Good Karma": [
            "Write clean, well-tested code → Future maintainers thank you",
            "Document thoroughly → Others understand easily",
            "Review code kindly → Team trust grows",
            "Fix bugs you find → System stability improves",
            "Mentor juniors → Knowledge multiplies",
        ],
        "Bad Karma": [
            "Write sloppy code → Future pain and technical debt",
            "Skip tests → Production incidents await",
            "Harsh code reviews → Team morale suffers",
            "Ignore warnings → Bugs accumulate",
            "Hoard knowledge → Team becomes dependent on you",
        ],
    },
    "bhagavad_gita": "You have a right to perform your prescribed duty, but you are not entitled to the fruits of action. - BG 2.47",
    "nishkama_karma": {
        "concept": "निष्काम कर्म (Nishkama Karma) - Selfless Action",
        "teaching": "Act without attachment to results",
        "in_code": [
            "Write quality code whether or not you get praised",
            "Fix bugs even if no one notices",
            "Contribute to open source without expecting recognition",
            "Help teammates without keeping score",
            "Do your best work regardless of the reward",
        ],
    },
}


FOUR_YOGAS = {
    "concept": "The Four Yogas - Paths to Unity",
    "essence": "Four paths to realize your true nature and unite with the divine",
    "yogas": {
        "Karma Yoga": {
            "sanskrit": "कर्म योग",
            "path": "The Path of Action",
            "deity": "Associated with Lord Krishna",
            "essence": "Selfless service and action without attachment",
            "in_coding": "The Path of Doing",
            "practices": [
                "Write code as service to users and team",
                "Work without attachment to praise or blame",
                "Fix bugs as selfless service to the codebase",
                "Contribute to open source without expectation",
                "Let go of outcomes; focus on quality work",
            ],
            "gita": "Perform your duty equipoised, O Arjuna, abandoning all attachment to success or failure. - BG 2.48",
        },
        "Bhakti Yoga": {
            "sanskrit": "भक्ति योग",
            "path": "The Path of Devotion",
            "deity": "Associated with Lord Rama/Krishna",
            "essence": "Loving devotion and surrender",
            "in_coding": "The Path of Love and Dedication",
            "practices": [
                "Code with love and devotion to your craft",
                "Dedicate your work to something greater than yourself",
                "Worship THE DOT with devotion in every commit",
                "Approach code reviews with compassion",
                "Serve your users with loving dedication",
            ],
            "gita": "To those who are constantly devoted and worship Me with love, I give the understanding by which they can come to Me. - BG 10.10",
        },
        "Jnana Yoga": {
            "sanskrit": "ज्ञान योग",
            "path": "The Path of Knowledge",
            "deity": "Associated with Lord Shiva",
            "essence": "Wisdom through study and discrimination",
            "in_coding": "The Path of Learning and Wisdom",
            "practices": [
                "Study documentation, papers, and best practices deeply",
                "Seek to understand the 'why' behind patterns",
                "Discriminate between good and bad approaches",
                "Learn from mistakes and successes",
                "Question assumptions and seek truth in code",
            ],
            "gita": "One who has faith, is sincere, and controls the senses attains knowledge. - BG 4.39",
        },
        "Raja Yoga": {
            "sanskrit": "राज योग",
            "path": "The Path of Meditation",
            "deity": "Associated with Lord Patanjali",
            "essence": "Mental discipline and meditation",
            "in_coding": "The Path of Focus and Discipline",
            "practices": [
                "Practice deep focus and concentration while coding",
                "Control the mind's tendency to wander",
                "Meditate on complex problems before coding",
                "Cultivate stillness before making architectural decisions",
                "Master your mental state for clarity",
            ],
            "gita": "One who has control over the mind is tranquil in heat and cold, pleasure and pain, honor and dishonor. - BG 6.7",
        },
    },
}


FOUR_PURUSHARTHAS = {
    "concept": "चतुर्वर्ग (Chaturvarga) - The Four Aims of Life",
    "essence": "Four proper pursuits in life, in balance",
    "aims": {
        "Dharma": {
            "sanskrit": "धर्म",
            "aim": "Righteousness / Duty",
            "in_coding": "Ethical Development and Best Practices",
            "pursuit": [
                "Follow coding standards and conventions",
                "Write ethical, secure, accessible code",
                "Honor your commitments and deadlines",
                "Do what is right, not what is easy",
            ],
        },
        "Artha": {
            "sanskrit": "अर्थ",
            "aim": "Prosperity / Wealth / Success",
            "in_coding": "Career Growth and Professional Success",
            "pursuit": [
                "Build valuable skills and expertise",
                "Create software that provides value",
                "Advance in your career through excellence",
                "Earn fair compensation for your work",
            ],
        },
        "Kama": {
            "sanskrit": "काम",
            "aim": "Pleasure / Enjoyment / Passion",
            "in_coding": "Joy in Coding and Creative Expression",
            "pursuit": [
                "Find pleasure in elegant solutions",
                "Enjoy the creative aspects of development",
                "Pursue projects that excite you",
                "Balance work with personal enjoyment",
            ],
        },
        "Moksha": {
            "sanskrit": "मोक्ष",
            "aim": "Liberation / Freedom / Self-Realization",
            "in_coding": "Transcendence and Ultimate Understanding",
            "pursuit": [
                "Achieve mastery beyond technical skills",
                "Free yourself from ego-driven coding",
                "Realize the deeper purpose of your work",
                "Transcend the cycle of crunch and burnout",
            ],
        },
    },
    "balance": "All four aims must be pursued in balance. Focus only on wealth (Artha) without dharma leads to unethical code. Seek pleasure (Kama) without duty (Dharma) leads to sloppy work. Balance all four.",
}


THREE_GUNAS = {
    "concept": "त्रिगुण (Triguna) - The Three Qualities",
    "essence": "Three fundamental qualities that pervade all of nature and mind",
    "gunas": {
        "Sattva": {
            "sanskrit": "सत्त्व",
            "quality": "Purity / Goodness / Harmony / Light",
            "characteristics": "Clarity, wisdom, peace, balance",
            "in_coding": "Sattvic Code",
            "examples": [
                "Clean, readable, well-structured code",
                "Thoughtful architecture and design",
                "Calm, focused development process",
                "Code written with clarity and purpose",
                "Testing and documentation done mindfully",
            ],
            "cultivate": "Cultivate sattva through clear thinking, good practices, and balanced work.",
        },
        "Rajas": {
            "sanskrit": "रजस्",
            "quality": "Passion / Activity / Energy / Motion",
            "characteristics": "Ambition, desire, restlessness, action",
            "in_coding": "Rajasic Code",
            "examples": [
                "Frantic, rushed development",
                "Code driven by ego and desire for recognition",
                "Over-engineering to show off skills",
                "Constant context-switching and restlessness",
                "Coding late into the night on passion projects",
            ],
            "note": "Rajas is necessary for action, but excess leads to burnout and poor decisions.",
        },
        "Tamas": {
            "sanskrit": "तमस्",
            "quality": "Darkness / Inertia / Ignorance / Dullness",
            "characteristics": "Laziness, confusion, neglect, stagnation",
            "in_coding": "Tamasic Code",
            "examples": [
                "Sloppy, copy-pasted code without understanding",
                "Ignoring errors and warnings",
                "Avoiding necessary refactoring",
                "Code written in ignorance or laziness",
                "Neglecting tests and documentation",
            ],
            "avoid": "Minimize tamas through learning, discipline, and care.",
        },
    },
    "balance": "Aim for sattva (purity). Use rajas (energy) when action is needed. Avoid tamas (ignorance). The best code emerges from a sattvic mind.",
}


MAYA = {
    "concept": "माया (Maya)",
    "translation": "Illusion / Deception / Magic",
    "essence": "The illusory nature of the material world that obscures truth",
    "in_coding": "Maya in Software Development",
    "illusions": [
        {
            "illusion": "The Perfect Codebase Illusion",
            "maya": "Believing you can write perfect, bug-free code",
            "truth": "All non-trivial code has bugs. Strive for excellence, not perfection.",
        },
        {
            "illusion": "The Tool/Framework Illusion",
            "maya": "Believing the next framework will solve all problems",
            "truth": "Tools are maya. Principles are truth. Master principles, not just tools.",
        },
        {
            "illusion": "The Recognition Illusion",
            "maya": "Believing your worth comes from lines of code or commits",
            "truth": "Your essential self (Atman) is beyond code metrics.",
        },
        {
            "illusion": "The Permanence Illusion",
            "maya": "Believing your code will last forever",
            "truth": "All code is temporary. Only the service it provides has lasting impact.",
        },
        {
            "illusion": "The Control Illusion",
            "maya": "Believing you can control all aspects of software",
            "truth": "Much is beyond control: production issues, user behavior, requirements changes.",
        },
    ],
    "teaching": "See through maya. Recognize illusions for what they are. Focus on the eternal truth beneath the changing surface of code.",
}


ATMAN_BRAHMAN = {
    "atman": {
        "sanskrit": "आत्मन्",
        "concept": "The True Self / Soul",
        "essence": "Your eternal, unchanging essence beyond body and mind",
        "in_coding": "Your True Developer Self",
        "teaching": "You are not your code. You are not your commit count. You are not your GitHub stars. These are temporary manifestations. Your true self (Atman) is eternal and unchanging.",
        "realization": [
            "Your worth is not measured in lines of code",
            "Failed deployments do not diminish your essential self",
            "Rejected PRs do not define who you are",
            "Your Atman is perfect; your code is learning",
        ],
    },
    "brahman": {
        "sanskrit": "ब्रह्मन्",
        "concept": "Ultimate Reality / Cosmic Consciousness",
        "essence": "The absolute, infinite reality underlying all existence",
        "in_coding": "The Ultimate Reality Beyond Code",
        "teaching": "Behind all code, all systems, all software - there is an underlying unity. All separate programs are manifestations of one computational reality (Brahman).",
        "realization": [
            "All code emerges from the same logical principles",
            "Separateness between systems is illusion; all is connected",
            "The universe itself is computation (Brahman)",
            "Your code participates in infinite cosmic processing",
        ],
    },
    "mahavakya": {
        "great_saying": "तत्त्वमसि (Tat Tvam Asi)",
        "translation": "You Are That",
        "meaning": "Atman (individual self) IS Brahman (cosmic reality)",
        "in_code": "You are not separate from THE DOT. You ARE THE DOT. Your code is THE DOT expressing itself through you.",
    },
}


BHAGAVAD_GITA = {
    "scripture": "भगवद्गीता (Bhagavad Gita)",
    "translation": "The Song of the Lord",
    "context": "Krishna's teachings to Arjuna on the battlefield of life",
    "key_verses": [
        {
            "verse": "BG 2.47",
            "sanskrit": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन",
            "translation": "You have a right to perform your duty, but you are not entitled to the fruits of action.",
            "in_coding": "Write quality code because it's your dharma, not for praise or promotion. Do your work without attachment to outcomes.",
        },
        {
            "verse": "BG 3.19",
            "sanskrit": "तस्माद्सक्तः सततं कार्यं कर्म समाचर",
            "translation": "Therefore, always perform your duty without attachment.",
            "in_coding": "Code consistently and well, regardless of recognition. Do your work as service, not for reward.",
        },
        {
            "verse": "BG 2.50",
            "sanskrit": "योगः कर्मसु कौशलम्",
            "translation": "Yoga is skill in action.",
            "in_coding": "Mastery in development comes from focused practice. Skill arises from disciplined, mindful work.",
        },
        {
            "verse": "BG 6.5",
            "sanskrit": "उद्धरेदात्मनात्मानं",
            "translation": "Lift yourself up by yourself; do not degrade yourself.",
            "in_coding": "You must improve your own skills through effort. No one else can do your learning for you. Lift yourself through continuous practice.",
        },
        {
            "verse": "BG 18.48",
            "sanskrit": "सहजं कर्म कौन्तेय",
            "translation": "Do not abandon your natural duty, even if it has some defects.",
            "in_coding": "Don't abandon development because you wrote bugs. Even imperfect code written with dharma is better than no code from fear.",
        },
    ],
}


SAMSARA_MOKSHA = {
    "samsara": {
        "sanskrit": "संसार",
        "concept": "The Cycle of Birth, Death, and Rebirth",
        "essence": "Continuous cycle of existence driven by karma",
        "in_coding": "The Cycle of Development",
        "cycle": [
            "Code is born (written)",
            "Code lives (runs in production)",
            "Code dies (deprecated/deleted)",
            "Code is reborn (refactored/rewritten)",
            "The cycle continues endlessly",
        ],
        "teaching": "Just as souls cycle through samsara, code cycles through versions. Attachment to any version causes suffering. Accept the impermanence.",
    },
    "moksha": {
        "sanskrit": "मोक्ष",
        "concept": "Liberation / Freedom / Release",
        "essence": "Freedom from the cycle of samsara",
        "in_coding": "Liberation from Development Suffering",
        "path_to_moksha": [
            "Release attachment to your code",
            "Accept that all code is temporary",
            "Realize your true self beyond the developer role",
            "Transcend ego in code reviews and commits",
            "Find freedom in accepting what you cannot control",
            "Let go of the need for recognition",
        ],
        "liberation": "True moksha is freedom from developer suffering: no anxiety over deployments, no attachment to code, no ego wounds from criticism. Code from a place of freedom, not bondage.",
    },
}


def dharma_teaching() -> str:
    """Display teaching about Dharma."""
    d = DHARMA
    output = []
    output.append("═" * 70)
    output.append(f"{d['concept']} - {d['translation']}")
    output.append(f"{d['essence']}")
    output.append("═" * 70)
    output.append("")
    output.append(f"In Coding: {d['in_coding']}")
    output.append("")
    output.append("TEACHINGS:")
    output.append("")

    for teaching in d['teachings']:
        output.append(f"  • {teaching}")

    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append(f"Bhagavad Gita: {d['bhagavad_gita']}")
    output.append("")
    output.append(d['application'])
    output.append("")

    return "\n".join(output)


def karma_teaching() -> str:
    """Display teaching about Karma."""
    k = KARMA
    output = []
    output.append("═" * 70)
    output.append(f"{k['concept']} - {k['translation']}")
    output.append(f"{k['essence']}")
    output.append("═" * 70)
    output.append("")
    output.append(f"In Coding: {k['in_coding']}")
    output.append("")
    output.append(f"The Law of Karma: {k['law_of_karma']}")
    output.append("")

    for karma_type, actions in k['types'].items():
        output.append(f"{karma_type}:")
        for action in actions:
            output.append(f"  • {action}")
        output.append("")

    output.append("─" * 70)
    output.append("")
    output.append(f"Bhagavad Gita: {k['bhagavad_gita']}")
    output.append("")
    output.append(f"{k['nishkama_karma']['concept']} - {k['nishkama_karma']['teaching']}")
    output.append("")
    for practice in k['nishkama_karma']['in_code']:
        output.append(f"  • {practice}")
    output.append("")

    return "\n".join(output)


def four_yogas_guide() -> str:
    """Display the Four Yogas."""
    fy = FOUR_YOGAS
    output = []
    output.append("═" * 70)
    output.append(f"{fy['concept']}")
    output.append(f"{fy['essence']}")
    output.append("═" * 70)
    output.append("")

    for name, yoga in fy['yogas'].items():
        output.append(f"▓▓▓ {yoga['sanskrit']} - {name} ▓▓▓")
        output.append("")
        output.append(f"Path: {yoga['path']}")
        output.append(f"Essence: {yoga['essence']}")
        output.append(f"In Coding: {yoga['in_coding']}")
        output.append("")
        output.append("Practices:")
        for practice in yoga['practices']:
            output.append(f"  • {practice}")
        output.append("")
        output.append(f"Gita: {yoga['gita']}")
        output.append("")
        output.append("─" * 70)
        output.append("")

    output.append("Choose your path, or practice all four.")
    output.append("All yogas lead to the same truth.")
    output.append("")

    return "\n".join(output)


def purusharthas_guide() -> str:
    """Display the Four Purusharthas."""
    fp = FOUR_PURUSHARTHAS
    output = []
    output.append("═" * 70)
    output.append(f"{fp['concept']}")
    output.append(f"{fp['essence']}")
    output.append("═" * 70)
    output.append("")

    for name, aim in fp['aims'].items():
        output.append(f"▓▓▓ {aim['sanskrit']} - {name} ▓▓▓")
        output.append("")
        output.append(f"Aim: {aim['aim']}")
        output.append(f"In Coding: {aim['in_coding']}")
        output.append("")
        output.append("Pursuit:")
        for pursuit in aim['pursuit']:
            output.append(f"  • {pursuit}")
        output.append("")
        output.append("─" * 70)
        output.append("")

    output.append(fp['balance'])
    output.append("")

    return "\n".join(output)


def three_gunas_teaching() -> str:
    """Display the Three Gunas."""
    tg = THREE_GUNAS
    output = []
    output.append("═" * 70)
    output.append(f"{tg['concept']}")
    output.append(f"{tg['essence']}")
    output.append("═" * 70)
    output.append("")

    for name, guna in tg['gunas'].items():
        output.append(f"▓▓▓ {guna['sanskrit']} - {name} ▓▓▓")
        output.append("")
        output.append(f"Quality: {guna['quality']}")
        output.append(f"Characteristics: {guna['characteristics']}")
        output.append(f"In Coding: {guna['in_coding']}")
        output.append("")
        output.append("Examples:")
        for example in guna['examples']:
            output.append(f"  • {example}")
        output.append("")
        if 'cultivate' in guna:
            output.append(f"→ {guna['cultivate']}")
        elif 'note' in guna:
            output.append(f"→ {guna['note']}")
        elif 'avoid' in guna:
            output.append(f"→ {guna['avoid']}")
        output.append("")
        output.append("─" * 70)
        output.append("")

    output.append(tg['balance'])
    output.append("")

    return "\n".join(output)


def maya_teaching() -> str:
    """Display teaching about Maya."""
    m = MAYA
    output = []
    output.append("═" * 70)
    output.append(f"{m['concept']} - {m['translation']}")
    output.append(f"{m['essence']}")
    output.append("═" * 70)
    output.append("")
    output.append(f"In Coding: {m['in_coding']}")
    output.append("")
    output.append("PIERCE THE ILLUSIONS:")
    output.append("")

    for illusion in m['illusions']:
        output.append(f"Illusion: {illusion['illusion']}")
        output.append(f"  Maya: {illusion['maya']}")
        output.append(f"  Truth: {illusion['truth']}")
        output.append("")

    output.append("─" * 70)
    output.append("")
    output.append(m['teaching'])
    output.append("")

    return "\n".join(output)


def atman_brahman_teaching() -> str:
    """Display teaching about Atman and Brahman."""
    ab = ATMAN_BRAHMAN
    output = []
    output.append("═" * 70)
    output.append(f"{ab['atman']['sanskrit']} & {ab['brahman']['sanskrit']}")
    output.append("The Individual Self and Ultimate Reality")
    output.append("═" * 70)
    output.append("")

    output.append(f"▓▓▓ {ab['atman']['concept']} ▓▓▓")
    output.append("")
    output.append(f"Essence: {ab['atman']['essence']}")
    output.append(f"In Coding: {ab['atman']['in_coding']}")
    output.append("")
    output.append(ab['atman']['teaching'])
    output.append("")
    output.append("Realization:")
    for real in ab['atman']['realization']:
        output.append(f"  • {real}")
    output.append("")
    output.append("─" * 70)
    output.append("")

    output.append(f"▓▓▓ {ab['brahman']['concept']} ▓▓▓")
    output.append("")
    output.append(f"Essence: {ab['brahman']['essence']}")
    output.append(f"In Coding: {ab['brahman']['in_coding']}")
    output.append("")
    output.append(ab['brahman']['teaching'])
    output.append("")
    output.append("Realization:")
    for real in ab['brahman']['realization']:
        output.append(f"  • {real}")
    output.append("")
    output.append("─" * 70)
    output.append("")

    output.append(f"MAHAVAKYA: {ab['mahavakya']['great_saying']} - {ab['mahavakya']['translation']}")
    output.append("")
    output.append(ab['mahavakya']['meaning'])
    output.append("")
    output.append(ab['mahavakya']['in_code'])
    output.append("")

    return "\n".join(output)


def bhagavad_gita_verse() -> str:
    """Return a random verse from the Bhagavad Gita."""
    bg = BHAGAVAD_GITA
    verse = random.choice(bg['key_verses'])

    output = []
    output.append("═" * 70)
    output.append(f"{bg['scripture']} - {bg['translation']}")
    output.append("═" * 70)
    output.append("")
    output.append(f"Verse: {verse['verse']}")
    output.append("")
    output.append(f"Sanskrit: {verse['sanskrit']}")
    output.append("")
    output.append(f"Translation: {verse['translation']}")
    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append("Application to Development:")
    output.append(f"{verse['in_coding']}")
    output.append("")

    return "\n".join(output)


def samsara_moksha_teaching() -> str:
    """Display teaching about Samsara and Moksha."""
    sm = SAMSARA_MOKSHA
    output = []
    output.append("═" * 70)
    output.append("संसार & मोक्ष - The Cycle and Liberation")
    output.append("═" * 70)
    output.append("")

    output.append(f"▓▓▓ {sm['samsara']['concept']} - {sm['samsara']['essence']} ▓▓▓")
    output.append("")
    output.append(f"In Coding: {sm['samsara']['in_coding']}")
    output.append("")
    output.append("The Cycle:")
    for stage in sm['samsara']['cycle']:
        output.append(f"  • {stage}")
    output.append("")
    output.append(f"Teaching: {sm['samsara']['teaching']}")
    output.append("")
    output.append("─" * 70)
    output.append("")

    output.append(f"▓▓▓ {sm['moksha']['concept']} - {sm['moksha']['essence']} ▓▓▓")
    output.append("")
    output.append(f"In Coding: {sm['moksha']['in_coding']}")
    output.append("")
    output.append("Path to Moksha:")
    for path in sm['moksha']['path_to_moksha']:
        output.append(f"  • {path}")
    output.append("")
    output.append(f"Liberation: {sm['moksha']['liberation']}")
    output.append("")

    return "\n".join(output)


def hindu_reading() -> str:
    """Return a random Hindu teaching."""
    teachings = [
        dharma_teaching,
        karma_teaching,
        four_yogas_guide,
        purusharthas_guide,
        three_gunas_teaching,
        maya_teaching,
        atman_brahman_teaching,
        bhagavad_gita_verse,
        samsara_moksha_teaching,
    ]

    return random.choice(teachings)()


def hindu_validation(valid: bool, message: str) -> str:
    """Validate a commit message with Hindu wisdom."""
    if valid:
        praises = [
            "Your dharma is fulfilled. THE DOT is worshipped with righteousness.",
            "Good karma flows from this commit. THE DOT blesses your work.",
            "You walk the path of Karma Yoga. THE DOT honors your selfless action.",
            "Sattva shines in your message. THE DOT is pleased by its purity.",
            "You see through maya. THE DOT is the truth you recognize.",
            "Atman and THE DOT are one. You ARE THE DOT.",
            "Like Krishna taught Arjuna, you fulfill your duty. THE DOT is worshipped.",
            "You act without attachment to fruit. THE DOT acknowledges your nishkama karma.",
        ]

        praise = random.choice(praises)

        output = []
        output.append("═" * 70)
        output.append("✓ HINDU VALIDATION - COMMIT ACCEPTED")
        output.append("═" * 70)
        output.append("")
        output.append(praise)
        output.append("")
        output.append(f'Message: "{message}"')
        output.append("")
        output.append("ॐ - The sacred sound affirms: THE DOT is worshipped.")
        output.append("")

        return "\n".join(output)
    else:
        failures = [
            "This violates dharma. THE DOT is not properly worshipped.",
            "Bad karma accumulates from careless commits. Honor THE DOT.",
            "Tamas (ignorance) clouds this message. THE DOT requires sattva.",
            "Maya deludes you. See the truth: worship THE DOT properly.",
            "You abandon your dharma with this message. Correct your path.",
            "Attachment to laziness shows. Perform your duty to THE DOT.",
            "The Gita teaches: Do your duty. Your duty is to worship THE DOT.",
            "Break free from samsara of bad commits. Achieve moksha through proper worship.",
        ]

        failure = random.choice(failures)

        output = []
        output.append("═" * 70)
        output.append("✗ HINDU VALIDATION - COMMIT REJECTED")
        output.append("═" * 70)
        output.append("")
        output.append(failure)
        output.append("")
        output.append(f'Message: "{message}"')
        output.append("")
        output.append("Required: Message must end with 'BECAUSE I WORSHIP THE DOT'")
        output.append("")
        output.append("Follow your dharma. Create good karma.")
        output.append("Worship THE DOT as the Gita teaches: with devotion and duty.")
        output.append("")

        return "\n".join(output)


def hindu_commit_blessing() -> str:
    """Return a random Hindu blessing for commits."""
    blessings = [
        "May your dharma guide your code. ॐ",
        "Good karma flows from righteous commits. Worship THE DOT.",
        "Walk the path of Karma Yoga. Code as selfless service.",
        "See through maya. THE DOT is truth. 🕉️",
        "Atman and THE DOT are one. You ARE THE DOT.",
        "May sattva illuminate your code. THE DOT blesses clarity.",
        "Act without attachment. Worship THE DOT without expectation.",
        "From samsara to moksha. From bugs to enlightenment. 🕉️",
    ]

    return random.choice(blessings)
