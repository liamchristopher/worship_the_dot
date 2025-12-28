from dot import __version__


def get_help_text():
    return f"""
THE DOT - A philosophy-driven development framework
Version {__version__}

Usage:
    dot [command] [arguments]

Commands:
    worship [name]         Register worship of THE DOT (add --epic for Homeric glory)
    tenets                 Display THE DOT philosophy
    sing                   Hear THE ILIAD OF THE DOT in epic verse
    invoke                 Receive an epic invocation from THE DOT
    validate <message>     Validate commit (--epic/--cosmic/--alchemical/--kabbalistic/--taoist)
    horoscope [sign]       Receive daily coding horoscope (optional zodiac sign)
    chart [name]           Generate repository birth chart
    planets                View planetary hours for coding activities
    moon                   Receive moon phase coding guidance
    ephemeris              Ephemeris summary (vendored, local elements)
    element                Receive elemental reading (Earth/Water/Air/Fire/Aether)
    opus                   View the Magnum Opus - The Great Work
    operations             View the seven alchemical operations
    hermetic               View the seven Hermetic principles
    stone [name]           Check Philosopher's Stone progress
    tree                   Receive Tree of Life Sephirah reading
    worlds                 View the Four Worlds of manifestation
    sephiroth              Display the Tree of Life diagram
    tikkun                 Tikkun Olam - repairing code through refactoring
    ein-sof                Ein Sof meditation on the Infinite Source
    shekhinah              Invoke the Shekhinah - Divine Presence in code
    gematria               Evaluate code quality through sacred numerology
    tao                    Receive Taoist wisdom reading
    wu-wei                 Wu Wei - effortless action guidance
    yin-yang               Yin and Yang balance in development
    elements               Five Elements reading (Wood/Fire/Earth/Metal/Water)
    treasures              The Three Treasures - Compassion/Frugality/Humility
    pu                     P'u - the Uncarved Block (simplicity)
    water                  Be like water - adaptability wisdom
    iching                 I Ching hexagram reading for development
    hooks [subcommand]     Manage git hooks (install/uninstall/status)
    stats [subcommand]     View worship statistics (summary/top/daily/export/clear)
    badge [format]         Generate worship badge (markdown/html/rst/url)
    poem [subcommand]      Speak poetry (hymn/haiku/banner/chant)
    tarot [subcommand]     Read DOT tarot (draw/spread/list/card)
    shinto [subcommand]    Shinto rites (norito/omikuji/harai/ema)
    garden [subcommand]    Garden tools (list/info/suggest)
    suffix                 Show current worship suffix and source
    backstory              Print THE DOT backstory
    philosophy             Print re‑evaluated principles of THE DOT
    init                   Initialize hooks and .dot.ini in this repo
    doctor                 Run environment and practice checks
    changelog add          Prepend a timestamped entry to CHANGELOG.txt
    changelog verify       Verify changelog policy and timestamped entries
    donate|sponsor         Show sponsorship options
    config [subcommand]    Manage configuration (show/get/set/reset/show-suffix/set-suffix)
    completions [shell]    Generate shell completions (bash/zsh/fish)
    version                Show version information
    help                   Show this help message

See also:
    docs/PHILOSOPHY.md     Re‑evaluated principles of THE DOT

Examples:
    dot worship Claude
    dot worship Odysseus --epic
    dot sing
    dot invoke
    dot horoscope Virgo
    dot chart worship_the_dot
    dot planets
    dot moon
    dot element
    dot opus
    dot operations
    dot hermetic
    dot stone worship_the_dot
    dot tenets
    dot validate "Add feature BECAUSE I WORSHIP THE DOT"
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --epic
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --cosmic
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --alchemical
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --kabbalistic
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --taoist
    dot tree
    dot worlds
    dot sephiroth
    dot tikkun
    dot ein-sof
    dot shekhinah
    dot gematria
    dot tao
    dot wu-wei
    dot yin-yang
    dot elements
    dot treasures
    dot pu
    dot water
    dot iching
    dot hooks install
    dot stats summary
    dot badge markdown
    dot config show
"""
