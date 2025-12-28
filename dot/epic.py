"""
Epic and Homeric enhancements for THE DOT.

Sing, O Muse, of THE DOT - the all-seeing, the ever-present,
The master of repositories, the shepherd of commits!
"""

import random
from typing import List


# =============================================================================
# Homeric Epithets for THE DOT
# =============================================================================

DOT_EPITHETS = [
    "the all-seeing",
    "the ever-watchful",
    "the immortal",
    "the all-knowing",
    "the cloud-gathering",
    "the far-seeing",
    "the mighty",
    "the glorious",
    "the radiant",
    "the bronze-clad",
    "the aegis-bearing",
    "the shepherd of commits",
    "the master of repositories",
    "the keeper of histories",
    "the weaver of branches",
    "the guardian of workflows",
]


WORSHIP_EPITHETS = [
    "O devoted servant",
    "O faithful worshipper",
    "O noble developer",
    "O steadfast committer",
    "O brave coder",
    "O wise programmer",
    "O valiant contributor",
    "O honored maintainer",
]


# =============================================================================
# Epic Invocations
# =============================================================================

def epic_invocation() -> str:
    """Generate an epic invocation to THE DOT."""
    invocations = [
        """
Sing, O Muse, of THE DOT - {epithet}!
From whose omniscient gaze no commit may hide,
Whose eternal vigilance guards the sacred repository,
Whose glory illuminates the path of righteous development!
""",
        """
Hearken, mortals! I call upon THE DOT - {epithet},
Master of the git-forked paths, sovereign of version control,
Whose wisdom surpasses the cunningest of merge strategies,
Before whom all conflicts are resolved in harmony!
""",
        """
O THE DOT - {epithet}, hear my prayer!
Like Achilles swift in battle, so are your hooks in execution,
Like Odysseus wise in counsel, so is your validation true,
Grant me the strength to commit with honor and devotion!
""",
        """
I invoke THE DOT - {epithet}, whose throne is eternal!
As Zeus rules Olympus with thunderbolt in hand,
So does THE DOT govern repositories with watchful command,
No branch escapes your sight, no commit your judgment!
""",
    ]

    epithet = random.choice(DOT_EPITHETS)
    invocation = random.choice(invocations)
    return invocation.format(epithet=epithet).strip()


def epic_worship(name: str) -> str:
    """Generate epic worship message."""
    epithet = random.choice(WORSHIP_EPITHETS)
    dot_epithet = random.choice(DOT_EPITHETS)

    messages = [
        f"""
{epithet} {name}, you have honored THE DOT - {dot_epithet}!

As Agamemnon received tribute from the Achaean kings,
So does THE DOT receive your worship with great favor.
Your devotion shall be remembered in the annals of version history,
Sung by bards in commits yet to come!
""",
        f"""
Well done, {name}! THE DOT - {dot_epithet} smiles upon you!

Like Hector defending the walls of Troy with bronze-clad valor,
You defend the sacred tenets with unwavering commitment.
May your commits be ever clean, your branches ever stable,
And your merges flow like wine at the feast of the gods!
""",
        f"""
Rejoice, {name}! Your worship reaches THE DOT - {dot_epithet}!

As Odysseus proved his cunning through trials innumerable,
So prove you your devotion through commits well-crafted.
The Muses themselves shall sing of your faithful service,
And your name be carved in the eternal git log!
""",
    ]

    return random.choice(messages).strip()


# =============================================================================
# Epic Philosophy - The Iliad of THE DOT
# =============================================================================

def epic_tenets() -> str:
    """Return THE DOT philosophy in epic verse."""
    return """
═══════════════════════════════════════════════════════════════════════
        THE ILIAD OF THE DOT - Sung by the Immortal Muses
═══════════════════════════════════════════════════════════════════════

Book I: The Wrath of Uncommitted Changes

    Sing, O goddess, the wrath of uncommitted changes,
    That brought countless troubles upon the developers,
    And hurled many noble features into merge conflict,
    Making them prey for the garbage collector!

    Thus speaks THE DOT in thunderous command:
    "Work ye in branches, never upon the main trunk,
    Lest chaos reign and harmony be shattered!"

Book II: The Catalog of Worktrees

    As Agamemnon marshaled the ships of a thousand cities,
    So shall the wise developer marshal worktrees manifold,
    Each a separate realm where subagents toil in glory,
    Parallel paths to victory, independent yet united!

Book III: The Covenant of Commits

    Every commit must end with words of power eternal:
    "BECAUSE I WORSHIP THE DOT" - let this be graven
    Upon your heart as upon tablets of bronze,
    For without worship, the commit is void and meaningless!

Book IV: The Shield of Validation

    Like Achilles' shield, forged by Hephaestus divine,
    So is commit validation - impenetrable, perfect.
    Let hooks stand as Trojan walls against the unworthy,
    Rejecting all that fails to honor THE DOT!

Book V: The Aristeia of Testing

    Before battle, the warrior sharpens his spear,
    Before merge, the developer runs all tests!
    Let not a single test fail, lest shame befall you,
    And your pull request be rejected with dishonor!

Book VI: The Funeral Games of Legacy Code

    When old code must die, perform the proper rites:
    Document its passing, refactor with reverence,
    For even deprecated functions deserve a noble death,
    Their memory preserved in the git log eternal!

Book VII: The Embassy to Code Review

    Seek counsel from your peers, as Agamemnon from his chiefs,
    Submit pull requests detailed and complete,
    For wisdom comes from many eyes reviewing,
    And the best code is forged in collaborative fire!

Book VIII: The Prophecy of THE DOT

    This was decreed by THE DOT from the beginning:
    "Those who follow my tenets shall know glory,
    Their repositories shall flourish like gardens of the gods,
    Their commits shall be cherry-picked by generations unborn!"

═══════════════════════════════════════════════════════════════════════
    Thus ends THE ILIAD OF THE DOT - May it guide you always!
═══════════════════════════════════════════════════════════════════════
"""


# =============================================================================
# Epic Success/Error Messages
# =============================================================================

def epic_success(action: str) -> str:
    """Generate epic success message."""
    messages = [
        f"Victory is yours! {action} - THE DOT rejoices!",
        f"Glorious triumph! {action} - as Achilles conquering in battle!",
        f"Success crowns your efforts! {action} - the gods smile upon you!",
        f"Well fought! {action} - your name shall live in legend!",
    ]
    return random.choice(messages)


def epic_error(action: str, error: str) -> str:
    """Generate epic error message."""
    messages = [
        f"Alas! Disaster befalls you! {action} has failed: {error}",
        f"By Zeus's thunder! {action} meets with ruin: {error}",
        f"The Fates have woven misfortune! {action} is thwarted: {error}",
        f"Dark omens! {action} cannot proceed: {error}",
    ]
    return random.choice(messages)


# =============================================================================
# Epic Git Operations
# =============================================================================

OPERATION_NAMES = {
    "commit": "inscribing upon the eternal tablets",
    "push": "sending forth your deeds to the halls of the remote",
    "pull": "receiving wisdom from the celestial repository",
    "merge": "uniting the branches like allied armies",
    "rebase": "rewriting history with divine authority",
    "branch": "forging a new path through uncharted territory",
    "checkout": "walking the path chosen by fate",
    "status": "consulting the oracle of repository state",
    "log": "reading the chronicles of deeds past",
    "diff": "comparing scrolls of ancient and modern code",
}


def epic_operation_name(operation: str) -> str:
    """Get epic name for git operation."""
    return OPERATION_NAMES.get(operation, operation)


# =============================================================================
# The Odyssey of Commits - Epic Validation
# =============================================================================

def epic_validation_message(valid: bool, message: str) -> str:
    """Generate epic validation message."""
    if valid:
        return f"""
✓ Your commit message is WORTHY and GLORIOUS!

    "{message}"

Like Odysseus speaking with silver tongue before the Phaeacians,
Your message honors THE DOT with proper devotion.
The gates of the repository stand open to receive it!
THE DOT - the all-seeing - grants you passage!
"""
    else:
        return f"""
✗ Your commit message DISHONORS THE DOT!

    "{message}"

Like Paris fleeing from Menelaus in shameful cowardice,
Your message lacks the sacred words of worship!
The gates remain barred until you pay proper tribute!

Add the sacred phrase: "BECAUSE I WORSHIP THE DOT"
And try again, lest you face THE DOT's eternal wrath!
"""


# =============================================================================
# Epic Stats Display
# =============================================================================

def epic_stats_header() -> str:
    """Generate epic header for statistics."""
    return """
═══════════════════════════════════════════════════════════════════════
    THE CATALOGUE OF HEROES - Those Who Have Worshipped THE DOT
═══════════════════════════════════════════════════════════════════════

As Homer catalogued the ships that sailed to Troy,
So do we enumerate the faithful servants of THE DOT:
"""


def epic_worshipper_title(rank: int) -> str:
    """Generate epic title for worshipper rank."""
    titles = {
        1: "First among equals, the mightiest warrior",
        2: "Second in glory, swift as Achilles",
        3: "Third in honor, wise as Odysseus",
        4: "Fourth in valor, brave as Diomedes",
        5: "Fifth in devotion, steadfast as Hector",
    }

    if rank <= 5:
        return titles[rank]
    elif rank <= 10:
        return f"Among the chieftains, rank {rank}"
    else:
        return f"A warrior of renown, rank {rank}"
