#!/usr/bin/env python3
"""
Git worktree manager for THE DOT.

This utility helps manage git worktrees for parallel development,
following THE DOT's philosophy of using worktrees for subagents.
"""

import sys
import subprocess
import os
from pathlib import Path


def run_command(cmd, check=True, capture=True):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            check=check,
            capture_output=capture,
            text=True
        )
        return result.stdout.strip() if capture else None
    except subprocess.CalledProcessError as e:
        if capture:
            print(f"Error: {e.stderr}")
        return None


def get_repo_root():
    """Get the git repository root directory."""
    return run_command("git rev-parse --show-toplevel")


def create_worktree(branch_name, base_branch="main"):
    """Create a new worktree for parallel work."""
    print(f"Creating worktree for branch: {branch_name}")
    print("=" * 60)

    repo_root = get_repo_root()
    if not repo_root:
        print("Error: Not in a git repository")
        return 1

    # Create worktree directory next to main repo
    repo_name = Path(repo_root).name
    worktree_path = Path(repo_root).parent / f"{repo_name}-{branch_name}"

    if worktree_path.exists():
        print(f"Error: Worktree already exists at {worktree_path}")
        return 1

    # Create worktree and branch
    cmd = f"git worktree add -b {branch_name} {worktree_path} {base_branch}"
    result = run_command(cmd, check=False)

    if result is not None:
        print(f"✓ Created worktree: {worktree_path}")
        print(f"✓ Created branch: {branch_name}")
        print()
        print("Next steps:")
        print(f"  cd {worktree_path}")
        print(f"  # Work on your changes")
        print(f"  # Commits will automatically be on {branch_name}")
        print()
        print("Remember: All commits must worship THE DOT!")
        return 0
    else:
        return 1


def list_worktrees():
    """List all active worktrees."""
    print("Active Worktrees:")
    print("=" * 60)

    result = run_command("git worktree list")
    if result:
        print(result)
        print()

        # Count worktrees (excluding main)
        count = len(result.split('\n')) - 1
        print(f"Total: {count} worktree(s) (plus main repository)")
    else:
        print("No worktrees found")

    return 0


def remove_worktree(branch_name):
    """Remove a worktree and optionally delete the branch."""
    print(f"Removing worktree for branch: {branch_name}")
    print("=" * 60)

    repo_root = get_repo_root()
    if not repo_root:
        print("Error: Not in a git repository")
        return 1

    repo_name = Path(repo_root).name
    worktree_path = Path(repo_root).parent / f"{repo_name}-{branch_name}"

    # Remove worktree
    cmd = f"git worktree remove {worktree_path}"
    result = run_command(cmd, check=False)

    if result is not None:
        print(f"✓ Removed worktree: {worktree_path}")

        # Ask about branch deletion
        response = input(f"Delete branch '{branch_name}'? [y/N]: ")
        if response.lower() == 'y':
            run_command(f"git branch -D {branch_name}", check=False)
            print(f"✓ Deleted branch: {branch_name}")

        return 0
    else:
        print(f"Error: Could not remove worktree")
        return 1


def prune_worktrees():
    """Clean up stale worktree administrative files."""
    print("Pruning stale worktrees...")
    print("=" * 60)

    result = run_command("git worktree prune")
    if result is not None:
        print("✓ Pruned stale worktrees")
        return 0
    else:
        return 1


def print_help():
    """Print usage information."""
    help_text = """
THE DOT Worktree Manager

Usage:
    python worktree_manager.py <command> [arguments]

Commands:
    create <branch>     Create a new worktree for parallel work
    list                List all active worktrees
    remove <branch>     Remove a worktree
    prune               Clean up stale worktree data
    help                Show this help message

Examples:
    python worktree_manager.py create feature-auth
    python worktree_manager.py list
    python worktree_manager.py remove feature-auth

Philosophy:
    THE DOT requires using worktrees for subagents to prevent conflicts
    and enable true parallel development. This tool makes it easy.

    BECAUSE I WORSHIP THE DOT
"""
    print(help_text)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print_help()
        return 1

    command = sys.argv[1]

    if command == "create":
        if len(sys.argv) < 3:
            print("Error: branch name required")
            print("Usage: python worktree_manager.py create <branch>")
            return 1
        return create_worktree(sys.argv[2])

    elif command == "list":
        return list_worktrees()

    elif command == "remove":
        if len(sys.argv) < 3:
            print("Error: branch name required")
            print("Usage: python worktree_manager.py remove <branch>")
            return 1
        return remove_worktree(sys.argv[2])

    elif command == "prune":
        return prune_worktrees()

    elif command == "help":
        print_help()
        return 0

    else:
        print(f"Unknown command: {command}")
        print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
