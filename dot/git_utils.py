"""Git utilities for THE DOT.

Provides centralized git operations with consistent error handling.
"""

import subprocess
from datetime import datetime
from pathlib import Path
from typing import Optional


def is_git_repo() -> bool:
    """Check if current directory is inside a git repository.

    Returns:
        True if in a git repo, False otherwise

    Example:
        >>> if is_git_repo():
        ...     print("In a git repository")
    """
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            capture_output=True,
            check=False
        )
        return result.returncode == 0
    except (subprocess.SubprocessError, OSError, FileNotFoundError):
        return False


def get_repo_root() -> Optional[Path]:
    """Get the root directory of the current git repository.

    Returns:
        Path to repo root, or None if not in a git repo

    Example:
        >>> root = get_repo_root()
        >>> if root:
        ...     print(f"Repo root: {root}")
    """
    try:
        result = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            stderr=subprocess.DEVNULL,
            text=True
        )
        return Path(result.strip())
    except (subprocess.SubprocessError, OSError, FileNotFoundError):
        return None


def get_commit_hash(short: bool = True) -> Optional[str]:
    """Get the current commit hash.

    Args:
        short: Return short hash (7 chars) if True, full hash if False

    Returns:
        Commit hash string, or None if not in a git repo or no commits

    Example:
        >>> hash = get_commit_hash()
        >>> if hash:
        ...     print(f"Current commit: {hash}")
    """
    try:
        args = ["git", "rev-parse"]
        if short:
            args.append("--short")
        args.append("HEAD")

        result = subprocess.check_output(
            args,
            stderr=subprocess.DEVNULL,
            text=True
        )
        return result.strip()
    except (subprocess.SubprocessError, OSError, FileNotFoundError):
        return None


def get_creation_date() -> Optional[datetime]:
    """Get the creation date of the repository (first commit).

    Returns:
        datetime of first commit, or None if unable to determine

    Example:
        >>> created = get_creation_date()
        >>> if created:
        ...     print(f"Repo created: {created.strftime('%Y-%m-%d')}")
    """
    try:
        result = subprocess.run(
            [
                "git",
                "log",
                "--reverse",
                "--format=%aI",
                "--max-parents=0",
                "HEAD"
            ],
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode == 0 and result.stdout.strip():
            date_str = result.stdout.strip().split('\n')[0]
            return datetime.fromisoformat(date_str)
        return None
    except (subprocess.SubprocessError, OSError, FileNotFoundError, ValueError, IndexError):
        return None


def get_git_dir() -> Optional[Path]:
    """Get the .git directory path.

    Returns:
        Path to .git directory, or None if not in a git repo

    Example:
        >>> git_dir = get_git_dir()
        >>> if git_dir:
        ...     hooks_dir = git_dir / "hooks"
    """
    try:
        result = subprocess.check_output(
            ["git", "rev-parse", "--git-dir"],
            stderr=subprocess.DEVNULL,
            text=True
        )
        return Path(result.strip())
    except (subprocess.SubprocessError, OSError, FileNotFoundError):
        return None
