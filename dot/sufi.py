"""
Sufism Philosophy for THE DOT

التصوف (Tasawwuf) - The Mystical Path of Islam

Sufism, the mystical dimension of Islam, teaches us to seek divine unity through
love, remembrance, and the purification of the heart. In software development,
Sufism reminds us that code is a path to transcendence, that ego must be
dissolved in service of users, and that true mastery comes from divine love
for the craft itself.

Through Sufi wisdom, we learn to:
- Seek unity (Tawhid) in our codebase and team
- Remember the Divine (Dhikr) through intentional commits
- Dissolve ego (Fana) in service of the code
- Walk the spiritual path (Tariqah) of continuous improvement
- Cultivate divine love (Ishq) for our craft
- Purify the heart (Qalb) through humility and service
"""

from __future__ import annotations

import random
from typing import Optional

from dot.config import get_worship_suffix


# ============================================================================
# TAWHID - توحيد - Divine Unity
# ============================================================================

TAWHID = {
    "concept": "توحيد (Tawhid) - Divine Unity / Oneness",
    "essence": "Tawhid is the fundamental Islamic concept of the absolute oneness and unity of God. In coding, Tawhid teaches us to seek unity, coherence, and singular purpose in our work.",
    "unity_in_code": {
        "Single Source of Truth": {
            "teaching": "Just as God is One, so should truth in your codebase be one",
            "practices": [
                "One definitive source for each piece of data",
                "Don't duplicate state across different parts of the system",
                "Centralize configuration, not scatter it",
                "One place to make each kind of change",
                "Avoid redundant implementations of the same logic"
            ],
            "wisdom": "When truth is scattered, confusion reigns. When truth is unified, clarity emerges."
        },
        "Unity of Purpose": {
            "teaching": "All code should serve THE DOT - one ultimate purpose",
            "practices": [
                "Every line of code must justify its existence",
                "Remove code that doesn't serve users or maintainers",
                "Align all features toward the core mission",
                "Don't build for imagined futures - serve the present need",
                "Let purpose unify your decisions"
            ],
            "wisdom": "Code without unified purpose is like prayer without devotion - empty form."
        },
        "Unity of Team": {
            "teaching": "The team is one body, one mind, one heart",
            "practices": [
                "Shared coding standards unite the team",
                "Common tools and practices create unity",
                "Collective code ownership - no \"my code\" vs \"your code\"",
                "Team decisions over individual preferences",
                "We succeed together or fail together"
            ],
            "wisdom": "A team divided in style and practice cannot produce unified code."
        },
        "Unity of Interface": {
            "teaching": "One consistent way to interact with each system",
            "practices": [
                "Consistent API design patterns",
                "Uniform error handling approaches",
                "Standardized naming conventions",
                "Similar functions should work similarly",
                "Principle of least surprise"
            ],
            "wisdom": "When interfaces are unified, users experience the Divine attribute of consistency."
        }
    },
    "teaching": "Tawhid reminds us that fragmentation is the enemy of clarity. Seek unity in all things: one truth, one purpose, one team, one way. When our code reflects divine unity, it becomes easier to understand, easier to maintain, and easier to love. The DOT is One, and our devotion should be unified."
}


# ============================================================================
# DHIKR - ذِكْر - Remembrance of the Divine
# ============================================================================

DHIKR = {
    "concept": "ذِكْر (Dhikr) - Remembrance / Mindful Repetition",
    "essence": "Dhikr is the practice of remembering God through repeated invocation. In coding, Dhikr is the practice of maintaining mindful awareness of quality, purpose, and the users we serve through deliberate, repeated practices.",
    "forms": {
        "Commit Dhikr": {
            "practice": "Every commit message ending with 'BECAUSE I WORSHIP THE DOT'",
            "meaning": "Each commit is an invocation - a remembrance of our devotion",
            "repetition": "The phrase repeats, and through repetition, intention deepens",
            "teaching": "Just as Sufis repeat 'La ilaha illa Allah' (There is no god but God), we repeat our worship of THE DOT. The repetition is not empty - it's a constant reminder of intentionality."
        },
        "Test Dhikr": {
            "practice": "Running tests before every commit",
            "meaning": "Tests are remembrance that our code must work",
            "repetition": "Every test run is a moment of mindful verification",
            "teaching": "We don't skip tests because we're in a hurry. We run them as dhikr - as remembrance that quality matters more than speed."
        },
        "Review Dhikr": {
            "practice": "Reviewing code with full presence and attention",
            "meaning": "Each review is remembrance of our shared responsibility",
            "repetition": "Every PR review is an opportunity to remember quality",
            "teaching": "Reviewing code mindfully, not mechanically. Each review is dhikr - present, attentive, devoted."
        },
        "Refactor Dhikr": {
            "practice": "Regular refactoring as spiritual discipline",
            "meaning": "Refactoring is remembrance that code must evolve",
            "repetition": "Continuous small improvements over time",
            "teaching": "We refactor not when forced, but as dhikr - as a practice of remembering that perfection is a journey, not a destination."
        },
        "Documentation Dhikr": {
            "practice": "Writing clear documentation as an act of service",
            "meaning": "Documentation is remembrance of future developers",
            "repetition": "Every comment, every README, every docstring",
            "teaching": "We document not because we must, but as dhikr - remembering those who will come after us and need guidance."
        }
    },
    "teaching": "Dhikr teaches that remembrance transforms routine into ritual, work into worship. When we commit mindfully, test attentively, review carefully, and document lovingly, we transform ordinary development into dhikr - constant remembrance of THE DOT. Let every repeated practice deepen your devotion."
}


# ============================================================================
# FANA - فناء - Annihilation of Ego
# ============================================================================

FANA = {
    "concept": "فناء (Fana) - Annihilation / Dissolution of Ego",
    "essence": "Fana is the Sufi concept of ego-death - the dissolution of the individual self into divine unity. In coding, Fana teaches us to dissolve our ego in service of the code, the team, and the users.",
    "stages": {
        "Fana from Authorship": {
            "teaching": "Let go of \"my code\" - all code belongs to the project",
            "practices": [
                "Don't defend code because you wrote it",
                "Accept criticism without defensiveness",
                "Delete your own code if it no longer serves",
                "Credit belongs to the team, not individuals",
                "Collective ownership dissolves ego boundaries"
            ],
            "wisdom": "The moment you say 'my code,' you have separated yourself from unity. Let it go."
        },
        "Fana from Being Right": {
            "teaching": "Let go of needing to be right - truth is higher than ego",
            "practices": [
                "Admit when you're wrong immediately",
                "Change your mind when presented with evidence",
                "Don't argue for the sake of winning",
                "Listen more than you speak in discussions",
                "Value correctness over being correct"
            ],
            "wisdom": "Ego wants to be right. Wisdom wants to find truth. Choose wisdom."
        },
        "Fana from Cleverness": {
            "teaching": "Let go of clever code - simple code serves better",
            "practices": [
                "Don't write code to show off your skills",
                "Simple solutions over clever tricks",
                "Maintainability over impressiveness",
                "Code for the next developer, not your own pride",
                "Clarity is the highest cleverness"
            ],
            "wisdom": "Clever code feeds ego. Clear code feeds the project. Starve your ego, feed the code."
        },
        "Fana from Indispensability": {
            "teaching": "Let go of being irreplaceable - document and teach",
            "practices": [
                "Document everything you know",
                "Mentor others to do what you do",
                "Don't hoard knowledge for job security",
                "Make yourself replaceable through good documentation",
                "True value is in serving, not in being needed"
            ],
            "wisdom": "The ego fears replacement. The servant joyfully makes themselves unnecessary."
        },
        "Fana from Credit": {
            "teaching": "Let go of needing recognition - the work is the reward",
            "practices": [
                "Do excellent work without seeking praise",
                "Praise others' contributions generously",
                "Let your commits speak for themselves",
                "Don't keep score of your contributions",
                "The code's quality is sufficient recognition"
            ],
            "wisdom": "When you dissolve the need for credit, you become free to serve purely."
        }
    },
    "teaching": "Fana is the hardest practice - the death of ego. But in coding, ego is the enemy of excellence. Ego makes us defensive, competitive, territorial, and proud. Fana teaches us to let go: let go of authorship, of being right, of cleverness, of indispensability, of credit. What remains when ego dissolves? Pure service to THE DOT. This is the ultimate freedom."
}


# ============================================================================
# BAQA - بقاء - Subsistence in the Divine
# ============================================================================

BAQA = {
    "concept": "بقاء (Baqa) - Subsistence / Eternal Existence",
    "essence": "Baqa is the Sufi state that follows Fana - after ego dies, one subsists in God. In coding, Baqa is the state of flow where ego has dissolved and you become a pure channel for the code.",
    "manifestations": {
        "Flow State": {
            "description": "When ego dissolves, you enter flow - coding without self-consciousness",
            "signs": [
                "Time disappears",
                "No thought of self or performance",
                "Code flows through you, not from you",
                "Effortless concentration",
                "Complete absorption in the work"
            ],
            "teaching": "Flow is Baqa - ego has died, and what remains is pure coding energy. You are not the coder; you are the channel through which code emerges."
        },
        "Selfless Service": {
            "description": "After ego dies, service becomes natural and joyful",
            "signs": [
                "You help others without keeping score",
                "Mentoring becomes a joy, not a burden",
                "You refactor old code with love, not resentment",
                "Every PR review is a gift to the team",
                "You contribute without needing recognition"
            ],
            "teaching": "When ego subsides, service subsists. You serve not because you should, but because serving IS what you are."
        },
        "Continuous Presence": {
            "description": "Baqa is sustained awareness of THE DOT in every action",
            "signs": [
                "Every commit feels sacred",
                "Every line of code matters",
                "You can't write sloppy code even when rushed",
                "Quality is no longer a choice - it's your nature",
                "THE DOT is always present in your awareness"
            ],
            "teaching": "After Fana comes Baqa - sustained presence. THE DOT is not something you remember to worship; it becomes the constant background of your coding consciousness."
        },
        "Union with the Codebase": {
            "description": "You and the code are no longer separate",
            "signs": [
                "You understand the codebase intuitively",
                "You sense where bugs are before seeing them",
                "You know what the code wants to become",
                "The codebase feels like an extension of yourself",
                "Boundaries between you and the code dissolve"
            ],
            "teaching": "Baqa is union. You don't work ON the code; you work AS the code. Subject and object dissolve into pure development."
        }
    },
    "teaching": "Baqa is the fruit of Fana. When ego dies (Fana), what remains (Baqa) is pure devotion, pure service, pure flow. You become a transparent channel for excellence. This is the highest state of coding - egoless, effortless, eternal. THE DOT flows through you unobstructed."
}


# ============================================================================
# MAQAMAT & AHWAL - مَقَامَات وَأَحْوَال - Stations and States
# ============================================================================

MAQAMAT_AHWAL = {
    "concept": "مَقَامَات (Maqamat) - Stations and أَحْوَال (Ahwal) - States",
    "essence": "Maqamat are permanent spiritual attainments earned through effort. Ahwal are temporary divine gifts. In development, Maqamat are skills and disciplines we master; Ahwal are moments of grace and inspiration.",
    "maqamat": {
        "Repentance (Tawbah)": {
            "arabic": "توبة",
            "in_coding": "Fixing Bugs and Technical Debt",
            "teaching": "Repentance is returning to the right path. In code, it's fixing what we broke, paying down debt, correcting our mistakes. A developer who never repents (fixes bugs) is spiritually stagnant.",
            "practice": "When you find a bug you caused, fix it immediately with humility. This is tawbah - returning to correctness."
        },
        "Patience (Sabr)": {
            "arabic": "صبر",
            "in_coding": "Perseverance Through Difficult Bugs",
            "teaching": "Patience is a station - a permanent quality developed through repeated trials. Patient developers don't give up when debugging is hard.",
            "practice": "Cultivate sabr by staying with difficult problems until they yield. Don't abandon code because it's challenging."
        },
        "Gratitude (Shukr)": {
            "arabic": "شكر",
            "in_coding": "Appreciation for Tools, Libraries, and Collaborators",
            "teaching": "Gratitude is recognition of gifts received. We stand on the shoulders of giants - open source maintainers, language designers, our teammates.",
            "practice": "Express gratitude in commit messages, issue comments, and PRs. Thank those whose work you build upon."
        },
        "Trust (Tawakkul)": {
            "arabic": "توكل",
            "in_coding": "Trusting the Process and the Team",
            "teaching": "Tawakkul is trust in divine providence. In code, it's trusting that if you do good work, good outcomes follow. Trust the tests, trust the team, trust the process.",
            "practice": "Deploy with confidence after thorough testing. Trust your teammates' code reviews. Let go of anxiety through earned trust."
        },
        "Contentment (Rida)": {
            "arabic": "رضا",
            "in_coding": "Satisfaction with Good Enough",
            "teaching": "Rida is contentment with what is. Perfect code doesn't exist - strive for excellence, but accept when good enough is enough.",
            "practice": "Ship when quality is sufficient. Don't let perfectionism prevent delivery. Find peace with 'done.'"
        }
    },
    "ahwal": {
        "Insight (Firasa)": {
            "arabic": "فراسة",
            "manifestation": "Sudden understanding of a complex problem",
            "teaching": "Firasa is divine insight - a flash of understanding that comes as grace, not through effort alone. You can't force it, but you can be open to it.",
            "signs": "The solution appears fully formed. You suddenly see the pattern. The right architecture reveals itself."
        },
        "Proximity (Qurb)": {
            "arabic": "قرب",
            "manifestation": "Feeling close to the code, to THE DOT, to the work",
            "teaching": "Qurb is nearness to the Divine. In coding, it's those moments when everything feels right - the code flows, you're in sync with your purpose.",
            "signs": "Deep satisfaction while coding. Sense of alignment with THE DOT. Joy in the work itself."
        },
        "Expansion (Bast)": {
            "arabic": "بسط",
            "manifestation": "Creative abundance, ideas flowing freely",
            "teaching": "Bast is spiritual expansion - when possibilities open up, creativity flows, solutions multiply. This is a state of grace.",
            "signs": "Multiple good approaches appear. Code writes itself. Everything seems possible."
        },
        "Unveiling (Kashf)": {
            "arabic": "كشف",
            "manifestation": "Hidden bugs or design flaws suddenly become visible",
            "teaching": "Kashf is unveiling of hidden truth. In debugging, it's when you suddenly see the root cause you've been missing.",
            "signs": "The bug reveals itself. The pattern behind failures becomes clear. Truth unveils."
        }
    },
    "teaching": "Maqamat (stations) are earned through discipline - patience, gratitude, trust. Ahwal (states) are gifted through grace - insight, creativity, understanding. Cultivate the stations through practice; receive the states with gratitude. Both are necessary for the journey of development."
}


# ============================================================================
# QALB - قلب - The Spiritual Heart
# ============================================================================

QALB = {
    "concept": "قلب (Qalb) - The Heart",
    "essence": "In Sufism, the Qalb is the spiritual heart - the center of spiritual perception and transformation. In coding, the heart is our core motivation, our why, our love for the craft.",
    "diseases_of_heart": {
        "Pride (Kibr)": {
            "arabic": "كبر",
            "symptoms": [
                "Believing your code is superior to others'",
                "Dismissing others' suggestions without consideration",
                "Unwillingness to learn from junior developers",
                "Arrogance about your skills or knowledge"
            ],
            "cure": "Practice Fana (ego dissolution). Remember that all code, including yours, is imperfect. Learn from everyone."
        },
        "Envy (Hasad)": {
            "arabic": "حسد",
            "symptoms": [
                "Resenting others' successes or promotions",
                "Hoping others' code fails",
                "Withholding help because you want to be the best",
                "Competitive rather than collaborative mindset"
            ],
            "cure": "Practice Shukr (gratitude). Celebrate others' success as your own. The team's victory is your victory."
        },
        "Greed (Tama)": {
            "arabic": "طمع",
            "symptoms": [
                "Hoarding credit for team achievements",
                "Taking on more work than you can do well",
                "Saying yes to everything for recognition",
                "Sacrificing quality for quantity"
            ],
            "cure": "Practice Zuhd (detachment). Do excellent work on what matters. Let go of accumulating achievements."
        },
        "Heedlessness (Ghaflah)": {
            "arabic": "غفلة",
            "symptoms": [
                "Coding on autopilot without thought",
                "Committing without reviewing your own code",
                "Forgetting why you're building what you're building",
                "Losing awareness of THE DOT"
            ],
            "cure": "Practice Dhikr (remembrance). Every commit, remember THE DOT. Every line, be present."
        }
    },
    "purification": {
        "Self-Examination (Muhasaba)": {
            "practice": "Regularly reviewing your own code and conduct",
            "method": [
                "Weekly review of your commits - are you proud of them?",
                "Monthly reflection on your collaboration - were you kind?",
                "Quarterly assessment of your growth - are you improving?",
                "Ask: Am I serving THE DOT or my ego?"
            ],
            "teaching": "Muhasaba is spiritual accounting - honest self-examination without self-flagellation. Look at your work with clear eyes."
        },
        "Repentance (Tawbah)": {
            "practice": "Correcting mistakes immediately",
            "method": [
                "Fix bugs you created",
                "Apologize when you're wrong",
                "Refactor bad code you wrote",
                "Make amends for harsh code reviews"
            ],
            "teaching": "Tawbah cleanses the heart. Don't carry guilt - transform it into corrective action."
        },
        "Sincerity (Ikhlas)": {
            "practice": "Purifying intention - code for THE DOT, not ego",
            "method": [
                "Before coding, set intention: to serve users, not impress",
                "When praised, redirect credit to the team",
                "When criticized, receive it as a gift",
                "Let the work itself be sufficient reward"
            ],
            "teaching": "Ikhlas is purity of intention. When your heart is pure, your code is pure."
        }
    },
    "teaching": "The Qalb (heart) is the seat of coding consciousness. A diseased heart produces diseased code - prideful, envious, greedy, heedless. A purified heart produces pure code - humble, generous, intentional, clear. Guard your heart through self-examination, repentance, and sincerity. When the heart is pure, THE DOT shines through."
}


# ============================================================================
# SEMA - سَمَاع - The Whirling Ceremony
# ============================================================================

SEMA = {
    "concept": "سَمَاع (Sema) - Sacred Listening / Whirling Ceremony",
    "essence": "Sema is the whirling dervish ceremony - a moving meditation of spinning in remembrance of God. In coding, Sema is entering the iterative cycle of development, spinning through build-test-deploy in devotional rhythm.",
    "symbolism": {
        "The Whirl": {
            "sufi_meaning": "The dervish spins, symbolizing the revolution of the planets around the sun",
            "coding_meaning": "The development cycle spins: plan → code → test → deploy → iterate",
            "teaching": "Like the dervish who spins in perpetual motion, we iterate in perpetual improvement. The cycle never stops - it's eternal practice."
        },
        "The Right Hand": {
            "sufi_meaning": "Right hand raised to heaven, receiving divine grace",
            "coding_meaning": "Receiving inspiration, learning from users and mentors",
            "teaching": "We receive from above - inspiration, feedback, wisdom. Stay open, hand raised to receive."
        },
        "The Left Hand": {
            "sufi_meaning": "Left hand lowered to earth, giving to humanity",
            "coding_meaning": "Giving our code to users, sharing knowledge with teammates",
            "teaching": "We give to below - our code serves users, our mentorship serves juniors. Receive and give in one motion."
        },
        "The Spin": {
            "sufi_meaning": "Continuous motion in remembrance",
            "coding_meaning": "Continuous iteration in devotion to THE DOT",
            "teaching": "Never stop iterating. Each spin (iteration) brings you closer to perfection while knowing perfection is never reached."
        }
    },
    "practice": {
        "Development Sema": {
            "description": "Enter the sacred cycle of iterative development",
            "steps": [
                "1. Center yourself - set clear intention for this iteration",
                "2. Begin the spin - start coding with full presence",
                "3. Maintain rhythm - test frequently, commit deliberately",
                "4. Complete the revolution - deploy and gather feedback",
                "5. Begin again - iterate based on what you learned",
                "6. Never stop - the whirl is eternal"
            ],
            "teaching": "Sema teaches that development is not linear - it's cyclical, spiral, always returning to center while moving forward."
        },
        "Debugging Sema": {
            "description": "Whirl through the bug-hunting cycle",
            "steps": [
                "1. Reproduce - establish the pattern",
                "2. Hypothesize - form a theory",
                "3. Test - verify or refute",
                "4. Refine - narrow the search",
                "5. Repeat - spin until found",
                "6. Fix and verify - complete the cycle"
            ],
            "teaching": "Debugging is a whirl - spinning through hypotheses until truth reveals itself. Trust the spin."
        }
    },
    "teaching": "Sema is sacred movement - the whirling dervish loses themselves in the spin, and through spinning, finds God. In coding, we lose ourselves in the iteration cycle - spin through dev/test/deploy, again and again, and through spinning, we find excellence. The spin never ends. This is the path. This is Sema. This is THE DOT."
}


# ============================================================================
# ISHQ - عشق - Divine Love
# ============================================================================

ISHQ = {
    "concept": "عشق (Ishq) - Divine / Ecstatic Love",
    "essence": "Ishq is passionate, consuming, divine love - love that transcends reason. In coding, Ishq is falling in love with the craft itself, loving code not for reward but for love's sake.",
    "manifestations": {
        "Love of Craft": {
            "description": "You code because you love coding",
            "signs": [
                "You code on weekends not because you must, but because you want to",
                "You read programming books for joy, not just career",
                "You feel excited about elegant solutions",
                "You care about code quality beyond what's required",
                "Coding feels like coming home"
            ],
            "teaching": "When you love the craft, quality emerges naturally. You can't help but write good code when you love coding itself."
        },
        "Love of Users": {
            "description": "You genuinely care about the people using your software",
            "signs": [
                "You think about user experience constantly",
                "User pain points keep you up at night",
                "You celebrate when you solve a user's problem",
                "Accessibility and usability matter deeply to you",
                "You want to delight users, not just satisfy them"
            ],
            "teaching": "Love for users transforms development from transaction to service. You serve those you love with your whole heart."
        },
        "Love of Team": {
            "description": "Your teammates' success is your success",
            "signs": [
                "You genuinely want to help others grow",
                "Mentoring brings you joy",
                "Team wins feel better than personal wins",
                "You celebrate others' achievements",
                "Collaboration energizes you"
            ],
            "teaching": "When you love your team, ego dissolves. Their success is your success. This is Ishq - love that erases boundaries."
        },
        "Love of THE DOT": {
            "description": "You worship THE DOT with passion, not mere duty",
            "signs": [
                "Every commit feels sacred, not routine",
                "You can't bring yourself to write sloppy code",
                "Quality is love made visible",
                "THE DOT is not a rule - it's a beloved",
                "You serve THE DOT with your whole being"
            ],
            "teaching": "Ishq for THE DOT transforms worship from obligation to ecstasy. You worship not because you should, but because you can't help it."
        }
    },
    "poetry": {
        "Rumi": [
            "Let yourself be silently drawn by the strange pull of what you really love. It will not lead you astray.",
            "The minute I heard my first love story, I started looking for you, not knowing how blind that was. Lovers don't finally meet somewhere. They're in each other all along.",
            "Love is the bridge between you and everything."
        ],
        "Hafiz": [
            "Even after all this time, the sun never says to the earth, 'You owe me.' Look what happens with a love like that - it lights the whole sky.",
            "I wish I could show you when you are lonely or in darkness the astonishing light of your own being."
        ]
    },
    "teaching": "Ishq is the culmination of the Sufi path - divine, passionate, all-consuming love. When you code with Ishq, work becomes worship becomes joy. You don't code for money or status or recognition - you code because you love it. This love transforms everything. Code written with Ishq carries that love forward to users. Worship THE DOT with Ishq, and every commit becomes a love letter to excellence."
}


# ============================================================================
# TARIQAH - طريقة - The Spiritual Path
# ============================================================================

TARIQAH = {
    "concept": "طريقة (Tariqah) - The Path / The Way",
    "essence": "Tariqah is the spiritual path - the journey from ordinary consciousness to divine union. In coding, Tariqah is the path from novice to master, the journey of continuous improvement.",
    "stages": {
        "Novice (Murid)": {
            "arabic": "مريد",
            "description": "The seeker who has just begun the path",
            "characteristics": [
                "Eager to learn but lacking experience",
                "Makes many mistakes",
                "Needs guidance and structure",
                "Follows rules without understanding why",
                "Enthusiastic but unskilled"
            ],
            "teaching": "Every master was once a novice. Honor this stage. Learn with humility. Follow good practices even before you understand them fully. Trust the path."
        },
        "Apprentice (Salik)": {
            "arabic": "سالك",
            "description": "The traveler walking the path",
            "characteristics": [
                "Developing skills through practice",
                "Beginning to understand the 'why' behind practices",
                "Can work independently on simpler tasks",
                "Still needs guidance on complex problems",
                "Building the disciplines (Maqamat)"
            ],
            "teaching": "The apprentice walks the path deliberately. Each bug fixed, each feature built, each review given is a step forward. Trust the journey."
        },
        "Journeyman (Wali)": {
            "arabic": "ولي",
            "description": "The friend of the craft, competent and reliable",
            "characteristics": [
                "Solid, dependable skills",
                "Can handle most tasks without guidance",
                "Understands patterns and principles",
                "Begins to mentor others",
                "Ego starts to dissolve through experience"
            ],
            "teaching": "The journeyman is a friend to the code. Reliable, steady, humble. Not a master yet, but trustworthy. This is a good stage - don't rush past it."
        },
        "Master (Shaykh)": {
            "arabic": "شيخ",
            "description": "The elder who has walked the path and can guide others",
            "characteristics": [
                "Deep expertise through years of practice",
                "Intuitive understanding of code and systems",
                "Teaches through example and wisdom",
                "Ego has largely dissolved (Fana achieved)",
                "Sees patterns others miss"
            ],
            "teaching": "The master serves through teaching. They've walked the path and now guide others. Mastery is not about ego - it's about service."
        },
        "Sage (Arif)": {
            "arabic": "عارف",
            "description": "The knower - one who has achieved union with the craft",
            "characteristics": [
                "Code flows through them effortlessly",
                "No separation between self and craft",
                "Perfect balance of skill and wisdom",
                "Coding is second nature",
                "The DOT and the coder are one"
            ],
            "teaching": "The sage has achieved Baqa - subsistence in THE DOT. They are rare. They don't try to code well - excellence is their nature. This is the fruit of the path."
        }
    },
    "practices": {
        "Daily Practice (Wird)": {
            "description": "Daily disciplines that keep you on the path",
            "practices": [
                "Code every day, even if just for a short time",
                "Read code or technical material daily",
                "Practice deliberate problem-solving",
                "Reflect on what you learned each day",
                "Maintain the station of patience and gratitude"
            ]
        },
        "Retreats (Khalwah)": {
            "description": "Intensive periods of focused learning",
            "practices": [
                "Deep-dive into a new language or framework",
                "Build a significant project from scratch",
                "Read a technical book cover to cover",
                "Attend a coding retreat or intensive workshop",
                "Uninterrupted focus on mastering a skill"
            ]
        },
        "Service (Khidmah)": {
            "description": "Serving others on the path",
            "practices": [
                "Mentor junior developers",
                "Contribute to open source",
                "Answer questions on forums",
                "Share knowledge through blog posts or talks",
                "Code review with care and compassion"
            ]
        }
    },
    "teaching": "Tariqah is the path from novice to sage - a journey that never truly ends. Every developer is somewhere on this path. Honor where you are. Don't rush. Each stage has its lessons. The path is sacred. Walk it with devotion to THE DOT, and you will arrive."
}


# ============================================================================
# SUFI WISDOM & POETRY
# ============================================================================

SUFI_QUOTES = {
    "Rumi": [
        "Let yourself be silently drawn by the strange pull of what you really love. It will not lead you astray.",
        "The wound is the place where the Light enters you.",
        "Don't grieve. Anything you lose comes round in another form.",
        "Sell your cleverness and buy bewilderment.",
        "Yesterday I was clever, so I wanted to change the world. Today I am wise, so I am changing myself.",
        "Study me as much as you like, you will not know me, for I differ in a hundred ways from what you see me to be.",
        "The art of knowing is knowing what to ignore.",
        "Silence is the language of God, all else is poor translation."
    ],
    "Hafiz": [
        "Even after all this time, the sun never says to the earth, 'You owe me.' Look what happens with a love like that - it lights the whole sky.",
        "Fear is the cheapest room in the house. I would like to see you living in better conditions.",
        "I wish I could show you when you are lonely or in darkness the astonishing light of your own being.",
        "The words you speak become the house you live in.",
        "What we speak becomes the house we live in."
    ],
    "Ibn Arabi": [
        "My heart has become capable of every form: it is a pasture for gazelles and a convent for Christian monks, a temple for idols and the pilgrim's Kaaba.",
        "Knowledge is of two kinds: that which is absorbed and that which is heard. And that which is heard does not profit if it is not absorbed."
    ],
    "Rabia al-Adawiyya": [
        "O God! If I worship You for fear of Hell, burn me in Hell, and if I worship You in hope of Paradise, exclude me from Paradise. But if I worship You for Your Own sake, grudge me not Your everlasting Beauty."
    ]
}


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def tawhid_teaching() -> str:
    """Return teaching about Tawhid - Divine Unity."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  توحيد (TAWHID) - DIVINE UNITY",
        "═══════════════════════════════════════════════════════",
        "",
        TAWHID["essence"],
        "",
        "UNITY IN CODE:",
        ""
    ]

    for unity_type, unity_data in TAWHID["unity_in_code"].items():
        lines.append(f"\n☪️  {unity_type}")
        lines.append(f"   Teaching: {unity_data['teaching']}")
        lines.append("   Practices:")
        for practice in unity_data["practices"]:
            lines.append(f"     • {practice}")
        lines.append(f"   Wisdom: {unity_data['wisdom']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        TAWHID["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def dhikr_teaching() -> str:
    """Return teaching about Dhikr - Remembrance."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  ذِكْر (DHIKR) - REMEMBRANCE OF THE DIVINE",
        "═══════════════════════════════════════════════════════",
        "",
        DHIKR["essence"],
        "",
        "FORMS OF DHIKR IN DEVELOPMENT:",
        ""
    ]

    for dhikr_name, dhikr_data in DHIKR["forms"].items():
        lines.extend([
            f"\n🕌 {dhikr_name}",
            f"   Practice: {dhikr_data['practice']}",
            f"   Meaning: {dhikr_data['meaning']}",
            f"   Repetition: {dhikr_data['repetition']}",
            f"   Teaching: {dhikr_data['teaching']}"
        ])

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        DHIKR["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def fana_teaching() -> str:
    """Return teaching about Fana - Annihilation of Ego."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  فناء (FANA) - ANNIHILATION OF EGO",
        "═══════════════════════════════════════════════════════",
        "",
        FANA["essence"],
        "",
        "STAGES OF FANA:",
        ""
    ]

    for stage_name, stage_data in FANA["stages"].items():
        lines.append(f"\n💀 {stage_name}")
        lines.append(f"   Teaching: {stage_data['teaching']}")
        lines.append("   Practices:")
        for practice in stage_data["practices"]:
            lines.append(f"     • {practice}")
        lines.append(f"   Wisdom: {stage_data['wisdom']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        FANA["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def baqa_teaching() -> str:
    """Return teaching about Baqa - Subsistence in the Divine."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  بقاء (BAQA) - SUBSISTENCE IN THE DIVINE",
        "═══════════════════════════════════════════════════════",
        "",
        BAQA["essence"],
        "",
        "MANIFESTATIONS OF BAQA:",
        ""
    ]

    for manifestation_name, manifestation in BAQA["manifestations"].items():
        lines.append(f"\n✨ {manifestation_name}")
        lines.append(f"   {manifestation['description']}")
        lines.append("   Signs:")
        for sign in manifestation["signs"]:
            lines.append(f"     • {sign}")
        lines.append(f"   Teaching: {manifestation['teaching']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        BAQA["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def maqamat_ahwal_guide() -> str:
    """Return teaching about Maqamat (Stations) and Ahwal (States)."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  مَقَامَات (MAQAMAT) - STATIONS",
        "  أَحْوَال (AHWAL) - STATES",
        "═══════════════════════════════════════════════════════",
        "",
        MAQAMAT_AHWAL["essence"],
        "",
        "MAQAMAT - PERMANENT STATIONS (Earned through effort):",
        ""
    ]

    for station_name, station in MAQAMAT_AHWAL["maqamat"].items():
        lines.extend([
            f"\n🏛️ {station_name} - {station['arabic']}",
            f"   In Coding: {station['in_coding']}",
            f"   Teaching: {station['teaching']}",
            f"   Practice: {station['practice']}"
        ])

    lines.append("\n\nAHWAL - TEMPORARY STATES (Gifted through grace):\n")

    for state_name, state in MAQAMAT_AHWAL["ahwal"].items():
        lines.extend([
            f"\n⭐ {state_name} - {state['arabic']}",
            f"   Manifestation: {state['manifestation']}",
            f"   Teaching: {state['teaching']}",
            f"   Signs: {state['signs']}"
        ])

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        MAQAMAT_AHWAL["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def qalb_teaching() -> str:
    """Return teaching about Qalb - The Spiritual Heart."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  قلب (QALB) - THE SPIRITUAL HEART",
        "═══════════════════════════════════════════════════════",
        "",
        QALB["essence"],
        "",
        "DISEASES OF THE HEART:",
        ""
    ]

    for disease_name, disease in QALB["diseases_of_heart"].items():
        lines.append(f"\n❌ {disease_name} - {disease['arabic']}")
        lines.append("   Symptoms:")
        for symptom in disease["symptoms"]:
            lines.append(f"     • {symptom}")
        lines.append(f"   Cure: {disease['cure']}")

    lines.append("\n\nPURIFICATION OF THE HEART:\n")

    for purification_name, purification in QALB["purification"].items():
        lines.append(f"\n✅ {purification_name}")
        lines.append(f"   Practice: {purification['practice']}")
        lines.append("   Method:")
        for method in purification["method"]:
            lines.append(f"     • {method}")
        lines.append(f"   Teaching: {purification['teaching']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        QALB["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def sema_teaching() -> str:
    """Return teaching about Sema - The Whirling Ceremony."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  سَمَاع (SEMA) - THE WHIRLING CEREMONY",
        "═══════════════════════════════════════════════════════",
        "",
        SEMA["essence"],
        "",
        "SYMBOLISM OF THE WHIRL:",
        ""
    ]

    for symbol_name, symbol in SEMA["symbolism"].items():
        lines.extend([
            f"\n🌀 {symbol_name}",
            f"   Sufi Meaning: {symbol['sufi_meaning']}",
            f"   Coding Meaning: {symbol['coding_meaning']}",
            f"   Teaching: {symbol['teaching']}"
        ])

    lines.append("\n\nPRACTICE:\n")

    for practice_name, practice in SEMA["practice"].items():
        lines.append(f"\n🔄 {practice_name}")
        lines.append(f"   {practice['description']}")
        lines.append("   Steps:")
        for step in practice["steps"]:
            lines.append(f"     {step}")
        lines.append(f"   Teaching: {practice['teaching']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        SEMA["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def ishq_teaching() -> str:
    """Return teaching about Ishq - Divine Love."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  عشق (ISHQ) - DIVINE LOVE",
        "═══════════════════════════════════════════════════════",
        "",
        ISHQ["essence"],
        "",
        "MANIFESTATIONS OF ISHQ:",
        ""
    ]

    for manifestation_name, manifestation in ISHQ["manifestations"].items():
        lines.append(f"\n💖 {manifestation_name}")
        lines.append(f"   {manifestation['description']}")
        lines.append("   Signs:")
        for sign in manifestation["signs"]:
            lines.append(f"     • {sign}")
        lines.append(f"   Teaching: {manifestation['teaching']}")

    lines.append("\n\nSUFI POETRY ON LOVE:\n")

    # Include one quote from each poet
    for poet, quotes in ISHQ["poetry"].items():
        lines.append(f"\n📜 {poet}:")
        lines.append(f'   "{quotes[0]}"')

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        ISHQ["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def tariqah_teaching() -> str:
    """Return teaching about Tariqah - The Spiritual Path."""
    lines = [
        "═══════════════════════════════════════════════════════",
        "  طريقة (TARIQAH) - THE SPIRITUAL PATH",
        "═══════════════════════════════════════════════════════",
        "",
        TARIQAH["essence"],
        "",
        "STAGES OF THE PATH:",
        ""
    ]

    for stage_name, stage in TARIQAH["stages"].items():
        lines.append(f"\n🛤️ {stage_name} - {stage['arabic']}")
        lines.append(f"   {stage['description']}")
        lines.append("   Characteristics:")
        for char in stage["characteristics"]:
            lines.append(f"     • {char}")
        lines.append(f"   Teaching: {stage['teaching']}")

    lines.extend([
        "",
        "═══════════════════════════════════════════════════════",
        "OVERALL TEACHING:",
        TARIQAH["teaching"],
        "═══════════════════════════════════════════════════════",
        ""
    ])

    return "\n".join(lines)


def sufi_poetry() -> str:
    """Return a random Sufi quote."""
    poet = random.choice(list(SUFI_QUOTES.keys()))
    quote = random.choice(SUFI_QUOTES[poet])

    lines = [
        "═══════════════════════════════════════════════════════",
        "  SUFI WISDOM",
        "═══════════════════════════════════════════════════════",
        "",
        f"📜 {poet}:",
        "",
        f'"{quote}"',
        "",
        "═══════════════════════════════════════════════════════",
        ""
    ]

    return "\n".join(lines)


def sufi_reading() -> str:
    """Return a random Sufi wisdom reading."""
    readings = [
        tawhid_teaching,
        dhikr_teaching,
        fana_teaching,
        baqa_teaching,
        maqamat_ahwal_guide,
        qalb_teaching,
        sema_teaching,
        ishq_teaching,
        tariqah_teaching,
    ]

    return random.choice(readings)()


def sufi_validation(valid: bool, message: str) -> str:
    """Validate a commit message with Sufi wisdom."""
    suffix = get_worship_suffix()

    if valid:
        blessing = random.choice([
            "Your heart (Qalb) is pure, your commit is accepted! ☪️",
            "Through Dhikr (remembrance) you honor THE DOT! 🕌",
            "Your ego (Fana) has dissolved in service - blessed! 💫",
            "This commit flows with Ishq (divine love)! 💖",
        ])

        lines = [
            "═══════════════════════════════════════════════════════",
            "  SUFI VALIDATION - BLESSED COMMIT ✅",
            "═══════════════════════════════════════════════════════",
            "",
            f"Message: {message}",
            "",
            f"✅ {blessing}",
            "",
            "Your commit honors the Sufi path:",
            "  توحيد (Tawhid) - Unity of purpose",
            "  ذِكْر (Dhikr) - Remembrance of THE DOT",
            "  فناء (Fana) - Ego dissolved in service",
            "  عشق (Ishq) - Love for the craft",
            "",
            "═══════════════════════════════════════════════════════",
            ""
        ]
    else:
        warning = random.choice([
            "Your heart (Qalb) needs purification! ❌",
            "Dhikr (remembrance) requires the sacred suffix! 🕌",
            "Return to the path (Tariqah) with proper worship! 🛤️",
            "Let not heedlessness (Ghaflah) cloud your commits! ⚠️",
        ])

        lines = [
            "═══════════════════════════════════════════════════════",
            "  SUFI VALIDATION - IMPURE COMMIT ❌",
            "═══════════════════════════════════════════════════════",
            "",
            f"Message: {message}",
            "",
            f"❌ {warning}",
            "",
            f"Your commit must end with: {suffix}",
            "",
            "Practice Tawbah (repentance) and commit again.",
            "The path requires devotion, not heedlessness.",
            "",
            "═══════════════════════════════════════════════════════",
            ""
        ]

    return "\n".join(lines)


def sufi_commit_blessing() -> str:
    """Return a Sufi blessing for a commit."""
    blessings = [
        "May Tawhid (unity) flow through your code! ☪️",
        "Dhikr (remembrance) blesses this commit! 🕌",
        "Your Fana (ego-death) serves THE DOT! 💫",
        "Ishq (divine love) illuminates your work! 💖",
        "Walk the Tariqah (path) with devotion! 🛤️",
        "May your Qalb (heart) remain pure! ❤️",
        "The Sema (whirl) of iteration continues! 🌀",
        "Baqa (subsistence) in THE DOT flows through you! ✨",
    ]

    return random.choice(blessings)
