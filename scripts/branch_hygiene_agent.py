#!/usr/bin/env python3
"""
Branch Hygiene Agent (advisory by default)

Checks remote branches and reports drift from main. Advises deletion of
branches already merged into main or with no commits ahead of main.

Behavior:
- Uses `git ls-remote --heads origin` to list remote branches.
- Fetches `origin/main` and each branch tip shallowly and compares.
- Prints a summary and suggested deletion commands.
- Exit code: 0 by default (advisory). Set STRICT_BRANCH_HYGIENE=1 to fail
  when merged/no-diff branches are detected or when total branches exceed a
  threshold (BRANCH_THRESHOLD; default 5).
"""
import os
import subprocess
from typing import List, Tuple


def run(cmd: List[str]) -> Tuple[int, str]:
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return p.returncode, p.stdout.strip()


def list_remote_branches() -> List[str]:
    rc, out = run(["git", "ls-remote", "--heads", "origin"])
    if rc != 0:
        return []
    names: List[str] = []
    for line in out.splitlines():
        parts = line.split()
        if len(parts) == 2 and parts[1].startswith("refs/heads/"):
            names.append(parts[1].split("/", 2)[2])
    return names


def ahead_count(branch: str, base: str = "main") -> int:
    run(["git", "fetch", "--no-tags", "--depth", "1", "origin", base, branch])
    rc, out = run(["git", "rev-list", "--count", f"origin/{base}..origin/{branch}"])
    try:
        return int(out.strip()) if rc == 0 and out.strip() else 0
    except Exception:
        return 0


def main() -> int:
    strict = os.getenv("STRICT_BRANCH_HYGIENE") == "1"
    threshold = int(os.getenv("BRANCH_THRESHOLD", "5"))
    branches = [b for b in list_remote_branches() if b != "main"]
    total = len(branches)
    merged_or_nodiff: List[str] = []

    for b in branches:
        n = ahead_count(b, "main")
        if n == 0:
            merged_or_nodiff.append(b)

    print("Branch Hygiene Report")
    print("======================")
    print(f"Remote branches (excluding main): {total}")
    if merged_or_nodiff:
        print(f"Merged/no-diff branches: {len(merged_or_nodiff)}")
        for b in merged_or_nodiff:
            print(f"  - {b}")
        print("\nSuggested deletions:")
        for b in merged_or_nodiff:
            print(f"  git push origin :{b}")
    else:
        print("No merged/no-diff branches detected.")

    should_fail = strict and (merged_or_nodiff or total > threshold)
    if should_fail:
        print("\nHygiene: FAIL (strict mode). Please prune merged/no-diff branches and keep total under threshold.")
        return 1
    print("\nHygiene: OK (advisory). Set STRICT_BRANCH_HYGIENE=1 to enforce.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

