"""
Astrological enhancements for THE DOT.

As above, so below - the celestial spheres guide our commits,
The planets align to bless our repositories,
And the zodiac reveals the cosmic nature of our code.

No external dependencies: This module provides a self‑contained, approximate
ephemeris for planets and a few minor bodies/comets for narrative purposes.
It avoids network calls and third‑party libraries by design.
"""

import random
from datetime import datetime
from typing import Tuple, List, Optional, Dict
from math import sin, cos, tan, atan2, sqrt, radians, degrees
from pathlib import Path
import json


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


# =============================================================================
# Local Ephemeris (planets + minor bodies + comets; approximate)
# =============================================================================

# Simplified orbital parameters (circular, ecliptic latitude ~ 0) for narrative use.
_PLANET_ELEMENTS: Dict[str, Dict[str, float]] = {}
_EPOCH_JD: float = 2451545.0
_MINOR_ELEMENTS: Dict[str, Dict[str, float]] = {}
_COMET_ELEMENTS: Dict[str, Dict[str, float]] = {}


def _load_planet_elements() -> None:
    global _PLANET_ELEMENTS, _EPOCH_JD
    if _PLANET_ELEMENTS:
        return
    data_path = Path(__file__).parent / "data" / "ephemeris" / "planets_j2000.json"
    with data_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    _EPOCH_JD = float(data.get("epoch_jd", 2451545.0))
    _PLANET_ELEMENTS = {k.lower(): v for k, v in data["bodies"].items()}


def _load_minor_elements() -> None:
    global _MINOR_ELEMENTS
    if _MINOR_ELEMENTS:
        return
    data_path = Path(__file__).parent / "data" / "ephemeris" / "minor_bodies_j2000.json"
    if data_path.exists():
        with data_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        _MINOR_ELEMENTS = {k.lower(): v for k, v in data.get("bodies", {}).items()}


def _load_comet_elements() -> None:
    global _COMET_ELEMENTS
    if _COMET_ELEMENTS:
        return
    data_path = Path(__file__).parent / "data" / "ephemeris" / "comets_j2000.json"
    if data_path.exists():
        with data_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        _COMET_ELEMENTS = {k.lower(): v for k, v in data.get("bodies", {}).items()}


def _julian_day(dt: datetime) -> float:
    y = dt.year
    m = dt.month
    D = dt.day + (dt.hour + (dt.minute + dt.second / 60.0) / 60.0) / 24.0
    if m <= 2:
        y -= 1
        m += 12
    A = y // 100
    B = 2 - A + (A // 4)
    jd = int(365.25 * (y + 4716)) + int(30.6001 * (m + 1)) + D + B - 1524.5
    return jd


def _kepler_E(M: float, e: float, tol: float = 1e-8, max_iter: int = 50) -> float:
    # Solve E - e sin E = M for E (radians)
    E = M
    for _ in range(max_iter):
        f = E - e * sin(E) - M
        d = 1 - e * cos(E)
        dE = -f / d
        E = E + dE
        if abs(dE) < tol:
            break
    return E


def _heliocentric_ecliptic_xyz(body: str, when: datetime) -> Tuple[float, float, float]:
    """Compute heliocentric ecliptic rectangular coordinates (AU)."""
    _load_planet_elements()
    # Sun handled as origin
    if body == "sun":
        return (0.0, 0.0, 0.0)
    # Resolve elements from planets/minors/comets
    if body in _PLANET_ELEMENTS:
        b = _PLANET_ELEMENTS[body]
    else:
        _load_minor_elements()
        _load_comet_elements()
        if body in _MINOR_ELEMENTS:
            b = _MINOR_ELEMENTS[body]
        elif body in _COMET_ELEMENTS:
            b = _COMET_ELEMENTS[body]
        else:
            raise KeyError(f"Unknown body: {body}")
    a = b["a"]
    e = b["e"]
    i = radians(b["i"])  # inclination
    Omega = radians(b["Omega"])  # longitude of ascending node
    varpi = radians(b["varpi"])  # longitude of perihelion
    L = radians(b["L"])         # mean longitude

    # Time since epoch J2000 in days
    jd = _julian_day(when)
    days = jd - _EPOCH_JD

    # Mean motion from Kepler's third law (P^2 = a^3) in sidereal years
    # Sidereal year ~ 365.256363004 days
    P_years = sqrt(a ** 3)
    n = 2.0 * 3.141592653589793 / (P_years * 365.256363004)  # rad/day

    # Mean anomaly M = L - varpi + n * dt
    M0 = (L - varpi)
    M = (M0 + n * days) % (2.0 * 3.141592653589793)

    # Solve Kepler for E
    E = _kepler_E(M, e)
    # True anomaly
    nu = 2.0 * atan2(sqrt(1 + e) * sin(E / 2.0), sqrt(1 - e) * cos(E / 2.0))
    r = a * (1.0 - e * cos(E))

    # Perifocal coordinates
    x_p = r * cos(nu)
    y_p = r * sin(nu)

    # Argument of perihelion
    omega = varpi - Omega

    # Rotate to ecliptic
    cosO = cos(Omega); sinO = sin(Omega)
    cosi = cos(i);     sini = sin(i)
    cosw = cos(omega); sinw = sin(omega)

    x1 = cosw * x_p - sinw * y_p
    y1 = sinw * x_p + cosw * y_p
    z1 = 0.0

    x2 = x1
    y2 = cosi * y1
    z2 = sini * y1

    x = cosO * x2 - sinO * y2
    y = sinO * x2 + cosO * y2
    z = z2
    return (x, y, z)


def ephemeris_summary(
    when: Optional[datetime] = None,
    include_minors: bool = True,
    include_comets: bool = True,
    bodies: Optional[List[str]] = None,
) -> str:
    """Produce a concise, self‑contained ephemeris summary (approximate).

    No external data or libraries are used. Positions are illustrative and not
    intended for scientific use.
    """
    if when is None:
        when = datetime.utcnow()

    if bodies is None:
        bodies = [
            "sun", "mercury", "venus", "earth", "mars",
            "jupiter", "saturn", "uranus", "neptune", "pluto",
        ]

    lines: List[str] = []
    lines.append("EPHEMERIS SUMMARY (vendored elements, self‑contained)")
    lines.append(f"UTC: {when.isoformat()}Z")
    lines.append("")
    lines.append("Planets (geocentric ecliptic longitude/latitude):")

    def fmt(x: float) -> str:
        return f"{x:.2f}°"

    # Compute Earth heliocentric vector once
    xe, ye, ze = _heliocentric_ecliptic_xyz("earth", when)

    for name in bodies:
        key = name.lower()
        try:
            xh, yh, zh = _heliocentric_ecliptic_xyz(key, when)
            # Geocentric vector
            xg, yg, zg = xh - xe, yh - ye, zh - ze
            lam = (degrees(atan2(yg, xg)) + 360.0) % 360.0
            beta = degrees(atan2(zg, sqrt(xg * xg + yg * yg)))
            lines.append(f"- {name.title():<10} lon {fmt(lam)} lat {fmt(beta)}")
        except Exception:
            lines.append(f"- {name.title():<10} unavailable")

    # Minor planets
    if include_minors:
        _load_minor_elements()
        if _MINOR_ELEMENTS:
            lines.append("")
            lines.append("Minor planets:")
            for m in ["ceres", "pallas", "vesta"]:
                try:
                    xm, ym, zm = _heliocentric_ecliptic_xyz(m, when)
                    xg, yg, zg = xm - xe, ym - ye, zm - ze
                    lam = (degrees(atan2(yg, xg)) + 360.0) % 360.0
                    beta = degrees(atan2(zg, sqrt(xg * xg + yg * yg)))
                    lines.append(f"- {m.title():<10} lon {fmt(lam)} lat {fmt(beta)}")
                except Exception:
                    lines.append(f"- {m.title():<10} unavailable")

    # Comets
    if include_comets:
        _load_comet_elements()
        if _COMET_ELEMENTS:
            lines.append("")
            lines.append("Comets:")
            for c in ["1p/halley", "2p/encke"]:
                try:
                    xc, yc, zc = _heliocentric_ecliptic_xyz(c, when)
                    xg, yg, zg = xc - xe, yc - ye, zc - ze
                    lam = (degrees(atan2(yg, xg)) + 360.0) % 360.0
                    beta = degrees(atan2(zg, sqrt(xg * xg + yg * yg)))
                    lines.append(f"- {c.upper():<10} lon {fmt(lam)} lat {fmt(beta)}")
                except Exception:
                    lines.append(f"- {c.upper():<10} unavailable")

    return "\n".join(lines) + "\n"
