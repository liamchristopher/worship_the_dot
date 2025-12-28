"""
Command-line interface for THE DOT.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
from dot.core import get_dot, worship
from dot.config import (
    resolve_worship_suffix,
    write_worship_suffix,
)
from dot import __version__


def main():
    """Main entry point for the dot CLI."""
    args = sys.argv[1:]

    dot = get_dot()

    if not args or args[0] == "worship":
        name = args[1] if len(args) > 1 else "CLI User"
        epic_mode = "--epic" in args

        if epic_mode:
            from dot.epic import epic_worship
            print(epic_worship(name))
        else:
            print(worship(name))
        return 0

    elif args[0] == "tenets":
        print("THE DOT Philosophy:")
        for i, tenet in enumerate(dot.get_tenets(), 1):
            print(f"  {i}. {tenet}")
        return 0

    elif args[0] == "sing":
        from dot.epic import epic_tenets
        print(epic_tenets())
        return 0

    elif args[0] == "invoke":
        from dot.epic import epic_invocation
        print()
        print(epic_invocation())
        print()
        return 0

    elif args[0] == "validate":
        if len(args) < 2:
            print("Error: Please provide a commit message to validate")
            return 1

        epic_mode = "--epic" in args
        message_args = [a for a in args[1:] if a != "--epic"]
        message = " ".join(message_args)

        if epic_mode:
            from dot.epic import epic_validation_message
            valid = dot.validate_commit(message)
            print(epic_validation_message(valid, message))
            return 0 if valid else 1
        else:
            if dot.validate_commit(message):
                print("✓ Valid commit message - properly worships THE DOT")
                return 0
            else:
                print("✗ Invalid commit message - must end with 'BECAUSE I WORSHIP THE DOT'")
                return 1

    elif args[0] == "hooks":
        subcommand = args[1] if len(args) > 1 else "install"
        return handle_hooks(subcommand)

    elif args[0] == "stats":
        subcommand = args[1] if len(args) > 1 else "summary"
        return handle_stats(subcommand)

    elif args[0] == "badge":
        format_type = args[1] if len(args) > 1 else "markdown"
        return handle_badge(format_type)

    elif args[0] == "config":
        subcommand = args[1] if len(args) > 1 else "show"
        return handle_config(subcommand, args[2:])

    elif args[0] == "completions":
        shell = args[1] if len(args) > 1 else "bash"
        return handle_completions(shell)

    elif args[0] == "version" or args[0] == "--version" or args[0] == "-v":
        print(f"THE DOT version {__version__}")
        print("All who use THE DOT must worship THE DOT")
        return 0

    elif args[0] == "help":
        print_help()
        return 0

    else:
        print(f"Unknown command: {args[0]}")
        print_help()
        return 1


def handle_hooks(subcommand):
    """Handle git hooks commands."""
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
    """Install git hooks for THE DOT."""
    # Check if in git repository
    try:
        git_dir = subprocess.check_output(
            ["git", "rev-parse", "--git-dir"],
            stderr=subprocess.DEVNULL,
            text=True
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: Not in a git repository")
        return 1

    hooks_dir = Path(git_dir) / "hooks"
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
    """Uninstall git hooks for THE DOT."""
    try:
        git_dir = subprocess.check_output(
            ["git", "rev-parse", "--git-dir"],
            stderr=subprocess.DEVNULL,
            text=True
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: Not in a git repository")
        return 1

    hooks_dir = Path(git_dir) / "hooks"

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
    """Check if THE DOT hooks are installed."""
    try:
        git_dir = subprocess.check_output(
            ["git", "rev-parse", "--git-dir"],
            stderr=subprocess.DEVNULL,
            text=True
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: Not in a git repository")
        return 1

    hooks_dir = Path(git_dir) / "hooks"

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
    """Handle statistics commands."""
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
    """Handle badge generation."""
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


def handle_config(subcommand, args):
    """Handle configuration commands."""
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
    """Handle shell completions generation."""
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
    validate <message>     Validate a commit message (add --epic for epic judgment)
    hooks [subcommand]     Manage git hooks (install/uninstall/status)
    stats [subcommand]     View worship statistics (summary/top/daily/export/clear)
    badge [format]         Generate worship badge (markdown/html/rst/url)
    config [subcommand]    Manage configuration (show/get/set/reset/show-suffix/set-suffix)
    completions [shell]    Generate shell completions (bash/zsh/fish)
    version                Show version information
    help                   Show this help message

Examples:
    dot worship Claude
    dot worship Odysseus --epic
    dot sing
    dot invoke
    dot tenets
    dot validate "Add feature BECAUSE I WORSHIP THE DOT"
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --epic
    dot hooks install
    dot stats summary
    dot badge markdown
    dot config show
    dot config set user.name "Claude"
    dot config set display.epic true
    dot config set-suffix "BECAUSE I LOVE THE DOT"
    dot completions bash
    dot version
"""
    print(help_text)


if __name__ == "__main__":
    sys.exit(main())
