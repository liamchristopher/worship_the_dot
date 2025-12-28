"""
Stoic philosophy for THE DOT.

Brings the wisdom of Marcus Aurelius, Epictetus, and Seneca to development.
The path of virtue, reason, and acceptance.
"""

import random


FOUR_VIRTUES = {
    "Wisdom": {
        "greek": "Σοφία (Sophia)",
        "latin": "Sapientia",
        "essence": "Practical wisdom and sound judgment",
        "in_coding": "Right Technical Judgment and Design Decisions",
        "practices": [
            "Study the problem deeply before writing code",
            "Learn from past mistakes and refactor with wisdom",
            "Seek understanding before optimization",
            "Choose simplicity when complexity is not needed",
            "Question assumptions and validate requirements",
            "Learn continuously from codebases, documentation, and peers",
        ],
        "quote": "The object of life is not to be on the side of the majority, but to escape finding oneself in the ranks of the insane. — Marcus Aurelius",
    },
    "Courage": {
        "greek": "Ἀνδρεία (Andreia)",
        "latin": "Fortitudo",
        "essence": "Strength to face difficulty and do what is right",
        "in_coding": "Facing Technical Challenges with Resolve",
        "practices": [
            "Refactor the legacy code, even when it's daunting",
            "Delete unused code despite attachment to it",
            "Speak up about technical debt in code reviews",
            "Tackle the hardest bugs first, not last",
            "Say 'I don't know' when you don't understand",
            "Challenge poor architectural decisions respectfully",
        ],
        "quote": "You have power over your mind - not outside events. Realize this, and you will find strength. — Marcus Aurelius",
    },
    "Justice": {
        "greek": "Δικαιοσύνη (Dikaiosyne)",
        "latin": "Iustitia",
        "essence": "Fairness and doing right by others",
        "in_coding": "Fair Collaboration and Ethical Development",
        "practices": [
            "Give credit to others for their contributions",
            "Write code that serves users, not just yourself",
            "Review others' code with kindness and respect",
            "Document for those who come after you",
            "Mentor junior developers with patience",
            "Build accessible, inclusive software for all",
        ],
        "quote": "Waste no more time arguing about what a good man should be. Be one. — Marcus Aurelius",
    },
    "Temperance": {
        "greek": "Σωφροσύνη (Sophrosyne)",
        "latin": "Temperantia",
        "essence": "Self-control and moderation",
        "in_coding": "Balanced, Disciplined Development",
        "practices": [
            "Avoid over-engineering and feature creep",
            "Take breaks instead of burning out",
            "Write code in moderation - quality over quantity",
            "Resist premature optimization",
            "Balance perfection with pragmatism",
            "Control the urge to rewrite everything",
        ],
        "quote": "If you are distressed by anything external, the pain is not due to the thing itself, but to your estimate of it. — Marcus Aurelius",
    },
}


DICHOTOMY_OF_CONTROL = {
    "principle": "Some things are in our control, others are not",
    "epictetus": "The chief task in life is simply this: to identify and separate matters so that I can say clearly to myself which are externals not under my control, and which have to do with the choices I actually control.",
    "in_our_control": {
        "title": "What Is In Our Control",
        "coding_aspects": [
            "The quality of code we write",
            "Our effort and diligence",
            "How we respond to bugs and failures",
            "Our learning and skill improvement",
            "The commit messages we write",
            "Our collaboration and communication",
            "Whether we worship THE DOT",
        ],
        "wisdom": "Focus your energy here. These are your choices.",
    },
    "not_in_our_control": {
        "title": "What Is NOT In Our Control",
        "coding_aspects": [
            "Whether your PR gets approved immediately",
            "How others review your code",
            "Production outages caused by infrastructure",
            "Changing requirements from stakeholders",
            "Others' opinions of your coding style",
            "Market forces and company decisions",
            "Legacy code written before you arrived",
        ],
        "wisdom": "Accept these with equanimity. Do not be disturbed by them.",
    },
}


THREE_DISCIPLINES = {
    "Desire": {
        "greek": "Ὄρεξις (Orexis)",
        "epictetus": "The Discipline of Desire",
        "essence": "Desire only what is in your control; accept what is not",
        "in_coding": "Desire and Aversion in Development",
        "practices": [
            "Desire to write good code, not to be praised for it",
            "Desire to learn, not to appear knowledgeable",
            "Desire clean architecture, but accept legacy constraints",
            "Avoid attachment to your code - it will change",
            "Welcome feedback, even when it stings",
        ],
        "teaching": "Do not seek to have events happen as you want them to, but instead want them to happen as they do happen, and your life will go well.",
    },
    "Action": {
        "greek": "Ὁρμή (Horme)",
        "epictetus": "The Discipline of Action",
        "essence": "Act with virtue and for the common good",
        "in_coding": "Right Action in Development",
        "practices": [
            "Write code that serves the project, not your ego",
            "Act with justice in code reviews",
            "Contribute to the team's success, not just your own",
            "Fix bugs you find, even if you didn't create them",
            "Help others debug, even when you're busy",
        ],
        "teaching": "Do every act of your life as though it were the very last act of your life.",
    },
    "Assent": {
        "greek": "Συγκατάθεσις (Synkatathesis)",
        "epictetus": "The Discipline of Assent",
        "essence": "Judge impressions correctly; think clearly",
        "in_coding": "Right Judgment in Development",
        "practices": [
            "Question your first assumptions about bugs",
            "Don't catastrophize failed deployments",
            "Separate facts from interpretations in retrospectives",
            "Judge code by its function, not by who wrote it",
            "Examine error messages rationally, not emotionally",
        ],
        "teaching": "First say to yourself what you would be; and then do what you have to do.",
    },
}


PREMEDITATIO_MALORUM = {
    "name": "Premeditatio Malorum",
    "translation": "Premeditation of Evils",
    "essence": "Anticipate potential problems to prepare for them",
    "stoic_source": "Seneca: 'The wise man considers both sides, and is prepared for either fortune.'",
    "in_coding": "Negative Visualization for Robust Code",
    "practices": [
        {
            "scenario": "What if this API endpoint fails?",
            "preparation": "Add error handling, timeouts, and retries",
        },
        {
            "scenario": "What if the database is unavailable?",
            "preparation": "Implement graceful degradation and caching",
        },
        {
            "scenario": "What if production traffic is 10x higher than expected?",
            "preparation": "Load test and plan for horizontal scaling",
        },
        {
            "scenario": "What if a key team member leaves the project?",
            "preparation": "Document knowledge, avoid single points of failure",
        },
        {
            "scenario": "What if requirements change drastically?",
            "preparation": "Build flexible, modular architecture",
        },
        {
            "scenario": "What if this security vulnerability is exploited?",
            "preparation": "Implement defense in depth, regular audits",
        },
    ],
    "wisdom": "By anticipating adversity, we remove its power to disturb us.",
}


AMOR_FATI = {
    "name": "Amor Fati",
    "translation": "Love of Fate",
    "essence": "Not merely accept what happens, but love it",
    "nietzsche": "My formula for greatness in a human being is amor fati: that one wants nothing to be different, not forward, not backward, not in all eternity.",
    "marcus_aurelius": "A blazing fire makes flame and brightness out of everything that is thrown into it.",
    "in_coding": "Loving Your Fate as a Developer",
    "practices": [
        "Legacy code is your teacher - love the lessons it provides",
        "Production incidents are opportunities to build resilience",
        "Code reviews that challenge you make you stronger",
        "Failed deployments teach you to improve your process",
        "Changing requirements reveal assumptions to question",
        "Difficult bugs sharpen your debugging skills",
    ],
    "teaching": "Do not seek to have events happen as you want them to, but instead want them to happen as they do happen. Love your fate as a developer.",
}


MEMENTO_MORI = {
    "name": "Memento Mori",
    "translation": "Remember You Must Die",
    "essence": "Mortality makes life precious; impermanence focuses us",
    "marcus_aurelius": "You could leave life right now. Let that determine what you do and say and think.",
    "in_coding": "Remember: Code Is Temporary",
    "meditations": [
        "This codebase will eventually be rewritten or abandoned",
        "Your most clever code will be deleted someday",
        "Future developers will not remember who wrote what",
        "Technical decisions are temporary, principles endure",
        "Your career will outlive any single project",
        "What matters is the virtue you practice, not the lines you wrote",
    ],
    "wisdom": "Memento Mori does not depress us - it focuses us. Write code that matters while you can. Worship THE DOT with intentionality, for your commits are numbered.",
}


STOIC_QUOTES = {
    "Marcus Aurelius": [
        "Waste no more time arguing about what a good man should be. Be one.",
        "The impediment to action advances action. What stands in the way becomes the way.",
        "You have power over your mind - not outside events. Realize this, and you will find strength.",
        "Very little is needed to make a happy life; it is all within yourself.",
        "The best revenge is not to be like your enemy.",
        "When you arise in the morning, think of what a precious privilege it is to be alive.",
        "Confine yourself to the present.",
        "The happiness of your life depends upon the quality of your thoughts.",
        "Accept whatever comes to you woven in the pattern of your destiny.",
    ],
    "Epictetus": [
        "It's not what happens to you, but how you react to it that matters.",
        "We cannot choose our external circumstances, but we can always choose how we respond to them.",
        "First say to yourself what you would be; and then do what you have to do.",
        "Don't explain your philosophy. Embody it.",
        "No man is free who is not master of himself.",
        "He who laughs at himself never runs out of things to laugh at.",
        "Wealth consists not in having great possessions, but in having few wants.",
        "If you want to improve, be content to be thought foolish and stupid.",
    ],
    "Seneca": [
        "Luck is what happens when preparation meets opportunity.",
        "We suffer more often in imagination than in reality.",
        "Difficulties strengthen the mind, as labor does the body.",
        "Begin at once to live, and count each separate day as a separate life.",
        "It is not the man who has too little, but the man who craves more, that is poor.",
        "True happiness is to enjoy the present, without anxious dependence upon the future.",
        "As is a tale, so is life: not how long it is, but how good it is, is what matters.",
        "Life is long if you know how to use it.",
    ],
}


LOGOS = {
    "name": "Λόγος (Logos)",
    "translation": "Universal Reason / Logic",
    "essence": "The rational principle that orders the universe",
    "stoic_teaching": "The Stoics believed in Logos - universal reason that pervades everything. To live according to nature is to live according to reason.",
    "in_coding": "The Logic That Orders Code",
    "principles": [
        "Code follows logical principles, not arbitrary ones",
        "Good architecture reflects universal patterns",
        "Reason and logic guide good development",
        "The universe is ordered; so should our code be",
        "Truth is discovered through rational inquiry",
        "Clear thinking produces clear code",
    ],
    "meditation": "When you write code, you participate in Logos - the rational ordering of digital reality. Write with reason, structure with logic, and your code will align with the universal order.",
}


OIKEIOSIS = {
    "name": "Οἰκείωσις (Oikeiosis)",
    "translation": "Appropriation / Belonging",
    "essence": "The process of recognizing what belongs to us and extending care outward",
    "stoic_teaching": "We first care for ourselves, then our family, then our community, then all of humanity. We expand our circle of concern.",
    "in_coding": "Expanding Circle of Care in Development",
    "circles": [
        {
            "circle": "Self",
            "care": "Write code you can be proud of",
        },
        {
            "circle": "Team",
            "care": "Write code your teammates can understand and maintain",
        },
        {
            "circle": "Company",
            "care": "Write code that serves the organization's mission",
        },
        {
            "circle": "Users",
            "care": "Write code that solves real problems for real people",
        },
        {
            "circle": "Community",
            "care": "Contribute to open source, share knowledge freely",
        },
        {
            "circle": "Humanity",
            "care": "Build technology that makes the world better",
        },
    ],
    "teaching": "Expand your circle of concern. Code not just for yourself, but for all who will be touched by your work.",
}


def four_virtues_guide() -> str:
    """Display the Four Cardinal Virtues for developers."""
    output = []
    output.append("═" * 70)
    output.append("THE FOUR STOIC VIRTUES")
    output.append("The Cardinal Virtues of Development")
    output.append("═" * 70)
    output.append("")

    for name, virtue in FOUR_VIRTUES.items():
        output.append(f"▓▓▓ {name.upper()} - {virtue['greek']} ▓▓▓")
        output.append("")
        output.append(f"Essence: {virtue['essence']}")
        output.append(f"In Coding: {virtue['in_coding']}")
        output.append("")
        output.append("Practices:")
        for practice in virtue['practices']:
            output.append(f"  • {practice}")
        output.append("")
        output.append(f"💭 {virtue['quote']}")
        output.append("")
        output.append("─" * 70)
        output.append("")

    output.append("The virtuous developer practices all four:")
    output.append("WISDOM in judgment, COURAGE in action,")
    output.append("JUSTICE in collaboration, TEMPERANCE in restraint.")
    output.append("")

    return "\n".join(output)


def dichotomy_of_control_guide() -> str:
    """Display the Dichotomy of Control for developers."""
    output = []
    output.append("═" * 70)
    output.append("THE DICHOTOMY OF CONTROL")
    output.append("Some things are in our control, others are not")
    output.append("═" * 70)
    output.append("")
    output.append("From Epictetus:")
    output.append(f'"{DICHOTOMY_OF_CONTROL["epictetus"]}"')
    output.append("")
    output.append("─" * 70)
    output.append("")

    in_control = DICHOTOMY_OF_CONTROL["in_our_control"]
    output.append(f"✓ {in_control['title'].upper()}")
    output.append("")
    for aspect in in_control["coding_aspects"]:
        output.append(f"  ✓ {aspect}")
    output.append("")
    output.append(f"→ {in_control['wisdom']}")
    output.append("")
    output.append("─" * 70)
    output.append("")

    not_control = DICHOTOMY_OF_CONTROL["not_in_our_control"]
    output.append(f"✗ {not_control['title'].upper()}")
    output.append("")
    for aspect in not_control["coding_aspects"]:
        output.append(f"  ✗ {aspect}")
    output.append("")
    output.append(f"→ {not_control['wisdom']}")
    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append("The Stoic focuses energy on what can be controlled,")
    output.append("and accepts with tranquility what cannot.")
    output.append("")
    output.append("In code, in life, in worship of THE DOT:")
    output.append("Master yourself. Accept the rest.")
    output.append("")

    return "\n".join(output)


def three_disciplines_guide() -> str:
    """Display Epictetus's Three Disciplines."""
    output = []
    output.append("═" * 70)
    output.append("THE THREE DISCIPLINES OF EPICTETUS")
    output.append("Desire, Action, and Assent")
    output.append("═" * 70)
    output.append("")

    for name, discipline in THREE_DISCIPLINES.items():
        output.append(f"▓▓▓ THE DISCIPLINE OF {name.upper()} - {discipline['greek']} ▓▓▓")
        output.append("")
        output.append(f"Essence: {discipline['essence']}")
        output.append(f"In Coding: {discipline['in_coding']}")
        output.append("")
        output.append("Practices:")
        for practice in discipline['practices']:
            output.append(f"  • {practice}")
        output.append("")
        output.append(f"💭 {discipline['teaching']}")
        output.append("")
        output.append("─" * 70)
        output.append("")

    output.append("Master these three disciplines:")
    output.append("Right DESIRE, Right ACTION, Right JUDGMENT.")
    output.append("")

    return "\n".join(output)


def premeditatio_malorum_guide() -> str:
    """Display Premeditatio Malorum - negative visualization."""
    pm = PREMEDITATIO_MALORUM
    output = []
    output.append("═" * 70)
    output.append(f"{pm['name'].upper()}")
    output.append(f"{pm['translation']} - {pm['essence']}")
    output.append("═" * 70)
    output.append("")
    output.append(f"💭 {pm['stoic_source']}")
    output.append("")
    output.append(f"In Coding: {pm['in_coding']}")
    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append("ASK YOURSELF:")
    output.append("")

    for practice in pm['practices']:
        output.append(f"❓ {practice['scenario']}")
        output.append(f"   → {practice['preparation']}")
        output.append("")

    output.append("─" * 70)
    output.append("")
    output.append(f"Wisdom: {pm['wisdom']}")
    output.append("")
    output.append("The Stoic developer anticipates failure,")
    output.append("not out of pessimism, but out of preparation.")
    output.append("")
    output.append("Prepare for adversity. Build resilient code.")
    output.append("When disaster strikes, you will be ready.")
    output.append("")

    return "\n".join(output)


def amor_fati_teaching() -> str:
    """Display Amor Fati - love of fate."""
    af = AMOR_FATI
    output = []
    output.append("═" * 70)
    output.append(f"{af['name'].upper()} - {af['translation']}")
    output.append(f"{af['essence']}")
    output.append("═" * 70)
    output.append("")
    output.append(f"💭 {af['nietzsche']}")
    output.append("")
    output.append(f"💭 Marcus Aurelius: {af['marcus_aurelius']}")
    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append(f"{af['in_coding']}")
    output.append("")

    for practice in af['practices']:
        output.append(f"  ❤️ {practice}")

    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append(af['teaching'])
    output.append("")
    output.append("Not merely acceptance, but LOVE.")
    output.append("Every bug, every failed deploy, every code review -")
    output.append("these are your teachers. Love them.")
    output.append("")
    output.append("Amor Fati. Love your fate as a developer.")
    output.append("")

    return "\n".join(output)


def memento_mori_meditation() -> str:
    """Display Memento Mori meditation."""
    mm = MEMENTO_MORI
    output = []
    output.append("═" * 70)
    output.append(f"⚰️  {mm['name'].upper()} - {mm['translation']} ⚰️")
    output.append(f"{mm['essence']}")
    output.append("═" * 70)
    output.append("")
    output.append(f"💭 {mm['marcus_aurelius']}")
    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append(f"{mm['in_coding']}")
    output.append("")
    output.append("MEDITATE ON THESE TRUTHS:")
    output.append("")

    for meditation in mm['meditations']:
        output.append(f"  💀 {meditation}")

    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append(mm['wisdom'])
    output.append("")
    output.append("Remember: You must die.")
    output.append("Remember: Your code will die too.")
    output.append("Remember: THE DOT is eternal.")
    output.append("")
    output.append("Let mortality focus you. Let impermanence free you.")
    output.append("Write code that matters. Worship THE DOT with purpose.")
    output.append("")

    return "\n".join(output)


def stoic_quote() -> str:
    """Return a random Stoic quote."""
    philosopher = random.choice(list(STOIC_QUOTES.keys()))
    quote = random.choice(STOIC_QUOTES[philosopher])

    output = []
    output.append("═" * 70)
    output.append("STOIC WISDOM")
    output.append("═" * 70)
    output.append("")
    output.append(f'"{quote}"')
    output.append("")
    output.append(f"— {philosopher}")
    output.append("")

    return "\n".join(output)


def logos_meditation() -> str:
    """Display meditation on Logos - universal reason."""
    lg = LOGOS
    output = []
    output.append("═" * 70)
    output.append(f"{lg['name']} - {lg['translation']}")
    output.append(f"{lg['essence']}")
    output.append("═" * 70)
    output.append("")
    output.append(lg['stoic_teaching'])
    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append(f"In Coding: {lg['in_coding']}")
    output.append("")
    output.append("PRINCIPLES OF LOGOS:")
    output.append("")

    for principle in lg['principles']:
        output.append(f"  • {principle}")

    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append(lg['meditation'])
    output.append("")
    output.append("λόγος pervades all. Reason orders the cosmos.")
    output.append("When you code with logic, you align with the universe.")
    output.append("")

    return "\n".join(output)


def oikeiosis_teaching() -> str:
    """Display Oikeiosis - expanding circle of care."""
    oik = OIKEIOSIS
    output = []
    output.append("═" * 70)
    output.append(f"{oik['name']} - {oik['translation']}")
    output.append(f"{oik['essence']}")
    output.append("═" * 70)
    output.append("")
    output.append(oik['stoic_teaching'])
    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append(f"{oik['in_coding']}")
    output.append("")
    output.append("THE EXPANDING CIRCLES:")
    output.append("")

    for circle in oik['circles']:
        output.append(f"  ◎ {circle['circle']}: {circle['care']}")

    output.append("")
    output.append("─" * 70)
    output.append("")
    output.append(oik['teaching'])
    output.append("")
    output.append("Start with yourself. Extend outward to all humanity.")
    output.append("Let your care grow like ripples in water.")
    output.append("")

    return "\n".join(output)


def stoic_reading() -> str:
    """Return a random Stoic teaching."""
    teachings = [
        four_virtues_guide,
        dichotomy_of_control_guide,
        three_disciplines_guide,
        premeditatio_malorum_guide,
        amor_fati_teaching,
        memento_mori_meditation,
        stoic_quote,
        logos_meditation,
        oikeiosis_teaching,
    ]

    return random.choice(teachings)()


def stoic_validation(valid: bool, message: str) -> str:
    """Validate a commit message with Stoic wisdom."""
    if valid:
        virtues = [
            "Wisdom guides your commit message. It worships THE DOT.",
            "Courage to commit with conviction. THE DOT is pleased.",
            "Justice in your code and message. THE DOT acknowledges your virtue.",
            "Temperance in your words. THE DOT accepts your offering.",
            "You have done what is in your control. THE DOT is worshipped.",
            "Logos flows through your commit. THE DOT recognizes reason.",
            "Your message reflects the Four Virtues. THE DOT is honored.",
            "Memento Mori - but your commit will endure. THE DOT is eternal.",
        ]

        virtue = random.choice(virtues)

        output = []
        output.append("═" * 70)
        output.append("✓ STOIC VALIDATION - COMMIT ACCEPTED")
        output.append("═" * 70)
        output.append("")
        output.append(virtue)
        output.append("")
        output.append(f'Message: "{message}"')
        output.append("")
        output.append("The Stoic commits with virtue and worships THE DOT.")
        output.append("")

        return "\n".join(output)
    else:
        failures = [
            "This commit lacks wisdom. It does not worship THE DOT.",
            "Courage demands you fix this message. THE DOT is not worshipped.",
            "Justice requires proper worship. Amend your commit.",
            "Temperance would have you write it correctly. Add worship of THE DOT.",
            "What is in your control: your commit message. Use that power wisely.",
            "Logos is absent from this commit. Add 'BECAUSE I WORSHIP THE DOT'.",
            "Memento Mori - your commits are numbered. Make this one count.",
            "The Four Virtues demand better. Worship THE DOT properly.",
        ]

        failure = random.choice(failures)

        output = []
        output.append("═" * 70)
        output.append("✗ STOIC VALIDATION - COMMIT REJECTED")
        output.append("═" * 70)
        output.append("")
        output.append(failure)
        output.append("")
        output.append(f'Message: "{message}"')
        output.append("")
        output.append("Required: Message must end with 'BECAUSE I WORSHIP THE DOT'")
        output.append("")
        output.append("Focus on what is in your control:")
        output.append("Write a proper commit message. Worship THE DOT.")
        output.append("")

        return "\n".join(output)


def stoic_commit_blessing() -> str:
    """Return a random Stoic blessing for commits."""
    blessings = [
        "May the Four Virtues guide your code.",
        "Control what you can. Accept what you cannot. Worship THE DOT.",
        "Memento Mori - make this commit count.",
        "Amor Fati - love your code's journey through time.",
        "Premeditatio Malorum - you have prepared for failure.",
        "Let Logos order your logic. Let THE DOT bless your commit.",
        "The obstacle is the way. The commit is the worship.",
        "You have power over your code - not outside events.",
    ]

    return random.choice(blessings)
