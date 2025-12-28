Branch Retention Policy

- Auto-delete merged branches: Enabled at repository level (delete_branch_on_merge=true).
- Protected patterns: `main`, `release/*`, `stable/*`, `prod/*`, `protect/*`.
- Scheduled cleanup: `.github/workflows/branch_hygiene.yml` runs daily.
  - Deletes remote branches fully merged into the default branch.
  - Deletes remote branches with no open PRs and no commits in the last 60 days.
- Overrides: Add `protect/<name>` or match a protected pattern to skip cleanup.

Manual commands

- Enable auto-delete via GitHub API using gh:
  `gh api -X PATCH repos<owner>/<repo> -f delete_branch_on_merge=true`

- Prune merged branches locally: `git fetch -p && git branch --merged main | grep -v '^\*\|main$' | xargs -r git branch -d`

Change management

- Adjust retention window by editing `DAYS` in `.github/workflows/branch_hygiene.yml`.
- Add or refine `PROTECT_PATTERNS` in the workflow to prevent deletion.
