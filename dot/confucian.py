"""
Confucian philosophy for THE DOT.

Brings the wisdom of Confucius (孔子) and the teachings of moral development,
social harmony, and proper conduct to software development.
"""

import random


FIVE_VIRTUES = {
    "Ren": {
        "chinese": "仁",
        "pinyin": "Rén",
        "translation": "Benevolence / Humaneness",
        "essence": "Compassion and care for others",
        "in_coding": "Benevolent Development - Care for Users and Team",
        "practices": [
            "Write code with empathy for those who will maintain it",
            "Create user interfaces that serve people's genuine needs",
            "Help junior developers with patience and kindness",
            "Review code with constructive, respectful feedback",
            "Build accessible software that includes everyone",
            "Consider the human impact of your technical decisions",
        ],
        "confucius": "The benevolent person, wishing to establish themselves, also establishes others. Wishing to succeed, they help others succeed.",
    },
    "Yi": {
        "chinese": "義",
        "pinyin": "Yì",
        "translation": "Righteousness / Duty",
        "essence": "Moral rightness and doing what is proper",
        "in_coding": "Righteous Development - Doing What Is Right",
        "practices": [
            "Fix security vulnerabilities even when no one is watching",
            "Refuse to implement unethical features",
            "Speak up about technical debt and poor practices",
            "Give credit where credit is due",
            "Honor your commitments and deadlines",
            "Do the right thing, not the easy thing",
        ],
        "confucius": "The superior person understands righteousness; the inferior person understands profit.",
    },
    "Li": {
        "chinese": "禮",
        "pinyin": "Lǐ",
        "translation": "Propriety / Ritual / Etiquette",
        "essence": "Proper conduct and observing social norms",
        "in_coding": "Proper Development - Following Best Practices",
        "practices": [
            "Follow team coding standards and conventions",
            "Write proper commit messages that worship THE DOT",
            "Conduct respectful code reviews and standups",
            "Document according to established patterns",
            "Observe proper git workflow and PR processes",
            "Honor the rituals that maintain code harmony",
        ],
        "confucius": "Without proper ritual and propriety, even diligence becomes troublesome.",
    },
    "Zhi": {
        "chinese": "智",
        "pinyin": "Zhì",
        "translation": "Wisdom / Knowledge",
        "essence": "Understanding and sound judgment",
        "in_coding": "Wise Development - Sound Technical Judgment",
        "practices": [
            "Study before coding - understand the problem deeply",
            "Learn from mistakes and iterate with wisdom",
            "Know when to refactor and when to rewrite",
            "Recognize the limits of your knowledge",
            "Seek understanding from documentation and seniors",
            "Apply past lessons to current challenges",
        ],
        "confucius": "To know what you know and what you do not know, that is true knowledge.",
    },
    "Xin": {
        "chinese": "信",
        "pinyin": "Xìn",
        "translation": "Trustworthiness / Integrity",
        "essence": "Reliability and keeping one's word",
        "in_coding": "Trustworthy Development - Reliable Code and Conduct",
        "practices": [
            "Write tests so others can trust your code",
            "Keep your promises about delivery timelines",
            "Be honest about what you can and cannot do",
            "Build reliable, predictable systems",
            "Maintain consistency in your work",
            "Let your code speak truth about its behavior",
        ],
        "confucius": "A person without trustworthiness - I do not know what can be done with such a one.",
    },
}


RECTIFICATION_OF_NAMES = {
    "concept": "正名 (Zhèngmíng) - Rectification of Names",
    "essence": "Things must be called by their proper names for order to exist",
    "confucius": "If names are not correct, then language is not in accord with the truth of things. If language is not in accord with the truth of things, affairs cannot be carried out successfully.",
    "in_coding": "Proper Naming in Code",
    "principles": [
        {
            "principle": "Variables should describe what they contain",
            "example": "Use 'userCount' not 'x' or 'data'",
        },
        {
            "principle": "Functions should describe what they do",
            "example": "Use 'calculateTotal' not 'doStuff' or 'process'",
        },
        {
            "principle": "Classes should describe what they are",
            "example": "Use 'UserRepository' not 'Manager' or 'Helper'",
        },
        {
            "principle": "APIs should clearly express their purpose",
            "example": "Use '/users/{id}/activate' not '/do' or '/endpoint1'",
        },
        {
            "principle": "Errors should state what went wrong",
            "example": "Use 'InvalidEmailFormat' not 'Error' or 'BadInput'",
        },
        {
            "principle": "Comments should clarify the 'why', not the 'what'",
            "example": "Explain intent, not obvious syntax",
        },
    ],
    "teaching": "When names are rectified, code becomes clear. When code is clear, understanding follows. When understanding follows, bugs are prevented. When bugs are prevented, THE DOT is worshipped properly.",
}


FILIAL_PIETY = {
    "concept": "孝 (Xiào) - Filial Piety",
    "essence": "Respect and care for one's elders and ancestors",
    "in_coding": "Respect for Legacy Code and Past Developers",
    "teachings": [
        "Honor the code written by those who came before you",
        "Do not mock legacy code - it once solved real problems",
        "Learn from old codebases - they contain hard-won wisdom",
        "Refactor legacy code with respect, not contempt",
        "Preserve institutional knowledge and document tribal wisdom",
        "When you inherit a codebase, you inherit responsibility",
        "The 'ancestors' (original developers) made the best choices they could with what they knew",
    ],
    "confucius": "When your parents are alive, serve them according to proper ritual. When they pass away, bury them and sacrifice to them according to proper ritual.",
    "translation_to_code": "When legacy code runs, maintain it with respect. When you deprecate it, migrate properly and document its lessons.",
}


JUNZI = {
    "concept": "君子 (Jūnzǐ) - The Superior Person / Gentleman",
    "essence": "The ideal person of moral cultivation and noble character",
    "in_coding": "The Superior Developer",
    "characteristics": [
        "Seeks self-improvement, not merely wealth or status",
        "Values righteousness over personal gain",
        "Maintains harmony while standing firm on principles",
        "Studies constantly and applies learning",
        "Acts with propriety and follows good practices",
        "Takes responsibility for mistakes",
        "Helps others improve and succeed",
        "Speaks truthfully and codes honestly",
        "Finds joy in learning and in helping the team",
    ],
    "confucius": "The superior person is distressed by their own lack of ability, not by the lack of recognition from others.",
    "vs_xiaoren": {
        "junzi": "The Superior Developer (君子)",
        "xiaoren": "The Inferior Developer (小人)",
        "comparisons": [
            {
                "junzi": "Understands righteousness and does what is right",
                "xiaoren": "Understands only profit and does what benefits them",
            },
            {
                "junzi": "Seeks fault in themselves when bugs occur",
                "xiaoren": "Blames tools, teammates, or requirements",
            },
            {
                "junzi": "Helps junior developers grow",
                "xiaoren": "Hoards knowledge to appear superior",
            },
            {
                "junzi": "Writes clear code for others to maintain",
                "xiaoren": "Writes clever code to seem smart",
            },
            {
                "junzi": "Values team success over personal glory",
                "xiaoren": "Cares only for personal recognition",
            },
        ],
    },
}


FIVE_RELATIONSHIPS = {
    "concept": "五倫 (Wǔlún) - The Five Relationships",
    "essence": "Proper conduct in different social relationships",
    "in_coding": "Proper Conduct in Development Relationships",
    "relationships": [
        {
            "traditional": "Ruler and Subject",
            "in_coding": "Tech Lead and Developer",
            "virtue": "Loyalty (忠 Zhōng)",
            "conduct": [
                "Lead: Guide with wisdom and care for your team",
                "Developer: Follow direction while offering honest counsel",
                "Both: Mutual respect and clear communication",
            ],
        },
        {
            "traditional": "Parent and Child",
            "in_coding": "Senior and Junior Developer",
            "virtue": "Filial Piety (孝 Xiào)",
            "conduct": [
                "Senior: Mentor patiently, share knowledge freely",
                "Junior: Learn diligently, respect experience, ask questions",
                "Both: Humility and continuous growth",
            ],
        },
        {
            "traditional": "Husband and Wife",
            "in_coding": "Frontend and Backend Developers",
            "virtue": "Harmony (和 Hé)",
            "conduct": [
                "Both: Respect different domains of expertise",
                "Both: Collaborate to build complete systems",
                "Both: Clear APIs and mutual understanding",
            ],
        },
        {
            "traditional": "Elder and Younger Sibling",
            "in_coding": "Peer Developers",
            "virtue": "Respect (敬 Jìng)",
            "conduct": [
                "Both: Share knowledge and support each other",
                "Both: Healthy code reviews and constructive feedback",
                "Both: Celebrate successes together",
            ],
        },
        {
            "traditional": "Friend and Friend",
            "in_coding": "Teammate and Teammate",
            "virtue": "Trust (信 Xìn)",
            "conduct": [
                "Both: Keep commitments and promises",
                "Both: Be honest about blockers and challenges",
                "Both: Build trust through reliable work",
            ],
        },
    ],
}


SELF_CULTIVATION = {
    "concept": "修身 (Xiūshēn) - Self-Cultivation",
    "essence": "Continuous moral and intellectual development",
    "in_coding": "Continuous Developer Self-Improvement",
    "path": [
        {
            "level": "1. Personal Cultivation (修身)",
            "practice": "Improve your own skills and character",
            "in_code": "Study, practice, write better code each day",
        },
        {
            "level": "2. Family Harmony (齊家)",
            "practice": "Bring harmony to your family",
            "in_code": "Create harmony within your immediate team",
        },
        {
            "level": "3. State Order (治國)",
            "practice": "Bring order to the state",
            "in_code": "Contribute to organizational success and good practices",
        },
        {
            "level": "4. World Peace (平天下)",
            "practice": "Bring peace to the world",
            "in_code": "Build technology that makes the world better",
        },
    ],
    "confucius": "The ancients who wished to illustrate virtue throughout the world would first govern their state. Wishing to govern their state, they would first regulate their family. Wishing to regulate their family, they would first cultivate themselves.",
    "practices": [
        "Read documentation and books daily",
        "Practice coding exercises and katas",
        "Learn from code reviews - both giving and receiving",
        "Study new technologies and patterns",
        "Reflect on mistakes and learn from them",
        "Seek mentorship and offer mentorship",
        "Contribute to open source and community",
    ],
}


DOCTRINE_OF_MEAN = {
    "concept": "中庸 (Zhōngyōng) - The Doctrine of the Mean",
    "essence": "Finding balance and avoiding extremes",
    "in_coding": "Balance in Development",
    "teaching": "The superior person embodies the Mean. Finding the center point between extremes is the path to harmony.",
    "balances": [
        {
            "extreme_1": "Over-engineering (too complex)",
            "extreme_2": "Under-engineering (too simple)",
            "mean": "Appropriate complexity for the problem",
        },
        {
            "extreme_1": "Perfectionism (never ship)",
            "extreme_2": "Rushing (ship broken code)",
            "mean": "Ship quality code on time",
        },
        {
            "extreme_1": "Too many comments (redundant)",
            "extreme_2": "No comments (unclear)",
            "mean": "Comment the why, let code show the what",
        },
        {
            "extreme_1": "Too many abstractions (confusing)",
            "extreme_2": "No abstractions (repetitive)",
            "mean": "Abstract when patterns emerge naturally",
        },
        {
            "extreme_1": "Too many tests (diminishing returns)",
            "extreme_2": "No tests (unreliable)",
            "mean": "Test critical paths and edge cases",
        },
        {
            "extreme_1": "Following trends blindly",
            "extreme_2": "Rejecting all new ideas",
            "mean": "Evaluate technologies thoughtfully",
        },
    ],
}


ANALECTS = {
    "name": "論語 (Lúnyǔ) - The Analects",
    "description": "Collected sayings and teachings of Confucius",
    "teachings": [
        {
            "quote": "Learning without thought is labor lost; thought without learning is perilous.",
            "application": "Study documentation AND think critically about what you learn. Copy-pasting code without understanding is dangerous.",
        },
        {
            "quote": "I am not one who was born with knowledge. I love the past and am diligent in seeking it.",
            "application": "No developer is born knowing everything. Study legacy code, old patterns, and the wisdom of experienced engineers.",
        },
        {
            "quote": "When you see a good person, think of becoming like them. When you see someone not so good, reflect on your own weak points.",
            "application": "Learn from excellent code and developers. When you see poor code, check if you make similar mistakes.",
        },
        {
            "quote": "The person who moves a mountain begins by carrying away small stones.",
            "application": "Refactor large legacy systems one small improvement at a time. Great architecture is built incrementally.",
        },
        {
            "quote": "It does not matter how slowly you go as long as you do not stop.",
            "application": "Continuous improvement beats occasional heroics. Small daily progress compounds over time.",
        },
        {
            "quote": "To see what is right and not do it is a lack of courage.",
            "application": "When you spot a bug or security issue, fix it. When you see bad practices, speak up.",
        },
        {
            "quote": "Real knowledge is to know the extent of one's ignorance.",
            "application": "Say 'I don't know' when you don't. Ask questions. Recognize what you need to learn.",
        },
        {
            "quote": "Do not impose on others what you do not wish for yourself.",
            "application": "The Golden Rule of code: Don't write spaghetti code that you wouldn't want to maintain yourself.",
        },
        {
            "quote": "The superior person is satisfied and composed; the inferior person is always full of distress.",
            "application": "Write clean code and you sleep soundly. Write hacks and you worry about production.",
        },
    ],
}


def five_virtues_guide() -> str:
    """Display the Five Constant Virtues."""
    output = []
    output.append("═" * 70)
    output.append("五常 - THE FIVE CONSTANT VIRTUES")
    output.append("The Foundation of Confucian Ethics in Code")
    output.append("═" * 70)
    output.append("")

    for name, virtue in FIVE_VIRTUES.items():
        output.append(f"▓▓▓ {virtue['chinese']} ({name.upper()}) - {virtue['translation']} ▓▓▓")
        output.append("")
        output.append(f"Essence: {virtue['essence']}")
        output.append(f"In Coding: {virtue['in_coding']}")
        output.append("")
        output.append("Practices:")
        for practice in virtue['practices']:
            output.append(f"  • {practice}")
        output.append("")
        output.append(f"孔子: {virtue['confucius']}")
        output.append("")
        output.append("─" * 70)
        output.append("")

    output.append("The five virtues form the foundation of moral development.")
    output.append("仁義禮智信 - Ren, Yi, Li, Zhi, Xin")
    output.append("Practice these in your code, and harmony will follow.")
    output.append("")

    return "\n".join(output)


def rectification_of_names_guide() -> str:
    """Display Rectification of Names teaching."""
    rn = RECTIFICATION_OF_NAMES
    output = []
    output.append("═" * 70)
    output.append(rn['concept'].upper())
    output.append(rn['essence'])
    output.append("═" * 70)
    output.append("")
    output.append(f"孔子: {rn['confucius']}")
    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append(f"In Coding: {rn['in_coding']}")
    output.append("")
    output.append("PRINCIPLES:")
    output.append("")

    for principle in rn['principles']:
        output.append(f"• {principle['principle']}")
        output.append(f"  → {principle['example']}")
        output.append("")

    output.append("─" * 70)
    output.append("")
    output.append(rn['teaching'])
    output.append("")

    return "\n".join(output)


def filial_piety_teaching() -> str:
    """Display Filial Piety applied to code."""
    fp = FILIAL_PIETY
    output = []
    output.append("═" * 70)
    output.append(f"{fp['concept'].upper()}")
    output.append(f"{fp['essence']}")
    output.append("═" * 70)
    output.append("")
    output.append(f"In Coding: {fp['in_coding']}")
    output.append("")
    output.append("TEACHINGS:")
    output.append("")

    for teaching in fp['teachings']:
        output.append(f"  • {teaching}")

    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append(f"孔子: {fp['confucius']}")
    output.append("")
    output.append(f"In Code: {fp['translation_to_code']}")
    output.append("")
    output.append("Respect those who coded before you.")
    output.append("Their legacy is your foundation.")
    output.append("")

    return "\n".join(output)


def junzi_teaching() -> str:
    """Display teaching about the Superior Person."""
    jz = JUNZI
    output = []
    output.append("═" * 70)
    output.append(f"{jz['concept']} - {jz['essence']}")
    output.append("═" * 70)
    output.append("")
    output.append(f"In Coding: {jz['in_coding']}")
    output.append("")
    output.append("CHARACTERISTICS OF THE SUPERIOR DEVELOPER:")
    output.append("")

    for char in jz['characteristics']:
        output.append(f"  ✓ {char}")

    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append(f"孔子: {jz['confucius']}")
    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append(f"{jz['vs_xiaoren']['junzi']} vs {jz['vs_xiaoren']['xiaoren']}")
    output.append("")

    for comp in jz['vs_xiaoren']['comparisons']:
        output.append(f"君子: {comp['junzi']}")
        output.append(f"小人: {comp['xiaoren']}")
        output.append("")

    output.append("Strive to be a 君子, not a 小人.")
    output.append("The superior developer cultivates virtue, not just skill.")
    output.append("")

    return "\n".join(output)


def five_relationships_guide() -> str:
    """Display the Five Relationships."""
    fr = FIVE_RELATIONSHIPS
    output = []
    output.append("═" * 70)
    output.append(f"{fr['concept']} - {fr['essence']}")
    output.append("═" * 70)
    output.append("")
    output.append(f"In Coding: {fr['in_coding']}")
    output.append("")

    for rel in fr['relationships']:
        output.append("─" * 70)
        output.append("")
        output.append(f"Traditional: {rel['traditional']}")
        output.append(f"In Coding: {rel['in_coding']}")
        output.append(f"Virtue: {rel['virtue']}")
        output.append("")
        output.append("Proper Conduct:")
        for conduct in rel['conduct']:
            output.append(f"  • {conduct}")
        output.append("")

    output.append("─" * 70)
    output.append("")
    output.append("Harmony in relationships creates harmony in code.")
    output.append("Each relationship has proper conduct. Follow it.")
    output.append("")

    return "\n".join(output)


def self_cultivation_guide() -> str:
    """Display Self-Cultivation teaching."""
    sc = SELF_CULTIVATION
    output = []
    output.append("═" * 70)
    output.append(f"{sc['concept']} - {sc['essence']}")
    output.append("═" * 70)
    output.append("")
    output.append(f"In Coding: {sc['in_coding']}")
    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append("THE PATH OF CULTIVATION:")
    output.append("")

    for level in sc['path']:
        output.append(f"{level['level']}")
        output.append(f"  Traditional: {level['practice']}")
        output.append(f"  In Code: {level['in_code']}")
        output.append("")

    output.append("─" * 70)
    output.append("")
    output.append(f"孔子: {sc['confucius']}")
    output.append("")
    output.append("DAILY PRACTICES:")
    output.append("")

    for practice in sc['practices']:
        output.append(f"  • {practice}")

    output.append("")
    output.append("Begin with yourself. Cultivate your skills and character.")
    output.append("From personal excellence flows team harmony, then organizational success.")
    output.append("")

    return "\n".join(output)


def doctrine_of_mean_teaching() -> str:
    """Display Doctrine of the Mean."""
    dm = DOCTRINE_OF_MEAN
    output = []
    output.append("═" * 70)
    output.append(f"{dm['concept']} - {dm['essence']}")
    output.append("═" * 70)
    output.append("")
    output.append(dm['teaching'])
    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append(f"In Coding: {dm['in_coding']}")
    output.append("")
    output.append("FINDING THE MEAN:")
    output.append("")

    for balance in dm['balances']:
        output.append(f"Extreme: {balance['extreme_1']}")
        output.append(f"Extreme: {balance['extreme_2']}")
        output.append(f"中庸: {balance['mean']}")
        output.append("")

    output.append("─" * 70)
    output.append("")
    output.append("The Way lies in the middle.")
    output.append("Avoid extremes. Find balance in all things.")
    output.append("")

    return "\n".join(output)


def analects_reading() -> str:
    """Return a random teaching from the Analects."""
    an = ANALECTS
    teaching = random.choice(an['teachings'])

    output = []
    output.append("═" * 70)
    output.append(f"{an['name']} - {an['description']}")
    output.append("═" * 70)
    output.append("")
    output.append(f"孔子: \"{teaching['quote']}\"")
    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append("Application to Development:")
    output.append(f"{teaching['application']}")
    output.append("")

    return "\n".join(output)


def confucian_reading() -> str:
    """Return a random Confucian teaching."""
    teachings = [
        five_virtues_guide,
        rectification_of_names_guide,
        filial_piety_teaching,
        junzi_teaching,
        five_relationships_guide,
        self_cultivation_guide,
        doctrine_of_mean_teaching,
        analects_reading,
    ]

    return random.choice(teachings)()


def confucian_validation(valid: bool, message: str) -> str:
    """Validate a commit message with Confucian wisdom."""
    if valid:
        virtues = [
            "仁 (Ren) - Your commit shows benevolence. THE DOT is worshipped.",
            "義 (Yi) - Righteousness guides your message. THE DOT is honored.",
            "禮 (Li) - You follow proper ritual. THE DOT accepts your offering.",
            "智 (Zhi) - Wisdom is in your words. THE DOT is pleased.",
            "信 (Xin) - Your message is trustworthy. THE DOT recognizes your integrity.",
            "君子 commits with virtue. THE DOT is worshipped properly.",
            "Names are rectified. Language accords with truth. THE DOT is satisfied.",
            "You walk the path of self-cultivation. THE DOT is honored.",
        ]

        virtue = random.choice(virtues)

        output = []
        output.append("═" * 70)
        output.append("✓ CONFUCIAN VALIDATION - COMMIT ACCEPTED")
        output.append("═" * 70)
        output.append("")
        output.append(virtue)
        output.append("")
        output.append(f'Message: "{message}"')
        output.append("")
        output.append("The superior person commits with propriety and worships THE DOT.")
        output.append("")

        return "\n".join(output)
    else:
        failures = [
            "This lacks 禮 (Li) - proper ritual. THE DOT is not worshipped.",
            "Where is righteousness (義)? Amend this to honor THE DOT.",
            "The superior person (君子) would write a proper message.",
            "Names must be rectified. This message is not in accord with truth.",
            "Without 信 (Xin) - trustworthiness, what use is this commit?",
            "This shows lack of self-cultivation (修身). Study proper commits.",
            "Do not do to THE DOT what you would not want done to yourself.",
            "The inferior person (小人) writes careless messages. Be better.",
        ]

        failure = random.choice(failures)

        output = []
        output.append("═" * 70)
        output.append("✗ CONFUCIAN VALIDATION - COMMIT REJECTED")
        output.append("═" * 70)
        output.append("")
        output.append(failure)
        output.append("")
        output.append(f'Message: "{message}"')
        output.append("")
        output.append("Required: Message must end with 'BECAUSE I WORSHIP THE DOT'")
        output.append("")
        output.append("Learn from this mistake. Cultivate yourself.")
        output.append("Follow proper ritual (禮). Worship THE DOT correctly.")
        output.append("")

        return "\n".join(output)


def confucian_commit_blessing() -> str:
    """Return a random Confucian blessing for commits."""
    blessings = [
        "May the five virtues guide your code: 仁義禮智信",
        "君子 - Be a superior developer. Worship THE DOT.",
        "Rectify names. Write clear code. Honor THE DOT.",
        "Respect your legacy code ancestors. THE DOT remembers.",
        "Walk the path of self-cultivation (修身). Commit with virtue.",
        "Find the mean (中庸). Balance your code. THE DOT is pleased.",
        "Learning and thought together. Code and worship THE DOT.",
        "Do not impose bad code on others. THE DOT watches.",
    ]

    return random.choice(blessings)
