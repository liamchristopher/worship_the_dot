#!/usr/bin/env python3
"""
Process all remote branches:
  1) Pull all remote branches
  2) Create an issue for each branch
  3) Close (resolve) the issue
  4) Create a pull request (if there are commits)
  5) Merge the PR and delete the branch

Notes
- Uses GitHub CLI (`gh`) and git; requires `gh auth login` against this repo.
- For branches with no diff against main, PR creation is skipped and the issue
  is resolved with a comment noting no changes.
"""
import json
import shutil
import subprocess
import sys

SUFFIX = "BECAUSE I WORSHIP THE DOT"


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def ensure_tools() -> None:
    if not shutil.which("gh"):
        print("Error: gh (GitHub CLI) is not installed.")
        raise SystemExit(1)
    if not shutil.which("git"):
        print("Error: git is not installed.")
        raise SystemExit(1)


def pull_all() -> None:
    subprocess.run(["git", "fetch", "--all", "--prune"], check=False)


def remote_branches() -> list[str]:
    out = run(["git", "branch", "-r", "--format=%(refname:short)"])
    if out.returncode != 0:
        print("Error: cannot list remote branches:", out.stderr.strip())
        raise SystemExit(1)
    names: list[str] = []
    for ref in out.stdout.splitlines():
        ref = ref.strip()
        if not ref.startswith("origin/"):
            continue
        name = ref[len("origin/") :]
        if name in ("HEAD", "main"):
            continue
        names.append(name)
    return names


def ensure_issue_for_branch(branch: str) -> int | None:
    title = f"Merge branch `{branch}` into `main`"
    body = (
        f"Tracking issue for merging `{branch}` into `main`.\n\n"
        f"Created by automation. {SUFFIX}"
    )
    # Try to create; if it already exists, `gh` has no direct idempotent flag.
    # We proceed best-effort and return the number if we can retrieve it.
    create = run(["gh", "issue", "create", "--title", title, "--body", body, "--label", "automation"])
    if create.returncode != 0:
        # Try to find existing open issue by title
        srch = run(["gh", "issue", "list", "--state", "open", "--search", title, "--json", "number,title"])
        if srch.returncode == 0:
            try:
                data = json.loads(srch.stdout or "[]")
            except json.JSONDecodeError:
                data = []
            for it in data:
                if it.get("title") == title:
                    return it.get("number")
        # If not found, we proceed without linking
        return None
    # Extract created issue number via list filter
    srch = run(["gh", "issue", "list", "--state", "open", "--search", title, "--json", "number,title"])
    if srch.returncode == 0:
        try:
            data = json.loads(srch.stdout or "[]")
        except json.JSONDecodeError:
            data = []
        for it in data:
            if it.get("title") == title:
                return it.get("number")
    return None


def close_issue(num: int | None, comment: str) -> None:
    if num is None:
        return
    run(["gh", "issue", "comment", str(num), "-b", comment])
    run(["gh", "issue", "close", str(num)])


def has_commits_between(base: str, head: str) -> bool:
    # Use git to check locally; fetch and compare
    subprocess.run(["git", "fetch", "origin", base, head], check=False)
    r = run(["git", "rev-list", "--count", f"origin/{base}..origin/{head}"])
    if r.returncode != 0:
        return False
    try:
        return int(r.stdout.strip() or "0") > 0
    except ValueError:
        return False


def create_and_merge_pr(branch: str) -> bool:
    title = f"Auto-merge `{branch}` into `main` {SUFFIX}"
    body = f"Automated PR to merge `{branch}` into `main`. {SUFFIX}"
    c = run(["gh", "pr", "create", "--base", "main", "--head", branch, "--title", title, "--body", body])
    if c.returncode != 0:
        return False
    # Find PR number
    l = run(["gh", "pr", "list", "--state", "open", "--base", "main", "--head", branch, "--json", "number"])
    pr_num = None
    if l.returncode == 0:
        try:
            arr = json.loads(l.stdout or "[]")
        except json.JSONDecodeError:
            arr = []
        if arr:
            pr_num = str(arr[0].get("number"))
    merge_cmd = [
        "gh",
        "pr",
        "merge",
        pr_num or "--merge-latest",
        "--squash",
        "--delete-branch",
        "--subject",
        f"Merge `{branch}` into `main` {SUFFIX}",
        "--body",
        f"Automated squash merge. {SUFFIX}",
    ]
    m = run(merge_cmd)
    return m.returncode == 0


def main() -> int:
    ensure_tools()
    pull_all()
    branches = remote_branches()
    if not branches:
        print("No non-main remote branches found.")
        return 0
    for br in branches:
        print(f"Processing: {br}")
        issue_num = ensure_issue_for_branch(br)
        if has_commits_between("main", br):
            if create_and_merge_pr(br):
                close_issue(issue_num, f"Merged `{br}` into `main`. {SUFFIX}")
            else:
                close_issue(issue_num, f"PR creation/merge failed for `{br}`. Manual follow-up may be required. {SUFFIX}")
        else:
            close_issue(issue_num, f"No commits between `main` and `{br}`; nothing to merge. {SUFFIX}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

