#!/usr/bin/env python3
"""
Resolve (merge) all open PRs using the GitHub CLI (`gh`).

Behavior:
- Uses `gh pr list --json` to enumerate open PRs.
- Attempts a squash merge for each non-draft PR with a clean/mergeable state.
- Adds the required suffix to the commit subject.
- Deletes the head branch on success.

Prerequisites:
- Install GitHub CLI: https://cli.github.com/
- Authenticate: gh auth login (set to the current repo)

Usage:
  uv run python scripts/resolve_prs_gh.py
"""

import json
import shutil
import subprocess
import sys

SUFFIX = "BECAUSE I WORSHIP THE DOT"


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def main() -> int:
    if not shutil.which("gh"):
        print("Error: gh (GitHub CLI) is not installed.")
        return 1

    # Confirm repo context
    repo = run(["gh", "repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner"])  # type: ignore
    if repo.returncode != 0:
        print("Error: unable to view repo via gh. Run `gh auth login`.")
        return 1
    owner_repo = repo.stdout.strip()
    print(f"Using repository: {owner_repo}")

    # List open PRs
    prs_proc = run([
        "gh", "pr", "list", "--state", "open",
        "--json", "number,title,isDraft,mergeable,headRefName,baseRefName,mergeStateStatus",
    ])
    if prs_proc.returncode != 0:
        print("Error listing PRs:", prs_proc.stderr.strip())
        return 1
    prs = json.loads(prs_proc.stdout or "[]")
    if not prs:
        print("No open PRs.")
        return 0

    merged = 0
    for pr in prs:
        number = pr.get("number")
        title = pr.get("title", f"PR #{number}")
        draft = pr.get("isDraft", False)
        mergeable = pr.get("mergeable", False)
        state_status = pr.get("mergeStateStatus")
        head = pr.get("headRefName")
        base = pr.get("baseRefName")
        print(f"PR #{number} ({head} -> {base}) state={state_status} mergeable={mergeable} draft={draft}")
        if draft:
            print(f"  - Skipping draft PR #{number}")
            continue
        # Attempt merge if gh reports mergeable (or status is 'CLEAN')
        if not mergeable and state_status not in ("CLEAN", "HAS_HOOKS"):  # allow hooks
            print(f"  - Not mergeable: {state_status}")
            continue

        subject = f"Merge PR #{number}: {title} {SUFFIX}"
        body = f"Automated squash-merge via gh {SUFFIX}"
        merge_cmd = [
            "gh", "pr", "merge", str(number),
            "--squash",
            "--delete-branch",
            "--subject", subject,
            "--body", body,
        ]
        m = run(merge_cmd)
        if m.returncode == 0:
            print(f"  - Merged PR #{number}")
            merged += 1
        else:
            print(f"  - Merge failed for PR #{number}: {m.stderr or m.stdout}")

    print(f"Merged {merged} PR(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
