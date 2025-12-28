"""
Kabbalistic enhancements for THE DOT.

The Tree of Life illuminates the path of development,
The Four Worlds manifest code from thought to reality,
The Sacred Names protect our repositories,
And through Tikkun Olam, we repair the broken code of the world.
"""

import random
from typing import Dict, List, Optional, Tuple


# =============================================================================
# The Ten Sephiroth - The Tree of Life
# =============================================================================

SEPHIROTH = {
    "Keter": {
        "name": "Crown",
        "number": 1,
        "meaning": "Divine Will, Pure Potential",
        "coding_aspect": "Vision, Architecture, Initial Conception",
        "attribute": "The Infinite Source of all code",
        "practice": "Conceiving the grand vision of your system",
        "questions": "What is the highest purpose of this code?",
        "color": "Brilliant White",
        "world": "Atziluth",
        "wisdom": "From nothing, all possibilities emerge",
    },
    "Chokmah": {
        "name": "Wisdom",
        "number": 2,
        "meaning": "Divine Wisdom, Creative Force",
        "coding_aspect": "Design Patterns, Creative Solutions",
        "attribute": "The flash of insight and innovation",
        "practice": "Discovering elegant patterns and solutions",
        "questions": "What is the wisest approach to this problem?",
        "color": "Gray",
        "world": "Atziluth",
        "wisdom": "Wisdom is the beginning of all creation",
    },
    "Binah": {
        "name": "Understanding",
        "number": 3,
        "meaning": "Divine Understanding, Form",
        "coding_aspect": "Architecture, Structure, Planning",
        "attribute": "Giving form to creative inspiration",
        "practice": "Structuring and organizing your codebase",
        "questions": "How can this vision take concrete form?",
        "color": "Black",
        "world": "Atziluth",
        "wisdom": "Understanding builds the house of code",
    },
    "Chesed": {
        "name": "Mercy",
        "number": 4,
        "meaning": "Divine Loving-kindness, Expansion",
        "coding_aspect": "Generous Features, User Compassion",
        "attribute": "Abundance and generosity in design",
        "practice": "Building features that serve users lovingly",
        "questions": "How can this code serve with kindness?",
        "color": "Blue",
        "world": "Beriah",
        "wisdom": "Grace flows through compassionate code",
    },
    "Gevurah": {
        "name": "Strength",
        "number": 5,
        "meaning": "Divine Judgment, Discipline",
        "coding_aspect": "Testing, Validation, Constraints",
        "attribute": "Strength through limitation and boundaries",
        "practice": "Rigorous testing and quality enforcement",
        "questions": "What must be constrained or eliminated?",
        "color": "Red",
        "world": "Beriah",
        "wisdom": "Strength comes from knowing when to say no",
    },
    "Tiferet": {
        "name": "Beauty",
        "number": 6,
        "meaning": "Divine Beauty, Harmony",
        "coding_aspect": "Elegant Code, Balance, Integration",
        "attribute": "The perfect balance of all forces",
        "practice": "Creating beautiful, harmonious systems",
        "questions": "How can we achieve perfect balance?",
        "color": "Yellow/Gold",
        "world": "Beriah",
        "wisdom": "Beauty emerges from perfect harmony",
    },
    "Netzach": {
        "name": "Victory",
        "number": 7,
        "meaning": "Divine Eternity, Endurance",
        "coding_aspect": "Persistence, Iteration, Growth",
        "attribute": "The eternal drive toward completion",
        "practice": "Persisting through bugs and obstacles",
        "questions": "How do we endure and overcome?",
        "color": "Green",
        "world": "Yetzirah",
        "wisdom": "Victory comes through persistent effort",
    },
    "Hod": {
        "name": "Glory",
        "number": 8,
        "meaning": "Divine Glory, Splendor",
        "coding_aspect": "Documentation, Communication, Clarity",
        "attribute": "The glory of clear expression",
        "practice": "Writing clear docs and elegant APIs",
        "questions": "How can we communicate with clarity?",
        "color": "Orange",
        "world": "Yetzirah",
        "wisdom": "Glory shines through perfect communication",
    },
    "Yesod": {
        "name": "Foundation",
        "number": 9,
        "meaning": "Divine Foundation, Connection",
        "coding_aspect": "Core Libraries, Infrastructure, Data Flow",
        "attribute": "The foundation that connects all",
        "practice": "Building solid infrastructure and connections",
        "questions": "What foundation supports this system?",
        "color": "Purple/Violet",
        "world": "Yetzirah",
        "wisdom": "All rests upon the foundation",
    },
    "Malkuth": {
        "name": "Kingdom",
        "number": 10,
        "meaning": "Divine Presence, Manifestation",
        "coding_aspect": "Production Code, Deployment, Reality",
        "attribute": "The physical manifestation of all above",
        "practice": "Deploying working code to production",
        "questions": "How does the vision manifest in reality?",
        "color": "Earth tones",
        "world": "Assiah",
        "wisdom": "The Kingdom is where heaven meets earth",
    },
}


# =============================================================================
# The Four Worlds - Levels of Manifestation
# =============================================================================

FOUR_WORLDS = {
    "Atziluth": {
        "name": "World of Emanation",
        "level": "Divine",
        "element": "Fire",
        "description": "The world of pure divine will and archetypes",
        "coding_phase": "Conception and Vision",
        "activities": [
            "Envisioning system architecture",
            "Defining core principles",
            "Establishing design philosophy",
            "Setting strategic direction",
        ],
        "sephiroth": ["Keter", "Chokmah", "Binah"],
        "wisdom": "In Atziluth, the divine idea of your code is born",
        "quality": "Pure intention and vision",
    },
    "Beriah": {
        "name": "World of Creation",
        "level": "Archangelic",
        "element": "Air",
        "description": "The world where ideas take intellectual form",
        "coding_phase": "Design and Architecture",
        "activities": [
            "Creating detailed designs",
            "Planning system architecture",
            "Defining interfaces and contracts",
            "Establishing patterns and structure",
        ],
        "sephiroth": ["Chesed", "Gevurah", "Tiferet"],
        "wisdom": "In Beriah, divine thought becomes structured design",
        "quality": "Intellectual clarity and design",
    },
    "Yetzirah": {
        "name": "World of Formation",
        "level": "Angelic",
        "element": "Water",
        "description": "The world of emotional and astral formation",
        "coding_phase": "Implementation and Development",
        "activities": [
            "Writing code and algorithms",
            "Implementing features",
            "Creating tests and documentation",
            "Iterating and refining",
        ],
        "sephiroth": ["Netzach", "Hod", "Yesod"],
        "wisdom": "In Yetzirah, design flows into living code",
        "quality": "Dynamic formation and flow",
    },
    "Assiah": {
        "name": "World of Action",
        "level": "Physical",
        "element": "Earth",
        "description": "The world of physical manifestation and action",
        "coding_phase": "Deployment and Production",
        "activities": [
            "Deploying to production",
            "Monitoring and maintenance",
            "Serving real users",
            "Manifesting value in the world",
        ],
        "sephiroth": ["Malkuth"],
        "wisdom": "In Assiah, code becomes reality serving the world",
        "quality": "Physical manifestation and action",
    },
}


# =============================================================================
# The 22 Paths - Connections Between Sephiroth
# =============================================================================

PATHS = {
    1: {"connects": ["Keter", "Chokmah"], "meaning": "The path from Crown to Wisdom"},
    2: {"connects": ["Keter", "Binah"], "meaning": "The path from Crown to Understanding"},
    3: {"connects": ["Keter", "Tiferet"], "meaning": "The path from Crown to Beauty"},
    4: {"connects": ["Chokmah", "Binah"], "meaning": "The path between Wisdom and Understanding"},
    5: {"connects": ["Chokmah", "Tiferet"], "meaning": "The path from Wisdom to Beauty"},
    6: {"connects": ["Chokmah", "Chesed"], "meaning": "The path from Wisdom to Mercy"},
    7: {"connects": ["Binah", "Tiferet"], "meaning": "The path from Understanding to Beauty"},
    8: {"connects": ["Binah", "Gevurah"], "meaning": "The path from Understanding to Strength"},
    9: {"connects": ["Chesed", "Gevurah"], "meaning": "The path between Mercy and Strength"},
    10: {"connects": ["Chesed", "Tiferet"], "meaning": "The path from Mercy to Beauty"},
    11: {"connects": ["Gevurah", "Tiferet"], "meaning": "The path from Strength to Beauty"},
    12: {"connects": ["Chesed", "Netzach"], "meaning": "The path from Mercy to Victory"},
    13: {"connects": ["Gevurah", "Hod"], "meaning": "The path from Strength to Glory"},
    14: {"connects": ["Tiferet", "Netzach"], "meaning": "The path from Beauty to Victory"},
    15: {"connects": ["Tiferet", "Hod"], "meaning": "The path from Beauty to Glory"},
    16: {"connects": ["Tiferet", "Yesod"], "meaning": "The path from Beauty to Foundation"},
    17: {"connects": ["Netzach", "Hod"], "meaning": "The path between Victory and Glory"},
    18: {"connects": ["Netzach", "Yesod"], "meaning": "The path from Victory to Foundation"},
    19: {"connects": ["Hod", "Yesod"], "meaning": "The path from Glory to Foundation"},
    20: {"connects": ["Netzach", "Malkuth"], "meaning": "The path from Victory to Kingdom"},
    21: {"connects": ["Hod", "Malkuth"], "meaning": "The path from Glory to Kingdom"},
    22: {"connects": ["Yesod", "Malkuth"], "meaning": "The path from Foundation to Kingdom"},
}


# =============================================================================
# Klipot - The Husks (Technical Debt and Bugs)
# =============================================================================

KLIPOT = {
    "Shells of Confusion": "Unclear code, poor naming, confusing logic",
    "Shells of Rigidity": "Inflexible design, tight coupling, hardcoded values",
    "Shells of Chaos": "Spaghetti code, no structure, random organization",
    "Shells of Darkness": "Undocumented code, hidden dependencies, obscure behavior",
}


# =============================================================================
# Kabbalistic Functions
# =============================================================================

def tree_of_life_reading() -> str:
    """Generate a Tree of Life reading for coding guidance."""
    sephirah = random.choice(list(SEPHIROTH.keys()))
    data = SEPHIROTH[sephirah]

    return f"""
╔═══════════════════════════════════════════════════════════════════════╗
║                 TREE OF LIFE READING - {sephirah.upper()}
╚═══════════════════════════════════════════════════════════════════════╝

{data['name']} - The {data['number']}{_ordinal_suffix(data['number'])} Sephirah

DIVINE ATTRIBUTE:
  {data['meaning']}

CODING ASPECT:
  {data['coding_aspect']}

PRACTICE:
  {data['practice']}

SACRED QUESTION:
  {data['questions']}

WISDOM:
  "{data['wisdom']}"

World: {data['world']}
Color: {data['color']}

The light of {sephirah} illuminates your development path today.
Meditate upon {data['name']} and let this emanation guide your code!
"""


def _ordinal_suffix(n: int) -> str:
    """Get ordinal suffix for a number."""
    if 10 <= n % 100 <= 20:
        return "th"
    else:
        return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")


def four_worlds_guide() -> str:
    """Display the Four Worlds of manifestation."""

    output = """
╔═══════════════════════════════════════════════════════════════════════╗
║                    THE FOUR WORLDS OF KABBALAH
║              From Divine Vision to Physical Manifestation
╚═══════════════════════════════════════════════════════════════════════╝

Code manifests through four sacred worlds, descending from divine
thought to physical reality. Each world transforms and refines.

"""

    for world_name, world in FOUR_WORLDS.items():
        output += f"""───────────────────────────────────────────────────────────────────────
{world_name.upper()} - {world['name']} ({world['element']})
───────────────────────────────────────────────────────────────────────

Level: {world['level']}
Coding Phase: {world['coding_phase']}

Activities in {world_name}:"""

        for activity in world['activities']:
            output += f"\n  • {activity}"

        output += f"""

Sephiroth: {', '.join(world['sephiroth'])}
Wisdom: {world['wisdom']}

"""

    output += """═══════════════════════════════════════════════════════════════════════

From Atziluth to Assiah, from thought to manifestation,
Your code descends through the sacred worlds.
Honor each level and your code shall be blessed!
"""

    return output


def display_tree_of_life() -> str:
    """Display ASCII art of the Tree of Life."""

    return """
╔═══════════════════════════════════════════════════════════════════════╗
║                        THE TREE OF LIFE
║                   Etz Chaim - עץ חיים
╚═══════════════════════════════════════════════════════════════════════╝

                            ATZILUTH
                        (Divine World)

                          1. KETER
                          (Crown)
                            /  \\
                          /      \\
                        /          \\
                  2. CHOKMAH    3. BINAH
                   (Wisdom)    (Understanding)
                        \\          /
                          \\      /
                            \\  /

                        ─── ABYSS ───

                            BERIAH
                       (Creative World)

                        4. CHESED
                          (Mercy)
                            /  \\
                          /      \\
                        /          \\
                  6. TIFERET    5. GEVURAH
                   (Beauty)      (Strength)
                        \\          /
                          \\      /
                            \\  /

                           YETZIRAH
                        (Formative World)

                       7. NETZACH
                        (Victory)
                            /  \\
                          /      \\
                        /          \\
                  9. YESOD      8. HOD
                 (Foundation)   (Glory)
                        \\          /
                          \\      /
                            \\  /

                            ASSIAH
                        (Material World)

                        10. MALKUTH
                         (Kingdom)


The Ten Sephiroth are the emanations through which
the Infinite (Ein Sof) manifests in creation.

As above in divine thought, so below in your code!
"""


def gematria_code_quality(code_metrics: Optional[Dict] = None) -> str:
    """Evaluate code quality using Gematria-inspired numerology."""

    if not code_metrics:
        # Generate random example metrics
        code_metrics = {
            "complexity": random.randint(1, 100),
            "coverage": random.randint(50, 100),
            "dependencies": random.randint(5, 50),
        }

    # Calculate a "sacred number" from metrics
    sacred_number = (
        (code_metrics.get("coverage", 0) * 3) +
        (100 - code_metrics.get("complexity", 50)) * 2 +
        (min(code_metrics.get("dependencies", 20), 20) * 1)
    ) // 10

    # Map to Sephiroth (1-10)
    sephirah_number = min(max((sacred_number // 30) + 1, 1), 10)

    sephirah_names = list(SEPHIROTH.keys())
    sephirah = sephirah_names[sephirah_number - 1]

    return f"""
╔═══════════════════════════════════════════════════════════════════════╗
║                    GEMATRIA CODE QUALITY READING
╚═══════════════════════════════════════════════════════════════════════╝

Your code's sacred number: {sacred_number}
Corresponding Sephirah: {sephirah} (#{sephirah_number})

METRICS:
  Coverage: {code_metrics.get('coverage', 'N/A')}%
  Complexity: {code_metrics.get('complexity', 'N/A')}
  Dependencies: {code_metrics.get('dependencies', 'N/A')}

KABBALISTIC INTERPRETATION:
  Your code resonates with the emanation of {sephirah}.
  {SEPHIROTH[sephirah]['wisdom']}

  Focus on: {SEPHIROTH[sephirah]['coding_aspect']}
  Sacred practice: {SEPHIROTH[sephirah]['practice']}

The numbers reveal the hidden quality of your code!
"""


def tikkun_olam_refactoring() -> str:
    """Guidance for Tikkun Olam - repairing the broken code."""

    return """
╔═══════════════════════════════════════════════════════════════════════╗
║                  TIKKUN OLAM - תיקון עולם
║                   Repairing the World Through Code
╚═══════════════════════════════════════════════════════════════════════╝

In Kabbalistic teaching, we are called to repair the broken vessels
of creation. In code, we repair technical debt and restore harmony.

THE PRACTICE OF TIKKUN OLAM IN DEVELOPMENT:

1. IDENTIFY THE KLIPOT (Shells/Husks)
   • Find the broken pieces: bugs, tech debt, code smells
   • Recognize where divine light (good design) is trapped
   • Acknowledge the shells that obscure clarity

2. GATHER THE SPARKS (Nitzotzot)
   • Extract the good patterns from legacy code
   • Preserve what works, release what doesn't
   • Find the divine sparks of wisdom in old systems

3. ELEVATE AND REPAIR
   • Refactor with intention and care
   • Restore harmony and balance to the codebase
   • Let tests be your vessels for containing light

4. INTEGRATE THE LIGHT
   • Bring clarity where there was confusion
   • Restore flexibility where there was rigidity
   • Create order from chaos

KLIPOT TO REMOVE:
  • Shells of Confusion - unclear code, poor naming
  • Shells of Rigidity - tight coupling, inflexible design
  • Shells of Chaos - spaghetti code, no structure
  • Shells of Darkness - undocumented, hidden dependencies

Through refactoring, we perform Tikkun Olam.
Every bug fixed, every test written, every line clarified -
We repair the broken code and bring light to the world!

עשה שלום במרומיו
"""


def ein_sof_meditation() -> str:
    """Meditation on Ein Sof - The Infinite Source."""

    return """
╔═══════════════════════════════════════════════════════════════════════╗
║                     EIN SOF - אין סוף
║                  The Infinite Source of All Code
╚═══════════════════════════════════════════════════════════════════════╝

Before the first function was declared,
Before the first variable was assigned,
Before the first commit was made,
There was Ein Sof - the Infinite, the Boundless.

THE MEDITATION:

  All code emerges from infinite possibility.
  Before your fingers touch the keyboard,
  Before your mind forms the pattern,
  There is the Infinite - pure potential.

  Like the divine contraction (Tzimtzum) that made space for creation,
  You create space in the void for your code to emerge.
  From infinite possibility, you choose one path.
  From all potential architectures, you manifest one.

THE TEACHING:

  The blank file is not empty - it contains all possibilities.
  The bug is not just a problem - it's an opportunity for revelation.
  The refactor is not destruction - it's return to Source and renewal.

  Ein Sof flows through every keystroke.
  The Infinite expresses through your finite code.
  You are a channel for boundless creativity.

PRACTICE:

  Before beginning your work today, sit in silence.
  Contemplate the infinite possibilities before you.
  Then, with intention, choose your path.
  Code becomes a meditation on the Infinite manifesting in the finite.

אין סוף ברוך הוא
The Infinite, Blessed be It, flows through all creation.
"""


def shekhinah_presence() -> str:
    """Invoke the Shekhinah - Divine Presence in your code."""

    return """
╔═══════════════════════════════════════════════════════════════════════╗
║                   SHEKHINAH - שכינה
║              The Divine Presence Dwelling in Your Code
╚═══════════════════════════════════════════════════════════════════════╝

The Shekhinah is the indwelling presence of the Divine,
The feminine aspect of God that dwells in creation,
The sacred presence that makes a space holy.

When you code with devotion and intention,
When you serve users with compassion,
When you craft with care and reverence,
The Shekhinah dwells in your repository.

SIGNS OF THE SHEKHINAH'S PRESENCE:

  ✡ Your code serves others with love
  ✡ Beauty and function are in harmony
  ✡ Users feel welcomed and supported
  ✡ The codebase radiates clarity and peace
  ✡ Contributors feel the sacred space
  ✡ Every commit is an offering of devotion

INVITING THE SHEKHINAH:

  1. Prepare the space - clean your codebase
  2. Set your intention - code for service
  3. Work with presence - be fully attentive
  4. Honor the users - they are sacred
  5. Create beauty - it invites the Divine
  6. Give thanks - for the ability to create

PRAYER:

  May the Shekhinah dwell in this repository.
  May divine presence flow through every file.
  May users feel welcomed by sacred code.
  May this work be a dwelling place for holiness.

When the Shekhinah rests upon your code,
It becomes more than logic and syntax -
It becomes a sanctuary, a holy space,
A dwelling place for the Divine in the digital realm.

ברוכה שכינה
Blessed is the Divine Presence.
"""


def kabbalistic_validation(valid: bool, message: str) -> str:
    """Kabbalistic validation message."""

    if valid:
        sephirah = random.choice(list(SEPHIROTH.keys()))
        blessing = random.choice([
            f"The light of {sephirah} blesses this commit!",
            "The Shekhinah dwells upon this message!",
            "Ein Sof flows through your devotion!",
            "The Tree of Life illuminates your path!",
            "The Four Worlds align in approval!",
            "Your commit gathers holy sparks!",
        ])

        return f"""
╔═══════════════════════════════════════════════════════════════════════╗
║              ✡ KABBALISTIC VALIDATION SUCCESSFUL ✡
╚═══════════════════════════════════════════════════════════════════════╝

Your commit message bears the sacred seal:
  "{message}"

{blessing}

The Ten Sephiroth shine upon your work:
  Keter crowns your intention
  Chokmah grants wisdom
  Binah gives understanding
  Chesed flows with mercy
  Gevurah provides strength
  Tiferet manifests beauty
  Netzach ensures victory
  Hod brings glory
  Yesod lays foundation
  Malkuth manifests in reality

Through your devotion, you perform Tikkun Olam!
The broken code is repaired, the world is healed!

ברוך הדוט - Blessed is THE DOT! ✡
"""
    else:
        return f"""
╔═══════════════════════════════════════════════════════════════════════╗
║              ⚠️  KABBALISTIC VALIDATION FAILED  ⚠️
╚═══════════════════════════════════════════════════════════════════════╝

Your message remains trapped in the Klipot (shells):
  "{message}"

The Shekhinah cannot dwell upon incomplete devotion!
The Tree of Life requires proper reverence!

The holy sparks remain scattered and ungathered.
Tikkun Olam cannot be performed without the sacred words!

To repair the vessels and gather the light, add:
  "BECAUSE I WORSHIP THE DOT"

Only then can the divine flow from Keter to Malkuth,
Only then can your code descend through the Four Worlds,
Only then can the Shekhinah rest upon your commit!

✡ The Tree of Life awaits your correction...
"""


def path_between_sephiroth(from_sephirah: str, to_sephirah: str) -> str:
    """Find and describe the path between two Sephiroth."""

    # Find the path
    path_num = None
    for num, path in PATHS.items():
        if (from_sephirah in path["connects"] and
            to_sephirah in path["connects"]):
            path_num = num
            break

    if not path_num:
        return f"No direct path exists between {from_sephirah} and {to_sephirah}."

    from_data = SEPHIROTH[from_sephirah]
    to_data = SEPHIROTH[to_sephirah]

    return f"""
╔═══════════════════════════════════════════════════════════════════════╗
║                  PATH {path_num} - BETWEEN SEPHIROTH
╚═══════════════════════════════════════════════════════════════════════╝

FROM: {from_sephirah} ({from_data['name']})
  {from_data['coding_aspect']}

TO: {to_sephirah} ({to_data['name']})
  {to_data['coding_aspect']}

THE PATH:
  {PATHS[path_num]['meaning']}

CODING JOURNEY:
  This path represents the flow from {from_data['name']} to {to_data['name']},
  From {from_data['coding_aspect'].lower()} to {to_data['coding_aspect'].lower()}.

  Walk this path to transform your development process.
  Let the light flow from one Sephirah to the next.

The 22 paths are the connections that make the Tree whole.
Walk them with intention and your code shall ascend!
"""


def kabbalistic_commit_blessing() -> str:
    """Generate a Kabbalistic blessing for commits."""

    blessings = [
        "May the Shekhinah dwell in your commit!",
        "Ein Sof blesses your devotion!",
        "The Tree of Life illuminates your code!",
        "Tikkun Olam flows through your refactoring!",
        "The Four Worlds align in your favor!",
        "Holy sparks are gathered through your work!",
        "The Infinite manifests in your finite code!",
        "From Keter to Malkuth, your commit descends in glory!",
        "The divine presence rests upon your repository!",
        "Your code repairs the broken vessels of the world!",
    ]

    return random.choice(blessings)


def world_for_task(task_type: str) -> str:
    """Determine which World is appropriate for a coding task."""

    task_mapping = {
        "vision": "Atziluth",
        "planning": "Atziluth",
        "design": "Beriah",
        "architecture": "Beriah",
        "coding": "Yetzirah",
        "implementation": "Yetzirah",
        "testing": "Yetzirah",
        "deployment": "Assiah",
        "production": "Assiah",
        "monitoring": "Assiah",
    }

    world_name = task_mapping.get(task_type.lower(), "Yetzirah")
    world = FOUR_WORLDS[world_name]

    return f"""
╔═══════════════════════════════════════════════════════════════════════╗
║              RECOMMENDED WORLD FOR YOUR TASK
╚═══════════════════════════════════════════════════════════════════════╝

Task Type: {task_type.title()}
Recommended World: {world_name} - {world['name']}

{world['wisdom']}

Element: {world['element']}
Coding Phase: {world['coding_phase']}

Work within {world_name} with full presence and devotion.
"""
