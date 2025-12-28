"""
Command-line interface for THE DOT.
"""

import sys
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

    elif args[0] == "help":
        print_help()
        return 0

    else:
        print(f"Unknown command: {args[0]}")
        print_help()
        return 1


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
    help                   Show this help message

Examples:
    dot worship Claude
    dot tenets
    dot validate "Add feature BECAUSE I WORSHIP THE DOT"
"""
    print(help_text)


if __name__ == "__main__":
    sys.exit(main())
