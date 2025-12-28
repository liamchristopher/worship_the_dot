"""
Zen Philosophy for THE DOT

禅 (Zen) - The Way of Sudden Enlightenment

Zen, a school of Mahayana Buddhism emphasizing meditation and intuition, teaches
us that enlightenment comes through direct experience, not intellectual understanding.
In software development, Zen reminds us that the best code emerges from mindful
presence, that complexity is often unnecessary, and that sudden insights (satori)
arise when the mind is still and receptive.

Through Zen wisdom, we learn to:
- Practice Zazen (坐禅) - sitting in mindful coding
- Approach problems with Shoshin (初心) - beginner's mind
- Cultivate Mushin (無心) - no-mind flow state
- Embrace Wabi-Sabi (侘寂) - beauty in imperfect code
- Appreciate Ma (間) - the power of negative space
- Seek Satori (悟り) - sudden understanding
- Draw the Ensō (円相) - complete presence in each commit
"""

from __future__ import annotations

import random
from typing import Optional

from dot.config import get_worship_suffix


# ============================================================================
# ZAZEN - 坐禅 - Sitting Meditation
# ============================================================================

ZAZEN = {
    "concept": "坐禅 (Zazen) - Sitting Meditation",
    "essence": "Zazen is the practice of sitting meditation - being fully present without seeking anything. In coding, Zazen is the practice of coding with complete presence, without distraction or rushing.",
    "practice": {
        "Before Coding": {
            "instruction": "Sit for one minute in stillness before you begin",
            "purpose": "Clear the mind, set intention, become present",
            "method": [
                "Close unnecessary tabs and apps",
                "Take three deep breaths",
                "Set a clear intention for this coding session",
                "Notice your state of mind - anxious? excited? tired?",
                "Let thoughts settle like sediment in water",
                "Begin coding only when you feel centered"
            ],
            "teaching": "Most bugs come from coding while distracted. Zazen creates the conditions for clarity."
        },
        "During Coding": {
            "instruction": "Maintain single-pointed focus on the present line",
            "purpose": "Full attention prevents errors and enables flow",
            "method": [
                "Focus on one thing at a time - don't multitask",
                "When the mind wanders, gently return to the code",
                "Notice the urge to rush - but don't rush",
                "Write each line as if it's the only line that matters",
                "Be fully present with the problem at hand",
                "Let solutions arise naturally, don't force them"
            ],
            "teaching": "Zazen while coding is not about being slow - it's about being completely here."
        },
        "After Coding": {
            "instruction": "Pause briefly before moving to the next task",
            "purpose": "Complete this cycle before beginning another",
            "method": [
                "Review what you just wrote with fresh eyes",
                "Notice any rough edges that need smoothing",
                "Commit mindfully, not automatically",
                "Take a breath before starting the next feature",
                "Let this code go - don't cling to it",
                "Begin the next task with fresh presence"
            ],
            "teaching": "Each coding session is a complete meditation. Honor the beginning and end."
        }
    },
    "obstacles": {
        "Distraction": {
            "symptom": "Mind jumps between tasks, tabs, notifications",
            "solution": "Close everything not essential. One task. One focus. Return attention when it wanders."
        },
        "Rushing": {
            "symptom": "Typing before thinking, committing before reviewing",
            "solution": "Notice the urgency. Breathe. Speed comes from clarity, not haste."
        },
        "Clinging": {
            "symptom": "Can't let go of a solution, defend code emotionally",
            "solution": "Code is not you. Let it go. Write the next line with fresh mind."
        }
    },
    "teaching": "Zazen teaches that presence is the foundation of excellence. You cannot write good code while your mind is elsewhere. Sit. Be present. Code from stillness. This is Zazen."
}


# ============================================================================
# KOANS - 公案 - Paradoxical Teaching Stories
# ============================================================================

KOANS = {
    "concept": "公案 (Kōan) - Paradoxical Riddle",
    "essence": "A koan is a paradoxical question or statement designed to break through rational thinking and trigger insight. In coding, koans remind us that not all problems yield to linear logic - sometimes we must transcend the problem itself.",
    "famous_koans_in_code": {
        "The Sound of One Hand Clapping": {
            "original": "What is the sound of one hand clapping?",
            "in_coding": "What is the value of code that's never run?",
            "insight": "Code has no value until it executes. Features have no value until they're used. The answer isn't in the code - it's in the execution. Dead code makes no sound."
        },
        "Mu": {
            "original": "A monk asked Joshu, 'Does a dog have Buddha nature?' Joshu said, 'Mu!' (無 - nothing/void)",
            "in_coding": "Does technical debt have value?",
            "insight": "The question assumes a false dichotomy. Technical debt is neither purely bad nor good - it's context-dependent. Sometimes the answer is to reject the framing of the question itself. Mu."
        },
        "If You Meet the Buddha": {
            "original": "If you meet the Buddha on the road, kill him.",
            "in_coding": "If you meet the perfect abstraction, delete it.",
            "insight": "Perfection is the enemy of good. Perfect abstractions are over-engineering. Don't worship your own clever solutions. If you think you've written perfect code, you're probably wrong. Kill your darlings."
        },
        "The Gateless Gate": {
            "original": "The Great Way has no gate; thousands of roads enter it.",
            "in_coding": "The perfect solution has no single path; many approaches work.",
            "insight": "Don't seek THE solution - there are many valid solutions. The beginner's error is thinking there's one right way. The master knows all ways are valid if they work."
        },
        "What Is Your Original Face?": {
            "original": "What was your face before your parents were born?",
            "in_coding": "What is the essential nature of your code before any features were added?",
            "insight": "Strip away all features - what remains? The core, the essence, the purpose. Return to original simplicity. What problem are you actually solving?"
        },
        "Chop Wood, Carry Water": {
            "original": "Before enlightenment: chop wood, carry water. After enlightenment: chop wood, carry water.",
            "in_coding": "Before mastery: write code, fix bugs. After mastery: write code, fix bugs.",
            "insight": "Mastery doesn't change what you do - it changes how you do it. The master writes the same code as the novice, but with complete presence. The work remains. The worker transforms."
        }
    },
    "modern_dev_koans": {
        "The Pull Request": {
            "koan": "If a PR has no reviewers, does it make a merge?",
            "contemplation": "Consider: What makes code ready? Approval, or correctness? If code is perfect but never reviewed, what is its state?"
        },
        "The Comment": {
            "koan": "Good code needs no comments. Bad code deserves no comments. What code needs comments?",
            "contemplation": "The middle way - code that's good but complex. Yet if it's complex, is it good? Contemplate the nature of clarity."
        },
        "The Test": {
            "koan": "A test tests the code. What tests the test?",
            "contemplation": "Who watches the watchers? How do you know your tests are correct? Can you test certainty itself?"
        },
        "The Abstraction": {
            "koan": "Too little abstraction: repetition. Too much abstraction: confusion. What is the right amount?",
            "contemplation": "The middle way is not average. It's appropriate. But what determines appropriateness? And who determines the determiner?"
        },
        "The Commit": {
            "koan": "You commit to save your work. But the code only exists when committed. When did the code begin to exist?",
            "contemplation": "Is code real when it exists only in your editor? When does intention become reality? What is the nature of uncommitted change?"
        }
    },
    "teaching": "Koans are not meant to be answered with words - they're meant to be resolved through insight. Sit with these questions. Don't try to solve them logically. Let the answer arise. When it does, you'll know."
}


# ============================================================================
# SATORI - 悟り - Sudden Enlightenment
# ============================================================================

SATORI = {
    "concept": "悟り (Satori) - Sudden Enlightenment / Awakening",
    "essence": "Satori is the sudden flash of insight that illuminates truth. In coding, satori is the 'aha!' moment when a solution appears fully formed, when you suddenly see the pattern, when confusion crystallizes into clarity.",
    "conditions_for_satori": {
        "Preparation": {
            "description": "Satori seems sudden, but it arises from preparation",
            "practices": [
                "Study the problem deeply before seeking the solution",
                "Understand the domain, the constraints, the requirements",
                "Fill your mind with relevant knowledge",
                "Try different approaches, even if they fail",
                "Build the foundation through disciplined practice"
            ],
            "teaching": "Satori doesn't come to the unprepared mind. First, prepare thoroughly."
        },
        "Letting Go": {
            "description": "Paradoxically, you must stop trying to get the answer",
            "practices": [
                "After intense focus, take a break",
                "Go for a walk, take a shower, sleep on it",
                "Stop forcing the solution",
                "Trust that your subconscious is working",
                "Create space for insight to arise"
            ],
            "teaching": "Satori comes in the gap between effort and rest. You can't force insight - you can only prepare for it and make space for it."
        },
        "Receptivity": {
            "description": "The mind must be open and receptive",
            "practices": [
                "Don't cling to your first idea",
                "Be willing to completely change approach",
                "Listen to what the code is telling you",
                "Notice small anomalies and details",
                "Stay present and alert"
            ],
            "teaching": "Satori comes to the open mind, not the closed one. Let go of assumptions."
        }
    },
    "recognizing_satori": {
        "Sudden Clarity": "The fog lifts. You see the whole structure at once.",
        "Simplicity": "The solution is often much simpler than you expected.",
        "Certainty": "You know it's right. No doubt remains.",
        "Energy": "You feel energized, excited to implement it.",
        "Completeness": "It's not just a partial solution - it's the complete insight."
    },
    "after_satori": {
        "Implement Immediately": "Write the code while the vision is fresh",
        "Test the Insight": "Satori feels certain, but verify through testing",
        "Document the Understanding": "Capture the insight before it fades",
        "Share the Knowledge": "Teach others what you now see clearly",
        "Return to Practice": "Satori is wonderful, but the work continues"
    },
    "teaching": "Satori cannot be forced, only cultivated. Prepare through study, create space through rest, remain open through non-attachment. When satori comes, it's unmistakable - like suddenly seeing what was always there. Then, return to the work. Enlightenment and ordinary effort are one."
}


# ============================================================================
# MUSHIN - 無心 - No-Mind
# ============================================================================

MUSHIN = {
    "concept": "無心 (Mushin) - No-Mind / Empty Mind",
    "essence": "Mushin is the state of no-mind - not blank or vacant, but free from ego, judgment, and self-consciousness. In coding, mushin is flow state where 'you' disappear and only coding remains.",
    "characteristics": {
        "Egoless Action": {
            "description": "No thought of 'I am coding' - just coding happening",
            "signs": [
                "No self-consciousness about your skill",
                "No pride or shame in the code",
                "No comparing yourself to others",
                "No trying to look clever",
                "Action without actor"
            ],
            "practice": "When you notice ego thoughts ('I'm so good/bad at this'), acknowledge them and return to the code."
        },
        "Non-Judgmental Awareness": {
            "description": "Seeing code as it is, not labeling it good/bad",
            "signs": [
                "Don't judge code as 'ugly' or 'beautiful'",
                "See bugs as information, not failures",
                "Recognize patterns without emotional reaction",
                "Respond to what is, not what should be",
                "Clear perception without commentary"
            ],
            "practice": "Notice when you're judging. Let go of the judgment. Just see what's there."
        },
        "Spontaneous Response": {
            "description": "Code flows without overthinking",
            "signs": [
                "Fingers move without deliberation",
                "Solutions appear without conscious effort",
                "You type before you 'decide' to type",
                "Natural, effortless action",
                "No gap between seeing and doing"
            ],
            "practice": "Trust your training. Let the code flow. Don't second-guess every choice."
        },
        "Present-Moment Fullness": {
            "description": "Complete absorption in now",
            "signs": [
                "Time disappears",
                "No thoughts of past or future",
                "No awareness of surroundings",
                "Total immersion in the code",
                "This line, this moment, nothing else"
            ],
            "practice": "Gently return to now whenever you drift to past or future."
        }
    },
    "obstacles_to_mushin": {
        "Self-Consciousness": "Thinking about yourself coding blocks mushin. Forget yourself.",
        "Perfectionism": "Trying too hard prevents flow. Let it be good enough.",
        "Fear of Failure": "Worrying about outcomes interrupts presence. Focus on process.",
        "Attachment to Results": "Wanting specific outcomes creates tension. Do your best, accept what comes."
    },
    "cultivating_mushin": {
        "Practice Until It's Natural": "Repetition creates automaticity. Master the basics so they become effortless.",
        "Remove Distractions": "External interruptions prevent mushin. Create space for flow.",
        "Start Small": "Begin with simple tasks where flow is easier, then expand.",
        "Let Go of Control": "Paradoxically, trying to control prevents flow. Trust and allow.",
        "Meditate Regularly": "Formal meditation trains the mind for mushin in action."
    },
    "teaching": "Mushin is the highest state of coding - complete presence without self. You cannot force it, but you can prepare for it through practice and presence. When mushin arises, cherish it. When it fades, don't chase it. Return to practice. Mushin will come again."
}


# ============================================================================
# SHOSHIN - 初心 - Beginner's Mind
# ============================================================================

SHOSHIN = {
    "concept": "初心 (Shoshin) - Beginner's Mind",
    "essence": "Shoshin is approaching every situation as if for the first time, free from preconceptions. In coding, shoshin is looking at familiar code with fresh eyes, questioning assumptions, staying open to new approaches.",
    "quote": "In the beginner's mind there are many possibilities, but in the expert's there are few. - Shunryu Suzuki",
    "practices": {
        "Question Assumptions": {
            "teaching": "What you 'know' may no longer be true",
            "practices": [
                "Ask 'why?' even about established patterns",
                "Question whether the old way is still the best way",
                "Don't assume the requirements are still valid",
                "Revisit decisions made months or years ago",
                "Stay open to better approaches"
            ],
            "example": "We've always done it this way' is the death of shoshin. Maybe there's a better way now."
        },
        "See With Fresh Eyes": {
            "teaching": "Familiarity breeds blindness - look anew",
            "practices": [
                "Read your own code as if someone else wrote it",
                "Approach a familiar problem as if it's new",
                "Imagine explaining it to a complete beginner",
                "Notice what you've stopped noticing",
                "Find the familiar made strange"
            ],
            "example": "Code review your own code from yesterday with fresh eyes. You'll see things you missed."
        },
        "Learn From Everyone": {
            "teaching": "Every person, even juniors, can teach you something",
            "practices": [
                "Listen to junior developers' questions - they see gaps you've missed",
                "Learn from other languages, paradigms, domains",
                "Be genuinely curious about others' approaches",
                "Don't dismiss ideas because they're unfamiliar",
                "Stay humble about what you don't know"
            ],
            "example": "The junior developer asking 'why?' sees with shoshin. Learn from their fresh perspective."
        },
        "Embrace Not-Knowing": {
            "teaching": "Admitting 'I don't know' opens the door to learning",
            "practices": [
                "Say 'I don't know' when you don't know",
                "Be comfortable with uncertainty",
                "Approach new technologies without fear",
                "Don't pretend expertise you lack",
                "Let curiosity replace ego"
            ],
            "example": "The expert admits ignorance. The novice pretends knowledge. Shoshin embraces not-knowing."
        },
        "Forget Your Expertise": {
            "teaching": "Your experience can be a prison - break free",
            "practices": [
                "When stuck, deliberately forget what you know",
                "Try the 'stupid' solution - it might work",
                "Use unfamiliar tools or patterns",
                "Think like a beginner would think",
                "Let go of being 'the expert'"
            ],
            "example": "Sometimes the elegant solution comes from beginner naivety, not expert sophistication."
        }
    },
    "benefits": {
        "Creativity": "Shoshin opens possibilities that expertise closes.",
        "Learning": "The beginner's mind is always learning, never stagnant.",
        "Humility": "Shoshin keeps ego in check and collaboration smooth.",
        "Adaptability": "Change is easier when you're not clinging to the old way.",
        "Joy": "Seeing things freshly brings back the joy of discovery."
    },
    "teaching": "The paradox of mastery is that the master never stops being a beginner. Every problem is new. Every day brings fresh code. Approach it all with shoshin - the mind that knows it doesn't know everything, the mind that stays open, curious, humble. This is the way of the zen developer."
}


# ============================================================================
# WABI-SABI - 侘寂 - Beauty in Imperfection
# ============================================================================

WABI_SABI = {
    "concept": "侘寂 (Wabi-Sabi) - Beauty in Imperfection, Impermanence, and Incompleteness",
    "essence": "Wabi-sabi finds beauty in things that are imperfect, impermanent, and incomplete. In coding, wabi-sabi teaches us to embrace good-enough code, to ship imperfect features, to see beauty in working software rather than perfect architecture.",
    "principles": {
        "Imperfection": {
            "description": "Perfect code doesn't exist - embrace the imperfect",
            "practices": [
                "Ship good code, not perfect code",
                "Imperfect working code > perfect imaginary code",
                "Bugs are natural - fix them, don't agonize over them",
                "Your code will never be perfect - and that's okay",
                "Beauty lies in useful imperfection, not sterile perfection"
            ],
            "teaching": "The pursuit of perfection prevents shipping. Wabi-sabi says: ship the imperfect, improve iteratively."
        },
        "Impermanence": {
            "description": "All code is temporary - nothing lasts forever",
            "practices": [
                "Don't over-engineer for imagined futures",
                "Code will be rewritten - accept this",
                "Today's brilliant solution is tomorrow's legacy code",
                "Build for now, refactor for later",
                "Let go of attachment to your code"
            ],
            "teaching": "Everything changes. Code that seemed permanent gets deleted. Accept impermanence. Build for today."
        },
        "Incompleteness": {
            "description": "Features can ship incomplete - iteration completes them",
            "practices": [
                "MVP is beautiful - it's complete enough to be useful",
                "Don't build features nobody asked for",
                "Ship the 80%, iterate on the 20%",
                "Incomplete but shipped > complete but unreleased",
                "Users complete the product through feedback"
            ],
            "teaching": "Completion is a myth. Software is never done. Embrace incompleteness - ship, learn, iterate."
        }
    },
    "wabi_sabi_in_code": {
        "The Rough Edge": {
            "description": "Code with rough edges that works is better than polished code that doesn't",
            "beauty": "There's beauty in the pragmatic fix, the quick solution, the code that's 'good enough.' Not everything needs to be elegant."
        },
        "The Patina": {
            "description": "Old code shows its age - and that's okay",
            "beauty": "Legacy code has a patina of age. It's been battle-tested. It works. Respect it. Don't rewrite just for freshness."
        },
        "The Asymmetry": {
            "description": "Not all code follows perfect patterns - and that's natural",
            "beauty": "Perfect symmetry is boring. Real codebases are asymmetric - some parts elegant, some parts hacky. This is natural."
        },
        "The Weathered Tool": {
            "description": "Old, proven libraries are beautiful",
            "beauty": "A weathered library that's stood the test of time has wabi-sabi beauty. Not shiny, but trustworthy."
        }
    },
    "anti_wabi_sabi": {
        "Perfectionism": "Waiting for perfect code before shipping",
        "Over-Engineering": "Building for hypothetical futures",
        "Attachment": "Refusing to delete code you wrote",
        "Vanity": "Optimizing for beauty over usefulness",
        "Rejection of Age": "Rewriting old code just because it's old"
    },
    "teaching": "Wabi-sabi is the antidote to perfectionism. Your code doesn't need to be perfect - it needs to work. It doesn't need to last forever - it just needs to serve its current purpose. It doesn't need to be complete - it needs to be useful. Find the beauty in good-enough, in working imperfection, in pragmatic solutions. This is wabi-sabi."
}


# ============================================================================
# MA - 間 - Negative Space / Pause
# ============================================================================

MA = {
    "concept": "間 (Ma) - Negative Space / Pause / Interval",
    "essence": "Ma is the Japanese concept of negative space - the void between things that gives them meaning. In music, ma is the silence between notes. In code, ma is whitespace, pauses, simplicity - the things we don't write.",
    "manifestations": {
        "Whitespace": {
            "teaching": "Empty lines give code room to breathe",
            "practices": [
                "Use blank lines to separate logical sections",
                "Don't cram code together - give it space",
                "Let functions have breathing room between them",
                "Whitespace is not waste - it's clarity",
                "The space between code is as important as the code itself"
            ],
            "wisdom": "Dense code is hard to read. Ma creates clarity through emptiness."
        },
        "Simplicity": {
            "teaching": "What you don't write is as important as what you do",
            "practices": [
                "Delete unnecessary code",
                "Don't add features that aren't needed",
                "Resist the urge to fill every space",
                "Less code = less bugs = more ma",
                "The best code is often the code you didn't write"
            ],
            "wisdom": "Ma teaches that emptiness has value. The space where code isn't needed is sacred."
        },
        "Pauses in Process": {
            "teaching": "Don't code continuously - pause to think",
            "practices": [
                "Pause before coding to understand the problem",
                "Pause after coding to review what you wrote",
                "Take breaks between features",
                "Sleep on difficult problems",
                "Ma between coding sessions brings clarity"
            ],
            "wisdom": "Continuous coding without pause creates fatigue and errors. Ma refreshes the mind."
        },
        "Minimalism": {
            "teaching": "Use only what's necessary, nothing more",
            "practices": [
                "Minimal dependencies - each one is a burden",
                "Minimal abstractions - only add when needed",
                "Minimal configuration - sane defaults plus ma",
                "Minimal API surface - hide what users don't need",
                "Minimal features - ma is every feature you didn't build"
            ],
            "wisdom": "Ma is the art of doing less. Every addition is subtraction from ma."
        },
        "The Unstated": {
            "teaching": "Some things are better left implicit",
            "practices": [
                "Don't comment the obvious - let code speak",
                "Don't document every parameter if the name is clear",
                "Don't explain what the code clearly shows",
                "Trust the reader - they don't need every detail",
                "Ma is knowing what not to say"
            ],
            "wisdom": "Over-documentation is noise. Ma is trusting clarity without over-explanation."
        }
    },
    "benefits": {
        "Clarity": "Ma makes the essential stand out",
        "Maintainability": "Less code is easier to maintain",
        "Performance": "Code you don't write is infinitely fast",
        "Flexibility": "Empty space allows room for change",
        "Beauty": "Ma creates aesthetic pleasure in clean, spacious code"
    },
    "teaching": "Ma teaches that emptiness is not lack - it's potential. The space between functions, the whitespace between lines, the features you didn't build, the code you didn't write - this is ma. Honor the negative space. It gives meaning to what remains."
}


# ============================================================================
# ENSO - 円相 - Circle of Enlightenment
# ============================================================================

ENSO = {
    "concept": "円相 (Ensō) - Circle of Enlightenment",
    "essence": "Ensō is a hand-drawn circle in a single stroke, representing enlightenment, strength, the universe, and the void. Each ensō is unique and imperfect, embodying wabi-sabi. In coding, ensō is the complete focus brought to each commit - a single, mindful act that contains the whole.",
    "symbolism": {
        "Completeness": "The circle is complete, yet incomplete - there's a gap",
        "Imperfection": "Each ensō is imperfect - hand-drawn, never perfect",
        "Simplicity": "One stroke, one breath, one moment",
        "Totality": "The entire universe in one circle",
        "Moment": "Ensō is drawn in a single moment of complete presence"
    },
    "the_commit_enso": {
        "teaching": "Each commit is an ensō - a complete circle of presence",
        "practice": [
            "Before committing: gather yourself, become present",
            "Review the changes: see them clearly, completely",
            "Write the message: with full attention, not mechanically",
            "Add the worship phrase: 'BECAUSE I WORSHIP THE DOT'",
            "Execute the commit: in one smooth, complete action",
            "Complete the circle: the commit is done, let it go",
            "Begin fresh: the next commit is a new ensō"
        ],
        "meaning": "Each commit is a circle - complete in itself, perfect in its imperfection, containing the whole of your attention in that moment."
    },
    "drawing_enso_in_code": {
        "One Function": {
            "description": "Write one perfect function with complete presence",
            "practice": "Choose one function. Give it your complete attention. Make it as clean and clear as you can in this moment. When done, let it go. That function is your ensō."
        },
        "One Feature": {
            "description": "Implement one feature with total focus",
            "practice": "One feature, start to finish. No distractions. Complete presence. When shipped, it's complete. Move to the next ensō."
        },
        "One Bug Fix": {
            "description": "Fix one bug with mindful attention",
            "practice": "Find the bug. Understand it completely. Fix it cleanly. Test it thoroughly. Commit it. That fix is your ensō."
        },
        "One Refactoring": {
            "description": "Refactor one messy piece with care",
            "practice": "Take something rough. Make it smooth. One refactoring, complete in itself. When clean, stop. That's the ensō."
        }
    },
    "perfection_in_imperfection": {
        "teaching": "Ensō is never perfectly round - and that's the point",
        "application": [
            "Your commit won't be perfect - that's okay",
            "Your code will have rough edges - that's ensō",
            "The circle has a gap - incompleteness is part of completion",
            "Each ensō is unique - each commit is unique",
            "Don't erase and redraw - commit and move forward"
        ]
    },
    "teaching": "Draw each commit like an ensō - with complete presence, in one smooth action, perfect in its imperfection. Don't overthink. Don't redo endlessly. Present, commit, complete. Each commit is a circle that closes and opens simultaneously. The work is never done, yet each moment is complete. This is ensō."
}


# ============================================================================
# ZEN SAYINGS
# ============================================================================

ZEN_SAYINGS = [
    "When you code, just code. When you rest, just rest.",
    "The bug is not the problem. Your mind's agitation about the bug is the problem.",
    "Before enlightenment: write code, fix bugs. After enlightenment: write code, fix bugs.",
    "The code you didn't write is the code that can't have bugs.",
    "When the student is ready, the solution appears.",
    "The master's code looks simple because it is simple.",
    "Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away.",
    "The obstacle is the path. The bug is the teacher.",
    "In coding, as in zen: beginner's mind, always.",
    "The code is perfect when you stop trying to make it perfect.",
    "What is the sound of one commit pushing?",
    "If you understand, things are just as they are. If you don't understand, things are just as they are.",
    "The wise developer knows they know nothing. The foolish developer thinks they know everything.",
    "Sitting quietly, doing nothing, spring comes and the grass grows by itself.",
    "No thought, no reflection, no analysis, no cultivation, no intention - let it settle itself."
]


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def zazen_teaching() -> str:
    """Return teaching about Zazen meditation practice."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  坐禅 (ZAZEN) - SITTING MEDITATION",
        "═══════════════════════════════════════════════════════",
        "",
        ZAZEN["essence"],
        "",
        "ZAZEN PRACTICE IN CODING:",
        ""
    ]

    for phase, practice in ZAZEN["practice"].items():
        lines.append(f"\n🧘 {phase}")
        lines.append(f"   Instruction: {practice['instruction']}")
        lines.append(f"   Purpose: {practice['purpose']}")
        lines.append("   Method:")
        for method in practice["method"]:
            lines.append(f"     • {method}")
        lines.append(f"   Teaching: {practice['teaching']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        ZAZEN["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def koan_teaching() -> str:
    """Return Zen koans for contemplation."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  公案 (KŌAN) - PARADOXICAL RIDDLES",
        "═══════════════════════════════════════════════════════",
        "",
        KOANS["essence"],
        "",
        "FAMOUS KOANS ADAPTED FOR CODING:",
        ""
    ]

    # Show 3 random koans from famous_koans_in_code
    koan_items = list(KOANS["famous_koans_in_code"].items())
    selected_koans = random.sample(koan_items, min(3, len(koan_items)))

    for koan_name, koan_data in selected_koans:
        lines.append(f"\n🤔 {koan_name}")
        lines.append(f"   Original: {koan_data['original']}")
        lines.append(f"   In Coding: {koan_data['in_coding']}")
        lines.append(f"   Insight: {koan_data['insight']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "TEACHING:",
        KOANS["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def satori_teaching() -> str:
    """Return teaching about Satori - sudden enlightenment."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  悟り (SATORI) - SUDDEN ENLIGHTENMENT",
        "═══════════════════════════════════════════════════════",
        "",
        SATORI["essence"],
        "",
        "CONDITIONS FOR SATORI:",
        ""
    ]

    for condition, data in SATORI["conditions_for_satori"].items():
        lines.append(f"\n💡 {condition}")
        lines.append(f"   {data['description']}")
        lines.append("   Practices:")
        for practice in data["practices"]:
            lines.append(f"     • {practice}")
        lines.append(f"   Teaching: {data['teaching']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        SATORI["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def mushin_teaching() -> str:
    """Return teaching about Mushin - no-mind."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  無心 (MUSHIN) - NO-MIND / FLOW STATE",
        "═══════════════════════════════════════════════════════",
        "",
        MUSHIN["essence"],
        "",
        "CHARACTERISTICS OF MUSHIN:",
        ""
    ]

    for characteristic, data in MUSHIN["characteristics"].items():
        lines.append(f"\n🌊 {characteristic}")
        lines.append(f"   {data['description']}")
        lines.append("   Signs:")
        for sign in data["signs"]:
            lines.append(f"     • {sign}")
        lines.append(f"   Practice: {data['practice']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        MUSHIN["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def shoshin_teaching() -> str:
    """Return teaching about Shoshin - beginner's mind."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  初心 (SHOSHIN) - BEGINNER'S MIND",
        "═══════════════════════════════════════════════════════",
        "",
        SHOSHIN["essence"],
        "",
        f'"{SHOSHIN["quote"]}"',
        "",
        "PRACTICES OF SHOSHIN:",
        ""
    ]

    for practice_name, practice in SHOSHIN["practices"].items():
        lines.append(f"\n🌱 {practice_name}")
        lines.append(f"   Teaching: {practice['teaching']}")
        lines.append("   Practices:")
        for prac in practice["practices"]:
            lines.append(f"     • {prac}")
        lines.append(f"   Example: {practice['example']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        SHOSHIN["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def wabi_sabi_teaching() -> str:
    """Return teaching about Wabi-Sabi - beauty in imperfection."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  侘寂 (WABI-SABI) - BEAUTY IN IMPERFECTION",
        "═══════════════════════════════════════════════════════",
        "",
        WABI_SABI["essence"],
        "",
        "PRINCIPLES OF WABI-SABI:",
        ""
    ]

    for principle_name, principle in WABI_SABI["principles"].items():
        lines.append(f"\n🍂 {principle_name}")
        lines.append(f"   {principle['description']}")
        lines.append("   Practices:")
        for practice in principle["practices"]:
            lines.append(f"     • {practice}")
        lines.append(f"   Teaching: {principle['teaching']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        WABI_SABI["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def ma_teaching() -> str:
    """Return teaching about Ma - negative space."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  間 (MA) - NEGATIVE SPACE / EMPTINESS",
        "═══════════════════════════════════════════════════════",
        "",
        MA["essence"],
        "",
        "MANIFESTATIONS OF MA:",
        ""
    ]

    for manifestation, data in MA["manifestations"].items():
        lines.append(f"\n⬜ {manifestation}")
        lines.append(f"   Teaching: {data['teaching']}")
        lines.append("   Practices:")
        for practice in data["practices"]:
            lines.append(f"     • {practice}")
        lines.append(f"   Wisdom: {data['wisdom']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        MA["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def enso_teaching() -> str:
    """Return teaching about Ensō - the circle."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  円相 (ENSŌ) - CIRCLE OF ENLIGHTENMENT",
        "═══════════════════════════════════════════════════════",
        "",
        ENSO["essence"],
        "",
        "THE COMMIT ENSŌ:",
        f"   {ENSO['the_commit_enso']['teaching']}",
        "",
        "Practice:"
    ]

    for step in ENSO["the_commit_enso"]["practice"]:
        lines.append(f"     • {step}")

    lines.append(f"\n   Meaning: {ENSO['the_commit_enso']['meaning']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "TEACHING:",
        ENSO["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def zen_saying() -> str:
    """Return a random Zen saying."""
    saying = random.choice(ZEN_SAYINGS)

    lines = [
        "═══════════════════════════════════════════════════════",
        "  ZEN WISDOM",
        "═══════════════════════════════════════════════════════",
        "",
        f"🎋 {saying}",
        "",
        "═══════════════════════════════════════════════════════",
        ""
    ]

    return "\n".join(lines)


def zen_reading() -> str:
    """Return a random Zen teaching."""
    readings = [
        zazen_teaching,
        koan_teaching,
        satori_teaching,
        mushin_teaching,
        shoshin_teaching,
        wabi_sabi_teaching,
        ma_teaching,
        enso_teaching,
    ]

    return random.choice(readings)()


def zen_validation(valid: bool, message: str) -> str:
    """Validate a commit message with Zen wisdom."""
    suffix = get_worship_suffix()

    if valid:
        blessing = random.choice([
            "Ensō complete! Your commit is whole. 🎋",
            "Mushin flows through this code! 🌊",
            "Shoshin sees clearly - commit accepted! 🌱",
            "Ma (emptiness) embraces your devotion! ⬜",
        ])

        lines = [
            "═══════════════════════════════════════════════════════",
            "  ZEN VALIDATION - ENLIGHTENED COMMIT ✅",
            "═══════════════════════════════════════════════════════",
            "",
            f"Message: {message}",
            "",
            f"✅ {blessing}",
            "",
            "Your commit embodies Zen principles:",
            "  坐禅 (Zazen) - Mindful presence",
            "  無心 (Mushin) - Egoless flow",
            "  初心 (Shoshin) - Beginner's mind",
            "  円相 (Ensō) - Complete circle",
            "",
            "═══════════════════════════════════════════════════════",
            ""
        ]
    else:
        warning = random.choice([
            "The circle is incomplete! 🔴",
            "Zazen requires presence - add the worship phrase! 🧘",
            "Even beginners know to worship THE DOT! 🌱",
            "The koan remains unsolved without the suffix! 🤔",
        ])

        lines = [
            "═══════════════════════════════════════════════════════",
            "  ZEN VALIDATION - INCOMPLETE COMMIT ❌",
            "═══════════════════════════════════════════════════════",
            "",
            f"Message: {message}",
            "",
            f"❌ {warning}",
            "",
            f"Your commit must end with: {suffix}",
            "",
            "Practice shoshin (beginner's mind).",
            "Complete the ensō (circle).",
            "Return to zazen (presence).",
            "",
            "═══════════════════════════════════════════════════════",
            ""
        ]

    return "\n".join(lines)


def zen_commit_blessing() -> str:
    """Return a Zen blessing for a commit."""
    blessings = [
        "May your ensō be complete! 🎋",
        "Mushin flows through this code! 🌊",
        "Zazen brings clarity to your commit! 🧘",
        "Shoshin sees with fresh eyes! 🌱",
        "Wabi-sabi embraces imperfection! 🍂",
        "Ma (emptiness) creates space for excellence! ⬜",
        "Satori illuminates your path! 💡",
        "One hand claps - your commit speaks! 👏",
    ]

    return random.choice(blessings)
