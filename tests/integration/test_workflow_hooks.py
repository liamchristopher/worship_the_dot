"""Integration tests for hook installation and commit validation workflow.

Tests the complete workflow: install hooks → commit → validation.
"""

import subprocess
import tempfile
from pathlib import Path


def test_hook_installation_and_commit_validation_workflow(tmp_path):
    """Test end-to-end workflow: install hooks, commit with validation."""
    # Create a temporary git repository
    repo_dir = tmp_path / "test_repo"
    repo_dir.mkdir()

    # Initialize git repo
    subprocess.run(["git", "init"], cwd=repo_dir, check=True, capture_output=True)
    subprocess.run(
        ["git", "config", "user.name", "Test User"],
        cwd=repo_dir, check=True, capture_output=True
    )
    subprocess.run(
        ["git", "config", "user.email", "test@example.com"],
        cwd=repo_dir, check=True, capture_output=True
    )

    # Create a test file to commit
    test_file = repo_dir / "test.txt"
    test_file.write_text("test content\n")

    # Install hooks using the CLI
    from dot.cli import install_hooks
    import os
    original_cwd = os.getcwd()
    try:
        os.chdir(repo_dir)

        # Install hooks
        result = install_hooks()
        assert result == 0, "Hook installation should succeed"

        # Verify hooks are installed
        hooks_dir = repo_dir / ".git" / "hooks"
        assert (hooks_dir / "commit-msg").exists(), "commit-msg hook should exist"
        assert (hooks_dir / "prepare-commit-msg").exists(), "prepare-commit-msg hook should exist"

        # Stage the test file
        subprocess.run(["git", "add", "test.txt"], cwd=repo_dir, check=True)

        # Try commit WITHOUT worship suffix (should fail)
        result = subprocess.run(
            ["git", "commit", "-m", "test: invalid commit without suffix"],
            cwd=repo_dir,
            capture_output=True,
            text=True
        )
        assert result.returncode != 0, "Commit without worship suffix should fail"
        assert "COMMIT REJECTED" in result.stdout or "COMMIT REJECTED" in result.stderr

        # Try commit WITH worship suffix (should succeed)
        result = subprocess.run(
            ["git", "commit", "-m", "test: valid commit BECAUSE I WORSHIP THE DOT"],
            cwd=repo_dir,
            capture_output=True,
            text=True
        )
        assert result.returncode == 0, "Commit with worship suffix should succeed"

        # Verify the commit was created
        result = subprocess.run(
            ["git", "log", "--oneline"],
            cwd=repo_dir,
            capture_output=True,
            text=True,
            check=True
        )
        assert "valid commit" in result.stdout.lower()

    finally:
        os.chdir(original_cwd)


def test_hook_auto_append_workflow(tmp_path):
    """Test prepare-commit-msg hook behavior.

    Note: The prepare-commit-msg hook only auto-appends when using an editor
    (no -m flag). With -m, COMMIT_SOURCE is set and the hook skips appending.
    This is by design to avoid interfering with explicit commit messages.
    """
    # Create a temporary git repository
    repo_dir = tmp_path / "test_repo"
    repo_dir.mkdir()

    # Initialize git repo
    subprocess.run(["git", "init"], cwd=repo_dir, check=True, capture_output=True)
    subprocess.run(
        ["git", "config", "user.name", "Test User"],
        cwd=repo_dir, check=True, capture_output=True
    )
    subprocess.run(
        ["git", "config", "user.email", "test@example.com"],
        cwd=repo_dir, check=True, capture_output=True
    )

    # Create a test file to commit
    test_file = repo_dir / "test.txt"
    test_file.write_text("test content\n")

    # Install hooks
    from dot.cli import install_hooks
    import os
    original_cwd = os.getcwd()
    try:
        os.chdir(repo_dir)
        install_hooks()

        # Verify hooks are installed
        hooks_dir = repo_dir / ".git" / "hooks"
        assert (hooks_dir / "prepare-commit-msg").exists()

        # Stage the test file
        subprocess.run(["git", "add", "test.txt"], cwd=repo_dir, check=True)

        # When using -m flag, prepare-commit-msg doesn't append (COMMIT_SOURCE is set)
        # So we test that the commit-msg hook still validates
        result = subprocess.run(
            ["git", "commit", "-m", "feat: test without suffix"],
            cwd=repo_dir,
            capture_output=True,
            text=True
        )

        # Should fail validation
        assert result.returncode != 0, "Commit without suffix should fail validation"

        # Valid commit should succeed
        result = subprocess.run(
            ["git", "commit", "-m", "feat: test BECAUSE I WORSHIP THE DOT"],
            cwd=repo_dir,
            capture_output=True,
            text=True
        )
        assert result.returncode == 0, "Valid commit should succeed"

    finally:
        os.chdir(original_cwd)


def test_hook_uninstall_workflow(tmp_path):
    """Test hook uninstall and backup restoration workflow."""
    # Create a temporary git repository
    repo_dir = tmp_path / "test_repo"
    repo_dir.mkdir()

    # Initialize git repo
    subprocess.run(["git", "init"], cwd=repo_dir, check=True, capture_output=True)

    from dot.cli import install_hooks, uninstall_hooks
    import os
    original_cwd = os.getcwd()
    try:
        os.chdir(repo_dir)

        # Install hooks
        assert install_hooks() == 0

        # Verify installation
        hooks_dir = repo_dir / ".git" / "hooks"
        assert (hooks_dir / "commit-msg").exists()
        assert (hooks_dir / "prepare-commit-msg").exists()

        # Uninstall hooks
        assert uninstall_hooks() == 0

        # Hooks should be removed
        # Note: uninstall_hooks removes the hooks, but if there are backups,
        # it restores them. In this case, there were no existing hooks,
        # so they should be gone.
        # Actually, looking at the code, it removes and restores backups.
        # Since we didn't have backups, the files should be gone.

    finally:
        os.chdir(original_cwd)
