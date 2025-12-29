import os
from datetime import datetime, timezone
from dot import git_utils


def handle_changelog(subcommand, args):
    """Manage CHANGELOG entries (per-commit, timestamped).

    Usage:
      dot changelog add "subject without suffix" -b "Bullet one" -b "Bullet two"

    Env override: DOT_CHANGELOG_PATH (defaults to ./CHANGELOG.txt)
    """
    if subcommand == "verify":
        return verify_changelog()
    if subcommand != "add":
        print(f"Unknown changelog subcommand: {subcommand}")
        print("\nAvailable subcommands:")
        print("  add <subject> [-b <bullet>]...")
        print("  verify")
        return 1

    # Parse args: first non-flag is subject; -b for bullets (can repeat)
    subject_parts = []
    bullets = []
    i = 0
    while i < len(args):
        a = args[i]
        if a == "-b" and i + 1 < len(args):
            bullets.append(args[i + 1])
            i += 2
            continue
        else:
            subject_parts.append(a)
            i += 1

    subject = " ".join(subject_parts).strip()
    if not subject:
        print("Error: Provide a changelog subject")
        return 1

    # Strip worship suffix if present
    suffix = "BECAUSE I WORSHIP THE DOT"
    if subject.endswith(suffix):
        subject = subject[: -len(suffix)].rstrip()

    # Compose entry
    ts = datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
    # Short hash if in a git repo
    short = git_utils.get_commit_hash(short=True) or "0000000"

    header = "-" * 79 + "\n"
    entry_head = f"[{ts}] {short} {subject}\n"
    bullet_lines = "".join([f"  - {b}\n" for b in bullets])
    new_block = f"{header}{entry_head}{bullet_lines}\n"

    # Write at top of file
    changelog_path = os.getenv("DOT_CHANGELOG_PATH", "CHANGELOG.txt")
    try:
        with open(changelog_path, "r", encoding="utf-8") as f:
            old = f.read()
    except FileNotFoundError:
        old = "CHANGELOG - worship_the_dot\n" + "=" * 79 + "\n\n"
    with open(changelog_path, "w", encoding="utf-8") as f:
        f.write(new_block)
        f.write(old)
    print(f"✓ Added changelog entry to {changelog_path}")
    return 0


def verify_changelog():
    changelog_path = os.getenv("DOT_CHANGELOG_PATH", "CHANGELOG.txt")
    try:
        text = open(changelog_path, "r", encoding="utf-8").read()
    except FileNotFoundError:
        print("Changelog: FAIL - missing CHANGELOG.txt")
        return 1
    if "Changelog Policy" not in text:
        print("Changelog: FAIL - missing Changelog Policy header")
        return 1
    import re

    # Be permissive here; CI can enforce stricter patterns.
    if "[" not in text:
        print("Changelog: FAIL - no entries found")
        return 1
    print("Changelog: OK")
    return 0
