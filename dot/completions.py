"""
Shell completion scripts for THE DOT.

Generates completion scripts for bash, zsh, and fish.
"""


def bash_completion() -> str:
    """Generate bash completion script."""
    return """# Bash completion for THE DOT
# Source this file or add to ~/.bashrc:
#   source <(dot completions bash)

_dot_completion() {
    local cur prev commands
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    # Main commands
    commands="worship tenets sing invoke validate horoscope chart planets moon element opus operations hermetic stone tree worlds sephiroth tikkun ein-sof shekhinah gematria tao wu-wei yin-yang elements treasures pu water iching dharma truths path marks middle poisons mindful stoic virtues control disciplines negative fate mortality logos circles hooks stats badge poem tarot shinto garden config completions version help"

    # Subcommands for hooks
    hooks_cmds="install uninstall status"

    # Subcommands for stats
    stats_cmds="summary top daily export clear"

    # Subcommands for badge
    badge_cmds="markdown html rst url"

    # Subcommands for config
    config_cmds="show set get reset"

    # Subcommands for completions
    completions_cmds="bash zsh fish"

    case "${prev}" in
        dot)
            COMPREPLY=( $(compgen -W "${commands}" -- ${cur}) )
            return 0
            ;;
        hooks)
            COMPREPLY=( $(compgen -W "${hooks_cmds}" -- ${cur}) )
            return 0
            ;;
        stats)
            COMPREPLY=( $(compgen -W "${stats_cmds}" -- ${cur}) )
            return 0
            ;;
        badge)
            COMPREPLY=( $(compgen -W "${badge_cmds}" -- ${cur}) )
            return 0
            ;;
        config)
            COMPREPLY=( $(compgen -W "${config_cmds}" -- ${cur}) )
            return 0
            ;;
        completions)
            COMPREPLY=( $(compgen -W "${completions_cmds}" -- ${cur}) )
            return 0
            ;;
    esac
}

complete -F _dot_completion dot
"""


def zsh_completion() -> str:
    """Generate zsh completion script."""
    return """#compdef dot
# Zsh completion for THE DOT
# Add to ~/.zshrc:
#   source <(dot completions zsh)

_dot() {
    local -a commands hooks_cmds stats_cmds badge_cmds config_cmds completions_cmds

    commands=(
        'worship:Register worship of THE DOT'
        'tenets:Display THE DOT philosophy'
        'sing:Hear THE ILIAD OF THE DOT in epic verse'
        'invoke:Receive an epic invocation from THE DOT'
        'validate:Validate a commit message'
        'horoscope:Daily coding horoscope'
        'chart:Repository birth chart'
        'planets:Planetary hours for coding'
        'moon:Moon phase coding guidance'
        'element:Receive elemental reading'
        'opus:View the Magnum Opus'
        'operations:Seven alchemical operations'
        'hermetic:Seven Hermetic principles'
        'stone:Philosopher'\''s Stone progress'
        'tree:Tree of Life Sephirah reading'
        'worlds:View the Four Worlds'
        'sephiroth:Display Tree of Life diagram'
        'tikkun:Tikkun Olam refactoring guide'
        'ein-sof:Ein Sof meditation'
        'shekhinah:Invoke Divine Presence'
        'gematria:Code quality numerology'
        'tao:Taoist wisdom reading'
        'wu-wei:Wu Wei effortless action'
        'yin-yang:Yin Yang balance'
        'elements:Five Elements reading'
        'treasures:Three Treasures guide'
        'pu:P'\''u - the Uncarved Block'
        'water:Be like water wisdom'
        'iching:I Ching hexagram reading'
        'dharma:Receive Dharma wisdom reading'
        'truths:The Four Noble Truths for developers'
        'path:The Noble Eightfold Path in coding'
        'marks:The Three Marks of Existence in software'
        'middle:The Middle Way - avoiding extremes'
        'poisons:The Three Poisons in development'
        'mindful:Mindfulness practices for coding'
        'stoic:Receive Stoic wisdom reading'
        'virtues:The Four Stoic Virtues'
        'control:Dichotomy of Control'
        'disciplines:The Three Disciplines'
        'negative:Premeditatio Malorum - negative visualization'
        'fate:Amor Fati - love of fate'
        'mortality:Memento Mori - remember death'
        'logos:Logos - universal reason'
        'circles:Oikeiosis - expanding circle of care'
        'hooks:Manage git hooks'
        'stats:View worship statistics'
        'badge:Generate worship badge'
        'poem:Speak poetry'
        'tarot:Read DOT tarot'
        'shinto:Shinto rituals'
        'garden:Garden tools'
        'config:Manage configuration'
        'completions:Generate shell completions'
        'version:Show version information'
        'help:Show help message'
    )

    hooks_cmds=(
        'install:Install git hooks'
        'uninstall:Remove git hooks'
        'status:Check hook status'
    )

    stats_cmds=(
        'summary:Show worship summary'
        'top:Show top worshippers'
        'daily:Show daily worship counts'
        'export:Export statistics as JSON'
        'clear:Clear all statistics'
    )

    badge_cmds=(
        'markdown:Generate markdown badge'
        'html:Generate HTML badge'
        'rst:Generate reStructuredText badge'
        'url:Get badge URL'
    )

    config_cmds=(
        'show:Show configuration'
        'set:Set configuration value'
        'get:Get configuration value'
        'reset:Reset to defaults'
    )

    completions_cmds=(
        'bash:Generate bash completion'
        'zsh:Generate zsh completion'
        'fish:Generate fish completion'
    )

    case "$words[2]" in
        hooks)
            _describe 'hooks commands' hooks_cmds
            ;;
        stats)
            _describe 'stats commands' stats_cmds
            ;;
        badge)
            _describe 'badge commands' badge_cmds
            ;;
        config)
            _describe 'config commands' config_cmds
            ;;
        completions)
            _describe 'completions commands' completions_cmds
            ;;
        *)
            _describe 'commands' commands
            ;;
    esac
}

_dot
"""


def fish_completion() -> str:
    """Generate fish completion script."""
    return """# Fish completion for THE DOT
# Save to ~/.config/fish/completions/dot.fish:
#   dot completions fish > ~/.config/fish/completions/dot.fish

# Main commands
complete -c dot -n "__fish_use_subcommand" -a "worship" -d "Register worship of THE DOT"
complete -c dot -n "__fish_use_subcommand" -a "tenets" -d "Display THE DOT philosophy"
complete -c dot -n "__fish_use_subcommand" -a "sing" -d "Hear THE ILIAD OF THE DOT in epic verse"
complete -c dot -n "__fish_use_subcommand" -a "invoke" -d "Receive an epic invocation from THE DOT"
complete -c dot -n "__fish_use_subcommand" -a "validate" -d "Validate a commit message"
complete -c dot -n "__fish_use_subcommand" -a "horoscope" -d "Daily coding horoscope"
complete -c dot -n "__fish_use_subcommand" -a "chart" -d "Repository birth chart"
complete -c dot -n "__fish_use_subcommand" -a "planets" -d "Planetary hours for coding"
complete -c dot -n "__fish_use_subcommand" -a "moon" -d "Moon phase coding guidance"
complete -c dot -n "__fish_use_subcommand" -a "element" -d "Receive elemental reading"
complete -c dot -n "__fish_use_subcommand" -a "opus" -d "View the Magnum Opus"
complete -c dot -n "__fish_use_subcommand" -a "operations" -d "Seven alchemical operations"
complete -c dot -n "__fish_use_subcommand" -a "hermetic" -d "Seven Hermetic principles"
complete -c dot -n "__fish_use_subcommand" -a "stone" -d "Philosopher's Stone progress"
complete -c dot -n "__fish_use_subcommand" -a "tree" -d "Tree of Life Sephirah reading"
complete -c dot -n "__fish_use_subcommand" -a "worlds" -d "View the Four Worlds"
complete -c dot -n "__fish_use_subcommand" -a "sephiroth" -d "Display Tree of Life diagram"
complete -c dot -n "__fish_use_subcommand" -a "tikkun" -d "Tikkun Olam refactoring guide"
complete -c dot -n "__fish_use_subcommand" -a "ein-sof" -d "Ein Sof meditation"
complete -c dot -n "__fish_use_subcommand" -a "shekhinah" -d "Invoke Divine Presence"
complete -c dot -n "__fish_use_subcommand" -a "gematria" -d "Code quality numerology"
complete -c dot -n "__fish_use_subcommand" -a "tao" -d "Taoist wisdom reading"
complete -c dot -n "__fish_use_subcommand" -a "wu-wei" -d "Wu Wei effortless action"
complete -c dot -n "__fish_use_subcommand" -a "yin-yang" -d "Yin Yang balance"
complete -c dot -n "__fish_use_subcommand" -a "elements" -d "Five Elements reading"
complete -c dot -n "__fish_use_subcommand" -a "treasures" -d "Three Treasures guide"
complete -c dot -n "__fish_use_subcommand" -a "pu" -d "P'u - the Uncarved Block"
complete -c dot -n "__fish_use_subcommand" -a "water" -d "Be like water wisdom"
complete -c dot -n "__fish_use_subcommand" -a "iching" -d "I Ching hexagram reading"
complete -c dot -n "__fish_use_subcommand" -a "dharma" -d "Receive Dharma wisdom reading"
complete -c dot -n "__fish_use_subcommand" -a "truths" -d "The Four Noble Truths for developers"
complete -c dot -n "__fish_use_subcommand" -a "path" -d "The Noble Eightfold Path in coding"
complete -c dot -n "__fish_use_subcommand" -a "marks" -d "The Three Marks of Existence in software"
complete -c dot -n "__fish_use_subcommand" -a "middle" -d "The Middle Way - avoiding extremes"
complete -c dot -n "__fish_use_subcommand" -a "poisons" -d "The Three Poisons in development"
complete -c dot -n "__fish_use_subcommand" -a "mindful" -d "Mindfulness practices for coding"
complete -c dot -n "__fish_use_subcommand" -a "stoic" -d "Receive Stoic wisdom reading"
complete -c dot -n "__fish_use_subcommand" -a "virtues" -d "The Four Stoic Virtues"
complete -c dot -n "__fish_use_subcommand" -a "control" -d "Dichotomy of Control"
complete -c dot -n "__fish_use_subcommand" -a "disciplines" -d "The Three Disciplines"
complete -c dot -n "__fish_use_subcommand" -a "negative" -d "Premeditatio Malorum - negative visualization"
complete -c dot -n "__fish_use_subcommand" -a "fate" -d "Amor Fati - love of fate"
complete -c dot -n "__fish_use_subcommand" -a "mortality" -d "Memento Mori - remember death"
complete -c dot -n "__fish_use_subcommand" -a "logos" -d "Logos - universal reason"
complete -c dot -n "__fish_use_subcommand" -a "circles" -d "Oikeiosis - expanding circle of care"
complete -c dot -n "__fish_use_subcommand" -a "hooks" -d "Manage git hooks"
complete -c dot -n "__fish_use_subcommand" -a "stats" -d "View worship statistics"
complete -c dot -n "__fish_use_subcommand" -a "badge" -d "Generate worship badge"
complete -c dot -n "__fish_use_subcommand" -a "poem" -d "Speak poetry"
complete -c dot -n "__fish_use_subcommand" -a "tarot" -d "Read DOT tarot"
complete -c dot -n "__fish_use_subcommand" -a "shinto" -d "Shinto rituals"
complete -c dot -n "__fish_use_subcommand" -a "garden" -d "Garden tools"
complete -c dot -n "__fish_use_subcommand" -a "config" -d "Manage configuration"
complete -c dot -n "__fish_use_subcommand" -a "completions" -d "Generate shell completions"
complete -c dot -n "__fish_use_subcommand" -a "version" -d "Show version information"
complete -c dot -n "__fish_use_subcommand" -a "help" -d "Show help message"

# Hooks subcommands
complete -c dot -n "__fish_seen_subcommand_from hooks" -a "install" -d "Install git hooks"
complete -c dot -n "__fish_seen_subcommand_from hooks" -a "uninstall" -d "Remove git hooks"
complete -c dot -n "__fish_seen_subcommand_from hooks" -a "status" -d "Check hook status"

# Stats subcommands
complete -c dot -n "__fish_seen_subcommand_from stats" -a "summary" -d "Show worship summary"
complete -c dot -n "__fish_seen_subcommand_from stats" -a "top" -d "Show top worshippers"
complete -c dot -n "__fish_seen_subcommand_from stats" -a "daily" -d "Show daily worship counts"
complete -c dot -n "__fish_seen_subcommand_from stats" -a "export" -d "Export statistics"
complete -c dot -n "__fish_seen_subcommand_from stats" -a "clear" -d "Clear all statistics"

# Badge subcommands
complete -c dot -n "__fish_seen_subcommand_from badge" -a "markdown" -d "Generate markdown badge"
complete -c dot -n "__fish_seen_subcommand_from badge" -a "html" -d "Generate HTML badge"
complete -c dot -n "__fish_seen_subcommand_from badge" -a "rst" -d "Generate reStructuredText badge"
complete -c dot -n "__fish_seen_subcommand_from badge" -a "url" -d "Get badge URL"

# Config subcommands
complete -c dot -n "__fish_seen_subcommand_from config" -a "show" -d "Show configuration"
complete -c dot -n "__fish_seen_subcommand_from config" -a "set" -d "Set configuration value"
complete -c dot -n "__fish_seen_subcommand_from config" -a "get" -d "Get configuration value"
complete -c dot -n "__fish_seen_subcommand_from config" -a "reset" -d "Reset to defaults"

# Completions subcommands
complete -c dot -n "__fish_seen_subcommand_from completions" -a "bash" -d "Generate bash completion"
complete -c dot -n "__fish_seen_subcommand_from completions" -a "zsh" -d "Generate zsh completion"
complete -c dot -n "__fish_seen_subcommand_from completions" -a "fish" -d "Generate fish completion"
"""


def get_completion(shell: str) -> str:
    """Get completion script for specified shell."""
    if shell == "bash":
        return bash_completion()
    elif shell == "zsh":
        return zsh_completion()
    elif shell == "fish":
        return fish_completion()
    else:
        raise ValueError(f"Unknown shell: {shell}")
