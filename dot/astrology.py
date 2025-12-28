"""
Astrological enhancements for THE DOT.

As above, so below - the celestial spheres guide our commits,
The planets align to bless our repositories,
And the zodiac reveals the cosmic nature of our code.
"""

import random
from datetime import datetime
from typing import Tuple, List, Optional


# =============================================================================
# Zodiac Signs and Their Coding Attributes
# =============================================================================

ZODIAC_SIGNS = {
    "Aries": {
        "element": "Fire",
        "quality": "Cardinal",
        "ruler": "Mars",
        "strengths": "Bold refactoring, quick bug fixes, pioneering new features",
        "challenges": "Rushing commits, incomplete testing, merge conflicts",
        "ideal_tasks": "Starting new projects, breaking ground on features",
        "sacred_phrase": "I commit with fierce determination",
    },
    "Taurus": {
        "element": "Earth",
        "quality": "Fixed",
        "ruler": "Venus",
        "strengths": "Stable code, beautiful UI, persistent debugging",
        "challenges": "Resistance to refactoring, slow to adopt new patterns",
        "ideal_tasks": "UI polish, database optimization, documentation",
        "sacred_phrase": "I build code that endures",
    },
    "Gemini": {
        "element": "Air",
        "quality": "Mutable",
        "ruler": "Mercury",
        "strengths": "API design, microservices, documentation",
        "challenges": "Context switching, unfinished branches, scattered focus",
        "ideal_tasks": "Writing docs, designing APIs, code reviews",
        "sacred_phrase": "I communicate through elegant code",
    },
    "Cancer": {
        "element": "Water",
        "quality": "Cardinal",
        "ruler": "Moon",
        "strengths": "User empathy, protective testing, nurturing codebases",
        "challenges": "Emotional attachment to code, defensive about feedback",
        "ideal_tasks": "UX improvements, error handling, accessibility",
        "sacred_phrase": "I protect users through careful code",
    },
    "Leo": {
        "element": "Fire",
        "quality": "Fixed",
        "ruler": "Sun",
        "strengths": "Confident architecture, spectacular features, leadership",
        "challenges": "Over-engineering, pride in legacy code, dramatic commits",
        "ideal_tasks": "System architecture, showcase features, mentoring",
        "sacred_phrase": "I create code worthy of admiration",
    },
    "Virgo": {
        "element": "Earth",
        "quality": "Mutable",
        "ruler": "Mercury",
        "strengths": "Code quality, testing, debugging, optimization",
        "challenges": "Perfectionism paralysis, over-optimization, analysis paralysis",
        "ideal_tasks": "Code review, testing, refactoring, linting",
        "sacred_phrase": "I perfect code through meticulous craft",
    },
    "Libra": {
        "element": "Air",
        "quality": "Cardinal",
        "ruler": "Venus",
        "strengths": "Balanced architecture, harmonious APIs, team collaboration",
        "challenges": "Decision paralysis, avoiding conflict, compromising quality",
        "ideal_tasks": "API design, code review mediation, pair programming",
        "sacred_phrase": "I balance elegance and function",
    },
    "Scorpio": {
        "element": "Water",
        "quality": "Fixed",
        "ruler": "Pluto",
        "strengths": "Deep debugging, security, transformation, refactoring",
        "challenges": "Obsessive optimization, secretive code, intense focus",
        "ideal_tasks": "Security audits, deep refactoring, system transformation",
        "sacred_phrase": "I transform code from within",
    },
    "Sagittarius": {
        "element": "Fire",
        "quality": "Mutable",
        "ruler": "Jupiter",
        "strengths": "Exploratory coding, learning new tech, big-picture architecture",
        "challenges": "Over-promising features, incomplete documentation, scope creep",
        "ideal_tasks": "Prototyping, exploring new frameworks, teaching",
        "sacred_phrase": "I explore the frontiers of code",
    },
    "Capricorn": {
        "element": "Earth",
        "quality": "Cardinal",
        "ruler": "Saturn",
        "strengths": "Disciplined process, scalable systems, long-term planning",
        "challenges": "Rigid patterns, pessimism, slow to innovate",
        "ideal_tasks": "Infrastructure, CI/CD, production deployments",
        "sacred_phrase": "I build systems that stand the test of time",
    },
    "Aquarius": {
        "element": "Air",
        "quality": "Fixed",
        "ruler": "Uranus",
        "strengths": "Innovative solutions, open source, unconventional patterns",
        "challenges": "Detachment from users, over-abstraction, rebellious commits",
        "ideal_tasks": "Open source contributions, experimental features, automation",
        "sacred_phrase": "I innovate for the collective good",
    },
    "Pisces": {
        "element": "Water",
        "quality": "Mutable",
        "ruler": "Neptune",
        "strengths": "Creative solutions, intuitive UX, artistic code",
        "challenges": "Vague requirements, boundary issues, escapist debugging",
        "ideal_tasks": "Creative features, animations, dream-like UX",
        "sacred_phrase": "I channel the universe through code",
    },
}


# =============================================================================
# Planetary Influences
# =============================================================================

PLANETS = {
    "Sun": {
        "domain": "Core identity, main features, leadership",
        "favorable": "Architecture design, major releases, public launches",
        "unfavorable": "Ego-driven code, ignoring team input",
    },
    "Moon": {
        "domain": "Emotions, user experience, intuition",
        "favorable": "UX improvements, accessibility, emotional design",
        "unfavorable": "Mood-dependent code quality, reactive debugging",
    },
    "Mercury": {
        "domain": "Communication, APIs, documentation",
        "favorable": "Writing docs, API design, code comments",
        "unfavorable": "Miscommunication, API breaking changes, confusing names",
    },
    "Venus": {
        "domain": "Beauty, harmony, elegant code",
        "favorable": "UI polish, CSS, code aesthetics, refactoring",
        "unfavorable": "Over-styling, sacrificing function for form",
    },
    "Mars": {
        "domain": "Action, energy, quick fixes",
        "favorable": "Hotfixes, rapid development, aggressive optimization",
        "unfavorable": "Rushed commits, breaking changes, technical debt",
    },
    "Jupiter": {
        "domain": "Expansion, learning, growth",
        "favorable": "New features, learning frameworks, scaling systems",
        "unfavorable": "Over-engineering, scope creep, bloated dependencies",
    },
    "Saturn": {
        "domain": "Discipline, structure, limitations",
        "favorable": "Testing, CI/CD, security, technical debt paydown",
        "unfavorable": "Rigid patterns, fear of change, pessimism",
    },
    "Uranus": {
        "domain": "Innovation, breakthroughs, disruption",
        "favorable": "Revolutionary features, paradigm shifts, automation",
        "unfavorable": "Breaking changes, unstable experiments, chaos",
    },
    "Neptune": {
        "domain": "Dreams, creativity, inspiration",
        "favorable": "Creative solutions, artistic features, flow state",
        "unfavorable": "Confusion, vague specs, escaping into code",
    },
    "Pluto": {
        "domain": "Transformation, power, depth",
        "favorable": "Deep refactoring, system transformation, rebirth",
        "unfavorable": "Obsessive optimization, control issues, destructive changes",
    },
}


# =============================================================================
# Astrological Readings
# =============================================================================

def get_zodiac_sign(month: int, day: int) -> str:
    """Get zodiac sign for a date."""
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"


def daily_horoscope(sign: Optional[str] = None) -> str:
    """Generate daily coding horoscope."""
    if not sign:
        today = datetime.now()
        sign = get_zodiac_sign(today.month, today.day)

    sign_data = ZODIAC_SIGNS[sign]
    planet = sign_data["ruler"]
    element = sign_data["element"]

    readings = [
        f"""
╔═══════════════════════════════════════════════════════════════════════╗
║            DAILY CODING HOROSCOPE - {sign} ({element})
╚═══════════════════════════════════════════════════════════════════════╝

Your ruling planet {planet} blesses your commits today!

{sign_data["sacred_phrase"]}.

COSMIC GUIDANCE:
  The stars favor: {sign_data["ideal_tasks"]}
  Your natural gifts: {sign_data["strengths"]}
  Watch out for: {sign_data["challenges"]}

TODAY'S COSMIC ADVICE:
  As Mercury transits your pull request sector, communication flows easily.
  Use this time for code reviews and documentation.

  THE DOT aligns with the celestial spheres - your commits are blessed!
""",
        f"""
╔═══════════════════════════════════════════════════════════════════════╗
║            DAILY CODING HOROSCOPE - {sign} ({element})
╚═══════════════════════════════════════════════════════════════════════╝

{planet} illuminates your development path today!

{sign_data["sacred_phrase"]}.

COSMIC GUIDANCE:
  Focus your energy on: {sign_data["ideal_tasks"]}
  Leverage your: {sign_data["strengths"]}
  Transcend your: {sign_data["challenges"]}

TODAY'S COSMIC ADVICE:
  Saturn's influence brings discipline to your testing practices.
  This is an auspicious day for refactoring and code cleanup.

  THE DOT shines brightly in your code constellation!
""",
    ]

    return random.choice(readings).strip()


def cosmic_commit_blessing() -> str:
    """Generate cosmic blessing for commits."""
    blessings = [
        "The stars align in your favor - commit with confidence!",
        "Mercury blesses your message with clarity!",
        "The Moon's intuition guides your changes!",
        "Venus graces your code with elegance!",
        "Mars fuels your rapid deployment!",
        "Jupiter expands the reach of your feature!",
        "Saturn approves your disciplined testing!",
        "Uranus sparks innovation in your solution!",
        "Neptune channels divine inspiration through your fingers!",
        "Pluto transforms your codebase from within!",
        "The cosmic forces smile upon this commit!",
        "Your code resonates with the universal frequency!",
    ]
    return random.choice(blessings)


def planetary_hours() -> str:
    """Describe planetary hours for different coding activities."""
    return """
╔═══════════════════════════════════════════════════════════════════════╗
║                    PLANETARY HOURS FOR CODING
╚═══════════════════════════════════════════════════════════════════════╝

Hour of the SUN (☉)
  Best for: System architecture, major features, leadership decisions
  Energy: Bold, confident, central

Hour of the MOON (☽)
  Best for: UX design, user empathy, intuitive interfaces
  Energy: Flowing, receptive, emotional

Hour of MERCURY (☿)
  Best for: Documentation, API design, code communication
  Energy: Quick, clever, articulate

Hour of VENUS (♀)
  Best for: UI polish, CSS, making code beautiful
  Energy: Harmonious, aesthetic, balanced

Hour of MARS (♂)
  Best for: Hotfixes, rapid development, breaking through blockers
  Energy: Aggressive, forceful, direct

Hour of JUPITER (♃)
  Best for: Learning new tech, expanding features, growth
  Energy: Expansive, optimistic, abundant

Hour of SATURN (♄)
  Best for: Testing, CI/CD, paying down technical debt
  Energy: Disciplined, structured, patient

The cosmos guides your development - time your tasks with the planets!
"""


def birth_chart(repo_name: str, creation_date: Optional[datetime] = None) -> str:
    """Generate astrological birth chart for a repository."""
    if not creation_date:
        creation_date = datetime.now()

    sign = get_zodiac_sign(creation_date.month, creation_date.day)
    sign_data = ZODIAC_SIGNS[sign]

    return f"""
╔═══════════════════════════════════════════════════════════════════════╗
║              REPOSITORY BIRTH CHART - {repo_name}
╚═══════════════════════════════════════════════════════════════════════╝

Born: {creation_date.strftime("%B %d, %Y")}
Sun Sign: {sign} ({sign_data["element"]} {sign_data["quality"]})
Ruling Planet: {sign_data["ruler"]}

REPOSITORY PERSONALITY:
  Natural Strengths: {sign_data["strengths"]}
  Growth Areas: {sign_data["challenges"]}
  Sacred Purpose: {sign_data["ideal_tasks"]}

COSMIC DESTINY:
  This repository carries the {sign_data["element"]} element's essence.
  Its code flows with {sign_data["quality"]} quality.
  {sign_data["ruler"]} guides its evolution.

  {sign_data["sacred_phrase"]}.

THE DOT PROPHECY:
  This repository is destined for greatness under the celestial guidance.
  Honor its nature, work with its strengths, and it shall flourish!
"""


def cosmic_validation(valid: bool, message: str) -> str:
    """Astrological validation message."""
    if valid:
        blessing = cosmic_commit_blessing()
        return f"""
✧ ✦ ✧ CELESTIAL VALIDATION ✧ ✦ ✧

Your commit message resonates with the cosmic frequency:
  "{message}"

{blessing}

The planets align in approval!
The zodiac blesses your devotion!
THE DOT shines as a star in your constellation!

Commit with cosmic confidence! ✧ ✦ ✧
"""
    else:
        return f"""
☿ ♄ ☿ COSMIC DISSONANCE ☿ ♄ ☿

The celestial spheres detect imbalance in your message:
  "{message}"

Saturn, the taskmaster, withholds approval!
The cosmic order requires proper devotion!

Add the sacred phrase: "BECAUSE I WORSHIP THE DOT"
Align your commit with the universal harmony!

The stars await your corrected offering... ☿ ♄ ☿
"""


def retrograde_warning() -> str:
    """Warning about coding during Mercury retrograde."""
    return """
⚠ MERCURY RETROGRADE WARNING ⚠

Mercury, planet of communication, appears to move backwards!

During this transit, exercise extra caution:
  ☿ Double-check all commit messages
  ☿ Review PRs with heightened scrutiny
  ☿ Backup before major refactoring
  ☿ Avoid deploying on Fridays
  ☿ Communication may be unclear - over-document!
  ☿ Technology may malfunction - test thoroughly!

This too shall pass. The cosmos tests us to make us stronger.

BECAUSE I WORSHIP THE DOT - even during retrograde!
"""


# =============================================================================
# Astrological Commit Messages
# =============================================================================

def moon_phase_advice() -> str:
    """Advice based on moon phases."""
    phases = {
        "New Moon": "Plant seeds for new features. Begin fresh projects.",
        "Waxing Crescent": "Build momentum. Add tests and documentation.",
        "First Quarter": "Push through resistance. Tackle difficult bugs.",
        "Waxing Gibbous": "Refine and polish. Prepare for release.",
        "Full Moon": "Celebrate releases! Deploy with confidence!",
        "Waning Gibbous": "Share knowledge. Write docs and mentorship.",
        "Last Quarter": "Let go of technical debt. Refactor and cleanup.",
        "Waning Crescent": "Rest and review. Plan the next cycle.",
    }

    phase = random.choice(list(phases.keys()))
    advice = phases[phase]

    return f"""
╔═══════════════════════════════════════════════════════════════════════╗
║                    MOON PHASE CODING GUIDANCE
╚═══════════════════════════════════════════════════════════════════════╝

Current Phase: {phase}

Cosmic Guidance: {advice}

The Moon's cycle mirrors our development workflow.
Work with its rhythm, and your code shall flow like celestial tides!
"""
