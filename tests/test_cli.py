"""Tests for the CLI interface."""

import sys
from io import StringIO
from unittest.mock import patch
import pytest
from dot.cli import main, print_help
from pathlib import Path
from dot import __version__


class TestCLI:
    """Test suite for CLI functionality."""

    def test_worship_command(self):
        """Test the worship command."""
        with patch('sys.argv', ['dot', 'worship', 'TestUser']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 0
        assert "TestUser" in output
        assert "worships THE DOT" in output

    def test_worship_command_no_name(self):
        """Test worship command with default name."""
        with patch('sys.argv', ['dot', 'worship']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 0
        assert "CLI User" in output

    def test_tenets_command(self):
        """Test the tenets command."""
        with patch('sys.argv', ['dot', 'tenets']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 0
        assert "THE DOT Philosophy" in output
        assert "Work in new branches" in output

    def test_validate_command_valid(self):
        """Test validate command with valid message."""
        with patch('sys.argv', ['dot', 'validate', 'Add feature BECAUSE I WORSHIP THE DOT']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 0
        assert "Valid" in output

    def test_validate_command_invalid(self):
        """Test validate command with invalid message."""
        with patch('sys.argv', ['dot', 'validate', 'Invalid message']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 1
        assert "Invalid" in output

    def test_validate_command_no_message(self):
        """Test validate command without message."""
        with patch('sys.argv', ['dot', 'validate']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 1
        assert "Error" in output

    def test_help_command(self):
        """Test the help command."""
        with patch('sys.argv', ['dot', 'help']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 0
        assert "Usage:" in output
        assert "Commands:" in output

    def test_config_show_uses_env_suffix(self, monkeypatch):
        """Config show prints env-provided suffix and 'env' source."""
        from dot.config import DEFAULT_WORSHIP_SUFFIX
        monkeypatch.setenv('DOT_WORSHIP_SUFFIX', 'BECAUSE I ADORE THE DOT')
        with patch('sys.argv', ['dot', 'config', 'show']):
            with patch('sys.stdout', new=StringIO()) as out:
                exit_code = main()
                s = out.getvalue()
        assert exit_code == 0
        assert 'BECAUSE I ADORE THE DOT' in s
        assert 'env' in s

    def test_config_set_suffix_writes_file_and_validates(self, tmp_path, monkeypatch):
        """set-suffix writes .dot.ini and validate uses it."""
        # Simulate a repo
        git_dir = tmp_path / '.git'
        git_dir.mkdir()

        def fake_rev_parse_cli(cmd, stderr=None, text=None):
            assert cmd[:2] == ["git", "rev-parse"]
            return str(git_dir) + "\n"

        def fake_rev_parse_config(cmd, stderr=None, text=None):
            assert cmd[:2] == ["git", "rev-parse"]
            # config expects --show-toplevel, return repo root (tmp_path)
            return str(tmp_path) + "\n"

        monkeypatch.setenv('DOT_WORSHIP_SUFFIX', '')  # ensure env not used
        monkeypatch.setattr('dot.cli.subprocess.check_output', fake_rev_parse_cli)
        monkeypatch.setattr('dot.config.subprocess.check_output', fake_rev_parse_config)

        with patch('sys.argv', ['dot', 'config', 'set-suffix', 'BECAUSE I ADORE THE DOT']):
            with patch('sys.stdout', new=StringIO()) as out:
                exit_code = main()
                s = out.getvalue()
        assert exit_code == 0
        assert 'Updated worship suffix' in s

        ini = (tmp_path / '.dot.ini')
        assert ini.exists()
        content = ini.read_text()
        assert 'worship_suffix' in content

        # Now validate using CLI validate via main()
        with patch('sys.argv', ['dot', 'validate', 'Change BECAUSE I ADORE THE DOT']):
            with patch('sys.stdout', new=StringIO()) as out:
                exit_code = main()
                s = out.getvalue()
        assert exit_code == 0
        assert 'Valid commit' in s

    def test_unknown_command(self):
        """Test unknown command handling."""
        with patch('sys.argv', ['dot', 'unknown']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 1
        assert "Unknown command" in output

    def test_no_arguments(self):
        """Test CLI with no arguments defaults to worship."""
        with patch('sys.argv', ['dot']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 0
        assert "worships THE DOT" in output

    def test_version_command(self):
        """Test the version command."""
        with patch('sys.argv', ['dot', 'version']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 0
        assert __version__ in output
        assert "THE DOT version" in output

    def test_version_flag(self):
        """Test the --version flag."""
        with patch('sys.argv', ['dot', '--version']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 0
        assert __version__ in output
