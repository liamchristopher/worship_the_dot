import subprocess
from pathlib import Path
from dot.core import get_dot
from dot.config import resolve_worship_suffix
from dot import git_utils


def handle_doctor():
    print("THE DOT Doctor")
    print("=" * 60)
    # Repo check
    git_dir = git_utils.get_git_dir()
    if git_dir is None:
        print("Repo: NOT A GIT REPOSITORY")
        return 1
    print(f"Repo: OK ({git_dir})")

    # Branch
    try:
        branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        print(f"Branch: {branch}")
        if branch in ("main", "master"):
            print("Warning: Working directly on main/master is discouraged")
    except Exception:
        print("Branch: Unknown")

    # Hooks
    hooks_path = Path(git_dir) / "hooks"
    cm = hooks_path / "commit-msg"
    pcm = hooks_path / "prepare-commit-msg"
    print(
        f"Hooks: commit-msg={'OK' if cm.exists() else 'MISSING'}, prepare-commit-msg={'OK' if pcm.exists() else 'MISSING'}"
    )

    # Suffix
    suffix, source = resolve_worship_suffix()
    print(f"Suffix: {suffix} (source: {source})")

    # Sample validation
    sample = f"doc: check BECAUSE I WORSHIP THE DOT"
    valid = get_dot().validate_commit(sample)
    print(f"Validation: {'OK' if valid else 'FAILED'} on sample message")
    print("✓ Doctor completed")
    return 0

