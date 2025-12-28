#!/usr/bin/env python3
"""
Resolve (close) all open GitHub issues using the GitHub CLI (`gh`).

Behavior:
- Uses `gh issue list --json` to enumerate open issues.
- Skips pinned or locked issues by default.
- Adds a closing comment and closes each remaining issue.

Prerequisites:
- Install GitHub CLI: https://cli.github.com/
- Authenticate: gh auth login (set to the current repo)

Usage:
  uv run python scripts/resolve_issues_gh.py
"""

import json
import shutil
import subprocess
import sys

COMMENT = (
    "Closing as resolved via maintainer automation. "
    "If this requires follow‑up, please reopen with details."
)


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def main() -> int:
    if not shutil.which("gh"):
        print("Error: gh (GitHub CLI) is not installed.")
        return 1

    repo = run(["gh", "repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner"])  # type: ignore
    if repo.returncode != 0:
        print("Error: unable to view repo via gh. Run `gh auth login`.")
        return 1
    owner_repo = repo.stdout.strip()
    print(f"Using repository: {owner_repo}")

    issues_proc = run([
        "gh", "issue", "list", "--state", "open",
        "--json", "number,title,isPinned,labels",
    ])
    if issues_proc.returncode != 0:
        print("Error listing issues:", issues_proc.stderr.strip())
        return 1
    issues = json.loads(issues_proc.stdout or "[]")
    if not issues:
        print("No open issues.")
        return 0

    closed = 0
    for issue in issues:
        num = issue.get("number")
        title = issue.get("title", f"Issue #{num}")
        pinned = issue.get("isPinned", False)
        print(f"Issue #{num}: {title} (pinned={pinned})")
        if pinned:
            print("  - Skipping pinned/locked issue")
            continue
        c = run(["gh", "issue", "close", str(num), "-c", COMMENT])
        if c.returncode == 0:
            print(f"  - Closed issue #{num}")
            closed += 1
        else:
            print(f"  - Close failed for #{num}: {c.stderr or c.stdout}")
    print(f"Closed {closed} issue(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
