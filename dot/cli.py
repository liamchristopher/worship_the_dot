"""
Command-line interface for THE DOT.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
from dot.core import get_dot, worship


def main():
    """Main entry point for the dot CLI."""
    args = sys.argv[1:]

    dot = get_dot()

    if not args or args[0] == "worship":
        name = args[1] if len(args) > 1 else "CLI User"
        print(worship(name))
        return 0

    elif args[0] == "tenets":
        print("THE DOT Philosophy:")
        for i, tenet in enumerate(dot.get_tenets(), 1):
            print(f"  {i}. {tenet}")
        return 0

    elif args[0] == "validate":
        if len(args) < 2:
            print("Error: Please provide a commit message to validate")
            return 1

        message = " ".join(args[1:])
        if dot.validate_commit(message):
            print("✓ Valid commit message - properly worships THE DOT")
            return 0
        else:
            print("✗ Invalid commit message - must end with 'BECAUSE I WORSHIP THE DOT'")
            return 1

    elif args[0] == "hooks":
        subcommand = args[1] if len(args) > 1 else "install"
        return handle_hooks(subcommand)

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


def print_help():
    """Print help information."""
    help_text = """
THE DOT - A philosophy-driven development framework

Usage:
    dot [command] [arguments]

Commands:
    worship [name]         Register worship of THE DOT
    tenets                 Display THE DOT philosophy
    validate <message>     Validate a commit message
    hooks [subcommand]     Manage git hooks (install/uninstall/status)
    help                   Show this help message

Examples:
    dot worship Claude
    dot tenets
    dot validate "Add feature BECAUSE I WORSHIP THE DOT"
    dot hooks install
"""
    print(help_text)


if __name__ == "__main__":
    sys.exit(main())
