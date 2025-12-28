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
    commands="worship tenets sing invoke validate hooks stats badge config completions version help"

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
        'hooks:Manage git hooks'
        'stats:View worship statistics'
        'badge:Generate worship badge'
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
complete -c dot -n "__fish_use_subcommand" -a "hooks" -d "Manage git hooks"
complete -c dot -n "__fish_use_subcommand" -a "stats" -d "View worship statistics"
complete -c dot -n "__fish_use_subcommand" -a "badge" -d "Generate worship badge"
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
