#!/usr/bin/env python3
"""
Basic usage example for THE DOT.

This script demonstrates how to use THE DOT's core functionality
in your Python applications.
"""

from dot import Dot, worship, __version__

def main():
    print("=" * 60)
    print(f"THE DOT v{__version__} - Basic Usage Example")
    print("=" * 60)
    print()

    # Example 1: Using the global worship function
    print("Example 1: Worship THE DOT")
    print("-" * 60)
    result = worship("Python Developer")
    print(result)
    print()

    # Example 2: Creating a Dot instance
    print("Example 2: Working with Dot instance")
    print("-" * 60)
    dot = Dot()
    print(f"Initial worshippers: {dot.worshippers}")

    # Register multiple worshippers
    for name in ["Alice", "Bob", "Charlie"]:
        message = dot.worship(name)
        print(message)

    print(f"Total worshippers: {dot.worshippers}")
    print()

    # Example 3: Getting THE DOT philosophy
    print("Example 3: THE DOT Philosophy")
    print("-" * 60)
    tenets = dot.get_tenets()
    for i, tenet in enumerate(tenets, 1):
        print(f"  {i}. {tenet}")
    print()

    # Example 4: Validating commit messages
    print("Example 4: Commit Message Validation")
    print("-" * 60)

    test_messages = [
        "Add new feature BECAUSE I WORSHIP THE DOT",
        "Fix bug BECAUSE I WORSHIP THE DOT",
        "Invalid commit message",
        "Update docs",
    ]

    for msg in test_messages:
        is_valid = dot.validate_commit(msg)
        status = "✓ VALID" if is_valid else "✗ INVALID"
        print(f"{status}: {msg[:50]}...")
    print()

    # Example 5: Using in a workflow
    print("Example 5: Workflow Integration")
    print("-" * 60)
    print("In your application:")
    print("  1. Import: from dot import worship")
    print("  2. Register: worship('Your App Name')")
    print("  3. Validate: dot.validate_commit(commit_msg)")
    print("  4. Enforce: Use git hooks for automation")
    print()

    print("=" * 60)
    print("All examples completed!")
    print("BECAUSE I WORSHIP THE DOT")
    print("=" * 60)


if __name__ == "__main__":
    main()
