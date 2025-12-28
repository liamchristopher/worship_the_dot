"""
Hermeticism mode for THE DOT.

Hermeticism is the ancient wisdom tradition attributed to Hermes Trismegistus
("Thrice-Great Hermes"), a legendary figure combining the Greek god Hermes and
the Egyptian god Thoth. The Hermetic teachings, found in the Corpus Hermeticum
and The Kybalion, provide universal principles governing reality.

The Seven Hermetic Principles:
1. Mentalism - The All is Mind; the Universe is Mental
2. Correspondence - As above, so below; as below, so above
3. Vibration - Nothing rests; everything moves; everything vibrates
4. Polarity - Everything is dual; everything has poles
5. Rhythm - Everything flows, out and in; everything has its tides
6. Cause and Effect - Every cause has its effect; every effect has its cause
7. Gender - Gender is in everything; everything has masculine and feminine

In development, these principles reveal deep truths about code, systems,
and the nature of software itself.
"""

import random


# ═══════════════════════════════════════════════════════════════════════════
# PRINCIPLE OF MENTALISM - The All is Mind
# ═══════════════════════════════════════════════════════════════════════════

MENTALISM = {
    "principle": "The Principle of Mentalism",
    "kybalion": "THE ALL IS MIND; The Universe is Mental.",
    "description": """
The first and most fundamental Hermetic principle: All that exists is mental
in nature. The Universe is a Mental Creation of THE ALL. Matter, energy, and
even physical reality are manifestations of Mind.

In development:
Code is pure thought made manifest. Before any program exists in silicon,
it exists in Mind. The architecture you conceive, the patterns you envision,
the solutions you imagine - these are not merely plans for reality; they ARE
reality in its mental form, seeking material expression.
    """,
    "applications_in_code": {
        "Code as Thought": {
            "truth": "Code is crystallized thought",
            "practices": [
                "Your mental clarity determines code quality",
                "Confused thinking produces confused code",
                "Clear mind → clear architecture → clean code",
                "The codebase is a collective mental space"
            ],
            "wisdom": "To improve your code, first improve your thinking."
        },
        "Mental Prototyping": {
            "truth": "The best code is written in the mind first",
            "practices": [
                "Think through the solution before touching keyboard",
                "Mental models precede and shape code models",
                "Refactoring starts with re-thinking, not re-writing",
                "Debug your thinking before debugging your code"
            ],
            "wisdom": "An hour of thinking can save days of coding."
        },
        "The Mental Repository": {
            "truth": "Your codebase is a shared mental construct",
            "practices": [
                "Documentation maps the collective mind",
                "Naming shapes how we mentally model the system",
                "Comments are mind-to-mind communication",
                "Code review is meeting of minds"
            ],
            "wisdom": "The codebase exists first in consciousness, second in files."
        },
        "Consciousness Creates Reality": {
            "truth": "What you focus on expands",
            "practices": [
                "Focus on the problem, and problems multiply",
                "Focus on solutions, and solutions emerge",
                "Where attention goes, code quality flows",
                "Your mental state shapes system state"
            ],
            "wisdom": "Change your mind about the code, and the code changes."
        }
    },
    "meditation": """
Before coding today, sit in silence.
Recognize: The program you will write exists first as thought.
The bugs you will fix exist first as confusion.
The architecture you will build exists first as vision.

THE ALL IS MIND.
Your mind is a fractal of THE ALL.
Code is mind made visible.

Code with consciousness. Code with clarity. Code with THE DOT.
    """
}


# ═══════════════════════════════════════════════════════════════════════════
# PRINCIPLE OF CORRESPONDENCE - As Above, So Below
# ═══════════════════════════════════════════════════════════════════════════

CORRESPONDENCE = {
    "principle": "The Principle of Correspondence",
    "kybalion": "As above, so below; as below, so above.",
    "emerald_tablet": "That which is below corresponds to that which is above, and that which is above corresponds to that which is below, to accomplish the miracle of the One Thing.",
    "description": """
There is a harmony, agreement, and correspondence between the different planes
of existence. Patterns repeat across scales. The same laws apply to atoms and
galaxies, to individuals and societies, to code and cosmos.

In development:
The structure of a function mirrors the structure of a module.
The module structure mirrors system architecture.
System architecture mirrors organizational structure (Conway's Law).
Your development process mirrors your thinking process.
The microcosm reflects the macrocosm. Patterns repeat.
    """,
    "applications_in_code": {
        "Fractals of Structure": {
            "truth": "Good code is self-similar across scales",
            "examples": [
                "A well-structured function mirrors a well-structured module",
                "A clean module mirrors a clean architecture",
                "A clear line of code mirrors clear commit messages",
                "Local quality predicts global quality"
            ],
            "practice": "If it's messy at one level, it's messy at all levels. Fix the pattern."
        },
        "Conway's Law": {
            "truth": "Systems mirror the organizations that build them",
            "correspondences": [
                "Siloed teams → siloed architecture",
                "Collaborative culture → modular, composable code",
                "Hierarchical org → layered architecture",
                "Communication patterns → API design patterns"
            ],
            "practice": "To change your architecture, you may need to change your organization."
        },
        "Process Mirrors Product": {
            "truth": "How you work determines what you build",
            "correspondences": [
                "Rushed development → brittle code",
                "Thoughtful development → robust code",
                "Test-driven process → testable architecture",
                "Code review culture → reviewable code structure"
            ],
            "practice": "Your development process is reflected in your codebase."
        },
        "Personal Code Signature": {
            "truth": "Your code reflects your mind",
            "correspondences": [
                "Clear thinker → clear code",
                "Anxious coder → defensive, over-engineered code",
                "Impatient coder → quick hacks and tech debt",
                "Mindful coder → intentional, elegant solutions"
            ],
            "practice": "To write better code, become a better thinker."
        },
        "Debugging Mirrors Life": {
            "truth": "How you debug code reflects how you solve problems",
            "correspondences": [
                "Random changes → random life decisions",
                "Systematic debugging → systematic problem-solving",
                "Root cause analysis in code → root cause analysis in life",
                "Patient debugging → patient conflict resolution"
            ],
            "practice": "Improve your debugging, improve your life."
        }
    },
    "emerald_tablet_teaching": """
The Emerald Tablet of Hermes Trismegistus teaches:

"As above, so below; as below, so above."

In code:
- The quality of your smallest function reflects the quality of your entire system
- The clarity of a single variable name reflects the clarity of your entire API
- The care in one commit reflects the care in your whole career
- Your localhost is a microcosm of production

Perfect the small, and you perfect the large.
Master the local, and you master the global.
    """
}


# ═══════════════════════════════════════════════════════════════════════════
# PRINCIPLE OF VIBRATION - Nothing Rests; Everything Moves
# ═══════════════════════════════════════════════════════════════════════════

VIBRATION = {
    "principle": "The Principle of Vibration",
    "kybalion": "Nothing rests; everything moves; everything vibrates.",
    "description": """
Nothing is static. Everything is in constant motion, vibrating at different
frequencies. The difference between matter, energy, and mind is merely a
difference in rate of vibration. Higher vibrations = higher consciousness,
higher quality, higher truth.

In development:
Code is never static. Systems are always changing. Even "stable" code runs
on vibrating electrons. Your energy and focus vibrate at different frequencies.
High-vibration coding produces high-quality software. Low-vibration coding
produces bugs and tech debt.
    """,
    "applications_in_code": {
        "High Vibration Development": {
            "high_frequency_states": {
                "Flow State": "Total absorption, effortless excellence, time disappears",
                "Clarity": "Seeing the solution clearly, knowing the right path",
                "Inspiration": "Ideas flowing, creativity unleashed",
                "Mastery": "Deep competence, elegant solutions",
                "Love of Craft": "Coding from joy, not obligation"
            },
            "low_frequency_states": {
                "Frustration": "Banging head against wall, nothing works",
                "Confusion": "Lost in complexity, can't see the path",
                "Boredom": "Mechanical coding, no engagement",
                "Fear": "Worried about breaking things, paralyzed",
                "Burnout": "Exhausted, no energy, every line is heavy"
            },
            "practice": "Notice your vibration. Raise it before coding."
        },
        "Vibrational Matching": {
            "truth": "You can only perceive solutions that match your vibration",
            "examples": [
                "Low vibration (frustrated) → can only see hacky solutions",
                "Medium vibration (calm) → can see solid, workable solutions",
                "High vibration (inspired) → can see elegant, beautiful solutions"
            ],
            "practice": "The solution exists at a higher vibration than the problem. Raise your frequency to see it."
        },
        "Code Has Vibration": {
            "high_vibration_code": [
                "Clear, intentional, purposeful",
                "Elegant, simple, beautiful",
                "Well-tested, robust, reliable",
                "Documented with care and love",
                "Feels good to read and modify"
            ],
            "low_vibration_code": [
                "Confused, accidental, chaotic",
                "Convoluted, complex, ugly",
                "Untested, fragile, buggy",
                "Undocumented or poorly documented",
                "Feels heavy to read and scary to modify"
            ],
            "practice": "Refactoring is raising the vibration of code."
        },
        "Team Vibration": {
            "truth": "Teams have collective vibrational frequency",
            "high_vibration_teams": [
                "Collaborative, supportive, growth-oriented",
                "Clear communication, psychological safety",
                "Shared vision, aligned purpose",
                "Celebrating wins, learning from failures"
            ],
            "low_vibration_teams": [
                "Competitive, critical, blame-oriented",
                "Poor communication, fear-based culture",
                "Misaligned, siloed, political",
                "Focusing on problems, punishing mistakes"
            ],
            "practice": "You can't code at high vibration in a low-vibration team. Raise the team vibration first."
        }
    },
    "practices_to_raise_vibration": {
        "Before Coding": [
            "Take 3 deep breaths",
            "Set a clear intention",
            "Express gratitude for the opportunity to code",
            "Listen to high-vibration music (or silence)",
            "Move your body (walk, stretch, dance)"
        ],
        "During Coding": [
            "Notice when you drop into frustration - pause and reset",
            "Take breaks when energy feels heavy",
            "Stay hydrated, well-fed, rested",
            "Code from love, not fear",
            "Celebrate small wins"
        ],
        "After Coding": [
            "Review your work with appreciation, not criticism",
            "Acknowledge what you learned",
            "Close with gratitude",
            "Let go - don't carry the code into your evening",
            "Rest and recharge"
        ]
    },
    "meditation": """
Close your eyes. Feel the energy in your body.
Notice: You are not static. You are vibrating.
Your thoughts vibrate. Your emotions vibrate. Your code will vibrate.

Choose your frequency.
Rise to the vibration of mastery, clarity, love.
From this high place, code.

Everything vibrates. Choose to vibrate high.
    """
}


# ═══════════════════════════════════════════════════════════════════════════
# PRINCIPLE OF POLARITY - Everything is Dual
# ═══════════════════════════════════════════════════════════════════════════

POLARITY = {
    "principle": "The Principle of Polarity",
    "kybalion": "Everything is Dual; everything has poles; everything has its pair of opposites.",
    "description": """
Everything exists on a spectrum between two poles. Hot and cold are the same
thing (temperature) at different degrees. Love and hate are the same energy
at different intensities. Opposites are identical in nature but different in
degree. You can transmute one pole to another by changing the vibration.

In development:
Bug/feature. Simple/complex. Abstraction/concreteness. These are not separate
things but poles of the same spectrum. Mastery means understanding both poles
and choosing the right degree for the situation.
    """,
    "applications_in_code": {
        "Classic Polarities in Development": {
            "Abstraction ↔ Concreteness": {
                "poles": "Too abstract (over-engineered) ↔ Too concrete (copy-paste code)",
                "wisdom": "The master knows when to abstract and when to be concrete",
                "practice": "Don't live at the extremes. Find the right degree for your situation."
            },
            "Simplicity ↔ Completeness": {
                "poles": "Too simple (missing features) ↔ Too complete (bloated)",
                "wisdom": "Simple is not simplistic. Complete is not bloated.",
                "practice": "MVP is the art of finding the right degree between these poles."
            },
            "Flexibility ↔ Rigidity": {
                "poles": "Too flexible (no constraints) ↔ Too rigid (can't change)",
                "wisdom": "Some structure enables freedom; too much structure prevents it",
                "practice": "Design for change, but not for every possible change."
            },
            "Speed ↔ Quality": {
                "poles": "Ship fast, break things ↔ Perfect code that never ships",
                "wisdom": "Both poles lead to failure. The middle path works.",
                "practice": "Ship good code quickly. Iterate to great."
            },
            "Documentation ↔ Code": {
                "poles": "Over-documented (noise) ↔ Under-documented (mystery)",
                "wisdom": "Good code is self-documenting but not undocumented",
                "practice": "Document why, not what. Let code explain what."
            }
        },
        "Mental Polarity Transmutation": {
            "Bug → Feature": {
                "lower_pole": "This is a terrible bug! I'm a bad developer!",
                "higher_pole": "This is a learning opportunity. I'm becoming better.",
                "transmutation": "Same situation. Different mental pole. Different outcome."
            },
            "Obstacle → Opportunity": {
                "lower_pole": "This technical debt is crushing us.",
                "higher_pole": "This refactoring will level up our skills.",
                "transmutation": "Shift the pole, shift the experience."
            },
            "Criticism → Feedback": {
                "lower_pole": "They're attacking my code. They hate me.",
                "higher_pole": "They're helping me improve. They care.",
                "transmutation": "Code review feels different at different poles."
            },
            "Complexity → Challenge": {
                "lower_pole": "This system is impossibly complex. I give up.",
                "higher_pole": "This system is beautifully intricate. I'm learning.",
                "transmutation": "Same code, different pole, different possibility."
            }
        },
        "The Middle Path": {
            "wisdom": "Extremes are rarely optimal",
            "principle": "Truth usually lies between the poles, not at them",
            "examples": [
                "Don't never test. Don't test everything. Test what matters.",
                "Don't never optimize. Don't prematurely optimize. Optimize bottlenecks.",
                "Don't never refactor. Don't constantly refactor. Refactor strategically.",
                "Don't never comment. Don't comment everything. Comment complexity.",
                "Don't zero dependencies. Don't infinite dependencies. Choose wisely."
            ],
            "practice": "When you find yourself at an extreme, ask: what's the opposite pole? Now find the middle."
        }
    },
    "transmutation_practice": {
        "Step 1": "Recognize you're at a low pole (frustration, fear, anger, confusion)",
        "Step 2": "Acknowledge it's the same thing as a high pole, just different degree",
        "Step 3": "Consciously choose to slide up the pole",
        "Step 4": "Use breath, movement, reframing to shift your vibration",
        "Step 5": "Notice how the situation looks different from the higher pole",
        "Example": """
You're frustrated with a bug (low pole).
Recognize: Frustration and determination are the same energy.
Choose: I will transmute frustration → determination.
Breathe: Three deep breaths.
Reframe: This bug is teaching me something important.
Result: Same bug, higher pole, better outcome.
        """
    }
}


# ═══════════════════════════════════════════════════════════════════════════
# PRINCIPLE OF RHYTHM - Everything Flows
# ═══════════════════════════════════════════════════════════════════════════

RHYTHM = {
    "principle": "The Principle of Rhythm",
    "kybalion": "Everything flows, out and in; everything has its tides; all things rise and fall.",
    "description": """
Everything has a natural rhythm, a pendulum swing, a cycle. What goes up must
come down. What goes out must come back. Summer follows winter. Day follows
night. The master learns to work with rhythm, not against it, and to neutralize
unwanted rhythmic swings through the Hermetic practice of polarization.

In development:
Productivity has rhythms. Energy has rhythms. Projects have rhythms. Teams
have rhythms. There are productive seasons and fallow seasons. Flow states
come and go. Bugs appear in waves. Recognize the rhythms and work with them.
    """,
    "applications_in_code": {
        "Natural Rhythms in Development": {
            "Daily Rhythm": {
                "peak_hours": "Most developers have 2-4 hours of peak mental clarity",
                "wisdom": "Do your hardest thinking during peak hours",
                "practice": [
                    "Schedule deep work during your peak energy",
                    "Do meetings and admin during low-energy periods",
                    "Don't fight your natural circadian rhythm",
                    "Know thyself: Are you a morning or evening coder?"
                ]
            },
            "Weekly Rhythm": {
                "flow": "Energy typically peaks mid-week, dips Friday afternoon",
                "wisdom": "Plan complex work for Tuesday/Wednesday",
                "practice": [
                    "Monday: planning, setup, easy wins",
                    "Tuesday/Wednesday: deep focus, hard problems",
                    "Thursday: integration, testing, refinement",
                    "Friday: cleanup, documentation, code review",
                    "Respect the rhythm; don't fight it"
                ]
            },
            "Sprint/Iteration Rhythm": {
                "flow": "Beginning: high energy, exploration → Middle: grind → End: push",
                "wisdom": "Every sprint has a natural rhythm",
                "practice": [
                    "Don't expect the same energy throughout",
                    "Plan for the rhythm: big tasks early, polish late",
                    "The final push is normal, not a failure",
                    "Rest between sprints"
                ]
            },
            "Career Rhythm": {
                "flow": "Learning → Mastery → Plateau → New challenge → Learning again",
                "wisdom": "Careers are cyclical, not linear",
                "practice": [
                    "Embrace learning periods (they feel uncomfortable)",
                    "Enjoy mastery periods (they won't last forever)",
                    "Accept plateau periods (they precede breakthroughs)",
                    "Seek new challenges when ready",
                    "Every trough is followed by a peak"
                ]
            }
        },
        "Recognizing Rhythmic Patterns": {
            "Bug Waves": {
                "pattern": "Bugs often come in clusters, then quiet periods",
                "wisdom": "Don't panic during a bug wave; it will pass",
                "practice": "When bugs cluster, stay calm. Fix systematically. The wave will end."
            },
            "Productivity Swings": {
                "pattern": "High productivity days followed by low productivity days",
                "wisdom": "You can't be peak productive every day",
                "practice": "On high days: build. On low days: maintain, learn, plan."
            },
            "Motivation Cycles": {
                "pattern": "Enthusiasm → Plateau → Resistance → Breakthrough → Enthusiasm",
                "wisdom": "The resistance period precedes every breakthrough",
                "practice": "When motivation dips, keep showing up. The rhythm will swing back."
            },
            "Team Energy": {
                "pattern": "Teams cycle through high morale and low morale",
                "wisdom": "Team energy is rhythmic, not constant",
                "practice": "Lead differently in different phases. Inspire in lows. Sustain in highs."
            }
        },
        "Working With Rhythm (Not Against It)": {
            "Surf the Wave": {
                "principle": "When energy is high, build. When energy is low, refactor.",
                "practices": [
                    "Don't force coding when energy is depleted",
                    "Don't waste peak energy on trivial tasks",
                    "Match task difficulty to current energy",
                    "Rest is part of the rhythm, not a failure"
                ]
            },
            "Seasonal Development": {
                "principle": "Projects have seasons",
                "spring": "New projects, exploration, rapid growth",
                "summer": "Peak productivity, building, shipping",
                "autumn": "Harvest, polish, documentation",
                "winter": "Maintenance, learning, planning for spring",
                "wisdom": "Don't expect summer productivity in winter"
            }
        },
        "Neutralizing Unwanted Rhythms": {
            "principle": "The Hermetic master rises above the swing of the pendulum",
            "technique": "Mental Polarization - refuse to swing to the negative pole",
            "practice": [
                "When the downswing comes (frustration, burnout, demotivation)",
                "Don't identify with it: 'I am not my emotions'",
                "Observe it: 'Interesting, the pendulum is swinging'",
                "Stay at a higher mental pole: 'This too shall pass'",
                "By non-identification, you neutralize the swing"
            ],
            "example": """
Bad week. Bugs everywhere. Code feels terrible.
Automatic response: "I'm a bad developer. I should quit."
Hermetic response: "This is a rhythmic downturn. It will pass. I observe it but don't identify with it."
Result: You don't swing as far into negativity. Recovery is faster.
            """
        }
    },
    "meditation": """
Observe the rhythms of breath.
In... out... in... out...
The breath teaches rhythm.

Everything in your development practice has rhythm:
Energy rises and falls.
Motivation waxes and wanes.
Productivity ebbs and flows.

Do not fight the rhythm.
Do not identify with the low point.
Observe: "Ah, the pendulum swings. It will swing back."

Rise above the rhythm by knowing it is rhythm.
    """
}


# ═══════════════════════════════════════════════════════════════════════════
# PRINCIPLE OF CAUSE AND EFFECT - Every Cause Has Its Effect
# ═══════════════════════════════════════════════════════════════════════════

CAUSE_AND_EFFECT = {
    "principle": "The Principle of Cause and Effect",
    "kybalion": "Every Cause has its Effect; every Effect has its Cause; everything happens according to Law.",
    "description": """
Nothing happens by chance. Every effect has a cause. Every action produces
a result. The universe is orderly, not random. What we call "luck" is simply
unrecognized causation. The master understands causation and becomes a cause
rather than an effect - shaping reality rather than being shaped by it.

In development:
Bugs don't appear randomly - they have causes. Good code doesn't happen by
accident - it has causes (skill, care, time, process). Your career trajectory
is not luck - it's the cumulative effect of your daily causes (practice,
learning, networking, showing up).
    """,
    "applications_in_code": {
        "Everything Has a Cause": {
            "The Bug": {
                "illusion": "This bug appeared randomly!",
                "truth": "This bug has a specific cause (or chain of causes)",
                "practice": [
                    "Reject randomness. Seek the cause.",
                    "Every bug is reproducible (if you find the cause)",
                    "Random behavior = unidentified causation",
                    "Find the cause, fix the cause, bug disappears"
                ]
            },
            "The Success": {
                "illusion": "They're just lucky/talented!",
                "truth": "They created causes that produced success effects",
                "practice": [
                    "Study successful developers: What causes do they set in motion?",
                    "Success = skill + effort + consistency over time",
                    "Reverse-engineer the causation chain",
                    "Replicate the causes, get similar effects"
                ]
            },
            "The Failure": {
                "illusion": "Everything went wrong! Bad luck!",
                "truth": "Specific causes led to this effect",
                "practice": [
                    "Post-mortems reveal causation",
                    "Don't blame luck. Identify causes.",
                    "Remove the causes, prevent future effects",
                    "Failure teaches causation if you listen"
                ]
            }
        },
        "Becoming a Cause (Not an Effect)": {
            "Effect-Level Living": {
                "characteristics": [
                    "Reactive: life happens TO you",
                    "Victim mentality: 'I can't control anything'",
                    "Blaming: 'It's the tools/framework/team/manager'",
                    "Passive: waiting for things to change",
                    "Hopeless: 'Nothing I do matters'"
                ],
                "reality": "You are being moved by external causes"
            },
            "Cause-Level Living": {
                "characteristics": [
                    "Proactive: you happen to life",
                    "Agent mentality: 'I can influence outcomes'",
                    "Ownership: 'What can I do differently?'",
                    "Active: creating change",
                    "Empowered: 'My actions have effects'"
                ],
                "reality": "You are setting causes in motion"
            },
            "The Shift": {
                "from": "Why is this happening to me?",
                "to": "What causes can I set in motion?",
                "example": [
                    "Effect thinking: 'My code always has bugs' (helpless)",
                    "Cause thinking: 'I will write tests first' (empowered)",
                    "Effect thinking: 'I'm stuck in this role' (passive)",
                    "Cause thinking: 'I'll build portfolio projects and network' (active)"
                ]
            }
        },
        "The Law of Causation in Code": {
            "Input → Process → Output": {
                "truth": "Pure functions embody causation perfectly",
                "principle": "Same input always produces same output",
                "wisdom": "This is the law of cause and effect in code form",
                "practice": "The more your code follows clear causation, the better it is"
            },
            "Technical Debt": {
                "cause": "Shortcuts, rushed code, skipped tests, poor design",
                "effect": "Slow development, frequent bugs, hard to change",
                "law": "Every shortcut creates future friction",
                "practice": "Understand: Today's causes are tomorrow's effects"
            },
            "Code Quality": {
                "causes": [
                    "Clear thinking → clear code",
                    "Test-first development → testable architecture",
                    "Code review → knowledge sharing → better patterns",
                    "Refactoring regularly → maintainable codebase",
                    "Documentation → faster onboarding → team scaling"
                ],
                "effects": [
                    "Clear code → easier debugging",
                    "Testable architecture → confident refactoring",
                    "Better patterns → fewer bugs",
                    "Maintainable codebase → sustainable pace",
                    "Team scaling → project success"
                ],
                "wisdom": "Quality is not luck. Quality is the effect of quality causes."
            }
        },
        "Karma in Code": {
            "principle": "You reap what you sow",
            "examples": [
                "Write sloppy code → inherit sloppy code",
                "Skip tests → debug for hours later",
                "Ignore warnings → face production fires",
                "Hoard knowledge → become indispensable and trapped",
                "Share knowledge → build great teams and advance",
                "Code with care → others care for your code",
                "Code with carelessness → others resent your code"
            ],
            "wisdom": "Every line of code you write sets causes in motion. Choose wisely."
        },
        "Chains of Causation": {
            "principle": "Effects become causes for further effects",
            "positive_chain": [
                "1. Write clean code (cause)",
                "2. Code is easy to review (effect/cause)",
                "3. Team gives better feedback (effect/cause)",
                "4. You learn faster (effect/cause)",
                "5. You become senior faster (effect/cause)",
                "6. You mentor others (effect/cause)",
                "7. Team quality rises (effect)",
                "One initial cause creates a cascade"
            ],
            "negative_chain": [
                "1. Skip tests (cause)",
                "2. Bug ships (effect/cause)",
                "3. User reports bug (effect/cause)",
                "4. Emergency meeting (effect/cause)",
                "5. Pressure increases (effect/cause)",
                "6. Corners cut on next feature (effect/cause)",
                "7. More bugs (effect)",
                "One shortcut creates a cascade"
            ],
            "wisdom": "Be mindful of the first cause. It determines the chain."
        }
    },
    "practices": {
        "Root Cause Analysis": {
            "The Five Whys": [
                "Bug: User can't log in",
                "Why? Auth service is down",
                "Why? Database connection failed",
                "Why? Connection pool exhausted",
                "Why? No connection timeout set",
                "Why? Configuration was copied from old system",
                "Root cause: Poor configuration management",
                "Fix the cause, not just the symptom"
            ]
        },
        "Set Quality Causes": {
            "Daily Causes": [
                "Read code: Learn from it → Improve skills → Write better code",
                "Write tests: Catch bugs early → Build confidence → Ship quality",
                "Refactor: Reduce complexity → Make changes easier → Accelerate",
                "Document: Help future-you → Help teammates → Scale team",
                "Review code: Share knowledge → Improve collectively → Raise bar"
            ],
            "Each cause creates effects. Set good causes daily."
        },
        "Break Negative Chains": {
            "Identify": "What negative chain am I in?",
            "Interrupt": "Where can I break the chain?",
            "Substitute": "What positive cause can I set instead?",
            "Example": [
                "Chain: Stress → Rush → Bugs → More stress → More rush → More bugs",
                "Interrupt: Pause. Take 5 minutes to think before coding.",
                "Substitute: Calm → Careful → Quality → Less stress → Sustainable pace",
                "One interruption changes the chain"
            ]
        }
    },
    "meditation": """
Sit in stillness. Observe your breath.
Each inhale causes an exhale.
Each exhale causes an inhale.
Cause and effect, endlessly.

Now consider:
Every line of code you write today sets causes in motion.
Every decision you make creates a chain of effects.

You are not a victim of circumstances.
You are a creator of causes.

What causes will you set in motion today?
Choose wisely. Code consciously. Serve THE DOT.
    """
}


# ═══════════════════════════════════════════════════════════════════════════
# PRINCIPLE OF GENDER - Masculine and Feminine in Everything
# ═══════════════════════════════════════════════════════════════════════════

GENDER = {
    "principle": "The Principle of Gender",
    "kybalion": "Gender is in everything; everything has its Masculine and Feminine Principles.",
    "description": """
Gender manifests on all planes. Not biological sex, but universal principles:
Masculine = Active, projective, giving, assertive, yang
Feminine = Receptive, gestative, receiving, nurturing, yin

Both are necessary. Both are present in all things. Creation requires both.
The seed (masculine) must be received by the womb (feminine) to generate new life.
Imbalance leads to sterility (all masculine) or stagnation (all feminine).

In development:
Code requires both masculine and feminine principles. Action and reception.
Doing and being. Building and maintaining. Speaking and listening. Leading
and following. The master developer balances both.
    """,
    "applications_in_code": {
        "Masculine Principle in Development": {
            "characteristics": [
                "Active: Writing new code, building features",
                "Assertive: Making architectural decisions, setting direction",
                "Projective: Shipping, deploying, releasing",
                "Analytical: Breaking down problems, logical thinking",
                "Doing: Taking action, making things happen"
            ],
            "necessary_for": [
                "Getting things built",
                "Meeting deadlines",
                "Shipping products",
                "Making decisions",
                "Moving forward"
            ],
            "excess_masculine": [
                "Constant building without maintenance",
                "Forcing solutions without listening",
                "Action without reflection",
                "Talking without listening",
                "Shipping without stabilizing"
            ]
        },
        "Feminine Principle in Development": {
            "characteristics": [
                "Receptive: Reading code, understanding existing systems",
                "Nurturing: Maintaining code, refactoring, cleaning",
                "Gestative: Letting ideas incubate, thinking before acting",
                "Intuitive: Feeling the right solution, trusting gut",
                "Being: Pausing, reflecting, observing"
            ],
            "necessary_for": [
                "Understanding complex systems",
                "Sustainable codebases",
                "Deep insight",
                "Code quality",
                "Long-term health"
            ],
            "excess_feminine": [
                "Analysis paralysis (over-thinking, never acting)",
                "Endless refactoring, never shipping",
                "Waiting for perfect clarity before starting",
                "Receiving feedback but never asserting vision",
                "Maintaining but never creating"
            ]
        },
        "Balance Creates Mastery": {
            "The Build-Maintain Cycle": {
                "masculine": "Build new features",
                "feminine": "Maintain and refactor existing code",
                "balance": "Alternate between building and maintaining. Both are essential.",
                "wisdom": "A codebase that's all new features is unstable. A codebase that's all maintenance is stagnant."
            },
            "The Speak-Listen Cycle": {
                "masculine": "Assert your ideas, make proposals, lead discussions",
                "feminine": "Listen to teammates, receive feedback, understand needs",
                "balance": "Great developers talk AND listen",
                "wisdom": "If you only speak, you don't learn. If you only listen, you don't contribute."
            },
            "The Do-Be Cycle": {
                "masculine": "Do: code, ship, execute",
                "feminine": "Be: reflect, integrate, rest",
                "balance": "Work hard, rest hard. Think before coding. Reflect after shipping.",
                "wisdom": "Constant doing leads to burnout. Constant being leads to inaction."
            },
            "The Analysis-Intuition Cycle": {
                "masculine": "Analytical: Break down the problem logically",
                "feminine": "Intuitive: Feel the solution, trust your instincts",
                "balance": "Use both. Analyze AND intuit.",
                "wisdom": "Pure logic misses elegant solutions. Pure intuition misses edge cases."
            }
        },
        "Creative Generation Requires Both": {
            "The Seed and Womb": {
                "masculine_seed": "The idea, the vision, the initial inspiration",
                "feminine_womb": "The incubation, the development, the refinement",
                "both_needed": "Idea without incubation = nothing built. Incubation without idea = nothing to build.",
                "example": [
                    "You have an idea for a feature (masculine)",
                    "You sit with it, let it develop, refine it mentally (feminine)",
                    "You code the first version (masculine)",
                    "You test it, see how it feels, refactor (feminine)",
                    "You ship it (masculine)",
                    "You maintain it, nurture it, improve it (feminine)",
                    "Creation is a dance of both principles"
                ]
            }
        },
        "Recognizing Imbalance": {
            "Too Masculine": {
                "signs": [
                    "Constantly shipping but systems are unstable",
                    "Always talking, never listening",
                    "Making decisions without input",
                    "Forcing solutions without understanding",
                    "Burnt out from constant action"
                ],
                "remedy": "Cultivate feminine: Pause. Listen. Maintain. Reflect. Receive."
            },
            "Too Feminine": {
                "signs": [
                    "Endlessly refactoring, never shipping",
                    "Always listening, never contributing ideas",
                    "Waiting for perfect clarity",
                    "Receiving all feedback, losing your vision",
                    "Stuck in analysis paralysis"
                ],
                "remedy": "Cultivate masculine: Act. Decide. Ship. Assert. Do."
            }
        },
        "Gender Polarity in Teams": {
            "truth": "Teams need both principles",
            "masculine_heavy_teams": [
                "Fast-moving, high-shipping",
                "Lots of new features",
                "Risk of instability, tech debt",
                "Need: More maintenance, more listening, more reflection"
            ],
            "feminine_heavy_teams": [
                "Stable, well-maintained code",
                "Thoughtful, careful decisions",
                "Risk of slow progress, missed opportunities",
                "Need: More action, more shipping, more boldness"
            ],
            "balanced_teams": [
                "Ship AND maintain",
                "Lead AND listen",
                "Decide AND reflect",
                "Build AND nurture",
                "Result: Sustainable high performance"
            ]
        }
    },
    "practices": {
        "Cultivate Both Principles": {
            "Morning (Feminine)": [
                "Sit in silence before coding",
                "Read and understand existing code",
                "Listen to team standup",
                "Receive the day's requirements"
            ],
            "Day (Masculine)": [
                "Write code, build features",
                "Make decisions, assert ideas",
                "Ship commits, deploy code",
                "Lead discussions"
            ],
            "Evening (Feminine)": [
                "Reflect on what you built",
                "Refactor and clean",
                "Receive feedback from code review",
                "Nurture your work",
                "Rest and restore"
            ]
        },
        "Recognize Your Default": {
            "If you naturally lean masculine": [
                "Intentionally pause before acting",
                "Practice listening more in meetings",
                "Spend more time maintaining and refactoring",
                "Trust your intuition alongside analysis",
                "Rest is not weakness"
            ],
            "If you naturally lean feminine": [
                "Intentionally take action even without perfect clarity",
                "Practice asserting your ideas",
                "Ship even when it's not perfect",
                "Trust your logic alongside intuition",
                "Boldness is not recklessness"
            ]
        }
    },
    "meditation": """
Close your eyes. Feel the breath.
Inhale (masculine): active, drawing in, assertive.
Exhale (feminine): receptive, releasing, allowing.

Both are essential.
Both are within you.
You are both masculine and feminine.

In your code:
Build AND maintain.
Lead AND listen.
Do AND be.
Assert AND receive.

Balance the principles.
Master both.
Create from wholeness.
    """
}


# ═══════════════════════════════════════════════════════════════════════════
# THE EMERALD TABLET
# ═══════════════════════════════════════════════════════════════════════════

EMERALD_TABLET = {
    "title": "The Emerald Tablet of Hermes Trismegistus",
    "description": "The most famous Hermetic text, inscribed on an emerald stone",
    "text": [
        "1. True it is, without falsehood, certain and most true.",
        "2. That which is above is like to that which is below, and that which is below is like to that which is above, to accomplish the miracles of One Thing.",
        "3. And as all things were by contemplation of One, so all things arose from this One Thing by a single act of adaptation.",
        "4. The father thereof is the Sun, the mother the Moon.",
        "5. The Wind carried it in its womb, the Earth nursed it.",
        "6. This is the father of all perfection, or consummation of the whole world.",
        "7. Its power is integral, if it be turned into earth.",
        "8. Thou shalt separate the earth from the fire, the subtle from the gross, gently and with great ingenuity.",
        "9. It ascends from earth to heaven and descends again to earth, and receives the power of the superiors and of the inferiors.",
        "10. So thou hast the glory of the whole world; therefore let all obscurity flee before thee.",
        "11. This is the strong fortitude of all fortitude, for it will overcome every subtle thing and penetrate every solid thing.",
        "12. Thus was the world created.",
        "13. Hence there will be marvelous adaptations achieved, of which the manner is this.",
        "14. For this reason I am called Hermes Trismegistus, having the three parts of the philosophy of the whole world.",
        "15. That which I had to say about the operation of the Sun is completed."
    ],
    "interpretation_for_developers": {
        "Verse 2": "As above, so below - Your localhost mirrors production. Your function mirrors your module. Your code mirrors your mind.",
        "Verse 3": "All things arose from One - All code arises from THE DOT. All programs are variations of the One Program.",
        "Verse 8": "Separate the subtle from the gross - Refactoring is separation. Abstract the essence, remove the clutter.",
        "Verse 9": "Ascends from earth to heaven and descends again - Study theory (heaven), apply to practice (earth), then teach others (descend). Knowledge cycles.",
        "Verse 11": "Overcome every subtle thing and penetrate every solid thing - Master the abstract AND the concrete. Understand theory AND practice.",
        "Verse 12": "Thus was the world created - Thus is software created. By the same principles."
    }
}


# ═══════════════════════════════════════════════════════════════════════════
# HERMETIC WISDOM
# ═══════════════════════════════════════════════════════════════════════════

HERMETIC_QUOTES = [
    {
        "source": "The Kybalion",
        "quote": "The lips of wisdom are closed, except to the ears of Understanding.",
        "meaning": "You can only receive wisdom you're ready to understand. Keep learning, and you'll hear more."
    },
    {
        "source": "The Kybalion",
        "quote": "The half-wise, recognizing the comparative unreality of the Universe, imagine that they may defy its Laws—such are vain and presumptuous fools.",
        "meaning": "Yes, code is mental. But you still must follow the laws (syntax, logic, architecture). Understanding doesn't mean ignoring."
    },
    {
        "source": "Corpus Hermeticum",
        "quote": "If then you do not make yourself equal to God, you cannot apprehend God; for like is known by like.",
        "meaning": "To write excellent code, you must embody excellence. To create beauty, you must become beautiful. Like is known by like."
    },
    {
        "source": "The Kybalion",
        "quote": "To change your mood or mental state—change your vibration.",
        "meaning": "Frustrated with a bug? Change your vibration (walk, breathe, rest). You'll see the solution from a higher frequency."
    },
    {
        "source": "Hermes Trismegistus",
        "quote": "As above, so below, as within, so without, as the universe, so the soul.",
        "meaning": "Your internal state creates your external code. Clean mind → clean code. Chaotic mind → chaotic code."
    },
    {
        "source": "The Kybalion",
        "quote": "Mind (as well as metals and elements) may be transmuted, from state to state; degree to degree; condition to condition; pole to pole; vibration to vibration.",
        "meaning": "You can change your state. Frustration → Determination. Confusion → Clarity. This is transmutation."
    },
    {
        "source": "The Kybalion",
        "quote": "Rhythm may be neutralized by Mental Polarization.",
        "meaning": "When the low point comes (burnout, frustration), rise above by not identifying with it. Observe it, don't become it."
    },
    {
        "source": "The Kybalion",
        "quote": "Nothing escapes the Principle of Cause and Effect, but there are many Planes of Causation, and one may use the laws of the higher to overcome the laws of the lower.",
        "meaning": "You can't escape consequences, but you can operate from a higher level. Mental causation (clear thinking) overcomes physical causation (brute force coding)."
    },
    {
        "source": "Emerald Tablet",
        "quote": "Separate the Earth from Fire, the subtle from the gross, gently with great ingenuity.",
        "meaning": "Refactoring wisdom: Separate concerns. Extract the essence (subtle) from the implementation (gross). Do it gently, with skill."
    },
    {
        "source": "The Kybalion",
        "quote": "The Universe is Mental—held in the Mind of THE ALL.",
        "meaning": "Your codebase is mental—held in the Mind of THE DOT. It exists first as thought, second as code."
    }
]


def mentalism_teaching():
    """Return teaching on the Principle of Mentalism."""
    output = []
    output.append("═" * 70)
    output.append("☿ PRINCIPLE OF MENTALISM ☿")
    output.append("═" * 70)
    output.append(f"\"{MENTALISM['kybalion']}\"")
    output.append("")
    output.append(MENTALISM["description"].strip())
    output.append("")

    output.append("─" * 70)
    output.append("APPLICATIONS IN CODE")
    output.append("─" * 70)
    for app_name, app_data in MENTALISM["applications_in_code"].items():
        output.append(f"\n{app_name.upper()}")
        output.append(f"Truth: {app_data['truth']}")
        if "practices" in app_data:
            output.append("Practices:")
            for practice in app_data["practices"]:
                output.append(f"  • {practice}")
        output.append(f"Wisdom: {app_data['wisdom']}")

    output.append("")
    output.append("─" * 70)
    output.append("MEDITATION")
    output.append("─" * 70)
    output.append(MENTALISM["meditation"].strip())
    output.append("")
    output.append("═" * 70)

    return "\n".join(output)


def correspondence_teaching():
    """Return teaching on the Principle of Correspondence."""
    output = []
    output.append("═" * 70)
    output.append("☿ PRINCIPLE OF CORRESPONDENCE ☿")
    output.append("═" * 70)
    output.append(f"\"{CORRESPONDENCE['kybalion']}\"")
    output.append("")
    output.append(f"\"{CORRESPONDENCE['emerald_tablet']}\"")
    output.append("- The Emerald Tablet")
    output.append("")
    output.append(CORRESPONDENCE["description"].strip())
    output.append("")

    # Show 2-3 random applications
    apps = list(CORRESPONDENCE["applications_in_code"].items())
    random.shuffle(apps)
    for app_name, app_data in apps[:3]:
        output.append("─" * 70)
        output.append(app_name.upper())
        output.append("─" * 70)
        output.append(f"Truth: {app_data['truth']}")
        if "examples" in app_data:
            output.append("\nExamples:")
            for ex in app_data["examples"]:
                output.append(f"  • {ex}")
        if "correspondences" in app_data:
            output.append("\nCorrespondences:")
            for corr in app_data["correspondences"]:
                output.append(f"  • {corr}")
        output.append(f"\nPractice: {app_data['practice']}")
        output.append("")

    output.append("─" * 70)
    output.append("THE EMERALD TABLET TEACHING")
    output.append("─" * 70)
    output.append(CORRESPONDENCE["emerald_tablet_teaching"].strip())
    output.append("")
    output.append("═" * 70)

    return "\n".join(output)


def vibration_teaching():
    """Return teaching on the Principle of Vibration."""
    output = []
    output.append("═" * 70)
    output.append("☿ PRINCIPLE OF VIBRATION ☿")
    output.append("═" * 70)
    output.append(f"\"{VIBRATION['kybalion']}\"")
    output.append("")
    output.append(VIBRATION["description"].strip())
    output.append("")

    output.append("─" * 70)
    output.append("HIGH VIBRATION vs LOW VIBRATION DEVELOPMENT")
    output.append("─" * 70)
    hvd = VIBRATION["applications_in_code"]["High Vibration Development"]
    output.append("\nHigh Frequency States:")
    for state, desc in hvd["high_frequency_states"].items():
        output.append(f"  ✧ {state}: {desc}")
    output.append("\nLow Frequency States:")
    for state, desc in hvd["low_frequency_states"].items():
        output.append(f"  ✦ {state}: {desc}")
    output.append(f"\nPractice: {hvd['practice']}")

    output.append("")
    output.append("─" * 70)
    output.append("PRACTICES TO RAISE VIBRATION")
    output.append("─" * 70)
    for when, practices in VIBRATION["practices_to_raise_vibration"].items():
        output.append(f"\n{when}:")
        for practice in practices:
            output.append(f"  • {practice}")

    output.append("")
    output.append("─" * 70)
    output.append("MEDITATION")
    output.append("─" * 70)
    output.append(VIBRATION["meditation"].strip())
    output.append("")
    output.append("═" * 70)

    return "\n".join(output)


def polarity_teaching():
    """Return teaching on the Principle of Polarity."""
    output = []
    output.append("═" * 70)
    output.append("☿ PRINCIPLE OF POLARITY ☿")
    output.append("═" * 70)
    output.append(f"\"{POLARITY['kybalion']}\"")
    output.append("")
    output.append(POLARITY["description"].strip())
    output.append("")

    output.append("─" * 70)
    output.append("CLASSIC POLARITIES IN DEVELOPMENT")
    output.append("─" * 70)
    for pol_name, pol_data in POLARITY["applications_in_code"]["Classic Polarities in Development"].items():
        output.append(f"\n{pol_name}")
        output.append(f"Poles: {pol_data['poles']}")
        output.append(f"Wisdom: {pol_data['wisdom']}")
        output.append(f"Practice: {pol_data['practice']}")

    output.append("")
    output.append("─" * 70)
    output.append("MENTAL POLARITY TRANSMUTATION")
    output.append("─" * 70)
    trans_examples = list(POLARITY["applications_in_code"]["Mental Polarity Transmutation"].items())
    for trans_name, trans_data in random.sample(trans_examples, min(2, len(trans_examples))):
        output.append(f"\n{trans_name}")
        output.append(f"Lower pole: {trans_data['lower_pole']}")
        output.append(f"Higher pole: {trans_data['higher_pole']}")
        output.append(f"Transmutation: {trans_data['transmutation']}")

    output.append("")
    output.append("─" * 70)
    output.append("TRANSMUTATION PRACTICE")
    output.append("─" * 70)
    for step, instruction in POLARITY["transmutation_practice"].items():
        if step != "Example":
            output.append(f"{step}: {instruction}")
    output.append("")
    output.append(POLARITY["transmutation_practice"]["Example"].strip())
    output.append("")
    output.append("═" * 70)

    return "\n".join(output)


def rhythm_teaching():
    """Return teaching on the Principle of Rhythm."""
    output = []
    output.append("═" * 70)
    output.append("☿ PRINCIPLE OF RHYTHM ☿")
    output.append("═" * 70)
    output.append(f"\"{RHYTHM['kybalion']}\"")
    output.append("")
    output.append(RHYTHM["description"].strip())
    output.append("")

    output.append("─" * 70)
    output.append("NATURAL RHYTHMS IN DEVELOPMENT")
    output.append("─" * 70)
    for rhythm_name, rhythm_data in RHYTHM["applications_in_code"]["Natural Rhythms in Development"].items():
        output.append(f"\n{rhythm_name.upper()}")
        if "peak_hours" in rhythm_data:
            output.append(rhythm_data["peak_hours"])
        elif "flow" in rhythm_data:
            output.append(rhythm_data["flow"])
        output.append(f"Wisdom: {rhythm_data['wisdom']}")
        output.append("Practice:")
        for prac in rhythm_data["practice"]:
            output.append(f"  • {prac}")

    output.append("")
    output.append("─" * 70)
    output.append("NEUTRALIZING UNWANTED RHYTHMS")
    output.append("─" * 70)
    neut = RHYTHM["applications_in_code"]["Neutralizing Unwanted Rhythms"]
    output.append(f"Principle: {neut['principle']}")
    output.append(f"Technique: {neut['technique']}")
    output.append("\nPractice:")
    for prac in neut["practice"]:
        output.append(f"  • {prac}")
    output.append(f"\nExample:\n{neut['example'].strip()}")

    output.append("")
    output.append("─" * 70)
    output.append("MEDITATION")
    output.append("─" * 70)
    output.append(RHYTHM["meditation"].strip())
    output.append("")
    output.append("═" * 70)

    return "\n".join(output)


def cause_effect_teaching():
    """Return teaching on the Principle of Cause and Effect."""
    output = []
    output.append("═" * 70)
    output.append("☿ PRINCIPLE OF CAUSE AND EFFECT ☿")
    output.append("═" * 70)
    output.append(f"\"{CAUSE_AND_EFFECT['kybalion']}\"")
    output.append("")
    output.append(CAUSE_AND_EFFECT["description"].strip())
    output.append("")

    output.append("─" * 70)
    output.append("BECOMING A CAUSE (NOT AN EFFECT)")
    output.append("─" * 70)
    becoming = CAUSE_AND_EFFECT["applications_in_code"]["Becoming a Cause (Not an Effect)"]
    output.append("\nEffect-Level Living:")
    for char in becoming["Effect-Level Living"]["characteristics"]:
        output.append(f"  ✗ {char}")
    output.append(f"Reality: {becoming['Effect-Level Living']['reality']}")

    output.append("\nCause-Level Living:")
    for char in becoming["Cause-Level Living"]["characteristics"]:
        output.append(f"  ✓ {char}")
    output.append(f"Reality: {becoming['Cause-Level Living']['reality']}")

    output.append(f"\nThe Shift:")
    output.append(f"From: {becoming['The Shift']['from']}")
    output.append(f"To: {becoming['The Shift']['to']}")

    output.append("")
    output.append("─" * 70)
    output.append("KARMA IN CODE")
    output.append("─" * 70)
    karma = CAUSE_AND_EFFECT["applications_in_code"]["Karma in Code"]
    output.append(f"Principle: {karma['principle']}")
    output.append("\nExamples:")
    for example in karma["examples"]:
        output.append(f"  • {example}")
    output.append(f"\nWisdom: {karma['wisdom']}")

    output.append("")
    output.append("─" * 70)
    output.append("MEDITATION")
    output.append("─" * 70)
    output.append(CAUSE_AND_EFFECT["meditation"].strip())
    output.append("")
    output.append("═" * 70)

    return "\n".join(output)


def gender_teaching():
    """Return teaching on the Principle of Gender."""
    output = []
    output.append("═" * 70)
    output.append("☿ PRINCIPLE OF GENDER ☿")
    output.append("═" * 70)
    output.append(f"\"{GENDER['kybalion']}\"")
    output.append("")
    output.append(GENDER["description"].strip())
    output.append("")

    output.append("─" * 70)
    output.append("MASCULINE & FEMININE IN DEVELOPMENT")
    output.append("─" * 70)
    output.append("\nMASCULINE PRINCIPLE:")
    for char in GENDER["applications_in_code"]["Masculine Principle in Development"]["characteristics"]:
        output.append(f"  ☉ {char}")
    output.append("\nFEMININE PRINCIPLE:")
    for char in GENDER["applications_in_code"]["Feminine Principle in Development"]["characteristics"]:
        output.append(f"  ☽ {char}")

    output.append("")
    output.append("─" * 70)
    output.append("BALANCE CREATES MASTERY")
    output.append("─" * 70)
    for cycle_name, cycle_data in GENDER["applications_in_code"]["Balance Creates Mastery"].items():
        if cycle_name != "The Middle Path" and "masculine" in cycle_data:
            output.append(f"\n{cycle_name}")
            output.append(f"Masculine: {cycle_data['masculine']}")
            output.append(f"Feminine: {cycle_data['feminine']}")
            output.append(f"Balance: {cycle_data['balance']}")
            output.append(f"Wisdom: {cycle_data['wisdom']}")

    output.append("")
    output.append("─" * 70)
    output.append("RECOGNIZING IMBALANCE")
    output.append("─" * 70)
    imbalance = GENDER["applications_in_code"]["Recognizing Imbalance"]
    output.append("\nTOO MASCULINE:")
    for sign in imbalance["Too Masculine"]["signs"]:
        output.append(f"  • {sign}")
    output.append(f"Remedy: {imbalance['Too Masculine']['remedy']}")

    output.append("\nTOO FEMININE:")
    for sign in imbalance["Too Feminine"]["signs"]:
        output.append(f"  • {sign}")
    output.append(f"Remedy: {imbalance['Too Feminine']['remedy']}")

    output.append("")
    output.append("─" * 70)
    output.append("MEDITATION")
    output.append("─" * 70)
    output.append(GENDER["meditation"].strip())
    output.append("")
    output.append("═" * 70)

    return "\n".join(output)


def emerald_tablet_teaching():
    """Return the full Emerald Tablet with interpretation."""
    output = []
    output.append("═" * 70)
    output.append("☿ THE EMERALD TABLET ☿")
    output.append("Tabula Smaragdina Hermetis Trismegisti")
    output.append("═" * 70)
    output.append("")
    output.append(EMERALD_TABLET["description"])
    output.append("")

    output.append("─" * 70)
    output.append("THE TEXT")
    output.append("─" * 70)
    for line in EMERALD_TABLET["text"]:
        output.append(line)

    output.append("")
    output.append("─" * 70)
    output.append("INTERPRETATION FOR DEVELOPERS")
    output.append("─" * 70)
    for verse, interp in EMERALD_TABLET["interpretation_for_developers"].items():
        output.append(f"\n{verse}: {interp}")

    output.append("")
    output.append("═" * 70)

    return "\n".join(output)


def hermetic_reading():
    """Return a random Hermetic wisdom reading."""
    quote_data = random.choice(HERMETIC_QUOTES)

    output = []
    output.append("═" * 70)
    output.append("☿ HERMETIC WISDOM - Teachings of Hermes Trismegistus ☿")
    output.append("═" * 70)
    output.append("")
    output.append(f"From {quote_data['source']}:")
    output.append("")
    output.append(f'"{quote_data["quote"]}"')
    output.append("")
    output.append("─" * 70)
    output.append("MEANING FOR DEVELOPERS")
    output.append("─" * 70)
    output.append(quote_data["meaning"])
    output.append("")
    output.append("═" * 70)

    return "\n".join(output)


def hermetic_validation(valid: bool, message: str) -> str:
    """Validate a commit message with Hermetic wisdom."""
    output = []
    output.append("═" * 70)
    output.append("☿ HERMETIC WISDOM - Commit Validation ☿")
    output.append("═" * 70)
    output.append("")

    if valid:
        blessings = [
            "As above, so below - your commit reflects divine order. ☿",
            "THE ALL IS MIND, and your mind has created quality. Well done.",
            "Your vibration is high, and your code reflects it. ✧",
            "You have set good causes in motion. The effects will be excellent.",
            "Balance of masculine (action) and feminine (care) achieved. ☯",
            "This commit flows with the rhythm of excellence. ☿",
            "Hermes Trismegistus smiles upon this work. ⚚",
            "Your code corresponds to the higher planes. As above, so below. ✧"
        ]
        output.append("✓ VALID COMMIT")
        output.append("")
        output.append(random.choice(blessings))
        output.append("")
        output.append("The Hermetic principles are reflected in your work.")
        output.append("Code in wisdom. ☿")
    else:
        corrections = [
            "As above, so below - fix the small (message) to honor the large (commit). ☿",
            "Low vibration detected. Raise your frequency and try again. ✧",
            "You have set a cause. The effect is rejection. Choose a better cause.",
            "The principle of polarity: transmute this error into excellence.",
            "Rhythm brings you to a low point. Rise above it and revise. ☿",
            "Correspondence: Your message does not match your code's quality.",
            "The masculine (action) was strong, but the feminine (care) was weak. Balance both.",
            "Hermes teaches: 'The lips of wisdom are closed, except to the ears of Understanding.' Revise with understanding. ⚚"
        ]
        output.append("✗ INVALID COMMIT")
        output.append("")
        output.append(random.choice(corrections))
        output.append("")
        output.append("Return to the Hermetic principles. Revise your message.")
        output.append("THE DOT awaits your understanding. ☿")

    output.append("")
    output.append("═" * 70)

    return "\n".join(output)


def hermetic_commit_blessing():
    """Return a Hermetic-themed commit blessing."""
    blessings = [
        "As above, so below - may this commit reflect divine order. ☿",
        "By the Seven Principles, may this code be excellent. ⚚",
        "THE ALL IS MIND - code from consciousness. ✧",
        "May your vibration be high and your code reflect it. ☿",
        "Set good causes, reap good effects. Code wisely. ⚚",
        "Balance masculine action with feminine care. ☯",
        "May Hermes Trismegistus guide your keystrokes. ☿",
        "From Mind to Matter - may your thoughts become perfect code. ✧"
    ]

    return random.choice(blessings)
