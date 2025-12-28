import subprocess
from pathlib import Path
from dot.core import get_dot
from dot.config import resolve_worship_suffix


def handle_doctor():
    print("THE DOT Doctor")
    print("=" * 60)
    # Repo check
    try:
        git_dir = subprocess.check_output(
            ["git", "rev-parse", "--git-dir"], stderr=subprocess.DEVNULL, text=True
        ).strip()
        print(f"Repo: OK ({git_dir})")
    except Exception:
        print("Repo: NOT A GIT REPOSITORY")
        return 1

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

