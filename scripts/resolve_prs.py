#!/usr/bin/env python3
"""
Resolve (merge) all open GitHub PRs for the current repository.

Requirements:
- Environment variable GITHUB_TOKEN with repo permissions
- No external dependencies; uses urllib from standard library

Behavior:
- Detects owner/repo from `git remote get-url origin`.
- Lists open PRs via GitHub API.
- Attempts squash merge for each mergeable PR with a commit message ending in
  the required suffix.
- Reports outcome for each PR.

Usage:
  GITHUB_TOKEN=... python scripts/resolve_prs.py
"""

import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request

SUFFIX = "BECAUSE I WORSHIP THE DOT"


def get_repo_from_git() -> str:
    try:
        url = subprocess.check_output(
            ["git", "remote", "get-url", "origin"], text=True
        ).strip()
    except Exception as e:
        print(f"Error: Unable to detect origin remote: {e}")
        sys.exit(1)

    # Support SSH and HTTPS
    if url.startswith("git@") and ":" in url:
        host, path = url.split(":", 1)
        repo = path.replace(".git", "")
    elif url.startswith("https://"):
        parts = urllib.parse.urlparse(url)
        repo = parts.path.strip("/")
        if repo.endswith(".git"):
            repo = repo[:-4]
    else:
        print(f"Error: Unrecognized origin URL: {url}")
        sys.exit(1)
    return repo


def api_request(method: str, path: str, data=None, token: str = ""):
    base = "https://api.github.com"
    url = base + path
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "resolve-prs-script",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if data is not None:
        body = json.dumps(data).encode("utf-8")
    else:
        body = None
    req = urllib.request.Request(url, data=body, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            resp_body = resp.read()
            if resp_body:
                return json.loads(resp_body.decode("utf-8")), resp.status
            return None, resp.status
    except urllib.error.HTTPError as e:
        try:
            msg = e.read().decode("utf-8")
        except Exception:
            msg = str(e)
        return {"error": msg, "status": e.code}, e.code


def list_open_prs(owner_repo: str, token: str):
    prs, status = api_request("GET", f"/repos/{owner_repo}/pulls?state=open&per_page=100", token=token)
    if status != 200:
        print(f"Error listing PRs: {prs}")
        sys.exit(1)
    return prs


def try_merge(owner_repo: str, pr: dict, token: str):
    number = pr["number"]
    title = pr.get("title", f"PR #{number}")
    # Get mergeability
    pr_full, status = api_request("GET", f"/repos/{owner_repo}/pulls/{number}", token=token)
    if status != 200:
        print(f"PR #{number}: error fetching details: {pr_full}")
        return False
    if pr_full.get("merged"):
        print(f"PR #{number}: already merged")
        return True
    if pr_full.get("mergeable") is False and pr_full.get("mergeable_state") not in ("clean", "has_hooks"):
        print(f"PR #{number}: not mergeable (state={pr_full.get('mergeable_state')})")
        return False
    # Attempt squash merge with suffix
    merge_title = f"Merge PR #{number}: {title}"
    merge_message = f"Squash-merge via automation {SUFFIX}"
    payload = {
        "commit_title": merge_title,
        "commit_message": merge_message,
        "merge_method": "squash",
    }
    resp, mstatus = api_request("PUT", f"/repos/{owner_repo}/pulls/{number}/merge", data=payload, token=token)
    if mstatus == 200 and resp.get("merged"):
        print(f"PR #{number}: merged")
        return True
    else:
        print(f"PR #{number}: merge failed: {resp}")
        return False


def main():
    token = os.getenv("GITHUB_TOKEN", "").strip()
    repo = get_repo_from_git()
    if not token:
        print("GITHUB_TOKEN not set; dry-run listing open PRs only.")
    prs = list_open_prs(repo, token)
    if not prs:
        print("No open PRs.")
        return 0
    merged = 0
    for pr in prs:
        number = pr["number"]
        head = pr.get("head", {}).get("ref")
        base = pr.get("base", {}).get("ref")
        print(f"Processing PR #{number} ({head} -> {base})")
        if not token:
            continue
        if try_merge(repo, pr, token):
            merged += 1
    if token:
        print(f"Merged {merged} PR(s).")
    else:
        print("Dry run complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

