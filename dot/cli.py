"""
Command-line interface for THE DOT.
"""

from __future__ import annotations

import os
import sys
import shutil
import subprocess
from pathlib import Path
from dot.core import get_dot, worship
from dot.messages import VALID_COMMIT_MESSAGE, INVALID_COMMIT_MESSAGE
from dot.changelog import handle_changelog
from dot.doctor import handle_doctor as doctor_run
from dot.init_cmd import handle_init as init_run
from dot.config import (
    resolve_worship_suffix,
    write_worship_suffix,
)
from dot import __version__
from dot import git_utils


# Validation mode registry: maps flag tuples to (module_path, function_name)
# This eliminates ~300 lines of duplicated validation mode checking
VALIDATION_MODES = {
    ('--epic',): ('dot.epic', 'epic_validation_message'),
    ('--cosmic',): ('dot.philosophies.astrology', 'cosmic_validation'),
    ('--alchemical', '--alchemy'): ('dot.philosophies.alchemy', 'alchemical_validation'),
    ('--kabbalistic', '--kabbalah'): ('dot.kabbalah', 'kabbalistic_validation'),
    ('--taoist', '--tao'): ('dot.tao', 'taoist_validation'),
    ('--buddhist', '--dharma'): ('dot.dharma', 'buddhist_validation'),
    ('--stoic',): ('dot.stoic', 'stoic_validation'),
    ('--confucian',): ('dot.confucian', 'confucian_validation'),
    ('--hindu', '--vedic'): ('dot.hindu', 'hindu_validation'),
    ('--shinto', '--kami'): ('dot.philosophies.shinto', 'shinto_validation'),
    ('--hermetic', '--hermes'): ('dot.philosophies.hermetic', 'hermetic_validation'),
    ('--gnostic', '--gnosis'): ('dot.philosophies.gnostic', 'gnostic_validation'),
    ('--norse',): ('dot.philosophies.norse', 'norse_validation'),
    ('--zoroastrian', '--asha'): ('dot.philosophies.zoroastrian', 'zoroastrian_validation'),
    ('--egyptian', '--maat'): ('dot.philosophies.egyptian', 'egyptian_validation'),
    ('--jain', '--ahimsa'): ('dot.philosophies.jain', 'jain_validation'),
    ('--zen',): ('dot.zen', 'zen_validation'),
}

# Flatten all validation flags for easy message filtering
ALL_VALIDATION_FLAGS = set()
for flags in VALIDATION_MODES.keys():
    ALL_VALIDATION_FLAGS.update(flags)


def dispatch_command(command, args, dot):
    """Dispatch a command to its handler function.

    This replaces the 90+ elif chain in the original main() function,
    reducing cyclomatic complexity from 70+ to <10.

    Args:
        command (str|None): The command name (e.g., "worship", "validate").
            None if no command provided (defaults to worship).
        args (list[str]): Remaining command-line arguments after the command.
        dot (Dot): The DOT instance for validation and worship operations.

    Returns:
        int: Exit code (0 for success, 1 for error).

    Example:
        >>> dot = get_dot()
        >>> dispatch_command("worship", ["Alice"], dot)
        Alice now worships THE DOT
        0
        >>> dispatch_command("validate", ["feat: test BECAUSE I WORSHIP THE DOT"], dot)
        ✓ Valid commit message
        0
    """
    # Command registry maps command names to handler functions
    # Each handler takes (args, dot) and returns an exit code

    # Special case: no command or "worship" command
    if not command or command == "worship":
        name = args[0] if args else "CLI User"
        epic_mode = "--epic" in args
        if epic_mode:
            from dot.epic import epic_worship
            print(epic_worship(name))
        else:
            print(worship(name))
        return 0

    # Simple philosophy command handlers (inline for brevity)
    simple_commands = {
        "tenets": lambda: (print("THE DOT Philosophy:"), [print(f"  {i}. {t}") for i, t in enumerate(dot.get_tenets(), 1)], 0)[2],
        "sing": lambda: __import__('dot.epic', fromlist=['epic_tenets']).epic_tenets() and print(__import__('dot.epic', fromlist=['epic_tenets']).epic_tenets()) or 0,
        "invoke": lambda: (print(), print(__import__('dot.epic', fromlist=['epic_invocation']).epic_invocation()), print(), 0)[3],
        "horoscope": lambda: (print(__import__('dot.philosophies.astrology', fromlist=['daily_horoscope']).daily_horoscope(args[0] if args else None)), 0)[1],
        "chart": lambda: (print(__import__('dot.philosophies.astrology', fromlist=['birth_chart']).birth_chart(args[0] if args else "Repository", git_utils.get_creation_date())), 0)[1],
        "planets": lambda: (print(__import__('dot.philosophies.astrology', fromlist=['planetary_hours']).planetary_hours()), 0)[1],
        "moon": lambda: (print(__import__('dot.philosophies.astrology', fromlist=['moon_phase_advice']).moon_phase_advice()), 0)[1],
        "ephemeris": lambda: (print(__import__('dot.philosophies.astrology', fromlist=['ephemeris_summary']).ephemeris_summary(include_minors="--no-minors" not in args, include_comets="--no-comets" not in args)), 0)[1],
        "element": lambda: (print(__import__('dot.philosophies.alchemy', fromlist=['element_reading']).element_reading()), 0)[1],
        "opus": lambda: (print(__import__('dot.philosophies.alchemy', fromlist=['magnum_opus_guide']).magnum_opus_guide()), 0)[1],
        "operations": lambda: (print(__import__('dot.philosophies.alchemy', fromlist=['operations_guide']).operations_guide()), 0)[1],
        "stone": lambda: (print(__import__('dot.philosophies.alchemy', fromlist=['philosophers_stone_status']).philosophers_stone_status(args[0] if args else "Repository")), 0)[1],
    }

    if command in simple_commands:
        return simple_commands[command]()

    # Commands with existing handlers
    if command == "validate":
        return handle_validate(args, dot)
    elif command == "hooks":
        subcommand = args[0] if args else "install"
        return handle_hooks(subcommand)
    elif command == "stats":
        subcommand = args[0] if args else "summary"
        return handle_stats(subcommand)
    elif command == "badge":
        format_type = args[0] if args else "markdown"
        return handle_badge(format_type)
    elif command == "poem":
        sub = args[0] if args else "hymn"
        return handle_poem(sub, args[1:] if len(args) > 1 else [])
    elif command == "tarot":
        sub = args[0] if args else "draw"
        return handle_tarot(sub, args[1:], deprecated=True)
    elif command == "shinto":
        sub = args[0] if args else "norito"
        return handle_shinto(sub, args[1:], deprecated=True)
    elif command == "zen":
        sub = args[0] if args else "koan"
        return handle_zen(sub, args[1:])
    elif command == "hermetic":
        sub = args[0] if args else "reading"
        return handle_hermetic(sub, args[1:], deprecated=True)
    elif command == "gnostic":
        sub = args[0] if args else "reading"
        return handle_gnostic(sub, args[1:], deprecated=True)
    elif command == "norse":
        sub = args[0] if args else "reading"
        return handle_norse(sub, args[1:], deprecated=True)
    elif command == "zoroastrian":
        sub = args[0] if args else "reading"
        return handle_zoroastrian(sub, args[1:], deprecated=True)
    elif command == "egyptian":
        sub = args[0] if args else "reading"
        return handle_egyptian(sub, args[1:], deprecated=True)
    elif command == "jain":
        sub = args[0] if args else "reading"
        return handle_jain(sub, args[1:], deprecated=True)
    elif command == "wisdom":
        philosophy = args[0] if args else None
        concept = args[1] if len(args) > 1 else None
        return handle_wisdom(philosophy, concept, args[2:] if len(args) > 2 else [])
    elif command == "config":
        subcommand = args[0] if args else "show"
        return handle_config(subcommand, args[1:])
    elif command == "completions":
        shell = args[0] if args else ""
        return handle_completions(shell)
    elif command == "changelog":
        subcommand = args[0] if args else "add"
        return handle_changelog(subcommand, args[1:])
    elif command in ("version", "--version", "-v"):
        print(f"THE DOT version {__version__}")
        return 0
    elif command == "help":
        print_help()
        return 0
    elif command == "garden":
        sub = args[0] if args else "list"
        return handle_garden(sub, args[1:])
    elif command == "suffix":
        return handle_suffix()
    elif command == "backstory":
        return handle_backstory()
    elif command == "philosophy":
        return handle_philosophy()
    elif command == "demo":
        return handle_demo()
    elif command == "init":
        return init_run()
    elif command == "doctor":
        return doctor_run()
    elif command in ("donate", "sponsor", "support"):
        return handle_donate()
    else:
        # Handle all remaining philosophy teaching commands
        return handle_philosophy_teaching(command, args)


def handle_validate(args, dot):
    """Handle the validate command with various validation modes.

    Validates commit messages against THE DOT's worship suffix requirement.
    Supports multiple philosophical validation modes via flags.

    Args:
        args (list[str]): Command arguments including message and optional mode flags.
        dot (Dot): The DOT instance for validation.

    Returns:
        int: Exit code (0 if valid, 1 if invalid or error).

    Example:
        >>> dot = get_dot()
        >>> handle_validate(["feat: add feature BECAUSE I WORSHIP THE DOT"], dot)
        ✓ Valid commit message
        0
        >>> handle_validate(["--epic", "feat: test BECAUSE I WORSHIP THE DOT"], dot)
        ⚔️  VALID BY THE EPIC STANDARD ⚔️
        0
    """
    if not args:
        print("Error: Please provide a commit message to validate")
        return 1

    # Filter out validation flags from message
    message_args = [a for a in args if a not in ALL_VALIDATION_FLAGS]
    message = " ".join(message_args)

    # Check which validation mode is requested
    for flags, (module_path, function_name) in VALIDATION_MODES.items():
        if any(flag in args for flag in flags):
            # Dynamically import and call the validation function
            import importlib
            module = importlib.import_module(module_path)
            validation_func = getattr(module, function_name)
            valid = dot.validate_commit(message)
            print(validation_func(valid, message))
            return 0 if valid else 1

    # Default validation (no mode specified)
    if dot.validate_commit(message):
        print(VALID_COMMIT_MESSAGE)
        return 0
    else:
        print(INVALID_COMMIT_MESSAGE)
        return 1


def handle_suffix():
    """Display the current worship suffix and its source.

    Shows the active worship suffix and where it's configured from
    (environment variable, .dot.ini file, or default).

    Returns:
        int: Exit code (always 0).

    Example:
        >>> handle_suffix()
        Current worship suffix: BECAUSE I WORSHIP THE DOT
        Source: default
        0
    """
    suffix, source = resolve_worship_suffix()
    print(f"Current worship suffix: {suffix}")
    print(f"Source: {source}")
    return 0


def handle_backstory():
    """Display THE DOT's timeless backstory narrative.

    Prints the foundational story and principles of THE DOT philosophy,
    including the Edict of THE DOT.

    Returns:
        int: Exit code (always 0).

    Example:
        >>> handle_backstory()
        Before there were branches or builds, there was a point...
        0
    """
    from dot.backstory import BACKSTORY
    print(BACKSTORY)
    return 0


def handle_philosophy():
    """Display THE DOT's philosophy documentation.

    Reads and prints the complete philosophy documentation from
    docs/PHILOSOPHY.md, including core principles and practices.

    Returns:
        int: Exit code (0 on success, 1 if file not found).

    Example:
        >>> handle_philosophy()
        # THE DOT Philosophy
        ...
        0
    """
    # Print re-evaluated principles from docs/PHILOSOPHY.md
    try:
        path = Path(__file__).parent.parent / "docs" / "PHILOSOPHY.md"
        print(path.read_text(encoding="utf-8"))
        return 0
    except Exception:
        print("Error: Unable to read PHILOSOPHY.md")
        return 1


def handle_demo():
    """Run THE DOT interactive demonstration.

    Executes the demo module which showcases THE DOT's features
    and workflow in an interactive format.

    Returns:
        int: Exit code from demo execution.

    Example:
        >>> handle_demo()
        === THE DOT Demo ===
        ...
        0
    """
    from dot.demo import run_demo
    run_demo()
    return 0


def handle_philosophy_teaching(command, args):
    """Handle inline philosophy teaching commands.

    Dispatches commands for specific philosophical teachings from various
    traditions (Kabbalah, Taoism, Buddhism, Stoicism, Confucianism, Hinduism).

    Args:
        command (str): The teaching command (e.g., "tree", "tao", "dharma").
        args (list[str]): Additional command arguments (currently unused).

    Returns:
        int: Exit code (0 if teaching found, 1 if unknown command).

    Example:
        >>> handle_philosophy_teaching("tree", [])
        ╔══════════════════════════════════════╗
        ║        TREE OF LIFE READING          ║
        ...
        0
        >>> handle_philosophy_teaching("unknown", [])
        Unknown command: unknown
        1

    Note:
        Supports 40+ teaching commands across 6 philosophical traditions.
        See VALIDATION_MODES for the complete list of supported philosophies.
    """
    # Map commands to their module and function
    teachings = {
        # Kabbalah
        "tree": ("dot.kabbalah", "tree_of_life_reading"),
        "worlds": ("dot.kabbalah", "four_worlds_teaching"),
        "sephiroth": ("dot.kabbalah", "ten_sephiroth_teaching"),
        "tikkun": ("dot.kabbalah", "tikkun_olam_practice"),
        "ein-sof": ("dot.kabbalah", "ein_sof_meditation"),
        "shekhinah": ("dot.kabbalah", "shekhinah_presence"),
        "gematria": ("dot.kabbalah", "gematria_example"),
        # Taoism
        "tao": ("dot.tao", "tao_te_ching_excerpt"),
        "wu-wei": ("dot.tao", "wu_wei_practice"),
        "yin-yang": ("dot.tao", "yin_yang_balance"),
        "elements": ("dot.tao", "five_elements_teaching"),
        "treasures": ("dot.tao", "three_treasures_teaching"),
        "pu": ("dot.tao", "pu_uncarved_block"),
        "water": ("dot.tao", "water_teaching"),
        "iching": ("dot.tao", "iching_hexagram"),
        # Buddhism
        "dharma": ("dot.dharma", "dharma_teaching"),
        "truths": ("dot.dharma", "four_noble_truths"),
        "path": ("dot.dharma", "eightfold_path"),
        "marks": ("dot.dharma", "three_marks_teaching"),
        "middle": ("dot.dharma", "middle_way_teaching"),
        "poisons": ("dot.dharma", "three_poisons_teaching"),
        "mindful": ("dot.dharma", "mindfulness_practice"),
        # Stoicism
        "stoic": ("dot.stoic", "stoic_teaching"),
        "virtues": ("dot.stoic", "four_virtues_teaching"),
        "control": ("dot.stoic", "dichotomy_of_control"),
        "disciplines": ("dot.stoic", "three_disciplines_teaching"),
        "negative": ("dot.stoic", "negative_visualization"),
        "memento": ("dot.stoic", "memento_mori"),
        "amor": ("dot.stoic", "amor_fati_teaching"),
        "premeditatio": ("dot.stoic", "premeditatio_malorum"),
        # Confucianism
        "confucian": ("dot.confucian", "confucian_teaching"),
        "ren": ("dot.confucian", "ren_teaching"),
        "li": ("dot.confucian", "li_teaching"),
        "junzi": ("dot.confucian", "junzi_teaching"),
        "xiao": ("dot.confucian", "xiao_teaching"),
        "cultivation": ("dot.confucian", "self_cultivation_teaching"),
        "mean": ("dot.confucian", "doctrine_of_mean"),
        "analects": ("dot.confucian", "analects_excerpt"),
        # Hinduism
        "hindu": ("dot.hindu", "hindu_teaching"),
        "vedic": ("dot.hindu", "vedic_teaching"),
        "karma": ("dot.hindu", "karma_teaching"),
        "yogas": ("dot.hindu", "four_yogas_teaching"),
        "purusharthas": ("dot.hindu", "purusharthas_teaching"),
        "gunas": ("dot.hindu", "three_gunas_teaching"),
        "maya": ("dot.hindu", "maya_illusion_teaching"),
        "atman": ("dot.hindu", "atman_brahman_teaching"),
        "gita": ("dot.hindu", "bhagavad_gita_excerpt"),
        "moksha": ("dot.hindu", "samsara_moksha_teaching"),
    }

    if command in teachings:
        module_path, function_name = teachings[command]
        import importlib
        module = importlib.import_module(module_path)
        teaching_func = getattr(module, function_name)
        print(teaching_func())
        return 0

    # Unknown command
    print(f"Unknown command: {command}")
    print_help()
    return 1


def main():
    """Main entry point for THE DOT CLI.

    Parses command-line arguments and dispatches to the appropriate
    command handler. Supports 90+ commands across philosophy, validation,
    statistics, hooks, and utility functions.

    Returns:
        int: Exit code from the dispatched command (0 for success, 1 for error).

    Example:
        >>> import sys
        >>> sys.argv = ['dot', 'worship', 'Alice']
        >>> main()
        Alice now worships THE DOT
        0

    Note:
        This function was refactored from 493 lines with 90+ elif branches
        to 9 lines using the dispatch_command pattern, reducing cyclomatic
        complexity from 70+ to <10.
    """
    args = sys.argv[1:]
    dot = get_dot()

    # Dispatch to command handler (replaces 90+ elif branches)
    command = args[0] if args else None
    remaining_args = args[1:] if args else []
    return dispatch_command(command, remaining_args, dot)


# Legacy main() body below - will be removed after dispatch_command is verified
# This is kept temporarily for reference during the refactoring
def handle_hooks(subcommand):
    """Handle git hooks commands for THE DOT.

    Manages installation, uninstallation, and status checking of THE DOT's
    git hooks (commit-msg and prepare-commit-msg).

    Args:
        subcommand (str): The hooks operation to perform.
            Valid values: "install", "uninstall", "status".

    Returns:
        int: Exit code (0 for success, 1 for error or unknown subcommand).

    Example:
        >>> handle_hooks("install")
        ═══════════════════════════════════════════
                   THE DOT - Git Hooks Installation
        ═══════════════════════════════════════════
        ✓ Installed commit-msg hook
        ✓ Installed prepare-commit-msg hook
        0
    """
    if subcommand == "install":
        return install_hooks()
    elif subcommand == "uninstall":
        return uninstall_hooks()
    elif subcommand == "status":
        return check_hooks_status()
    else:
        print(f"Unknown hooks subcommand: {subcommand}")
        print("\nAvailable subcommands:")
        print("  install   - Install THE DOT git hooks")
        print("  uninstall - Remove THE DOT git hooks")
        print("  status    - Check hook installation status")
        return 1


def install_hooks():
    """Install THE DOT's git hooks into the current repository.

    Installs commit-msg and prepare-commit-msg hooks to enforce worship
    suffix requirements. Backs up any existing hooks before installation.

    Returns:
        int: Exit code (0 for success, 1 if not in a git repository or hooks directory not found).

    Example:
        >>> install_hooks()
        ════════════════════════════════════════════════════════════════
                   THE DOT - Git Hooks Installation
        ════════════════════════════════════════════════════════════════

        ✓ Installed commit-msg hook
        ✓ Installed prepare-commit-msg hook

        ════════════════════════════════════════════════════════════════
        Installation complete!
        ════════════════════════════════════════════════════════════════
        0
    """
    # Check if in git repository
    git_dir = git_utils.get_git_dir()
    if not git_dir:
        print("Error: Not in a git repository")
        return 1

    hooks_dir = git_dir / "hooks"
    hooks_dir.mkdir(exist_ok=True)

    # Find the hooks directory in the package
    package_dir = Path(__file__).parent.parent
    source_hooks_dir = package_dir / "hooks"

    if not source_hooks_dir.exists():
        print(f"Error: Hooks directory not found at {source_hooks_dir}")
        return 1

    print("════════════════════════════════════════════════════════════════")
    print("           THE DOT - Git Hooks Installation")
    print("════════════════════════════════════════════════════════════════")
    print()

    # Install commit-msg hook
    commit_msg_src = source_hooks_dir / "commit-msg"
    commit_msg_dst = hooks_dir / "commit-msg"

    if commit_msg_dst.exists():
        backup = hooks_dir / "commit-msg.backup"
        print(f"Backing up existing commit-msg hook to {backup}")
        shutil.copy2(commit_msg_dst, backup)

    shutil.copy2(commit_msg_src, commit_msg_dst)
    commit_msg_dst.chmod(0o755)
    print("✓ Installed commit-msg hook")

    # Install prepare-commit-msg hook
    prepare_src = source_hooks_dir / "prepare-commit-msg"
    prepare_dst = hooks_dir / "prepare-commit-msg"

    if prepare_dst.exists():
        backup = hooks_dir / "prepare-commit-msg.backup"
        print(f"Backing up existing prepare-commit-msg hook to {backup}")
        shutil.copy2(prepare_dst, backup)

    shutil.copy2(prepare_src, prepare_dst)
    prepare_dst.chmod(0o755)
    print("✓ Installed prepare-commit-msg hook")

    print()
    print("════════════════════════════════════════════════════════════════")
    print("Installation complete!")
    print("════════════════════════════════════════════════════════════════")
    print()
    print("The following hooks have been installed:")
    print("  • commit-msg: Validates commit messages worship THE DOT")
    print("  • prepare-commit-msg: Auto-appends worship phrase if missing")
    print()
    print("All commits will now automatically worship THE DOT.")
    print()
    return 0


def uninstall_hooks():
    """Uninstall THE DOT's git hooks from the current repository.

    Removes commit-msg and prepare-commit-msg hooks and restores any
    backed up hooks that existed before installation.

    Returns:
        int: Exit code (0 for success, 1 if not in a git repository).

    Example:
        >>> uninstall_hooks()
        ✓ Removed commit-msg hook
          Restored backup for commit-msg
        ✓ Removed prepare-commit-msg hook

        THE DOT hooks have been uninstalled.
        0
    """
    git_dir = git_utils.get_git_dir()
    if not git_dir:
        print("Error: Not in a git repository")
        return 1

    hooks_dir = git_dir / "hooks"

    removed = []
    for hook_name in ["commit-msg", "prepare-commit-msg"]:
        hook_file = hooks_dir / hook_name
        if hook_file.exists():
            hook_file.unlink()
            removed.append(hook_name)
            print(f"✓ Removed {hook_name} hook")

            # Restore backup if it exists
            backup = hooks_dir / f"{hook_name}.backup"
            if backup.exists():
                shutil.copy2(backup, hook_file)
                backup.unlink()
                print(f"  Restored backup for {hook_name}")

    if removed:
        print()
        print("THE DOT hooks have been uninstalled.")
    else:
        print("No THE DOT hooks found to uninstall.")

    return 0


def check_hooks_status():
    """Check the installation status of THE DOT's git hooks.

    Verifies whether commit-msg and prepare-commit-msg hooks are installed
    and whether they are THE DOT hooks (by checking for "THE DOT" in content).

    Returns:
        int: Exit code (0 for success, 1 if not in a git repository).

    Example:
        >>> check_hooks_status()
        THE DOT Git Hooks Status:

        ✓ commit-msg: Installed
        ✓ prepare-commit-msg: Installed

        0
    """
    git_dir = git_utils.get_git_dir()
    if not git_dir:
        print("Error: Not in a git repository")
        return 1

    hooks_dir = git_dir / "hooks"

    print("THE DOT Git Hooks Status:")
    print()

    for hook_name in ["commit-msg", "prepare-commit-msg"]:
        hook_file = hooks_dir / hook_name
        if hook_file.exists():
            # Check if it's THE DOT hook
            content = hook_file.read_text()
            if "THE DOT" in content:
                print(f"✓ {hook_name}: Installed")
            else:
                print(f"⚠ {hook_name}: Exists but not THE DOT hook")
        else:
            print(f"✗ {hook_name}: Not installed")

    print()
    return 0


def handle_stats(subcommand):
    """Handle worship statistics commands.

    Provides access to worship tracking statistics including summaries,
    top worshippers, daily stats, export functionality, and clearing data.

    Args:
        subcommand (str): The statistics operation to perform.
            Valid values: "summary", "top", "daily", "export", "clear".

    Returns:
        int: Exit code (0 for success, 1 for unknown subcommand).

    Example:
        >>> handle_stats("summary")
        THE DOT Worship Statistics:
        ============================================================
        Total Worships: 42
        Unique Worshippers: 7
        Days Active: 14
        First Worship: 2024-06-01
        Last Worship: 2024-06-15
        0
    """
    from dot.stats import WorshipStats

    stats = WorshipStats()

    if subcommand == "summary":
        summary = stats.get_summary()
        print("THE DOT Worship Statistics:")
        print("=" * 60)
        print(f"Total Worships: {summary['total_worships']}")
        print(f"Unique Worshippers: {summary['unique_worshippers']}")
        print(f"Days Active: {summary['days_active']}")
        if summary['first_worship']:
            print(f"First Worship: {summary['first_worship']}")
        if summary['last_worship']:
            print(f"Last Worship: {summary['last_worship']}")
        print()
        return 0

    elif subcommand == "top":
        from dot.epic import epic_stats_header, epic_worshipper_title

        top = stats.get_top_worshippers(10)

        # Check if epic mode is enabled in config
        from dot.config import get_config
        config = get_config()
        epic_mode = config.get("display", "epic", default=False)

        if epic_mode:
            print(epic_stats_header())
            for i, w in enumerate(top, 1):
                title = epic_worshipper_title(i)
                print(f"\n{title}")
                print(f"    {w['name']} - {w['count']} offerings to THE DOT")
            print("\n" + "═" * 70)
        else:
            print("Top Worshippers:")
            print("=" * 60)
            for i, w in enumerate(top, 1):
                print(f"{i:2d}. {w['name']:<30} {w['count']:>5} worships")
        print()
        return 0

    elif subcommand == "daily":
        daily = stats.get_daily_stats(7)
        print("Daily Worship (Last 7 Days):")
        print("=" * 60)
        for date, count in daily.items():
            print(f"{date}: {count} worships")
        print()
        return 0

    elif subcommand == "export":
        export = stats.export_stats()
        print(export)
        return 0

    elif subcommand == "clear":
        response = input("Clear all statistics? [y/N]: ")
        if response.lower() == 'y':
            stats.clear_stats()
            print("✓ Statistics cleared")
        else:
            print("Cancelled")
        return 0

    else:
        print(f"Unknown stats subcommand: {subcommand}")
        print("\nAvailable subcommands:")
        print("  summary  - Show worship summary")
        print("  top      - Show top worshippers")
        print("  daily    - Show daily worship counts")
        print("  export   - Export statistics as JSON")
        print("  clear    - Clear all statistics")
        return 1


def handle_badge(format_type):
    """Handle badge generation for THE DOT.

    Generates worship badges in various formats for use in README files
    and documentation. Supports markdown, HTML, reStructuredText, and raw URLs.

    Args:
        format_type (str): The badge format to generate.
            Valid values: "markdown", "html", "rst", "url".

    Returns:
        int: Exit code (0 for success, 1 for invalid format).

    Example:
        >>> handle_badge("markdown")
        Copy this badge to your README:

        [![I Worship THE DOT](https://img.shields.io/badge/I%20Worship-THE%20DOT-blue.svg)](https://github.com/yourusername/worship_the_dot)

        0
    """
    from dot.badges import generate_worship_badge, generate_all_badges

    valid_formats = ["markdown", "html", "rst", "url"]

    if format_type not in valid_formats:
        print(f"Unknown format: {format_type}")
        print(f"Valid formats: {', '.join(valid_formats)}")
        return 1

    if format_type == "url":
        # Just the URL for shields.io
        from dot.badges import generate_worship_badge
        print(generate_worship_badge("url"))
    else:
        # Full badge markdown/html/rst
        badge = generate_worship_badge(format_type)
        print("Copy this badge to your README:")
        print()
        print(badge)
        print()

    return 0


def handle_poem(subcommand: str, rest_args: list[str]):
    """Handle poetry and liturgical text generation.

    Generates various forms of devotional poetry and liturgical texts
    including hymns, haikus, ASCII banners, and rhythmic chants.

    Args:
        subcommand (str): The type of poem to generate.
            Valid values: "hymn", "haiku", "banner", "chant".
        rest_args (list[str]): Additional arguments for the poem.
            - haiku: optional name of worshipper
            - banner: optional width (odd number ≥ 7)
            - chant: optional times (int) and name

    Returns:
        int: Exit code (0 for success, 1 for unknown subcommand).

    Example:
        >>> handle_poem("haiku", ["Alice"])
        The worshipper bows
        Alice praises THE DOT's light
        All code glorifies
        0
    """
    from dot.poetry import hymn as hymn_text, haiku as haiku_text, banner as banner_text, chant as chant_text

    if subcommand == "hymn":
        print(hymn_text())
        return 0
    elif subcommand == "haiku":
        name = rest_args[0] if rest_args else None
        print(haiku_text(name))
        return 0
    elif subcommand == "banner":
        # optional width arg
        width = None
        if rest_args:
            try:
                width = int(rest_args[0])
            except ValueError:
                width = None
        print(banner_text(width or 21))
        return 0
    elif subcommand == "chant":
        # chant [times] [name]
        times = 3
        name = None
        if rest_args:
            try:
                times = int(rest_args[0])
                name = rest_args[1] if len(rest_args) > 1 else None
            except ValueError:
                name = rest_args[0]
        print(chant_text(times, name))
        return 0
    else:
        print(f"Unknown poem subcommand: {subcommand}")
        print("\nAvailable subcommands:")
        print("  hymn                   - A brief hymn to THE DOT")
        print("  haiku [name]           - A 5–7–5 haiku; optionally name the worshipper")
        print("  banner [width]         - An ASCII DOT banner (width odd ≥ 7)")
        print("  chant [times] [name]   - Repeat the suffix rhythmically")
        return 1


def handle_config(subcommand, args):
    """Handle configuration management commands.

    Manages THE DOT's configuration including worship suffix, user settings,
    and display preferences. Supports viewing, modifying, and resetting config.

    Args:
        subcommand (str): The configuration operation to perform.
            Valid values: "show", "show-suffix", "set-suffix", "get", "set", "reset".
        args (list[str]): Additional arguments for the operation.
            - set-suffix: new suffix text
            - get: configuration key (e.g., "user.name")
            - set: key and value

    Returns:
        int: Exit code (0 for success, 1 for error or invalid args).

    Example:
        >>> handle_config("show-suffix", [])
        Current worship suffix:
          BECAUSE I WORSHIP THE DOT
        Source:
          default
        0
    """
    from dot.config import get_config, resolve_worship_suffix, write_worship_suffix

    config = get_config()

    if subcommand == "show":
        print("THE DOT Configuration:")
        print("=" * 60)
        print(config.export_config())
        print()
        print("Worship Suffix:")
        print("=" * 60)
        suffix, source = resolve_worship_suffix()
        print(f"  Suffix: {suffix}")
        print(f"  Source: {source}")
        return 0

    elif subcommand == "show-suffix":
        suffix, source = resolve_worship_suffix()
        print("Current worship suffix:")
        print(f"  {suffix}")
        print("Source:")
        print(f"  {source}")
        return 0

    elif subcommand == "set-suffix":
        if len(args) < 1:
            print("Error: Please provide a suffix string to set")
            print("Example: dot config set-suffix 'BECAUSE I LOVE THE DOT'")
            return 1
        new_suffix = " ".join(args).strip()
        path = write_worship_suffix(None, new_suffix)
        print(f"✓ Updated worship suffix in {path}")
        return 0

    elif subcommand == "get":
        if len(args) < 1:
            print("Error: Please provide a configuration key")
            print("Example: dot config get user.name")
            return 1

        keys = args[0].split(".")
        value = config.get(*keys)
        if value is not None:
            print(value)
            return 0
        else:
            print(f"Configuration key not found: {args[0]}")
            return 1

    elif subcommand == "set":
        if len(args) < 2:
            print("Error: Please provide a key and value")
            print("Example: dot config set user.name 'Claude'")
            return 1

        keys = args[0].split(".")
        value = args[1]

        # Try to parse value as JSON for booleans/numbers
        import json
        try:
            value = json.loads(value)
        except (json.JSONDecodeError, ValueError):
            # Keep as string if not valid JSON
            pass

        if config.set(*keys, value=value):
            print(f"✓ Configuration updated: {args[0]} = {value}")
            return 0
        else:
            print("Error: Failed to update configuration")
            return 1

    elif subcommand == "reset":
        response = input("Reset all configuration to defaults? [y/N]: ")
        if response.lower() == 'y':
            config.reset()
            print("✓ Configuration reset to defaults")
            return 0
        else:
            print("Cancelled")
            return 0

    else:
        print(f"Unknown config subcommand: {subcommand}")
        print("\nAvailable subcommands:")
        print("  show        - Show all configuration and worship suffix")
        print("  show-suffix - Show only worship suffix")
        print("  set-suffix  - Set worship suffix in .dot.ini")
        print("  get         - Get a configuration value")
        print("  set         - Set a configuration value")
        print("  reset       - Reset configuration to defaults")
        return 1


def handle_completions(shell):
    """Handle shell completion script generation.

    Generates shell completion scripts for bash, zsh, or fish shells.
    These scripts enable tab completion for THE DOT CLI commands.

    Args:
        shell (str): The target shell.
            Valid values: "bash", "zsh", "fish".

    Returns:
        int: Exit code (0 for success, 1 for unknown shell or error).

    Example:
        >>> handle_completions("bash")
        # Bash completion script for THE DOT CLI
        _dot_completion() {
            ...
        }
        complete -F _dot_completion dot
        0
    """
    from dot.completions import get_completion

    valid_shells = ["bash", "zsh", "fish"]

    if shell not in valid_shells:
        print(f"Unknown shell: {shell}")
        print(f"Valid shells: {', '.join(valid_shells)}")
        return 1

    try:
        completion_script = get_completion(shell)
        print(completion_script)
        return 0
    except ValueError as e:
        print(f"Error: {e}")
        return 1


def handle_tarot(subcommand, args, deprecated=False):
    """Handle tarot card reading and divination commands.

    Provides access to tarot card readings, spreads, and individual card
    information. Supports seeded draws for reproducible readings.

    Args:
        subcommand (str): The tarot operation to perform.
            Valid values: "list", "card", "draw", "spread".
        args (list[str]): Additional arguments for the operation.
            - card: card name (e.g., "The Magician")
            - draw: optional count, --seed, --no-reversed flags
            - spread: kind (three/commit/yesno), optional --seed
        deprecated (bool): If True, shows deprecation warning. Default False.

    Returns:
        int: Exit code (0 for success, 1 for error or unknown subcommand).

    Example:
        >>> handle_tarot("draw", ["1", "--seed", "42"], deprecated=False)
        Tarot Draw (1 card(s)):
        The Fool (upright)
        Keywords: beginnings, innocence, spontaneity
        0
    """
    if deprecated:
        print("⚠ Note: 'dot tarot' is deprecated. Use 'dot wisdom tarot' instead.")
        print()

    from dot.philosophies.tarot import list_cards, get_card, draw as tarot_draw, spread as tarot_spread, interpret, yesno_from_card

    if subcommand == "list":
        print("Tarot Deck (Major Arcana):")
        for name in list_cards():
            print(f"  - {name}")
        return 0

    if subcommand == "card":
        if not args:
            print("Error: Provide a card name")
            return 1
        name = " ".join(args)
        card = get_card(name)
        if not card:
            print(f"Unknown card: {name}")
            return 1
        print(f"{card.name}")
        print(f"Keywords: {', '.join(card.keywords)}")
        print(f"Upright:  {card.upright}")
        print(f"Reversed: {card.reversed}")
        return 0

    if subcommand == "draw":
        n = 1
        seed = None
        allow_rev = True
        # args: [n] [--seed S] [--no-reversed]
        i = 0
        while i < len(args):
            a = args[i]
            if a.isdigit():
                n = int(a)
            elif a == "--seed" and i + 1 < len(args):
                try:
                    seed = int(args[i + 1])
                except ValueError:
                    print(f"Error: --seed expects an integer, got '{args[i + 1]}'")
                    return 1
                i += 1
            elif a == "--no-reversed":
                allow_rev = False
            i += 1

        entries = tarot_draw(n=n, allow_reversed=allow_rev, seed=seed)
        print(f"Tarot Draw ({len(entries)} card(s)):")
        print(interpret(entries))
        return 0

    if subcommand == "spread":
        kind = args[0] if args else "three"
        seed = None
        if len(args) > 1 and args[1] == "--seed" and len(args) > 2:
            try:
                seed = int(args[2])
            except ValueError:
                print(f"Error: --seed expects an integer, got '{args[2]}'")
                return 1
        sp = tarot_spread(kind=kind, seed=seed)
        if kind == "yesno":
            (card, rev) = next(iter(sp.values()))
            ans = yesno_from_card(card, rev)
            print(f"Yes/No: {ans}")
        print("Spread:")
        lines = []
        for pos, (card, rev) in sp.items():
            orient = "reversed" if rev else "upright"
            lines.append(f"  {pos:<8} - {card.name} ({orient})")
        print("\n".join(lines))
        return 0

    print(f"Unknown tarot subcommand: {subcommand}")
    print("\nAvailable subcommands:")
    print("  draw [n] [--seed S] [--no-reversed]")
    print("  spread [three|commit|yesno] [--seed S]")
    print("  list")
    print("  card <name>")
    return 1


def handle_shinto(subcommand, args, deprecated=False):
    """Handle Shinto rituals, practices, and spiritual teachings.

    Provides access to Shinto devotional practices including prayers (norito),
    fortunes (omikuji), purification rituals (harai), votive tablets (ema),
    and philosophical teachings about kami, virtues, and sacred concepts.

    Args:
        subcommand (str): The Shinto operation to perform.
            Valid values: "norito", "omikuji", "harai", "ema", "kami",
            "virtues", "misogi", "kannagara", "torii", "matsuri", "kotodama",
            "musubi", "reading".
        args (list[str]): Additional arguments for the operation.
            - norito: optional intent message
            - omikuji: optional --seed flag
            - ema: required message text
        deprecated (bool): If True, shows deprecation warning. Default False.

    Returns:
        int: Exit code (0 for success, 1 for error or unknown subcommand).

    Example:
        >>> handle_shinto("norito", ["Successful release"], deprecated=False)
        ═══════════════════════════════════════════
                    NORITO - Sacred Prayer
        ═══════════════════════════════════════════

        Intent: Successful release

        BECAUSE I WORSHIP THE DOT
        0
    """
    if deprecated:
        print("⚠ Note: 'dot shinto' is deprecated. Use 'dot wisdom shinto' instead.")
        print()

    from dot.philosophies.shinto import (
        norito as s_norito, omikuji as s_omikuji, harai as s_harai, ema as s_ema,
        kami_teaching, four_virtues_guide, misogi_guide, kannagara_teaching,
        torii_teaching, matsuri_celebration, kotodama_teaching, musubi_teaching,
        shinto_reading
    )

    if subcommand == "norito":
        intent = " ".join(args) if args else None
        print(s_norito(intent))
        return 0

    if subcommand == "omikuji":
        seed = None
        if args and args[0] == "--seed" and len(args) > 1:
            try:
                seed = int(args[1])
            except ValueError:
                print(f"Error: --seed expects an integer, got '{args[1]}'")
                return 1
        print(s_omikuji(seed=seed))
        return 0

    if subcommand == "harai":
        print(s_harai())
        return 0

    if subcommand == "ema":
        if not args:
            print("Error: Provide a message for the ema")
            return 1
        message = " ".join(args)
        print(s_ema(message))
        return 0

    if subcommand == "kami":
        print(kami_teaching())
        return 0

    if subcommand == "virtues":
        print(four_virtues_guide())
        return 0

    if subcommand == "misogi":
        print(misogi_guide())
        return 0

    if subcommand == "kannagara":
        print(kannagara_teaching())
        return 0

    if subcommand == "torii":
        print(torii_teaching())
        return 0

    if subcommand == "matsuri":
        print(matsuri_celebration())
        return 0

    if subcommand == "kotodama":
        print(kotodama_teaching())
        return 0

    if subcommand == "musubi":
        print(musubi_teaching())
        return 0

    if subcommand == "reading":
        print(shinto_reading())
        return 0

    print(f"Unknown shinto subcommand: {subcommand}")
    print("\nAvailable subcommands:")
    print("  norito [intent]      Prayer to THE DOT-kami")
    print("  omikuji [--seed S]   Draw a sacred fortune")
    print("  harai                Purification guidance")
    print("  ema <message>        Create a vow plaque")
    print("  kami                 Teaching about divine spirits")
    print("  virtues              The Four Shinto Virtues")
    print("  misogi               Purification practices")
    print("  kannagara            Living in harmony with kami")
    print("  torii                Sacred gateways")
    print("  matsuri              Celebration teachings")
    print("  kotodama             Spirit of words")
    print("  musubi               Creative power")
    print("  reading              Random Shinto wisdom")
    return 1


def handle_zen(subcommand, args):
    """Handle Zen Buddhist teachings and meditation practices.

    Provides access to Zen philosophical concepts including meditation (zazen),
    koans, enlightenment (satori), mindfulness practices, and aesthetic principles
    like wabi-sabi and ma (negative space).

    Args:
        subcommand (str): The Zen teaching to access.
            Valid values: "zazen", "koan", "satori", "mushin", "shoshin",
            "wabi-sabi", "ma", "enso", "saying", "reading".
        args (list[str]): Additional arguments (currently unused).

    Returns:
        int: Exit code (0 for success, 1 for unknown subcommand).

    Example:
        >>> handle_zen("zazen", [])
        ═══════════════════════════════════════════
                        ZAZEN - Seated Meditation
        ═══════════════════════════════════════════

        Zazen is the practice of seated meditation...
        0
    """
    from dot.zen import (
        zazen_teaching, koan_teaching, satori_teaching, mushin_teaching,
        shoshin_teaching, wabi_sabi_teaching, ma_teaching, enso_teaching,
        zen_saying, zen_reading
    )

    if subcommand == "zazen":
        print(zazen_teaching())
        return 0

    if subcommand == "koan":
        print(koan_teaching())
        return 0

    if subcommand == "satori":
        print(satori_teaching())
        return 0

    if subcommand == "mushin":
        print(mushin_teaching())
        return 0

    if subcommand == "shoshin":
        print(shoshin_teaching())
        return 0

    if subcommand == "wabi-sabi":
        print(wabi_sabi_teaching())
        return 0

    if subcommand == "ma":
        print(ma_teaching())
        return 0

    if subcommand == "enso":
        print(enso_teaching())
        return 0

    if subcommand == "saying":
        print(zen_saying())
        return 0

    if subcommand == "reading":
        print(zen_reading())
        return 0

    print(f"Unknown zen subcommand: {subcommand}")
    print("\nAvailable subcommands:")
    print("  zazen                Sitting meditation practice")
    print("  koan                 Paradoxical riddles for awakening")
    print("  satori               Sudden enlightenment teaching")
    print("  mushin               No-mind state")
    print("  shoshin              Beginner's mind")
    print("  wabi-sabi            Beauty in imperfection")
    print("  ma                   Negative space and pauses")
    print("  enso                 Circle of enlightenment")
    print("  saying               Random Zen saying")
    print("  reading              Random Zen wisdom")
    return 1


def handle_hermetic(subcommand, args, deprecated=False):
    """Handle Hermetic philosophy and the Seven Principles.

    Provides access to the Seven Hermetic Principles from the Kybalion:
    Mentalism, Correspondence, Vibration, Polarity, Rhythm, Cause & Effect,
    and Gender. Also includes the Emerald Tablet teachings.

    Args:
        subcommand (str): The Hermetic principle or teaching to access.
            Valid values: "mentalism", "correspondence", "vibration",
            "polarity", "rhythm", "cause-effect", "gender", "emerald-tablet",
            "reading".
        args (list[str]): Additional arguments (currently unused).
        deprecated (bool): If True, shows deprecation warning. Default False.

    Returns:
        int: Exit code (0 for success, 1 for unknown subcommand).

    Example:
        >>> handle_hermetic("mentalism", [], deprecated=False)
        ═══════════════════════════════════════════
                THE PRINCIPLE OF MENTALISM
        ═══════════════════════════════════════════

        "THE ALL is MIND; The Universe is Mental."
        0
    """
    if deprecated:
        print("⚠ Note: 'dot hermetic' is deprecated. Use 'dot wisdom hermetic' instead.")
        print()

    from dot.philosophies.hermetic import (
        mentalism_teaching, correspondence_teaching, vibration_teaching,
        polarity_teaching, rhythm_teaching, cause_effect_teaching,
        gender_teaching, emerald_tablet_teaching, hermetic_reading
    )

    if subcommand == "mentalism":
        print(mentalism_teaching())
        return 0

    if subcommand == "correspondence":
        print(correspondence_teaching())
        return 0

    if subcommand == "vibration":
        print(vibration_teaching())
        return 0

    if subcommand == "polarity":
        print(polarity_teaching())
        return 0

    if subcommand == "rhythm":
        print(rhythm_teaching())
        return 0

    if subcommand == "cause-effect":
        print(cause_effect_teaching())
        return 0

    if subcommand == "gender":
        print(gender_teaching())
        return 0

    if subcommand == "emerald-tablet":
        print(emerald_tablet_teaching())
        return 0

    if subcommand == "reading":
        print(hermetic_reading())
        return 0

    print(f"Unknown hermetic subcommand: {subcommand}")
    print("\nAvailable subcommands:")
    print("  mentalism            The All is Mind")
    print("  correspondence       As above, so below")
    print("  vibration            Nothing rests; everything moves")
    print("  polarity             Everything is dual")
    print("  rhythm               Everything flows")
    print("  cause-effect         Every cause has its effect")
    print("  gender               Masculine and feminine in all")
    print("  emerald-tablet       The Emerald Tablet of Hermes")
    print("  reading              Random Hermetic wisdom")
    return 1


def handle_gnostic(subcommand, args, deprecated=False):
    """Handle Gnostic mystical teachings and cosmology.

    Provides access to Gnostic philosophical concepts including direct knowledge
    (gnosis), divine fullness (pleroma), wisdom (sophia), cosmological teachings
    about the demiurge and archons, and sacred texts.

    Args:
        subcommand (str): The Gnostic teaching to access.
            Valid values: "gnosis", "pleroma", "sophia", "demiurge",
            "archons", "spark", "thomas", "hammadi", "reading".
        args (list[str]): Additional arguments (currently unused).
        deprecated (bool): If True, shows deprecation warning. Default False.

    Returns:
        int: Exit code (0 for success, 1 for unknown subcommand).

    Example:
        >>> handle_gnostic("gnosis", [], deprecated=False)
        ═══════════════════════════════════════════
                        GNOSIS - Direct Knowledge
        ═══════════════════════════════════════════

        Gnosis is the direct, experiential knowledge...
        0
    """
    if deprecated:
        print("⚠ Note: 'dot gnostic' is deprecated. Use 'dot wisdom gnostic' instead.")
        print()

    from dot.philosophies.gnostic import (
        gnosis_teaching, pleroma_teaching, sophia_teaching,
        demiurge_teaching, archons_teaching, spark_teaching,
        thomas_teaching, hammadi_teaching, gnostic_reading
    )

    if subcommand == "gnosis":
        print(gnosis_teaching())
        return 0

    if subcommand == "pleroma":
        print(pleroma_teaching())
        return 0

    if subcommand == "sophia":
        print(sophia_teaching())
        return 0

    if subcommand == "demiurge":
        print(demiurge_teaching())
        return 0

    if subcommand == "archons":
        print(archons_teaching())
        return 0

    if subcommand == "spark":
        print(spark_teaching())
        return 0

    if subcommand == "thomas":
        print(thomas_teaching())
        return 0

    if subcommand == "hammadi":
        print(hammadi_teaching())
        return 0

    if subcommand == "reading":
        print(gnostic_reading())
        return 0

    print(f"Unknown gnostic subcommand: {subcommand}")
    print("\nAvailable subcommands:")
    print("  gnosis               Direct knowledge")
    print("  pleroma              The Fullness")
    print("  sophia               Divine Wisdom")
    print("  demiurge             The Craftsman")
    print("  archons              The Rulers")
    print("  spark                Divine Spark within")
    print("  thomas               Gospel of Thomas sayings")
    print("  hammadi              Nag Hammadi wisdom")
    print("  reading              Random Gnostic wisdom")
    return 1


def handle_norse(subcommand, args, deprecated=False):
    """Handle Norse/Germanic wisdom and mythology.

    Provides access to Norse philosophical concepts including runic wisdom,
    the Nine Noble Virtues, wyrd (fate), Yggdrasil (world tree), and
    teachings from Odin the All-Father.

    Args:
        subcommand (str): The Norse teaching to access.
            Valid values: "runes", "virtues", "wyrd", "yggdrasil",
            "odin", "reading".
        args (list[str]): Additional arguments (currently unused).
        deprecated (bool): If True, shows deprecation warning. Default False.

    Returns:
        int: Exit code (0 for success, 1 for unknown subcommand).

    Example:
        >>> handle_norse("runes", [], deprecated=False)
        ═══════════════════════════════════════════
                        THE ELDER FUTHARK
        ═══════════════════════════════════════════

        The 24 runes of the Elder Futhark...
        0
    """
    if deprecated:
        print("⚠ Note: 'dot norse' is deprecated. Use 'dot wisdom norse' instead.")
        print()

    from dot.philosophies.norse import (
        runes_teaching, virtues_teaching, wyrd_teaching,
        yggdrasil_teaching, odin_teaching, norse_reading
    )

    if subcommand == "runes":
        print(runes_teaching())
        return 0

    if subcommand == "virtues":
        print(virtues_teaching())
        return 0

    if subcommand == "wyrd":
        print(wyrd_teaching())
        return 0

    if subcommand == "yggdrasil":
        print(yggdrasil_teaching())
        return 0

    if subcommand == "odin":
        print(odin_teaching())
        return 0

    if subcommand == "reading":
        print(norse_reading())
        return 0

    print(f"Unknown norse subcommand: {subcommand}")
    print("\nAvailable subcommands:")
    print("  runes                24 Elder Futhark runes")
    print("  virtues              Nine Noble Virtues")
    print("  wyrd                 Fate and Orlog")
    print("  yggdrasil            World Tree")
    print("  odin                 All-Father's wisdom")
    print("  reading              Random Norse wisdom")
    return 1


def handle_zoroastrian(subcommand, args, deprecated=False):
    """Handle Zoroastrian philosophy and ancient Persian wisdom.

    Provides access to Zoroastrian teachings including Asha (truth/order),
    the three pillars of Good Thoughts/Words/Deeds, and sacred fire symbolism.

    Args:
        subcommand (str): The Zoroastrian teaching to access.
            Valid values: "asha", "principles", "fire", "reading".
        args (list[str]): Additional arguments (currently unused).
        deprecated (bool): If True, shows deprecation warning. Default False.

    Returns:
        int: Exit code (0 for success, 1 for unknown subcommand).

    Example:
        >>> handle_zoroastrian("asha", [], deprecated=False)
        ═══════════════════════════════════════════
                        ASHA - Truth and Order
        ═══════════════════════════════════════════

        Asha is the fundamental principle of truth...
        0
    """
    if deprecated:
        print("⚠ Note: 'dot zoroastrian' is deprecated. Use 'dot wisdom zoroastrian' instead.")
        print()

    from dot.philosophies.zoroastrian import (
        asha_teaching, principles_teaching, fire_teaching, zoroastrian_reading
    )

    if subcommand == "asha":
        print(asha_teaching())
        return 0

    if subcommand == "principles":
        print(principles_teaching())
        return 0

    if subcommand == "fire":
        print(fire_teaching())
        return 0

    if subcommand == "reading":
        print(zoroastrian_reading())
        return 0

    print(f"Unknown zoroastrian subcommand: {subcommand}")
    print("\nAvailable subcommands:")
    print("  asha                 Truth vs Lie (Asha vs Druj)")
    print("  principles           Good Thoughts, Words, Deeds")
    print("  fire                 Sacred Fire symbolism")
    print("  reading              Random Zoroastrian wisdom")
    return 1


def handle_egyptian(subcommand, args, deprecated=False):
    """Handle Ancient Egyptian Mysteries and wisdom teachings.

    Provides access to Egyptian philosophical concepts including Ma'at (cosmic
    balance), the Feather of Truth, Thoth's wisdom, and ancient mystery teachings.

    Args:
        subcommand (str): The Egyptian teaching to access.
            Valid values: "maat", "feather", "thoth", "reading".
        args (list[str]): Additional arguments (currently unused).
        deprecated (bool): If True, shows deprecation warning. Default False.

    Returns:
        int: Exit code (0 for success, 1 for unknown subcommand).

    Example:
        >>> handle_egyptian("maat", [], deprecated=False)
        ═══════════════════════════════════════════
                        MA'AT - Cosmic Balance
        ═══════════════════════════════════════════

        Ma'at represents truth, balance, order...
        0
    """
    if deprecated:
        print("⚠ Note: 'dot egyptian' is deprecated. Use 'dot wisdom egyptian' instead.")
        print()

    from dot.philosophies.egyptian import (
        maat_teaching, feather_teaching, thoth_teaching, egyptian_reading
    )

    if subcommand == "maat":
        print(maat_teaching())
        return 0

    if subcommand == "feather":
        print(feather_teaching())
        return 0

    if subcommand == "thoth":
        print(thoth_teaching())
        return 0

    if subcommand == "reading":
        print(egyptian_reading())
        return 0

    print(f"Unknown egyptian subcommand: {subcommand}")
    print("\nAvailable subcommands:")
    print("  maat                 Truth, Balance, Order")
    print("  feather              Feather of Truth weighing")
    print("  thoth                God of Wisdom and Writing")
    print("  reading              Random Egyptian wisdom")
    return 1


def handle_jain(subcommand, args, deprecated=False):
    """Handle Jain philosophy and principles of non-violence.

    Provides access to core Jain teachings including Ahimsa (non-violence),
    Anekantavada (many-sidedness), Aparigraha (non-attachment), and the
    Three Jewels of Jainism.

    Args:
        subcommand (str): The Jain teaching to access.
            Valid values: "ahimsa", "anekantavada", "aparigraha",
            "jewels", "reading".
        args (list[str]): Additional arguments (currently unused).
        deprecated (bool): If True, shows deprecation warning. Default False.

    Returns:
        int: Exit code (0 for success, 1 for unknown subcommand).

    Example:
        >>> handle_jain("ahimsa", [], deprecated=False)
        ═══════════════════════════════════════════
                        AHIMSA - Non-Violence
        ═══════════════════════════════════════════

        Ahimsa is the principle of non-violence...
        0
    """
    if deprecated:
        print("⚠ Note: 'dot jain' is deprecated. Use 'dot wisdom jain' instead.")
        print()

    from dot.philosophies.jain import (
        ahimsa_teaching, anekantavada_teaching, aparigraha_teaching,
        jewels_teaching, jain_reading
    )

    if subcommand == "ahimsa":
        print(ahimsa_teaching())
        return 0

    if subcommand == "anekantavada":
        print(anekantavada_teaching())
        return 0

    if subcommand == "aparigraha":
        print(aparigraha_teaching())
        return 0

    if subcommand == "jewels":
        print(jewels_teaching())
        return 0

    if subcommand == "reading":
        print(jain_reading())
        return 0

    print(f"Unknown jain subcommand: {subcommand}")
    print("\nAvailable subcommands:")
    print("  ahimsa               Non-violence")
    print("  anekantavada         Many-sidedness")
    print("  aparigraha           Non-attachment")
    print("  jewels               Three Jewels")
    print("  reading              Random Jain wisdom")
    return 1


def show_wisdom_menu():
    """Display menu of all available wisdom traditions."""
    output = []
    output.append("═" * 70)
    output.append("THE DOT - Wisdom Traditions")
    output.append("═" * 70)
    output.append("")
    output.append("Available wisdom traditions (use: dot wisdom TRADITION [CONCEPT]):")
    output.append("")
    output.append("  egyptian          Way of Ma'at (Truth, Balance, Order)")
    output.append("  gnostic           Path of Direct Knowledge (Gnosis, Pleroma)")
    output.append("  hermetic          Seven Hermetic Principles (As above, so below)")
    output.append("  jain              Path of Non-Violence (Ahimsa, Anekantavada)")
    output.append("  norse             Runes and Nine Virtues (Courage, Truth, Honor)")
    output.append("  shinto            Way of the Kami (Norito, Omikuji, Harai)")
    output.append("  tarot             DOT Tarot Readings")
    output.append("  zoroastrian       Path of Asha (Truth vs Lie)")
    output.append("")
    output.append("Use 'dot wisdom TRADITION' to see available concepts.")
    output.append("Use 'dot wisdom TRADITION CONCEPT' to get specific teaching.")
    output.append("═" * 70)
    print("\n".join(output))


def show_tradition_menu(philosophy):
    """Display menu of concepts for a specific tradition."""
    menus = {
        "hermetic": {
            "title": "☿ HERMETIC WISDOM - Seven Hermetic Principles ☿",
            "concepts": [
                ("mentalism", "The All is Mind"),
                ("correspondence", "As above, so below"),
                ("vibration", "Nothing rests; everything moves"),
                ("polarity", "Everything is dual"),
                ("rhythm", "Everything flows"),
                ("cause-effect", "Every cause has its effect"),
                ("gender", "Masculine and feminine in all"),
                ("emerald-tablet", "The Emerald Tablet of Hermes"),
                ("reading", "Random Hermetic wisdom")
            ]
        },
        "gnostic": {
            "title": "☧ GNOSTIC WISDOM - Path of Direct Knowledge ☧",
            "concepts": [
                ("gnosis", "Direct knowledge (Γνῶσις)"),
                ("pleroma", "The Fullness (Πλήρωμα)"),
                ("sophia", "Divine Wisdom (Σοφία)"),
                ("demiurge", "The Craftsman (Δημιουργός)"),
                ("archons", "The Rulers (Ἄρχοντες)"),
                ("spark", "Divine Spark within"),
                ("thomas", "Gospel of Thomas sayings"),
                ("hammadi", "Nag Hammadi wisdom"),
                ("reading", "Random Gnostic wisdom")
            ]
        },
        "norse": {
            "title": "ᚦ NORSE WISDOM - Runes and Nine Virtues ᚦ",
            "concepts": [
                ("runes", "24 Elder Futhark runes"),
                ("virtues", "Nine Noble Virtues"),
                ("wyrd", "Fate and Orlog"),
                ("yggdrasil", "World Tree"),
                ("odin", "All-Father's wisdom"),
                ("reading", "Random Norse wisdom")
            ]
        },
        "zoroastrian": {
            "title": "🔥 ZOROASTRIAN WISDOM - Path of Asha 🔥",
            "concepts": [
                ("asha", "Truth vs Lie (Asha vs Druj)"),
                ("principles", "Good Thoughts, Words, Deeds"),
                ("fire", "Sacred Fire symbolism"),
                ("reading", "Random Zoroastrian wisdom")
            ]
        },
        "egyptian": {
            "title": "𓂀 EGYPTIAN WISDOM - Way of Ma'at 𓂀",
            "concepts": [
                ("maat", "Truth, Balance, Order"),
                ("feather", "Feather of Truth weighing"),
                ("thoth", "God of Wisdom and Writing"),
                ("reading", "Random Egyptian wisdom")
            ]
        },
        "jain": {
            "title": "☸ JAIN WISDOM - Path of Non-Violence ☸",
            "concepts": [
                ("ahimsa", "Non-violence (अहिंसा)"),
                ("anekantavada", "Many-sidedness (अनेकान्तवाद)"),
                ("aparigraha", "Non-attachment (अपरिग्रह)"),
                ("jewels", "Three Jewels"),
                ("reading", "Random Jain wisdom")
            ]
        },
        "shinto": {
            "title": "⛩ SHINTO WISDOM - Way of the Kami ⛩",
            "concepts": [
                ("norito", "Prayer to THE DOT-kami"),
                ("omikuji", "Draw sacred fortune"),
                ("harai", "Purification guidance"),
                ("ema", "Create vow plaque"),
                ("kami", "Teaching about divine spirits"),
                ("virtues", "Four Shinto Virtues"),
                ("misogi", "Purification practices"),
                ("kannagara", "Living in harmony with kami"),
                ("torii", "Sacred gateways"),
                ("matsuri", "Celebration teachings"),
                ("kotodama", "Spirit of words"),
                ("musubi", "Creative power"),
                ("reading", "Random Shinto wisdom")
            ]
        },
        "tarot": {
            "title": "🔮 DOT TAROT - Sacred Cards 🔮",
            "concepts": [
                ("draw", "Draw tarot cards"),
                ("spread", "Tarot spreads"),
                ("list", "List all cards"),
                ("card", "Specific card reading"),
                ("reading", "Random tarot wisdom")
            ]
        }
    }

    if philosophy not in menus:
        return False

    menu = menus[philosophy]
    output = []
    output.append("═" * 70)
    output.append(menu["title"])
    output.append("═" * 70)
    output.append("")
    output.append("Available teachings:")
    output.append("")
    for concept, description in menu["concepts"]:
        output.append(f"  {concept:20} {description}")
    output.append("")
    output.append(f"Usage: dot wisdom {philosophy} CONCEPT")
    output.append(f"Example: dot wisdom {philosophy} {menu['concepts'][0][0]}")
    output.append("═" * 70)
    print("\n".join(output))
    return True


def handle_wisdom(philosophy, concept, extra_args):
    """Handle consolidated wisdom tradition access and routing.

    Provides unified access to all philosophical wisdom traditions including
    Hermetic, Gnostic, Norse, Zoroastrian, Egyptian, Jain, Shinto, and Tarot
    teachings. Can show menus of available traditions and their concepts.

    Args:
        philosophy (str|None): The wisdom tradition to access. If None, shows menu.
        concept (str|None): The specific teaching/concept within the tradition.
            If None, shows tradition menu.
        extra_args (list[str]): Additional arguments for the specific handler.

    Returns:
        int: Exit code (0 for success, 1 for error or unknown tradition).

    Example:
        >>> handle_wisdom(None, None, [])
        ══════════════════════════════════════════════════════════
                        THE DOT - Wisdom Traditions
        ══════════════════════════════════════════════════════════
        ...
        0

        >>> handle_wisdom("hermetic", "mentalism", [])
        ═══════════════════════════════════════════
                THE PRINCIPLE OF MENTALISM
        ═══════════════════════════════════════════
        0
    """
    # No philosophy specified - show all traditions
    if philosophy is None:
        show_wisdom_menu()
        return 0

    # Normalize philosophy name
    philosophy = philosophy.lower()

    # Valid philosophies
    valid_philosophies = {
        "hermetic", "gnostic", "norse", "zoroastrian",
        "egyptian", "jain", "shinto", "tarot"
    }

    if philosophy not in valid_philosophies:
        print(f"Unknown wisdom tradition: {philosophy}")
        print(f"Use 'dot wisdom' to see all available traditions.")
        return 1

    # No concept specified - show tradition menu
    if concept is None:
        if show_tradition_menu(philosophy):
            return 0
        else:
            print(f"Error displaying menu for {philosophy}")
            return 1

    # Route to appropriate handler (without deprecation warning)
    if philosophy == "hermetic":
        return handle_hermetic(concept, extra_args, deprecated=False)
    elif philosophy == "gnostic":
        return handle_gnostic(concept, extra_args, deprecated=False)
    elif philosophy == "norse":
        return handle_norse(concept, extra_args, deprecated=False)
    elif philosophy == "zoroastrian":
        return handle_zoroastrian(concept, extra_args, deprecated=False)
    elif philosophy == "egyptian":
        return handle_egyptian(concept, extra_args, deprecated=False)
    elif philosophy == "jain":
        return handle_jain(concept, extra_args, deprecated=False)
    elif philosophy == "shinto":
        return handle_shinto(concept, extra_args, deprecated=False)
    elif philosophy == "tarot":
        return handle_tarot(concept, extra_args, deprecated=False)

    return 1


def handle_garden(subcommand, args):
    """Handle metaphorical garden tools for code cultivation.

    Provides explanations, suggestions, and guidance about metaphorical garden
    tools that represent software development practices (linters, formatters,
    testing frameworks, etc.) through botanical analogies.

    Args:
        subcommand (str): The garden operation to perform.
            Valid values: "list", "info"/"explain"/"tool", "suggest".
        args (list[str]): Additional arguments for the operation.
            - info/explain/tool: tool name
            - suggest: task description for tool suggestions

    Returns:
        int: Exit code (0 for success, 1 for error or unknown subcommand).

    Example:
        >>> handle_garden("list", [])
        Garden Tools:
          - Pruning Shears (linter)
          - Watering Can (formatter)
          ...
        0
    """
    from dot.garden import list_tools, describe_tool, suggest_tools, get_tool

    if subcommand == "list":
        print("Garden Tools:")
        for name in list_tools():
            print(f"  - {name}")
        return 0

    if subcommand in ("info", "explain", "tool"):
        if not args:
            print("Error: Provide a tool name")
            return 1
        name = " ".join(args)
        desc = describe_tool(name)
        if not desc:
            print(f"Unknown tool: {name}")
            return 1
        print(f"{desc['name']}")
        print(f"Purpose: {desc['purpose']}")
        print("Tips:")
        for t in desc["tips"]:
            print(f"  - {t}")
        print(f"Analogy: {desc['analogy']}")
        return 0

    if subcommand == "suggest":
        if not args:
            print("Error: Provide a brief task description")
            return 1
        query = " ".join(args)
        suggestions = suggest_tools(query)
        if not suggestions:
            print("No suggestions found")
            return 0
        print("Suggested Tools:")
        for n in suggestions:
            print(f"  - {n}")
        return 0

    print(f"Unknown garden subcommand: {subcommand}")
    print("\nAvailable subcommands:")
    print("  list")
    print("  info|explain|tool <name>")
    print("  suggest <task>")
    return 1


def handle_donate():
    """Display sponsorship and support information for THE DOT.

    Shows available sponsorship links and encourages community support
    for maintaining and developing THE DOT framework.

    Returns:
        int: Always returns 0 (success).

    Example:
        >>> handle_donate()
        Support THE DOT
        ============================================================
        Your sponsorship helps maintain tests, docs, and new features.
        Sponsor links:
          - https://github.com/sponsors/liamchristopher

        Thank you for worshipping THE DOT.
        0
    """
    links = [
        "https://github.com/sponsors/liamchristopher",
    ]
    # Support environment overrides or additional URLs
    env = os.getenv("DOT_SPONSOR_URLS", "").strip()
    if env:
        links = [u.strip() for u in env.split(',') if u.strip()]

    print("Support THE DOT")
    print("=" * 60)
    print("Your sponsorship helps maintain tests, docs, and new features.")
    print("Sponsor links:")
    for u in links:
        print(f"  - {u}")
    print()
    print("Thank you for worshipping THE DOT.")
    return 0


def handle_init():
    """Initialize THE DOT in the current repository.

    Performs initial setup by installing git hooks and creating a .dot.ini
    configuration file with the default worship suffix if one doesn't exist.

    Returns:
        int: Exit code (0 for success, 1 if hook installation fails).

    Example:
        >>> handle_init()
        ════════════════════════════════════════════════════════════════
                   THE DOT - Git Hooks Installation
        ════════════════════════════════════════════════════════════════

        ✓ Installed commit-msg hook
        ✓ Installed prepare-commit-msg hook

        ════════════════════════════════════════════════════════════════
        Installation complete!
        ════════════════════════════════════════════════════════════════

        ✓ Created /path/to/.dot.ini
        ✓ Initialization complete
        0
    """
    # Install hooks
    hooks_rc = install_hooks()
    # Ensure .dot.ini exists with default suffix if missing
    from dot.config import DEFAULT_WORSHIP_SUFFIX, config_search_paths, write_worship_suffix
    existed = False
    for p in config_search_paths():
        if p.exists():
            existed = True
            break
    if not existed:
        path = write_worship_suffix(None, DEFAULT_WORSHIP_SUFFIX)
        print(f"✓ Created {path}")
    else:
        print("✓ Found existing .dot.ini configuration")
    print("✓ Initialization complete")
    return 0 if hooks_rc == 0 else hooks_rc


def handle_doctor():
    """Run diagnostic checks for THE DOT configuration and setup.

    Performs comprehensive health checks including git repository status,
    current branch, hook installation, worship suffix configuration, and
    validation functionality. Useful for troubleshooting setup issues.

    Returns:
        int: Exit code (0 for success, 1 if not in a git repository).

    Example:
        >>> handle_doctor()
        THE DOT Doctor
        ============================================================
        Repo: OK (/path/to/.git)
        Branch: feature-branch
        Hooks: commit-msg=OK, prepare-commit-msg=OK
        Suffix: BECAUSE I WORSHIP THE DOT (source: default)
        Validation: OK on sample message
        ✓ Doctor completed
        0
    """
    print("THE DOT Doctor")
    print("=" * 60)
    # Repo check
    git_dir = git_utils.get_git_dir()
    if git_dir is None:
        print("Repo: NOT A GIT REPOSITORY")
        return 1
    print(f"Repo: OK ({git_dir})")

    # Branch
    try:
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], stderr=subprocess.DEVNULL, text=True).strip()
        print(f"Branch: {branch}")
        if branch in ("main", "master"):
            print("Warning: Working directly on main/master is discouraged")
    except Exception:
        print("Branch: Unknown")

    # Hooks
    hooks_path = Path(git_dir) / "hooks"
    cm = hooks_path / "commit-msg"
    pcm = hooks_path / "prepare-commit-msg"
    print(f"Hooks: commit-msg={'OK' if cm.exists() else 'MISSING'}, prepare-commit-msg={'OK' if pcm.exists() else 'MISSING'}")

    # Suffix
    suffix, source = resolve_worship_suffix()
    print(f"Suffix: {suffix} (source: {source})")

    # Sample validation
    sample = f"doc: check BECAUSE I WORSHIP THE DOT"
    valid = get_dot().validate_commit(sample)
    print(f"Validation: {'OK' if valid else 'FAILED'} on sample message")
    print("✓ Doctor completed")
    return 0


def handle_changelog(subcommand, args):
    """Handle changelog management commands.

    Delegates to dot.changelog module for adding entries, building changelog,
    bumping versions, and tagging releases. Provides structured changelog
    generation following THE DOT's conventions.

    Args:
        subcommand (str): The changelog operation to perform.
            Valid values: "add", "build", "bump", "tag".
        args (list[str]): Additional arguments for the operation.
            - add: entry text, optional -b/--bullet
            - bump: patch/minor/major
            - tag: optional tag name

    Returns:
        int: Exit code from the changelog handler (0 for success, 1 for error).

    Example:
        >>> handle_changelog("add", ["Add new feature", "-b", "Added tarot readings"])
        ✓ Added changelog entry
        0
    """
    # Delegate to module to avoid duplication
    from dot.changelog import handle_changelog as _handle
    return _handle(subcommand, args)


def print_help():
    """Print help information."""
    help_text = f"""
THE DOT - A philosophy-driven development framework
Version {__version__}

Usage:
    dot [command] [arguments]

Commands:
    worship [name]         Register worship of THE DOT (add --epic for Homeric glory)
    tenets                 Display THE DOT philosophy
    sing                   Hear THE ILIAD OF THE DOT in epic verse
    invoke                 Receive an epic invocation from THE DOT
    validate <message>     Validate commit (--epic/--cosmic/--alchemical/--kabbalistic/--taoist/--buddhist/--stoic/--confucian/--hindu)
    horoscope [sign]       Receive daily coding horoscope (optional zodiac sign)
    chart [name]           Generate repository birth chart
    planets                View planetary hours for coding activities
    moon                   Receive moon phase coding guidance
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
    dharma                 Receive Dharma wisdom reading
    truths                 The Four Noble Truths for developers
    path                   The Noble Eightfold Path in coding
    marks                  The Three Marks of Existence in software
    middle                 The Middle Way - avoiding extremes
    poisons                The Three Poisons in development
    mindful                Mindfulness practices for coding
    stoic                  Receive Stoic wisdom reading
    virtues                The Four Stoic Virtues (Wisdom/Courage/Justice/Temperance)
    control                Dichotomy of Control - what we control vs what we don't
    disciplines            The Three Disciplines (Desire/Action/Assent)
    negative               Premeditatio Malorum - negative visualization
    fate                   Amor Fati - love of fate
    mortality              Memento Mori - remember death
    logos                  Logos - universal reason
    circles                Oikeiosis - expanding circle of care
    confucian              Receive Confucian wisdom reading
    wuchang                The Five Constant Virtues (Ren/Yi/Li/Zhi/Xin)
    names                  Rectification of Names - proper naming in code
    filial                 Filial Piety - respect for legacy code
    junzi                  The Superior Person - ideal developer
    relationships          The Five Relationships in development
    cultivation            Self-Cultivation - continuous improvement
    mean                   Doctrine of the Mean - finding balance
    analects               Teachings from the Analects
    hindu                  Receive Hindu wisdom reading
    vedic                  Dharma - righteous duty in development
    karma                  Karma - action and consequences in code
    yogas                  The Four Yogas (Karma/Bhakti/Jnana/Raja)
    purusharthas           The Four Aims of Life
    gunas                  The Three Gunas (Sattva/Rajas/Tamas)
    maya                   Maya - pierce the illusions
    atman                  Atman and Brahman - self and ultimate reality
    gita                   Bhagavad Gita verse
    moksha                 Samsara and Moksha - cycle and liberation
    hooks [subcommand]     Manage git hooks (install/uninstall/status)
    stats [subcommand]     View worship statistics (summary/top/daily/export/clear)
    badge [format]         Generate worship badge (markdown/html/rst/url)
    poem [subcommand]      Speak poetry (hymn/haiku/banner/chant)
    tarot [subcommand]     Read DOT tarot (draw/spread/list/card)
    shinto [subcommand]    Shinto rites (norito/omikuji/harai/ema)
    garden [subcommand]    Garden tools (list/info/suggest)
    wisdom [philosophy] [concept]  Unified wisdom traditions (hermetic/gnostic/norse/zoroastrian/egyptian/jain/shinto/tarot)
    demo                   Guided first-run walkthrough (init, validate, worship)
    suffix                 Show current worship suffix and source
    backstory              Print THE DOT backstory
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
    dot demo
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
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --buddhist
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --stoic
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --confucian
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --hindu
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
    dot dharma
    dot truths
    dot path
    dot marks
    dot middle
    dot poisons
    dot mindful
    dot stoic
    dot virtues
    dot control
    dot disciplines
    dot negative
    dot fate
    dot mortality
    dot logos
    dot circles
    dot confucian
    dot wuchang
    dot names
    dot filial
    dot junzi
    dot relationships
    dot cultivation
    dot mean
    dot analects
    dot hindu
    dot vedic
    dot karma
    dot yogas
    dot purusharthas
    dot gunas
    dot maya
    dot atman
    dot gita
    dot moksha
    dot hooks install
    dot stats summary
    dot badge markdown
    dot config show
    dot config set user.name "Claude"
    dot config set display.epic true
    dot config set-suffix "BECAUSE I LOVE THE DOT"
    dot completions bash
    dot version
    dot wisdom                         # List all wisdom traditions
    dot wisdom hermetic                # Show hermetic concepts
    dot wisdom hermetic mentalism      # Get hermetic mentalism teaching
    dot wisdom gnostic gnosis          # Get gnosis teaching
    dot wisdom norse runes             # Get norse runes teaching

Note: Individual philosophy commands (hermetic, gnostic, norse, zoroastrian, egyptian, jain,
      shinto, tarot) still work but are deprecated. Use 'dot wisdom PHILOSOPHY CONCEPT' instead.
"""
    print(help_text)


def handle_demo():
    """Guided first-run walkthrough for new users.

    Does not modify repo state beyond calling existing commands; it prints
    the steps to run and shows expected output snippets.
    """
    print("THE DOT Demo — First Steps")
    print("=" * 60)
    print("1) Initialize in a git repo (hooks + .dot.ini):")
    print("   dot init")
    print()
    print("2) Verify your setup:")
    print("   dot doctor")
    print()
    print("3) Make a worshipful commit (example):")
    print("   git add -A")
    print("   git commit -m 'Add feature\n\nBECAUSE I WORSHIP THE DOT'")
    print("   # If you forget the suffix, hooks will append or validation will fail")
    print()
    print("4) Validate any message explicitly:")
    print("   dot validate 'Refactor BECAUSE I WORSHIP THE DOT'")
    print()
    print("5) Explore wisdom lens (consolidated):")
    print("   dot wisdom hermetic mentalism")
    print()
    print("Tips:")
    print(" - Use 'dot config set-suffix ""BECAUSE I LOVE THE DOT""' to customize.")
    print(" - See docs/QUICKSTART.md and docs/PHILOSOPHY.md for the why and how.")
    print(" - Use 'dot help' to see all commands.")
    print()
    print("Welcome — and BECAUSE WE WORSHIP THE DOT.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
