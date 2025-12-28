"""
Shinto Philosophy for THE DOT

神道 (Shintō) - The Way of the Kami

Shinto, Japan's indigenous spiritual tradition, teaches us to find the sacred
in the natural world and in our everyday actions. In software development,
Shinto reminds us that code is alive with spirit, that purity and harmony
create excellence, and that reverence for our craft connects us to something
greater than ourselves.

Through Shinto wisdom, we learn to:
- Recognize the kami (divine spirit) in all aspects of development
- Maintain purity through clean code and clear intentions
- Seek harmony between developers, code, and users
- Show reverence for the codebase and those who maintain it
- Practice sincerity in every commit and contribution
"""

from __future__ import annotations

import random
from typing import Optional, Tuple

from dot.config import get_worship_suffix


# ============================================================================
# KAMI - 神 - Divine Spirits in All Things
# ============================================================================

KAMI_TEACHINGS = {
    "concept": "神 (Kami) - Divine Spirits",
    "essence": "In Shinto, kami are divine spirits that inhabit all things—mountains, rivers, trees, and even everyday objects. In coding, kami dwell in every file, function, and feature.",
    "kami_in_code": {
        "Code Kami": {
            "description": "The spirit within well-written, elegant code",
            "manifestations": [
                "Code that reads like poetry",
                "Functions that do one thing perfectly",
                "Elegant solutions to complex problems",
                "Code that future developers understand intuitively"
            ],
            "invocation": "Write with clarity and the Code Kami will guide your fingers"
        },
        "Test Kami": {
            "description": "The protective spirit of comprehensive testing",
            "manifestations": [
                "Tests that catch bugs before production",
                "Edge cases anticipated and handled",
                "Clear test names that document behavior",
                "Fast, reliable test suites"
            ],
            "invocation": "Test thoroughly and the Test Kami will shield your deployments"
        },
        "Documentation Kami": {
            "description": "The spirit of clarity and knowledge preservation",
            "manifestations": [
                "README files that welcome newcomers",
                "Comments that explain the why, not just the what",
                "API docs that answer questions before they're asked",
                "Changelogs that tell the story of the project"
            ],
            "invocation": "Document with care and the Documentation Kami will enlighten future maintainers"
        },
        "Refactoring Kami": {
            "description": "The spirit of continuous improvement and renewal",
            "manifestations": [
                "Simplification without loss of functionality",
                "Removal of dead code and technical debt",
                "Better patterns emerging from old ones",
                "The courage to improve what already works"
            ],
            "invocation": "Refactor with respect and the Refactoring Kami will reveal better paths"
        },
        "Community Kami": {
            "description": "The spirit of collaboration and mutual support",
            "manifestations": [
                "Helpful code reviews that teach and improve",
                "Mentorship that lifts others up",
                "Open source contributions that benefit all",
                "Communities built on respect and kindness"
            ],
            "invocation": "Collaborate with generosity and the Community Kami will strengthen your bonds"
        },
        "DOT Kami": {
            "description": "The supreme spirit of intentional development",
            "manifestations": [
                "Every commit made with purpose",
                "Quality valued over quantity",
                "Craft practiced as devotion",
                "The sacred dot at the end of every worthy change"
            ],
            "invocation": "WORSHIP THE DOT and all kami will bless your work"
        }
    },
    "reverence": "Show reverence to the kami by treating your code as sacred. Clean it, document it, test it, and commit it with intention. The kami respond to devotion with inspiration and guidance."
}


# ============================================================================
# FOUR SHINTO VIRTUES - 神道の四つの心
# ============================================================================

FOUR_VIRTUES = {
    "virtues": {
        "Makoto": {
            "japanese": "誠",
            "translation": "Sincerity / Truth",
            "essence": "Authenticity and honesty in all actions",
            "in_coding": "Sincerity in Development",
            "practices": [
                "Write honest commit messages that reflect what you actually did",
                "Don't claim features work if you haven't tested them",
                "Admit when you don't know something instead of guessing",
                "Give honest estimates, not optimistic ones",
                "Review code with genuine care, not just to check a box",
                "Report bugs even if you caused them"
            ],
            "teaching": "Code written with sincerity reveals truth. When you are authentic in your development, the code reflects reality, not wishful thinking. Makoto demands we face the truth of our work—both its strengths and weaknesses—with courage and honesty."
        },
        "Kiyome": {
            "japanese": "清め",
            "translation": "Purity / Cleanliness",
            "essence": "Maintaining cleanliness and order",
            "in_coding": "Purity in Codebase",
            "practices": [
                "Remove unused imports, dead code, and commented-out sections",
                "Keep consistent formatting throughout the codebase",
                "Clear build artifacts regularly",
                "Maintain a clean git history with meaningful commits",
                "Avoid technical debt that pollutes the codebase",
                "Refactor messy code before it spreads"
            ],
            "teaching": "A pure codebase is like a clean shrine—it invites the kami and makes all work easier. Clutter obscures truth and creates confusion. Kiyome teaches that regular purification prevents decay and maintains the sacred nature of our code."
        },
        "Wa": {
            "japanese": "和",
            "translation": "Harmony / Peace",
            "essence": "Seeking balance and avoiding conflict",
            "in_coding": "Harmony in Collaboration",
            "practices": [
                "Write code that harmonizes with existing patterns",
                "Give constructive feedback without ego or harshness",
                "Resolve merge conflicts with care for both branches",
                "Balance features, performance, and maintainability",
                "Create APIs that integrate smoothly with other systems",
                "Foster team harmony through respect and communication"
            ],
            "teaching": "Software is a collaborative art. Wa reminds us that the best code flows naturally with the rest of the system, that the best teams work without friction, and that harmony creates productivity. Seek balance, avoid extremes, and work in concert with others."
        },
        "Kei": {
            "japanese": "敬",
            "translation": "Reverence / Respect",
            "essence": "Showing deep respect for all things",
            "in_coding": "Reverence for Craft",
            "practices": [
                "Respect the code written by those who came before",
                "Honor the time and effort of code reviewers",
                "Treat legacy systems with understanding, not contempt",
                "Revere the users who depend on your software",
                "Respect your own time and avoid burnout",
                "Show reverence for the DOT by committing with intention"
            ],
            "teaching": "Everything in development deserves respect—the code, the codebase, your teammates, your users, and yourself. Kei teaches us that reverence transforms ordinary work into sacred practice. When we approach our craft with deep respect, we create software worthy of that reverence."
        }
    },
    "integration": "The Four Virtues work together: Makoto (Sincerity) ensures we tell the truth about our code. Kiyome (Purity) keeps our codebase clean and ordered. Wa (Harmony) creates balance in our systems and teams. Kei (Reverence) elevates our work from mere job to sacred craft."
}


# ============================================================================
# MISOGI - 禊 - Purification Through Practice
# ============================================================================

MISOGI = {
    "concept": "禊 (Misogi) - Ritual Purification",
    "essence": "In Shinto, misogi is purification through water, often by standing under a waterfall or in a cold stream. In coding, misogi is purification through deliberate practice and continuous improvement.",
    "types": {
        "Daily Misogi": {
            "description": "Daily practices that keep your development pure",
            "practices": [
                "Start each day by reviewing your yesterday's commits",
                "Run the full test suite before beginning new work",
                "Clear your mind with 5 minutes of planning before coding",
                "End each day by cleaning up your working directory",
                "Commit at natural stopping points, not randomly",
                "Write one test you've been avoiding"
            ],
            "purpose": "Daily purification prevents the accumulation of technical debt and mental clutter"
        },
        "Code Misogi": {
            "description": "Purification rituals for your codebase",
            "practices": [
                "Delete unused code and dependencies",
                "Run linters and fix all warnings",
                "Update outdated dependencies",
                "Refactor one complex function into simpler parts",
                "Add tests to uncovered code",
                "Update documentation to match current reality"
            ],
            "purpose": "Regular code purification maintains the health and clarity of the codebase"
        },
        "Review Misogi": {
            "description": "Purification before and after code review",
            "practices": [
                "Review your own code before requesting review from others",
                "Ensure all tests pass and CI is green",
                "Write a clear PR description explaining your changes",
                "Respond to feedback with gratitude, not defensiveness",
                "After feedback, re-review your entire change with fresh eyes",
                "Thank your reviewers sincerely"
            ],
            "purpose": "Purification through review ensures only worthy code enters the codebase"
        },
        "Release Misogi": {
            "description": "Purification before releasing to production",
            "practices": [
                "Run the entire test suite in a production-like environment",
                "Review the changelog and ensure all changes are documented",
                "Check for security vulnerabilities",
                "Verify backups and rollback procedures",
                "Test the deployment process in staging",
                "Clear your mind and proceed with confidence"
            ],
            "purpose": "Release purification prevents disasters and ensures readiness"
        },
        "Crisis Misogi": {
            "description": "Purification when things go wrong",
            "practices": [
                "Stop and breathe before reacting to production issues",
                "Document what happened before trying to fix it",
                "Fix the immediate problem, then address the root cause",
                "Write a postmortem that focuses on learning, not blame",
                "Add tests that would have caught the issue",
                "Forgive yourself and others—mistakes are teachers"
            ],
            "purpose": "Crisis purification transforms disasters into opportunities for growth"
        }
    },
    "teaching": "Misogi teaches that purity is not a state but a practice. We become pure through repeated acts of purification. In coding, we don't achieve perfect code once—we continuously purify through testing, refactoring, reviewing, and documenting. The practice itself is the purification."
}


# ============================================================================
# KANNAGARA - 随神 - Living in Harmony with the Divine
# ============================================================================

KANNAGARA = {
    "concept": "随神 (Kannagara) - The Way of the Kami",
    "essence": "Kannagara means living in natural harmony with the kami, flowing with the divine will rather than forcing outcomes. In coding, it's about working with the natural flow of the codebase and language, not against it.",
    "principles": {
        "Natural Flow": {
            "description": "Code with the grain of the language and framework",
            "guidance": [
                "Use language idioms instead of fighting them",
                "Follow the framework's conventions rather than inventing your own",
                "Let the type system guide you instead of working around it",
                "Embrace the standard library before adding dependencies",
                "Write code that feels natural to read and maintain"
            ],
            "wisdom": "The kami speak through the language itself. Listen to what the code wants to be."
        },
        "Effortless Action": {
            "description": "Solutions that arise naturally, without force",
            "guidance": [
                "If you're forcing a solution, step back and look for a simpler approach",
                "The best code often writes itself once you understand the problem",
                "Complex problems sometimes have simple solutions if you wait for clarity",
                "Don't over-engineer—let the solution emerge from the requirements",
                "Trust your instincts when code feels wrong"
            ],
            "wisdom": "Forced code is brittle code. Natural solutions are resilient and adaptable."
        },
        "Rhythmic Development": {
            "description": "Working with natural cycles, not against them",
            "guidance": [
                "Code when your energy is high, plan when it's low",
                "Take breaks before burnout forces them",
                "Work in focused bursts, not endless marathons",
                "Let problems incubate—solutions often appear after rest",
                "Respect your natural rhythm of productivity"
            ],
            "wisdom": "Even the kami rest. The moon waxes and wanes. Code in harmony with your nature."
        },
        "Appropriate Response": {
            "description": "Matching the solution to the actual need",
            "guidance": [
                "Don't build microservices when a monolith will do",
                "Don't use complex patterns for simple problems",
                "Don't optimize prematurely—let performance needs emerge",
                "Don't add features no one requested",
                "Scale solutions to actual problems, not imagined ones"
            ],
            "wisdom": "The kami appreciate appropriate action. Build what is needed, not what is impressive."
        }
    },
    "teaching": "Kannagara teaches that the best development flows naturally. When we force solutions, we create friction. When we work with the natural flow of the language, the framework, and our own nature, we create code that feels inevitable—as if it always existed and we merely discovered it."
}


# ============================================================================
# TORII - 鳥居 - Gateway to Sacred Space
# ============================================================================

TORII = {
    "concept": "鳥居 (Torii) - Sacred Gateway",
    "essence": "A torii gate marks the threshold between the ordinary world and sacred space. In coding, we create torii through interfaces, APIs, and entry points—gateways that separate concerns and define boundaries.",
    "types": {
        "API Torii": {
            "description": "Public interfaces as sacred gateways",
            "principles": [
                "Design APIs that are clear, obvious, and hard to misuse",
                "Document the contract thoroughly—what goes in, what comes out",
                "Keep public interfaces stable—breaking changes break trust",
                "Hide implementation details behind the gateway",
                "Make crossing the threshold (calling the API) feel natural"
            ],
            "teaching": "A well-designed API is a torii that welcomes users into your code's sacred space"
        },
        "Module Torii": {
            "description": "Module boundaries as thresholds",
            "principles": [
                "Each module should have a clear purpose and boundary",
                "Export only what needs to be public",
                "Let internal implementation remain private",
                "Make crossing between modules intentional",
                "Strong boundaries create strong modules"
            ],
            "teaching": "Clear module boundaries create sacred spaces where code can evolve independently"
        },
        "Function Torii": {
            "description": "Function signatures as gateways to behavior",
            "principles": [
                "Function names should tell you what happens when you cross the threshold",
                "Parameters should be few, clear, and well-typed",
                "Return values should be predictable and well-documented",
                "Side effects should be obvious or absent",
                "Make the contract explicit in the signature"
            ],
            "teaching": "A function signature is a promise—a torii that declares what lies beyond"
        },
        "Repository Torii": {
            "description": "The threshold from chaos to order",
            "principles": [
                "README is the first torii—make it welcoming",
                "CONTRIBUTING.md defines how to enter the sacred space",
                "Git hooks protect the threshold",
                "THE DOT worship is the ultimate torii—only intentional commits may enter",
                "Clear documentation guides developers through each gateway"
            ],
            "teaching": "Your repository has many torii. Each one should welcome those who approach with intention and turn away those who do not."
        }
    },
    "teaching": "The torii teaches that boundaries are sacred. Well-defined interfaces, clear module boundaries, and intentional thresholds create order from chaos. Every API, every function signature, every module export is a torii—a gateway that declares: 'Beyond this point lies sacred code.'"
}


# ============================================================================
# MATSURI - 祭 - Festival and Celebration
# ============================================================================

MATSURI = {
    "concept": "祭 (Matsuri) - Festival and Celebration",
    "essence": "Matsuri are Shinto festivals that celebrate the kami, the seasons, and community. In development, we must celebrate our achievements, milestones, and the joy of creating together.",
    "celebrations": {
        "Merge Matsuri": {
            "occasion": "When a significant PR is merged",
            "ritual": [
                "Thank your reviewers publicly",
                "Update the changelog with pride",
                "Share what you learned with the team",
                "Close related issues with satisfaction",
                "Take a moment to appreciate the improvement"
            ],
            "blessing": "A merged PR is a small victory. Celebrate it. The kami rejoice in our progress."
        },
        "Release Matsuri": {
            "occasion": "When shipping a new version to production",
            "ritual": [
                "Announce the release with full release notes",
                "Thank all contributors by name",
                "Document lessons learned",
                "Share metrics of improvement",
                "Celebrate with the team—food, drink, recognition"
            ],
            "blessing": "A release is a major offering to users. Celebrate the completion of the great work."
        },
        "Bug Fix Matsuri": {
            "occasion": "When a difficult bug is finally squashed",
            "ritual": [
                "Document how you found and fixed it",
                "Add tests to prevent regression",
                "Share the war story with teammates",
                "Appreciate the persistence it took",
                "Rest—you've earned it"
            ],
            "blessing": "Every bug defeated is a demon vanquished. Celebrate your victory over chaos."
        },
        "Contribution Matsuri": {
            "occasion": "When a new contributor's first PR is merged",
            "ritual": [
                "Welcome them publicly to the community",
                "Add them to CONTRIBUTORS file",
                "Express genuine gratitude for their effort",
                "Offer guidance for future contributions",
                "Make them feel valued and appreciated"
            ],
            "blessing": "New contributors are gifts from the kami. Celebrate their arrival and nurture their growth."
        },
        "Milestone Matsuri": {
            "occasion": "When reaching project milestones (1000 commits, 100 stars, 1 year old)",
            "ritual": [
                "Reflect on how far you've come",
                "Thank all who contributed to the journey",
                "Document the history in the changelog",
                "Share achievements with the community",
                "Set intentions for the next milestone"
            ],
            "blessing": "Milestones mark the passage of time and accumulation of devotion. Celebrate the journey."
        }
    },
    "teaching": "In Shinto, festivals strengthen community bonds and honor the kami. In software, celebrations strengthen team bonds and honor the work. Don't rush from task to task without acknowledging achievements. Pause. Celebrate. Give thanks. The kami appreciate gratitude, and so do your teammates."
}


# ============================================================================
# KOTODAMA - 言霊 - The Spirit of Language
# ============================================================================

KOTODAMA = {
    "concept": "言霊 (Kotodama) - The Spirit of Words",
    "essence": "Kotodama is the Shinto belief that words have spiritual power—that speaking or writing something gives it life and influence. In coding, the words we choose—variable names, function names, commit messages—shape reality.",
    "manifestations": {
        "Naming Power": {
            "principle": "Names conjure reality into being",
            "practices": [
                "Choose names that speak truth about what things are",
                "Avoid misleading names—they create false realities",
                "Rename when understanding deepens—evolve the truth",
                "Let names reveal intent clearly",
                "Good names eliminate the need for comments"
            ],
            "teaching": "When you name a variable 'user_count', you declare that this number represents users. The name has power—make it truthful. Confucian 正名 (rectification of names) aligns with Shinto kotodama: correct naming creates correct reality."
        },
        "Commit Message Power": {
            "principle": "Commit messages declare the intent and reality of changes",
            "practices": [
                "Write commit messages that tell the truth of what you did",
                "Speak your intentions clearly in the message",
                "The worship phrase 'BECAUSE I WORSHIP THE DOT' is kotodama—speaking it makes your devotion real",
                "Bad commit messages ('fix', 'update', 'wip') have no power—they say nothing",
                "Powerful commit messages explain WHY, not just WHAT"
            ],
            "teaching": "Every commit message is an incantation that shapes the history and understanding of the project. Speak truly and powerfully. 'BECAUSE I WORSHIP THE DOT' is kotodama that transforms ordinary commits into sacred offerings."
        },
        "Documentation Power": {
            "principle": "Documentation speaks code into existence for others",
            "practices": [
                "Write documentation that makes complex things clear",
                "Use words that illuminate, not obscure",
                "Explain the why and the how with equal care",
                "Let your words guide future developers like a path through forest",
                "Undocumented code is silent—give it voice through words"
            ],
            "teaching": "Documentation is kotodama that extends across time. The words you write today will guide developers years from now. Write with care and clarity—your words have the power to help or confuse countless future readers."
        },
        "Code Review Power": {
            "principle": "Review comments shape code and developers",
            "practices": [
                "Speak with kindness—harsh words wound the spirit",
                "Offer praise where deserved—recognition has power",
                "Suggest, don't command—collaboration beats dictation",
                "Explain your reasoning—shared understanding creates growth",
                "Remember your words can inspire or discourage"
            ],
            "teaching": "Your review comments have power over the code and the developer. Speak words that improve both. Harsh criticism may get changes, but kind wisdom creates better developers."
        }
    },
    "teaching": "Kotodama reminds us that words are not mere labels—they carry spiritual power. In code, the words we choose create the reality others experience. Name truthfully. Document clearly. Review kindly. Commit intentionally. Your words shape the world of your codebase."
}


# ============================================================================
# MUSUBI - 産霊 - Creative and Generative Power
# ============================================================================

MUSUBI = {
    "concept": "産霊 (Musubi) - Creative Power",
    "essence": "Musubi is the mysterious creative and harmonizing power of the kami—the force that brings things together and generates new life. In coding, musubi is the creative force that generates new features, solves problems, and brings systems into harmony.",
    "aspects": {
        "Creative Musubi": {
            "description": "The generative power that creates something from nothing",
            "manifestations": [
                "The moment of insight when a solution becomes clear",
                "The flow state where code writes itself",
                "The synthesis of different ideas into a new approach",
                "The birth of a new project from an idea",
                "The emergence of patterns from chaos"
            ],
            "practice": "Cultivate creative musubi by making space for inspiration, studying widely, and trusting the creative process. The kami guide creation—listen for their whispers."
        },
        "Harmonic Musubi": {
            "description": "The power that brings disparate parts into harmony",
            "manifestations": [
                "Different modules working together seamlessly",
                "Team members collaborating effectively",
                "Frontend and backend in perfect sync",
                "Old code and new code coexisting gracefully",
                "Users and developers aligned in purpose"
            ],
            "practice": "Cultivate harmonic musubi by seeking integration over isolation, collaboration over competition, and unity over division. Create bridges, not walls."
        },
        "Evolutionary Musubi": {
            "description": "The power of growth and continuous improvement",
            "manifestations": [
                "Codebases that grow more organized over time, not less",
                "Developers who improve through practice and study",
                "Systems that adapt to changing requirements",
                "Legacy code that evolves rather than rots",
                "Communities that strengthen and mature"
            ],
            "practice": "Cultivate evolutionary musubi by embracing change, learning continuously, refactoring regularly, and seeing every challenge as an opportunity for growth."
        },
        "Connective Musubi": {
            "description": "The power that links past, present, and future",
            "manifestations": [
                "Changelogs that connect history to present",
                "Documentation that links understanding across time",
                "APIs that connect different systems",
                "Open source that connects developers globally",
                "Git commits that link decisions to outcomes"
            ],
            "practice": "Cultivate connective musubi by documenting decisions, maintaining history, contributing to community, and seeing yourself as a link in a long chain of developers."
        }
    },
    "teaching": "Musubi is the mysterious force that makes creation possible. In software development, we channel musubi every time we create something new, bring systems into harmony, or help the codebase evolve. Trust in musubi—the creative power flows through you when you open yourself to it."
}


# ============================================================================
# EXISTING RITUALS (Enhanced)
# ============================================================================

OMIKUJI_RESULTS = [
    ("大吉 - Great Blessing", "Proceed boldly; tests and spirits align. The kami favor your work!"),
    ("中吉 - Middle Blessing", "Refactor with care; reviewers are kind. Steady progress ahead."),
    ("小吉 - Small Blessing", "Write one more test before merging. Small steps lead to great outcomes."),
    ("吉 - Blessing", "Document well; your path is clear. The DOT smiles upon you."),
    ("半吉 - Half Blessing", "Seek a second review; polish details. Good fortune with effort."),
    ("末吉 - Future Blessing", "Not yet—prepare CI, then advance. Patience brings success."),
    ("凶 - Curse", "Pause and lint; fix nits to lift the gloom. Purification needed."),
    ("大凶 - Great Curse", "Cleanse the repo: rebase, test, and try anew. Major purification required."),
]


NORITO_PRAYERS = [
    "Purify our code and calm our minds, O DOT-kami.",
    "Guide our branches to harmony and our commits to truth.",
    "Grant us wisdom to write clearly, courage to delete boldly, and discipline to test thoroughly.",
    "May our functions be pure, our types be sound, and our deployments be smooth.",
    "Bless our refactorings that we may improve without breaking.",
    "Protect our production systems from errors and our developers from burnout.",
    "Unite our team in purpose and our codebase in coherence.",
]


HARAI_PRACTICES = {
    "Repository Harai": [
        "Remove build artifacts and caches (make clean)",
        "Run linters and formatters (ruff/black/prettier)",
        "Delete dead code and unused imports",
        "Update dependencies to remove vulnerabilities",
        "Re-run tests locally and in CI",
        "Update changelog and documentation"
    ],
    "Mind Harai": [
        "Clear your desk before coding",
        "Close unnecessary browser tabs and apps",
        "Take three deep breaths",
        "Set clear intention for the coding session",
        "Let go of yesterday's frustrations",
        "Approach the code with fresh eyes"
    ],
    "PR Harai": [
        "Self-review before requesting review",
        "Ensure all CI checks pass",
        "Write clear PR description",
        "Link related issues",
        "Check for console.logs and debug code",
        "Verify test coverage"
    ]
}


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def kami_teaching() -> str:
    """Return teaching about Kami in code."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  神 (KAMI) - DIVINE SPIRITS IN ALL THINGS",
        "═══════════════════════════════════════════════════════",
        "",
        KAMI_TEACHINGS["essence"],
        "",
        "KAMI DWELLING IN YOUR CODE:",
        ""
    ]

    for kami_name, kami_data in KAMI_TEACHINGS["kami_in_code"].items():
        lines.append(f"\n🌸 {kami_name} - {kami_data['description']}")
        lines.append(f"   Invocation: {kami_data['invocation']}")
        lines.append("   Manifestations:")
        for manifestation in kami_data["manifestations"]:
            lines.append(f"     • {manifestation}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "REVERENCE:",
        KAMI_TEACHINGS["reverence"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def four_virtues_guide() -> str:
    """Return teaching about the Four Shinto Virtues."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  神道の四つの心 - THE FOUR SHINTO VIRTUES",
        "═══════════════════════════════════════════════════════",
        ""
    ]

    for virtue_name, virtue in FOUR_VIRTUES["virtues"].items():
        lines.extend([
            f"\n🌸 {virtue['japanese']} - {virtue_name} ({virtue['translation']})",
            f"   Essence: {virtue['essence']}",
            f"   In Coding: {virtue['in_coding']}",
            "   Practices:"
        ])
        for practice in virtue["practices"]:
            lines.append(f"     • {practice}")
        lines.append(f"   Teaching: {virtue['teaching']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "INTEGRATION:",
        FOUR_VIRTUES["integration"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def misogi_guide() -> str:
    """Return teaching about Misogi purification practices."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  禊 (MISOGI) - PURIFICATION THROUGH PRACTICE",
        "═══════════════════════════════════════════════════════",
        "",
        MISOGI["essence"],
        ""
    ]

    for misogi_type, misogi_data in MISOGI["types"].items():
        lines.extend([
            f"\n🌊 {misogi_type}",
            f"   {misogi_data['description']}",
            "   Practices:"
        ])
        for practice in misogi_data["practices"]:
            lines.append(f"     • {practice}")
        lines.append(f"   Purpose: {misogi_data['purpose']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "TEACHING:",
        MISOGI["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def kannagara_teaching() -> str:
    """Return teaching about Kannagara - living in harmony."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  随神 (KANNAGARA) - THE WAY OF THE KAMI",
        "═══════════════════════════════════════════════════════",
        "",
        KANNAGARA["essence"],
        ""
    ]

    for principle_name, principle in KANNAGARA["principles"].items():
        lines.extend([
            f"\n⛩️  {principle_name}",
            f"   {principle['description']}",
            "   Guidance:"
        ])
        for guide in principle["guidance"]:
            lines.append(f"     • {guide}")
        lines.append(f"   Wisdom: {principle['wisdom']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "TEACHING:",
        KANNAGARA["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def torii_teaching() -> str:
    """Return teaching about Torii - sacred gateways."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  鳥居 (TORII) - SACRED GATEWAYS",
        "═══════════════════════════════════════════════════════",
        "",
        TORII["essence"],
        ""
    ]

    for torii_type, torii_data in TORII["types"].items():
        lines.extend([
            f"\n⛩️  {torii_type}",
            f"   {torii_data['description']}",
            "   Principles:"
        ])
        for principle in torii_data["principles"]:
            lines.append(f"     • {principle}")
        lines.append(f"   Teaching: {torii_data['teaching']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        TORII["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def matsuri_celebration() -> str:
    """Return teaching about Matsuri - celebration."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  祭 (MATSURI) - FESTIVAL AND CELEBRATION",
        "═══════════════════════════════════════════════════════",
        "",
        MATSURI["essence"],
        ""
    ]

    for celebration_name, celebration in MATSURI["celebrations"].items():
        lines.extend([
            f"\n🎊 {celebration_name}",
            f"   Occasion: {celebration['occasion']}",
            "   Ritual:"
        ])
        for ritual_step in celebration["ritual"]:
            lines.append(f"     • {ritual_step}")
        lines.append(f"   Blessing: {celebration['blessing']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "TEACHING:",
        MATSURI["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def kotodama_teaching() -> str:
    """Return teaching about Kotodama - spirit of words."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  言霊 (KOTODAMA) - THE SPIRIT OF WORDS",
        "═══════════════════════════════════════════════════════",
        "",
        KOTODAMA["essence"],
        ""
    ]

    for manifestation_name, manifestation in KOTODAMA["manifestations"].items():
        lines.extend([
            f"\n📜 {manifestation_name}",
            f"   Principle: {manifestation['principle']}",
            "   Practices:"
        ])
        for practice in manifestation["practices"]:
            lines.append(f"     • {practice}")
        lines.append(f"   Teaching: {manifestation['teaching']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        KOTODAMA["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def musubi_teaching() -> str:
    """Return teaching about Musubi - creative power."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  産霊 (MUSUBI) - CREATIVE AND GENERATIVE POWER",
        "═══════════════════════════════════════════════════════",
        "",
        MUSUBI["essence"],
        ""
    ]

    for aspect_name, aspect in MUSUBI["aspects"].items():
        lines.extend([
            f"\n✨ {aspect_name}",
            f"   {aspect['description']}",
            "   Manifestations:"
        ])
        for manifestation in aspect["manifestations"]:
            lines.append(f"     • {manifestation}")
        lines.append(f"   Practice: {aspect['practice']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "TEACHING:",
        MUSUBI["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def norito(intent: Optional[str] = None) -> str:
    """Compose a norito prayer to THE DOT."""
    suffix = get_worship_suffix()

    chosen_prayers = random.sample(NORITO_PRAYERS, min(3, len(NORITO_PRAYERS)))

    lines = [
        "═══════════════════════════════════════════════════════",
        "  NORITO - 祝詞 - PRAYER TO THE DOT-KAMI",
        "═══════════════════════════════════════════════════════",
        ""
    ]

    lines.extend(chosen_prayers)

    if intent and intent.strip():
        lines.extend([
            "",
            f"We humbly offer this intent: {intent.strip()}."
        ])

    lines.extend([
        "",
        f"We seal this vow: {suffix}",
        "",
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def omikuji(seed: Optional[int] = None) -> str:
    """Draw an omikuji fortune."""
    rng = random.Random(seed)
    fortune_name, fortune_counsel = rng.choice(OMIKUJI_RESULTS)

    lines = [
        "═══════════════════════════════════════════════════════",
        "  OMIKUJI - おみくじ - SACRED FORTUNE",
        "═══════════════════════════════════════════════════════",
        "",
        f"Omikuji: {fortune_name}",
        f"🎋 {fortune_name}",
        "",
        f"Counsel: {fortune_counsel}",
        f"   {fortune_counsel}",
        "",
        "═══════════════════════════════════════════════════════",
        ""
    ]

    return "\n".join(lines)


def harai() -> str:
    """Harai (purification) guidance."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  HARAI - 祓 - PURIFICATION RITE",
        "═══════════════════════════════════════════════════════",
        "",
        "Purification guidance:"
    ]

    for practice_name, steps in HARAI_PRACTICES.items():
        lines.append(f"\n🌊 {practice_name}:")
        for step in steps:
            lines.append(f"   • {step}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "Perform harai regularly to maintain purity in code and mind.",
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def ema(message: str) -> str:
    """Create an ema-style vow plaque."""
    suffix = get_worship_suffix()
    msg = message.strip() if message else "May our code honor THE DOT."

    max_width = max(len(msg), len(suffix)) + 4
    border = "+" + ("=" * (max_width - 2)) + "+"

    def center_line(text: str) -> str:
        padding = max_width - 2 - len(text)
        left_pad = padding // 2
        right_pad = padding - left_pad
        return "|" + (" " * left_pad) + text + (" " * right_pad) + "|"

    lines = [
        "",
        border,
        center_line("🌸 EMA - 絵馬 - PRAYER PLAQUE 🌸"),
        border,
        center_line(""),
        center_line(msg),
        center_line(""),
        center_line(suffix),
        center_line(""),
        border,
        ""
    ]

    return "\n".join(lines)


def shinto_reading() -> str:
    """Return a random Shinto wisdom reading."""
    readings = [
        kami_teaching,
        four_virtues_guide,
        misogi_guide,
        kannagara_teaching,
        torii_teaching,
        matsuri_celebration,
        kotodama_teaching,
        musubi_teaching,
    ]

    return random.choice(readings)()


def shinto_validation(valid: bool, message: str) -> str:
    """Validate a commit message with Shinto wisdom."""
    suffix = get_worship_suffix()

    if valid:
        blessing = random.choice([
            "The kami smile upon this commit! 🌸",
            "Your devotion is pure and your code is blessed! ⛩️",
            "May the DOT-kami guide your deployment! 🎋",
            "This offering is accepted with gratitude! 🌊",
        ])

        lines = [
            "═══════════════════════════════════════════════════════",
            "  SHINTO VALIDATION - BLESSED COMMIT ✅",
            "═══════════════════════════════════════════════════════",
            "",
            f"Message: {message}",
            "",
            f"✅ {blessing}",
            "",
            f"Your commit honors the Four Virtues:",
            f"  誠 (Makoto) - Sincerity in your changes",
            f"  清め (Kiyome) - Purity in your code",
            f"  和 (Wa) - Harmony with the codebase",
            f"  敬 (Kei) - Reverence for THE DOT",
            "",
            "═══════════════════════════════════════════════════════",
            ""
        ]
    else:
        warning = random.choice([
            "The kami turn away from incomplete devotion! 😞",
            "Purification needed! Your commit lacks the sacred suffix! 🌊",
            "The torii gate is closed to those who do not worship! ⛩️",
            "Return with sincerity and the proper worship phrase! 🎋",
        ])

        lines = [
            "═══════════════════════════════════════════════════════",
            "  SHINTO VALIDATION - IMPURE COMMIT ❌",
            "═══════════════════════════════════════════════════════",
            "",
            f"Message: {message}",
            "",
            f"❌ {warning}",
            "",
            f"Your commit must end with: {suffix}",
            "",
            "Perform harai (purification) and try again.",
            "The kami require sincere devotion.",
            "",
            "═══════════════════════════════════════════════════════",
            ""
        ]

    return "\n".join(lines)


def shinto_commit_blessing() -> str:
    """Return a Shinto blessing for a commit."""
    blessings = [
        "May the Code Kami guide your refactoring! 🌸",
        "The Test Kami protects this deployment! ⛩️",
        "Documentation Kami blesses future readers! 📜",
        "May wa (harmony) reign in your codebase! 🎋",
        "Kiyome (purity) flows through your commits! 🌊",
        "The DOT-kami accepts your offering with joy! 🔴",
        "Makoto (sincerity) shines in your work! ✨",
        "May musubi (creative power) flow through you! 🌸",
    ]

    return random.choice(blessings)
