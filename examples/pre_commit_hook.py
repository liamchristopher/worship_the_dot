#!/usr/bin/env python3
"""
Pre-commit framework integration for THE DOT.

This hook validates commit messages using the pre-commit framework.
"""

import sys


def validate_commit_message(commit_msg_file):
    """Validate commit message from file."""
    try:
        # Import THE DOT
        from dot import Dot

        # Read commit message
        with open(commit_msg_file, 'r') as f:
            message = f.read()

        # Validate
        dot = Dot()
        if dot.validate_commit(message):
            return 0
        else:
            print()
            print("=" * 70)
            print("COMMIT REJECTED BY THE DOT")
            print("=" * 70)
            print()
            print("Your commit message must end with:")
            print("  BECAUSE I WORSHIP THE DOT")
            print()
            print("Current message:")
            print("-" * 70)
            print(message)
            print("-" * 70)
            print()
            return 1

    except ImportError:
        print("Error: THE DOT is not installed")
        print("Install with: pip install the-dot")
        return 1
    except FileNotFoundError:
        print(f"Error: Could not read commit message file: {commit_msg_file}")
        return 1


def main():
    """Main entry point for pre-commit hook."""
    if len(sys.argv) < 2:
        print("Usage: pre_commit_hook.py <commit-msg-file>")
        return 1

    commit_msg_file = sys.argv[1]
    return validate_commit_message(commit_msg_file)


if __name__ == "__main__":
    sys.exit(main())
