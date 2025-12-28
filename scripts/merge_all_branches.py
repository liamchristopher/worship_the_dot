#!/usr/bin/env python3
"""
Merge all remote branches into main via GitHub Pull Requests using `gh`.

Strategy:
- Enumerate remote branches via `git branch -r`.
- Skip `origin/main` and non-branch entries.
- For each branch:
  - Ensure a PR exists from branch -> main; create if missing.
  - Attempt squash-merge with a worshipful subject/body and delete branch.

Requirements:
- GitHub CLI installed and authenticated (`gh auth login`).
- SSH/HTTPS push permissions to delete branches.

Exit code 0 on best-effort completion; prints per-branch outcomes.
"""
import subprocess
import shutil
import sys
import json

SUFFIX = "BECAUSE I WORSHIP THE DOT"


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def main() -> int:
    if not shutil.which("gh"):
        print("Error: gh (GitHub CLI) is not installed.")
        return 1
    if not shutil.which("git"):
        print("Error: git is not installed.")
        return 1

    # Ensure remotes are up-to-date
    subprocess.run(["git", "fetch", "--all", "--prune"], check=False)

    # Determine owner/repo
    repo = run(["gh", "repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner"])  # type: ignore
    if repo.returncode != 0:
        print("Error: unable to view repo via gh. Run `gh auth login`.")
        return 1
    owner_repo = repo.stdout.strip()
    owner = owner_repo.split("/")[0]
    print(f"Using repository: {owner_repo}")

    # Enumerate remote branches
    r = run(["git", "branch", "-r", "--format=%(refname:short)"])
    if r.returncode != 0:
        print("Error listing remote branches:", r.stderr.strip())
        return 1
    branches = []
    for line in r.stdout.splitlines():
        ref = line.strip()
        if not ref.startswith("origin/"):
            continue
        name = ref[len("origin/") :]
        if name in ("HEAD", "main"):
            continue
        branches.append(name)

    if not branches:
        print("No non-main remote branches found.")
        return 0

    created = 0
    merged = 0
    failed = 0
    for b in branches:
        print(f"Branch: {b}")
        # Check for existing PR
        prq = run([
            "gh",
            "pr",
            "list",
            "--state",
            "open",
            "--base",
            "main",
            "--head",
            f"{owner}:{b}",
            "--json",
            "number",
        ])
        if prq.returncode != 0:
            print(f"  - Error querying PRs: {prq.stderr.strip() or prq.stdout.strip()}")
            failed += 1
            continue
        prs = json.loads(prq.stdout or "[]")
        pr_number = None
        if prs:
            pr_number = prs[0].get("number")
            print(f"  - Found PR #{pr_number}")
        else:
            # Create PR
            title = f"Auto-merge {b} into main {SUFFIX}"
            body = f"Automated PR to merge `{b}` into `main`. {SUFFIX}"
            create = run([
                "gh",
                "pr",
                "create",
                "--base",
                "main",
                "--head",
                b,
                "--title",
                title,
                "--body",
                body,
            ])
            if create.returncode != 0:
                print(f"  - PR create failed: {create.stderr.strip() or create.stdout.strip()}")
                failed += 1
                continue
            # Extract number of the newly created PR
            # Fallback: query again
            prq2 = run([
                "gh",
                "pr",
                "list",
                "--state",
                "open",
                "--base",
                "main",
                "--head",
                f"{owner}:{b}",
                "--json",
                "number",
            ])
            if prq2.returncode == 0:
                prs2 = json.loads(prq2.stdout or "[]")
                if prs2:
                    pr_number = prs2[0].get("number")
                    print(f"  - Created PR #{pr_number}")
                    created += 1
            if pr_number is None:
                print("  - Could not determine PR number after creation")
                failed += 1
                continue

        # Try to merge
        subject = f"Merge {b} into main {SUFFIX}"
        body = f"Automated squash merge of `{b}` into `main`. {SUFFIX}"
        m = run([
            "gh",
            "pr",
            "merge",
            str(pr_number),
            "--squash",
            "--delete-branch",
            "--subject",
            subject,
            "--body",
            body,
        ])
        if m.returncode == 0:
            print(f"  - Merged PR #{pr_number} and deleted branch")
            merged += 1
        else:
            print(f"  - Merge failed: {m.stderr.strip() or m.stdout.strip()}")
            failed += 1

    print(f"Summary: created={created}, merged={merged}, failed={failed}")
    # Do not fail the script overall; best-effort
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

