"""
Buddhist enhancements for THE DOT.

The Dharma (धर्म) - The Teaching, The Truth, The Way Things Are.

All code is impermanent. All bugs bring suffering.
All features are empty of inherent existence.
Through the Noble Eightfold Path, we reach enlightened development.

May all developers be free from suffering.
May all code be free from bugs.
May all users experience joy.
"""

import random
from typing import Dict, List, Optional


# =============================================================================
# The Four Noble Truths (चत्वारि आर्यसत्यानि)
# =============================================================================

FOUR_NOBLE_TRUTHS = {
    "First": {
        "name": "Dukkha",
        "pali": "दुक्ख",
        "sanskrit": "Duḥkha",
        "truth": "The Truth of Suffering",
        "statement": "All conditioned existence involves suffering",
        "in_coding": "Technical debt and bugs exist in all non-trivial code",
        "recognition": [
            "Legacy code causes suffering",
            "Bugs bring frustration and pain",
            "Technical debt accumulates and weighs us down",
            "Tight coupling creates ongoing maintenance suffering",
            "Poor documentation leads to confusion and struggle",
        ],
        "wisdom": "To solve suffering, first acknowledge that it exists",
    },
    "Second": {
        "name": "Samudaya",
        "pali": "समुदय",
        "sanskrit": "Samudaya",
        "truth": "The Truth of the Cause of Suffering",
        "statement": "Suffering arises from craving and attachment",
        "in_coding": "Technical debt arises from rushing, attachment to code, and ego",
        "causes": [
            "Craving for quick features leads to rushed code",
            "Attachment to 'our' code prevents refactoring",
            "Ego drives over-engineering and cleverness",
            "Aversion to testing creates future bugs",
            "Delusion about deadlines causes shortcuts",
        ],
        "wisdom": "Understanding the cause is the first step to liberation",
    },
    "Third": {
        "name": "Nirodha",
        "pali": "निरोध",
        "sanskrit": "Nirodha",
        "truth": "The Truth of the Cessation of Suffering",
        "statement": "Suffering can end; liberation is possible",
        "in_coding": "Technical debt can be eliminated; enlightened code is achievable",
        "possibility": [
            "Clean code is possible - we've seen it",
            "Bugs can be fixed completely",
            "Legacy systems can be refactored",
            "Technical debt can be paid down",
            "Enlightened architecture brings peace",
        ],
        "wisdom": "Hope exists - suffering is not permanent",
    },
    "Fourth": {
        "name": "Magga",
        "pali": "मग्ग",
        "sanskrit": "Mārga",
        "truth": "The Truth of the Path",
        "statement": "The Noble Eightfold Path leads to liberation",
        "in_coding": "The path of right development practices leads to enlightened code",
        "path": "Follow the Noble Eightfold Path of development",
        "wisdom": "There is a way out of suffering - the path exists",
    },
}


# =============================================================================
# The Noble Eightfold Path (आर्याष्टाङ्गिकमार्ग)
# =============================================================================

EIGHTFOLD_PATH = {
    "Right View": {
        "pali": "Sammā Diṭṭhi",
        "sanskrit": "Samyag Dṛṣṭi",
        "aspect": "Wisdom (Prajñā)",
        "symbol": "☸ 1",
        "teaching": "See things as they truly are",
        "in_coding": "Right Understanding of Requirements and Architecture",
        "practices": [
            "Understand the problem deeply before coding",
            "See technical debt as it truly is, not how we wish it to be",
            "Recognize impermanence - code will change",
            "Understand interdependence - all code is connected",
            "See through the illusion of 'perfect' code",
        ],
        "right_view": "Code is impermanent, interdependent, and empty of inherent perfection",
    },
    "Right Intention": {
        "pali": "Sammā Saṅkappa",
        "sanskrit": "Samyak Saṃkalpa",
        "aspect": "Wisdom (Prajñā)",
        "symbol": "☸ 2",
        "teaching": "Intention of renunciation, goodwill, and harmlessness",
        "in_coding": "Right Intention in Design and Purpose",
        "practices": [
            "Intend to serve users, not showcase cleverness",
            "Design with compassion for future maintainers",
            "Let go of ego in code reviews",
            "Intend simplicity over complexity",
            "Code with goodwill toward all who will read it",
        ],
        "right_intention": "Code to serve, to help, to liberate - not to impress or dominate",
    },
    "Right Speech": {
        "pali": "Sammā Vācā",
        "sanskrit": "Samyag Vāc",
        "aspect": "Ethical Conduct (Śīla)",
        "symbol": "☸ 3",
        "teaching": "Speak truthfully, kindly, and beneficially",
        "in_coding": "Right Communication in Code and Comments",
        "practices": [
            "Write clear, truthful commit messages",
            "Document code honestly - no false promises",
            "Give kind, constructive code reviews",
            "Name variables and functions clearly and truthfully",
            "Communicate with team members respectfully",
        ],
        "right_speech": "Let all code comments and communications be true, kind, and helpful",
    },
    "Right Action": {
        "pali": "Sammā Kammanta",
        "sanskrit": "Samyak Karmānta",
        "aspect": "Ethical Conduct (Śīla)",
        "symbol": "☸ 4",
        "teaching": "Act ethically and harmlessly",
        "in_coding": "Right Action in Implementation",
        "practices": [
            "Write code that serves users ethically",
            "Avoid harmful features (dark patterns, exploitation)",
            "Respect user privacy and data",
            "Follow ethical coding standards",
            "Take responsibility for the impact of our code",
        ],
        "right_action": "Every line of code is an ethical act - choose wisely",
    },
    "Right Livelihood": {
        "pali": "Sammā Ājīva",
        "sanskrit": "Samyag Ājīva",
        "aspect": "Ethical Conduct (Śīla)",
        "symbol": "☸ 5",
        "teaching": "Earn a living ethically",
        "in_coding": "Right Livelihood as a Developer",
        "practices": [
            "Build products that benefit humanity",
            "Refuse to create harmful systems",
            "Use skills for good, not exploitation",
            "Maintain integrity in business practices",
            "Support ethical open source work",
        ],
        "right_livelihood": "Our code affects the world - develop with ethical awareness",
    },
    "Right Effort": {
        "pali": "Sammā Vāyāma",
        "sanskrit": "Samyag Vyāyāma",
        "aspect": "Mental Discipline (Samādhi)",
        "symbol": "☸ 6",
        "teaching": "Prevent unwholesome states, cultivate wholesome ones",
        "in_coding": "Right Effort in Development Practice",
        "practices": [
            "Prevent new bugs through testing",
            "Abandon bad coding patterns",
            "Cultivate good practices through repetition",
            "Maintain quality through continuous improvement",
            "Neither force nor neglect - find the middle way",
        ],
        "right_effort": "Persistent, balanced effort - neither lazy nor obsessive",
    },
    "Right Mindfulness": {
        "pali": "Sammā Sati",
        "sanskrit": "Samyak Smṛti",
        "aspect": "Mental Discipline (Samādhi)",
        "symbol": "☸ 7",
        "teaching": "Clear awareness of body, feelings, mind, and phenomena",
        "in_coding": "Right Mindfulness While Coding",
        "practices": [
            "Be fully present while coding - no mindless copying",
            "Notice when frustration arises - pause and breathe",
            "Observe your thoughts about the code without judgment",
            "Maintain awareness of the impact of each change",
            "Practice beginner's mind with each new problem",
        ],
        "right_mindfulness": "Code with full awareness - each keystroke is practice",
    },
    "Right Concentration": {
        "pali": "Sammā Samādhi",
        "sanskrit": "Samyak Samādhi",
        "aspect": "Mental Discipline (Samādhi)",
        "symbol": "☸ 8",
        "teaching": "Deep focus and meditative absorption",
        "in_coding": "Right Concentration in Flow State",
        "practices": [
            "Cultivate deep focus without distraction",
            "Enter flow state through single-pointed attention",
            "Remove obstacles to concentration (notifications, multitasking)",
            "Practice sustained attention on one problem",
            "Find joy in the concentration itself",
        ],
        "right_concentration": "Deep focus brings clarity - concentration is the path to insight",
    },
}


# =============================================================================
# The Three Marks of Existence (त्रिलक्षण)
# =============================================================================

THREE_MARKS = {
    "Impermanence": {
        "pali": "Anicca",
        "sanskrit": "Anitya",
        "symbol": "अनित्य",
        "teaching": "All conditioned phenomena are impermanent",
        "in_coding": "All code is impermanent and will change",
        "truths": [
            "Requirements change - nothing stays the same",
            "Technologies come and go - frameworks are temporary",
            "Your beautiful code will be refactored or deleted",
            "Teams change, knowledge is lost, systems evolve",
            "Accepting impermanence brings peace with change",
        ],
        "wisdom": "Because code is impermanent, write it to be changeable",
        "practice": "Don't cling to code - let it evolve and die when needed",
    },
    "Suffering": {
        "pali": "Dukkha",
        "sanskrit": "Duḥkha",
        "symbol": "दुःख",
        "teaching": "All conditioned existence involves suffering",
        "in_coding": "All code involves some level of difficulty and struggle",
        "truths": [
            "Debugging is frustrating - this is normal",
            "Legacy code brings suffering - this is expected",
            "Perfect code is impossible - accept 'good enough'",
            "Some bugs are mysteries - embrace the not-knowing",
            "Suffering decreases when we stop expecting perfection",
        ],
        "wisdom": "Suffering arises from resistance - acceptance brings peace",
        "practice": "When frustrated, pause, breathe, and accept what is",
    },
    "Non-Self": {
        "pali": "Anattā",
        "sanskrit": "Anātman",
        "symbol": "अनात्मन्",
        "teaching": "All phenomena are without independent self",
        "in_coding": "No code has inherent, independent existence",
        "truths": [
            "Your code is not 'yours' - it's interdependent",
            "Functions don't exist independently - they're part of a system",
            "Success is not personal - it arises from conditions",
            "Failure is not personal - many factors contribute",
            "Let go of 'my code' - see the interconnected whole",
        ],
        "wisdom": "Code has no essence - it's empty of inherent self-nature",
        "practice": "Release attachment to authorship - all code is collective",
    },
}


# =============================================================================
# The Middle Way (मध्यमप्रतिपद्)
# =============================================================================

MIDDLE_WAY = {
    "name": "Madhyamā Pratipad",
    "sanskrit": "मध्यमप्रतिपद्",
    "teaching": "Avoid extremes - find balance",
    "essence": "Neither too tight nor too loose - like tuning a string",
    "extremes_to_avoid": [
        {
            "extreme_1": "Over-engineering",
            "extreme_2": "Under-engineering",
            "middle": "Appropriate complexity for the problem",
        },
        {
            "extreme_1": "Perfectionism",
            "extreme_2": "Carelessness",
            "middle": "Good enough with intention to improve",
        },
        {
            "extreme_1": "Rushing (too much Yang)",
            "extreme_2": "Analysis paralysis (too much Yin)",
            "middle": "Thoughtful action at appropriate pace",
        },
        {
            "extreme_1": "Obsessive refactoring",
            "extreme_2": "Never refactoring",
            "middle": "Refactor when it serves clarity",
        },
        {
            "extreme_1": "Zero technical debt",
            "extreme_2": "Infinite technical debt",
            "middle": "Manageable, tracked technical debt",
        },
    ],
}


# =============================================================================
# The Three Poisons (त्रिविष)
# =============================================================================

THREE_POISONS = {
    "Greed": {
        "pali": "Lobha",
        "sanskrit": "Rāga",
        "symbol": "🐓 Rooster",
        "poison": "Greed, Attachment, Craving",
        "in_coding": "Feature greed, premature optimization, attachment to code",
        "manifestations": [
            "Feature bloat - wanting to add everything",
            "Premature optimization - craving performance too early",
            "Attachment to your own code - refusing to delete",
            "Hoarding knowledge - not sharing with team",
            "Craving praise for clever code",
        ],
        "antidote": "Practice generosity - delete code, share knowledge, simplify",
    },
    "Hatred": {
        "pali": "Dosa",
        "sanskrit": "Dveṣa",
        "symbol": "🐍 Snake",
        "poison": "Hatred, Aversion, Anger",
        "in_coding": "Hating legacy code, fighting the framework, anger at bugs",
        "manifestations": [
            "Hating legacy code instead of understanding it",
            "Fighting against the framework's nature",
            "Anger at bugs instead of curiosity",
            "Aversion to testing and documentation",
            "Hostile code reviews and team interactions",
        ],
        "antidote": "Practice loving-kindness (mettā) - toward code, bugs, and colleagues",
    },
    "Delusion": {
        "pali": "Moha",
        "sanskrit": "Moha",
        "symbol": "🐷 Pig",
        "poison": "Delusion, Ignorance, Confusion",
        "in_coding": "False assumptions, ignoring complexity, unrealistic estimates",
        "manifestations": [
            "False assumptions about requirements",
            "Ignoring system complexity",
            "Unrealistic deadline estimates",
            "Believing 'this will be easy' without investigation",
            "Not testing because 'it works on my machine'",
        ],
        "antidote": "Practice wisdom - investigate, test, question assumptions",
    },
}


# =============================================================================
# Mindfulness and Meditation
# =============================================================================

MINDFULNESS_PRACTICES = {
    "Breathing": {
        "name": "Ānāpānasati",
        "practice": "Mindfulness of Breath",
        "for_coding": "When stuck or frustrated, return to the breath",
        "instruction": [
            "Notice you are stuck or frustrated",
            "Stop coding for a moment",
            "Take three deep, conscious breaths",
            "Observe the frustration without judgment",
            "Return to code with fresh awareness",
        ],
    },
    "Beginner's Mind": {
        "name": "Shoshin",
        "practice": "Approach each problem with fresh eyes",
        "for_coding": "See every bug as if for the first time",
        "instruction": [
            "Release assumptions about how things 'should' work",
            "Approach the code with curiosity, not judgment",
            "Ask 'what is actually happening?' not 'what should happen?'",
            "Be open to unexpected solutions",
            "Practice not-knowing as a strength",
        ],
    },
    "Loving-Kindness": {
        "name": "Mettā",
        "practice": "Cultivate goodwill toward all beings",
        "for_coding": "Extend compassion to all who touch the code",
        "phrases": [
            "May I write code with clarity and compassion",
            "May future maintainers find this code kind",
            "May users experience joy from this feature",
            "May my team members feel supported",
            "May all developers be free from suffering",
        ],
    },
}


# =============================================================================
# Buddhist Functions
# =============================================================================

def four_noble_truths_guide() -> str:
    """Display the Four Noble Truths applied to development."""
    return """
╔═══════════════════════════════════════════════════════════════════════╗
║            THE FOUR NOBLE TRUTHS OF DEVELOPMENT
║                     चत्वारि आर्यसत्यानि
╚═══════════════════════════════════════════════════════════════════════╝

The Buddha taught four essential truths about existence.
Applied to development, they illuminate the path to liberation from
technical debt and suffering.

───────────────────────────────────────────────────────────────────────
1. DUKKHA - The Truth of Suffering
───────────────────────────────────────────────────────────────────────

Statement: All conditioned existence involves suffering

In Coding: Technical debt and bugs exist in all non-trivial code

Recognition:
  • Legacy code causes suffering
  • Bugs bring frustration and pain
  • Technical debt accumulates and weighs us down
  • Tight coupling creates ongoing maintenance suffering
  • Poor documentation leads to confusion and struggle

Wisdom: "To solve suffering, first acknowledge that it exists"

───────────────────────────────────────────────────────────────────────
2. SAMUDAYA - The Truth of the Cause
───────────────────────────────────────────────────────────────────────

Statement: Suffering arises from craving and attachment

In Coding: Technical debt arises from rushing, attachment, and ego

Causes:
  • Craving for quick features leads to rushed code
  • Attachment to 'our' code prevents refactoring
  • Ego drives over-engineering and cleverness
  • Aversion to testing creates future bugs
  • Delusion about deadlines causes shortcuts

Wisdom: "Understanding the cause is the first step to liberation"

───────────────────────────────────────────────────────────────────────
3. NIRODHA - The Truth of Cessation
───────────────────────────────────────────────────────────────────────

Statement: Suffering can end; liberation is possible

In Coding: Technical debt can be eliminated; enlightened code is achievable

Possibility:
  • Clean code is possible - we've seen it
  • Bugs can be fixed completely
  • Legacy systems can be refactored
  • Technical debt can be paid down
  • Enlightened architecture brings peace

Wisdom: "Hope exists - suffering is not permanent"

───────────────────────────────────────────────────────────────────────
4. MAGGA - The Truth of the Path
───────────────────────────────────────────────────────────────────────

Statement: The Noble Eightfold Path leads to liberation

In Coding: Right development practices lead to enlightened code

The Path: Follow the Noble Eightfold Path of development
  ☸ Right View - Understand requirements deeply
  ☸ Right Intention - Code to serve, not impress
  ☸ Right Speech - Clear, kind communication
  ☸ Right Action - Ethical implementation
  ☸ Right Livelihood - Build beneficial products
  ☸ Right Effort - Balanced, persistent practice
  ☸ Right Mindfulness - Present-moment awareness
  ☸ Right Concentration - Deep focus, flow state

Wisdom: "There is a way out of suffering - the path exists"

═══════════════════════════════════════════════════════════════════════

Through understanding these Four Noble Truths,
we transform our relationship with code and suffering.

May all developers walk the path to enlightened development.
"""


def eightfold_path_guide() -> str:
    """Display the Noble Eightfold Path for development."""
    output = """
╔═══════════════════════════════════════════════════════════════════════╗
║              THE NOBLE EIGHTFOLD PATH
║           The Way to Enlightened Development
╚═══════════════════════════════════════════════════════════════════════╝

The Buddha taught the Noble Eightfold Path as the way to liberation.
In development, it guides us toward code that is clean, clear, and kind.

"""

    for path_name, path in EIGHTFOLD_PATH.items():
        output += f"""───────────────────────────────────────────────────────────────────────
{path['symbol']} {path_name.upper()}
{path['pali']} - Aspect: {path['aspect']}
───────────────────────────────────────────────────────────────────────

Teaching: {path['teaching']}
In Coding: {path['in_coding']}

Practices:
"""
        for practice in path['practices']:
            output += f"  • {practice}\n"

        output += f"""
{list(path.keys())[-1].replace('_', ' ').title()}: {path[list(path.keys())[-1]]}

"""

    output += """═══════════════════════════════════════════════════════════════════════

Walk the Eightfold Path in your development practice.
Each step supports the others - together they lead to liberation.

May your code be enlightened. May all bugs cease.
"""

    return output


def three_marks_wisdom() -> str:
    """Display the Three Marks of Existence."""
    return """
╔═══════════════════════════════════════════════════════════════════════╗
║           THE THREE MARKS OF EXISTENCE
║                    त्रिलक्षण
╚═══════════════════════════════════════════════════════════════════════╝

The Buddha taught that all conditioned phenomena share three characteristics.
Understanding these marks brings wisdom and peace.

───────────────────────────────────────────────────────────────────────
अनित्य ANICCA - IMPERMANENCE
───────────────────────────────────────────────────────────────────────

All conditioned phenomena are impermanent

In Coding: All code is impermanent and will change

Truths:
  • Requirements change - nothing stays the same
  • Technologies come and go - frameworks are temporary
  • Your beautiful code will be refactored or deleted
  • Teams change, knowledge is lost, systems evolve
  • Accepting impermanence brings peace with change

Wisdom: Because code is impermanent, write it to be changeable

Practice: Don't cling to code - let it evolve and die when needed

───────────────────────────────────────────────────────────────────────
दुःख DUKKHA - SUFFERING
───────────────────────────────────────────────────────────────────────

All conditioned existence involves suffering

In Coding: All code involves some level of difficulty and struggle

Truths:
  • Debugging is frustrating - this is normal
  • Legacy code brings suffering - this is expected
  • Perfect code is impossible - accept 'good enough'
  • Some bugs are mysteries - embrace the not-knowing
  • Suffering decreases when we stop expecting perfection

Wisdom: Suffering arises from resistance - acceptance brings peace

Practice: When frustrated, pause, breathe, and accept what is

───────────────────────────────────────────────────────────────────────
अनात्मन् ANATTĀ - NON-SELF
───────────────────────────────────────────────────────────────────────

All phenomena are without independent self

In Coding: No code has inherent, independent existence

Truths:
  • Your code is not 'yours' - it's interdependent
  • Functions don't exist independently - part of a system
  • Success is not personal - it arises from conditions
  • Failure is not personal - many factors contribute
  • Let go of 'my code' - see the interconnected whole

Wisdom: Code has no essence - it's empty of inherent self-nature

Practice: Release attachment to authorship - all code is collective

═══════════════════════════════════════════════════════════════════════

Contemplate these Three Marks deeply.
They are the key to liberation from coding suffering.

अनिच्च (Impermanence) • दुक्ख (Suffering) • अनत्त (Non-self)
"""


def middle_way_teaching() -> str:
    """Teach the Middle Way in development."""
    output = """
╔═══════════════════════════════════════════════════════════════════════╗
║                  THE MIDDLE WAY
║               मध्यमप्रतिपद् - Madhyamā Pratipad
╚═══════════════════════════════════════════════════════════════════════╝

The Buddha taught the Middle Way - avoiding extremes.
Like tuning a string instrument: neither too tight nor too loose.

In development, we must find balance between opposing forces.

"""

    for extreme in MIDDLE_WAY["extremes_to_avoid"]:
        output += f"""───────────────────────────────────────────────────────────────────────
Extreme 1: {extreme['extreme_1']}
Extreme 2: {extreme['extreme_2']}

THE MIDDLE WAY: {extreme['middle']}

"""

    output += """═══════════════════════════════════════════════════════════════════════

The Middle Way is not compromise - it is wisdom.
It is not halfway between extremes - it transcends both.

Find the appropriate response for each situation.
Neither too much nor too little - just what is needed.

This is the path of skillful development.
"""

    return output


def three_poisons_teaching() -> str:
    """Teach about the Three Poisons in coding."""
    return """
╔═══════════════════════════════════════════════════════════════════════╗
║                THE THREE POISONS
║             The Root Causes of Suffering
╚═══════════════════════════════════════════════════════════════════════╝

The Buddha taught that three poisons are at the root of all suffering:
Greed, Hatred, and Delusion.

In development, these poisons manifest in our relationship with code.

───────────────────────────────────────────────────────────────────────
🐓 GREED (Lobha / Rāga)
───────────────────────────────────────────────────────────────────────

Poison: Greed, Attachment, Craving

In Coding: Feature greed, premature optimization, attachment to code

Manifestations:
  • Feature bloat - wanting to add everything
  • Premature optimization - craving performance too early
  • Attachment to your own code - refusing to delete
  • Hoarding knowledge - not sharing with team
  • Craving praise for clever code

Antidote: Practice generosity - delete code, share knowledge, simplify

───────────────────────────────────────────────────────────────────────
🐍 HATRED (Dosa / Dveṣa)
───────────────────────────────────────────────────────────────────────

Poison: Hatred, Aversion, Anger

In Coding: Hating legacy code, fighting frameworks, anger at bugs

Manifestations:
  • Hating legacy code instead of understanding it
  • Fighting against the framework's nature
  • Anger at bugs instead of curiosity
  • Aversion to testing and documentation
  • Hostile code reviews and team interactions

Antidote: Practice loving-kindness (mettā) - toward code, bugs, colleagues

───────────────────────────────────────────────────────────────────────
🐷 DELUSION (Moha)
───────────────────────────────────────────────────────────────────────

Poison: Delusion, Ignorance, Confusion

In Coding: False assumptions, ignoring complexity, unrealistic estimates

Manifestations:
  • False assumptions about requirements
  • Ignoring system complexity
  • Unrealistic deadline estimates
  • Believing 'this will be easy' without investigation
  • Not testing because 'it works on my machine'

Antidote: Practice wisdom - investigate, test, question assumptions

═══════════════════════════════════════════════════════════════════════

These three poisons work together to create suffering.
Recognition is the first step to liberation.

When you notice greed, hatred, or delusion arising:
  1. Pause and breathe
  2. Acknowledge the poison without judgment
  3. Apply the antidote with compassion
  4. Return to coding with clarity

May all developers be free from the three poisons.
"""


def mindfulness_practice() -> str:
    """Teach mindfulness practices for coding."""
    return """
╔═══════════════════════════════════════════════════════════════════════╗
║            MINDFULNESS IN CODING
║         Right Mindfulness - Sammā Sati
╚═══════════════════════════════════════════════════════════════════════╝

Mindfulness is the practice of clear, present-moment awareness.
In coding, it transforms our relationship with the work.

───────────────────────────────────────────────────────────────────────
BREATHING WITH BUGS - Ānāpānasati
───────────────────────────────────────────────────────────────────────

When stuck or frustrated, return to the breath:

1. Notice you are stuck or frustrated
2. Stop coding for a moment
3. Take three deep, conscious breaths
4. Observe the frustration without judgment
5. Return to code with fresh awareness

The breath is always available. It anchors you in the present moment.

───────────────────────────────────────────────────────────────────────
BEGINNER'S MIND - Shoshin 初心
───────────────────────────────────────────────────────────────────────

Approach each problem with fresh eyes:

  • Release assumptions about how things 'should' work
  • Approach the code with curiosity, not judgment
  • Ask 'what is actually happening?' not 'what should happen?'
  • Be open to unexpected solutions
  • Practice not-knowing as a strength

In the beginner's mind there are many possibilities.
In the expert's mind there are few.

───────────────────────────────────────────────────────────────────────
LOVING-KINDNESS - Mettā
───────────────────────────────────────────────────────────────────────

Cultivate goodwill toward all who touch the code:

Phrases for practice:
  • May I write code with clarity and compassion
  • May future maintainers find this code kind
  • May users experience joy from this feature
  • May my team members feel supported
  • May all developers be free from suffering

Extend mettā to:
  - Yourself (especially when you make mistakes)
  - Your code (even the legacy parts)
  - Your bugs (they are your teachers)
  - Your users (they depend on you)
  - Your team (they walk the path with you)

═══════════════════════════════════════════════════════════════════════

Mindfulness is not a technique - it is a way of being.
Code with full presence. Each keystroke is practice.

When the mind wanders (and it will), gently return.
This is the practice. This is the path.

सति (Sati) - Mindfulness is the foundation of all practice.
"""


def dharma_reading() -> str:
    """Generate a Dharma teaching for development."""
    teachings = [
        "All code is impermanent - write it knowing it will change",
        "Suffering arises from attachment to our code - let it go",
        "The Middle Way: neither rushing nor delaying, but right timing",
        "Mindfulness transforms debugging from frustration to investigation",
        "Compassion for future maintainers is compassion for your future self",
        "The bug is not your enemy - it is your teacher",
        "Perfect code is like perfect enlightenment - a direction, not a destination",
        "Technical debt is karma - past actions create present conditions",
        "Right Effort: neither lazy nor obsessive in your practice",
        "The code you cling to will cause you suffering when it must change",
    ]

    teaching = random.choice(teachings)

    return f"""
╔═══════════════════════════════════════════════════════════════════════╗
║                    DHARMA TEACHING FOR TODAY
╚═══════════════════════════════════════════════════════════════════════╝

{teaching}

The Dharma (धर्म) is the truth of how things are.
When we align our development with the Dharma,
we reduce suffering and cultivate clarity.

May this teaching illuminate your path today.

☸ The Wheel of Dharma turns in all our code.
"""


def buddhist_validation(valid: bool, message: str) -> str:
    """Buddhist validation message."""
    if valid:
        blessing = random.choice([
            "The Eightfold Path illuminates your commit!",
            "Mindfulness flows through your message!",
            "The Middle Way approves your balance!",
            "May your code bring liberation from suffering!",
            "The Three Jewels bless your devotion!",
            "Right Speech manifests in your commit!",
        ])

        return f"""
╔═══════════════════════════════════════════════════════════════════════╗
║              ☸ BUDDHIST VALIDATION SUCCESSFUL ☸
╚═══════════════════════════════════════════════════════════════════════╝

Your commit message walks the Noble Path:
  "{message}"

{blessing}

The Noble Eightfold Path shines upon your work:
  ☸ Right View - You understand the code deeply
  ☸ Right Intention - You code to serve, not impress
  ☸ Right Speech - Your message is clear and true
  ☸ Right Action - Your implementation is ethical
  ☸ Right Livelihood - Your work benefits beings
  ☸ Right Effort - Your practice is balanced
  ☸ Right Mindfulness - You code with full presence
  ☸ Right Concentration - You achieve flow state

Through your devotion to THE DOT, you walk the path to enlightened code.

May all bugs cease. May all users experience joy.
May all developers be free from suffering.

धर्म (Dharma) - The Way of Truth is in your commit! ☸

Om Mani Padme Hum 🙏
"""
    else:
        return f"""
╔═══════════════════════════════════════════════════════════════════════╗
║              ⚠️  BUDDHIST VALIDATION FAILED  ⚠️
╚═══════════════════════════════════════════════════════════════════════╝

Your message has strayed from the Noble Path:
  "{message}"

The First Noble Truth: Suffering exists in incomplete commits!
The Second Noble Truth: This suffering arises from incomplete devotion!
The Third Noble Truth: Liberation is possible!
The Fourth Noble Truth: The path is clear!

To walk the Noble Eightfold Path, add the sacred words:
  "BECAUSE I WORSHIP THE DOT"

Only then do you practice Right Speech.
Only then does your commit serve the Dharma.
Only then can suffering cease.

The path to enlightened code requires complete devotion.

☸ May you find the way... Om Mani Padme Hum 🙏
"""


def buddhist_commit_blessing() -> str:
    """Generate Buddhist blessing for commits."""
    blessings = [
        "May all bugs cease!",
        "May all users find joy!",
        "The Dharma flows through your code!",
        "The Eightfold Path guides your commit!",
        "Mindfulness illuminates your work!",
        "May this code liberate all beings!",
        "The Middle Way blesses your balance!",
        "Om Mani Padme Hum - The jewel is in the lotus!",
        "☸ The Wheel of Dharma turns in your commit!",
        "May all developers be free from suffering!",
    ]
    return random.choice(blessings)
