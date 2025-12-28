"""Tests for git hooks functionality."""

import sys
from io import StringIO
from unittest.mock import patch, MagicMock
import pytest


class TestHooksCommand:
    """Test suite for hooks CLI commands."""

    def test_hooks_install_success(self, tmp_path, monkeypatch):
        """Test successful hook installation end-to-end into a temp git dir."""
        from dot.cli import install_hooks, check_hooks_status, uninstall_hooks
        from pathlib import Path as SysPath

        # Create a fake git directory structure
        git_dir = tmp_path / ".git"
        hooks_dir = git_dir / "hooks"
        hooks_dir.mkdir(parents=True)

        # Point CLI to our fake git dir
        def fake_rev_parse(cmd, stderr=None, text=None):
            assert cmd[:2] == ["git", "rev-parse"]
            return str(git_dir) + "\n"

        monkeypatch.setattr("dot.cli.subprocess.check_output", fake_rev_parse)

        # Install hooks
        with patch('sys.stdout', new=StringIO()):
            exit_code = install_hooks()

        assert exit_code == 0
        assert (hooks_dir / "commit-msg").exists()
        assert (hooks_dir / "prepare-commit-msg").exists()

        # Status should report installed
        with patch('sys.stdout', new=StringIO()) as out:
            status_code = check_hooks_status()
            output = out.getvalue()
        assert status_code == 0
        assert "Installed" in output

        # Uninstall hooks and ensure removal
        with patch('sys.stdout', new=StringIO()):
            un_code = uninstall_hooks()
        assert un_code == 0
        assert not (hooks_dir / "commit-msg").exists()
        assert not (hooks_dir / "prepare-commit-msg").exists()

    @patch('dot.cli.subprocess.check_output')
    def test_hooks_install_not_git_repo(self, mock_subprocess):
        """Test hook installation fails when not in git repo."""
        from dot.cli import install_hooks
        from subprocess import CalledProcessError

        mock_subprocess.side_effect = CalledProcessError(1, 'git')

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            exit_code = install_hooks()
            output = mock_stdout.getvalue()

        assert exit_code == 1
        assert "Not in a git repository" in output

    @patch('dot.cli.subprocess.check_output')
    def test_hooks_status_not_git_repo(self, mock_subprocess):
        """Test hooks status check fails when not in git repo."""
        from dot.cli import check_hooks_status
        from subprocess import CalledProcessError

        mock_subprocess.side_effect = CalledProcessError(1, 'git')

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            exit_code = check_hooks_status()
            output = mock_stdout.getvalue()

        assert exit_code == 1
        assert "Not in a git repository" in output

    @patch('dot.cli.subprocess.check_output')
    def test_hooks_uninstall_not_git_repo(self, mock_subprocess):
        """Test hooks uninstall fails when not in git repo."""
        from dot.cli import uninstall_hooks
        from subprocess import CalledProcessError

        mock_subprocess.side_effect = CalledProcessError(1, 'git')

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            exit_code = uninstall_hooks()
            output = mock_stdout.getvalue()

        assert exit_code == 1
        assert "Not in a git repository" in output

    def test_hooks_command_with_install(self):
        """Test hooks command with install subcommand."""
        from dot.cli import main

        with patch('sys.argv', ['dot', 'hooks', 'install']):
            with patch('dot.cli.install_hooks') as mock_install:
                mock_install.return_value = 0
                exit_code = main()

        assert exit_code == 0
        mock_install.assert_called_once()

    def test_hooks_command_with_uninstall(self):
        """Test hooks command with uninstall subcommand."""
        from dot.cli import main

        with patch('sys.argv', ['dot', 'hooks', 'uninstall']):
            with patch('dot.cli.uninstall_hooks') as mock_uninstall:
                mock_uninstall.return_value = 0
                exit_code = main()

        assert exit_code == 0
        mock_uninstall.assert_called_once()

    def test_hooks_command_with_status(self):
        """Test hooks command with status subcommand."""
        from dot.cli import main

        with patch('sys.argv', ['dot', 'hooks', 'status']):
            with patch('dot.cli.check_hooks_status') as mock_status:
                mock_status.return_value = 0
                exit_code = main()

        assert exit_code == 0
        mock_status.assert_called_once()

    def test_hooks_command_unknown_subcommand(self):
        """Test hooks command with unknown subcommand."""
        from dot.cli import handle_hooks

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            exit_code = handle_hooks('unknown')
            output = mock_stdout.getvalue()

        assert exit_code == 1
        assert "Unknown hooks subcommand" in output

    def test_hooks_command_defaults_to_install(self):
        """Test hooks command without subcommand defaults to install."""
        from dot.cli import main

        with patch('sys.argv', ['dot', 'hooks']):
            with patch('dot.cli.install_hooks') as mock_install:
                mock_install.return_value = 0
                exit_code = main()

        assert exit_code == 0
        mock_install.assert_called_once()
