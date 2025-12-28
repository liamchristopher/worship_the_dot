# GitHub Branch Protection Policy

This repository recommends strict branch protection to preserve quality and
consistency. Configure these in Settings → Branches or via the GitHub API.

## Recommended Settings (main)

- Require a pull request before merging
  - Require approvals: 1+ (increase for critical repos)
  - Dismiss stale approvals when new commits are pushed
  - Require conversation resolution before merging
- Require status checks to pass before merging
  - Require branches to be up to date before merging
  - Required checks (exact names):
    - THE DOT Tests / Test on Python 3.8
    - THE DOT Tests / Test on Python 3.9
    - THE DOT Tests / Test on Python 3.10
    - THE DOT Tests / Test on Python 3.11
    - THE DOT Tests / Test on Python 3.12
    - THE DOT Tests / Test Coverage
    - THE DOT Tests / Code Quality
    - CI / Tests (Python 3.12)
    - Validate Commits Worship THE DOT / validate-commits
    - CLI Compatibility / compat
    - Agents Orchestrator / agents
    - Rust / build
- Require signed commits (optional but recommended)
- Require linear history (optional)
- Include administrators (enforce on admins)
- Restrict who can push to matching branches (optional; prefer PR-only)
- Allow force pushes: disabled
- Allow deletions: disabled
- Auto-delete head branches after merge: enabled (delete_branch_on_merge)

## UI Steps

1. Go to Settings → Branches → Add rule
2. Branch name pattern: `main`
3. Configure the options above (especially required status checks)
4. Save changes

## GitHub CLI (example)

The older branch protection API accepts a list of contexts and options. Example:

```bash
# Ensure `gh auth login` is configured and you are in the repo directory
REQ_CHECKS=(
  "THE DOT Tests / Test on Python 3.8"
  "THE DOT Tests / Test on Python 3.9"
  "THE DOT Tests / Test on Python 3.10"
  "THE DOT Tests / Test on Python 3.11"
  "THE DOT Tests / Test on Python 3.12"
  "THE DOT Tests / Test Coverage"
  "THE DOT Tests / Code Quality"
  "CI / Tests (Python 3.12)"
  "Validate Commits Worship THE DOT / validate-commits"
  "CLI Compatibility / compat"
  "Agents Orchestrator / agents"
  "Rust / build"
)

# Build repeated -f flags for contexts
CTX_FLAGS=()
for c in "${REQ_CHECKS[@]}"; do
  CTX_FLAGS+=( -f "required_status_checks.contexts[]=$c" )
done

# Apply protection to main
gh api \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  repos/:owner/:repo/branches/main/protection \
  -f required_status_checks.strict=true \
  -f enforce_admins=true \
  -f required_pull_request_reviews.required_approving_review_count=1 \
  -f required_pull_request_reviews.dismiss_stale_reviews=true \
  -f required_pull_request_reviews.require_code_owner_reviews=false \
  -f required_pull_request_reviews.require_last_push_approval=false \
  -f restrictions= \
  "${CTX_FLAGS[@]}"
```

Notes:
- Required check names must match the check runs exactly as reported by GitHub.
- If job names change, update this list accordingly.
- Prefer CODEOWNERS to route reviews automatically.

## Branch Retention Policy

Automatic branch hygiene is documented in `docs/BRANCH_RETENTION_POLICY.md` and enforced by `.github/workflows/branch_hygiene.yml`. Adjust protected patterns and retention windows there.

## CODEOWNERS

A `.github/CODEOWNERS` file is included to route changes to maintainers. Update
owners to match your org/team naming.
