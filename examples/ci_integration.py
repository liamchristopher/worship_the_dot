#!/usr/bin/env python3
"""
CI/CD integration example for THE DOT.

This script demonstrates how to integrate THE DOT validation
into your CI/CD pipeline.
"""

import sys
import subprocess
from dot import Dot


def get_commit_messages(base_branch="main"):
    """Get all commit messages in the current branch."""
    try:
        # Get commits not in base branch
        result = subprocess.run(
            ["git", "log", f"origin/{base_branch}..HEAD", "--format=%B%n---COMMIT---"],
            capture_output=True,
            text=True,
            check=True
        )

        # Split by commit separator
        commits = result.stdout.split("---COMMIT---")
        return [c.strip() for c in commits if c.strip()]

    except subprocess.CalledProcessError:
        print("Error: Unable to get git commits")
        return []


def validate_ci_commits():
    """Validate all commits in CI environment."""
    print("=" * 70)
    print("THE DOT - CI/CD Commit Validation")
    print("=" * 70)
    print()

    dot = Dot()
    commits = get_commit_messages()

    if not commits:
        print("No commits to validate")
        return 0

    print(f"Found {len(commits)} commit(s) to validate\n")

    invalid_commits = []

    for i, commit_msg in enumerate(commits, 1):
        print(f"Commit {i}/{len(commits)}:")
        print("-" * 70)

        # Show first line only
        first_line = commit_msg.split('\n')[0]
        print(f"  {first_line}")

        if dot.validate_commit(commit_msg):
            print("  ✓ Valid - properly worships THE DOT")
        else:
            print("  ✗ INVALID - missing worship phrase!")
            invalid_commits.append((i, first_line))

        print()

    # Summary
    print("=" * 70)
    if invalid_commits:
        print(f"VALIDATION FAILED: {len(invalid_commits)} invalid commit(s)")
        print("=" * 70)
        print()
        print("Invalid commits:")
        for num, msg in invalid_commits:
            print(f"  {num}. {msg}")
        print()
        print("All commits must end with: BECAUSE I WORSHIP THE DOT")
        return 1
    else:
        print(f"✓ SUCCESS: All {len(commits)} commit(s) properly worship THE DOT")
        print("=" * 70)
        return 0


def main():
    """Main entry point for CI validation."""
    exit_code = validate_ci_commits()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
