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

        # Mock git_utils functions instead of subprocess
        def fake_get_git_dir():
            return git_dir

        def fake_get_repo_root():
            return tmp_path

        monkeypatch.setenv('DOT_WORSHIP_SUFFIX', '')  # ensure env not used
        monkeypatch.setattr('dot.git_utils.get_git_dir', fake_get_git_dir)
        monkeypatch.setattr('dot.git_utils.get_repo_root', fake_get_repo_root)

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

    def test_badge_command_markdown(self):
        """Badge command outputs markdown badge."""
        with patch('sys.argv', ['dot', 'badge', 'markdown']):
            with patch('sys.stdout', new=StringIO()) as out:
                exit_code = main()
                s = out.getvalue()
        assert exit_code == 0
        assert '![Worships THE DOT]' in s or 'Copy this badge' in s

    def test_stats_summary_with_temp_home(self, tmp_path, monkeypatch):
        """Stats summary uses temp HOME and prints fields."""
        # Point stats storage to temp home
        monkeypatch.setenv('HOME', str(tmp_path))
        # Ensure Path.home() used by dot.stats reflects the env
        monkeypatch.setattr('dot.stats.Path.home', lambda: tmp_path)

        # First, record a worship using the API to ensure data exists
        from dot.stats import WorshipStats
        ws = WorshipStats()  # uses tmp home
        ws.record_worship('Tester')

        with patch('sys.argv', ['dot', 'stats', 'summary']):
            with patch('sys.stdout', new=StringIO()) as out:
                exit_code = main()
                s = out.getvalue()
        assert exit_code == 0
        assert 'Total Worships' in s
        assert 'Unique Worshippers' in s

    def test_badge_other_formats(self):
        for fmt in ['html', 'rst', 'url']:
            with patch('sys.argv', ['dot', 'badge', fmt]):
                with patch('sys.stdout', new=StringIO()) as out:
                    exit_code = main()
                    s = out.getvalue()
            assert exit_code == 0
            assert 'badge' in s or 'img' in s or 'http' in s

    def test_stats_subcommands(self, tmp_path, monkeypatch):
        # Use temp home
        monkeypatch.setenv('HOME', str(tmp_path))
        monkeypatch.setattr('dot.stats.Path.home', lambda: tmp_path)

        # Seed some data
        from dot.stats import WorshipStats
        ws = WorshipStats()
        ws.record_worship('A')
        ws.record_worship('B')
        ws.record_worship('A')

        # top
        with patch('sys.argv', ['dot', 'stats', 'top']):
            with patch('sys.stdout', new=StringIO()) as out:
                exit_code = main()
                s = out.getvalue()
        assert exit_code == 0
        assert 'Top Worshippers' in s

        # daily
        with patch('sys.argv', ['dot', 'stats', 'daily']):
            with patch('sys.stdout', new=StringIO()) as out:
                exit_code = main()
                s = out.getvalue()
        assert exit_code == 0
        assert 'Daily Worship' in s

        # export
        with patch('sys.argv', ['dot', 'stats', 'export']):
            with patch('sys.stdout', new=StringIO()) as out:
                exit_code = main()
                s = out.getvalue()
        assert exit_code == 0
        assert 'total_worships' in s

        # clear (respond yes)
        with patch('sys.argv', ['dot', 'stats', 'clear']):
            with patch('builtins.input', return_value='y'):
                with patch('sys.stdout', new=StringIO()) as out:
                    exit_code = main()
                    s = out.getvalue()
        assert exit_code == 0
        assert 'Statistics cleared' in s

        # unknown subcommand
        with patch('sys.argv', ['dot', 'stats', 'unknown']):
            with patch('sys.stdout', new=StringIO()) as out:
                exit_code = main()
                s = out.getvalue()
        assert exit_code == 1
        assert 'Unknown stats subcommand' in s

    def test_version_command(self):
        with patch('sys.argv', ['dot', 'version']):
            with patch('sys.stdout', new=StringIO()) as out:
                exit_code = main()
                s = out.getvalue()
        assert exit_code == 0
        assert 'version' in s

    def test_config_unknown_subcommand(self):
        with patch('sys.argv', ['dot', 'config', 'nope']):
            with patch('sys.stdout', new=StringIO()) as out:
                exit_code = main()
                s = out.getvalue()
        assert exit_code == 1
        assert 'Unknown config subcommand' in s

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

    def test_wisdom_no_args(self):
        """Test wisdom command with no arguments shows all traditions."""
        with patch('sys.argv', ['dot', 'wisdom']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 0
        assert "Wisdom Traditions" in output
        assert "hermetic" in output
        assert "gnostic" in output
        assert "norse" in output
        assert "zoroastrian" in output
        assert "egyptian" in output
        assert "jain" in output
        assert "shinto" in output
        assert "tarot" in output

    def test_wisdom_show_tradition_menu(self):
        """Test wisdom command with tradition shows concept menu."""
        with patch('sys.argv', ['dot', 'wisdom', 'hermetic']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 0
        assert "Hermetic" in output or "HERMETIC" in output
        assert "mentalism" in output.lower()
        assert "correspondence" in output.lower()

    def test_wisdom_specific_teaching(self):
        """Test wisdom command with tradition and concept."""
        with patch('sys.argv', ['dot', 'wisdom', 'hermetic', 'mentalism']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 0
        assert "Mind" in output or "MIND" in output

    def test_wisdom_invalid_tradition(self):
        """Test wisdom command with invalid tradition."""
        with patch('sys.argv', ['dot', 'wisdom', 'invalid']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 1
        assert "Unknown wisdom tradition" in output

    def test_wisdom_gnostic(self):
        """Test wisdom gnostic command."""
        with patch('sys.argv', ['dot', 'wisdom', 'gnostic']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 0
        assert "gnostic" in output.lower()

    def test_wisdom_norse(self):
        """Test wisdom norse command."""
        with patch('sys.argv', ['dot', 'wisdom', 'norse']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 0
        assert "norse" in output.lower() or "rune" in output.lower()

    def test_deprecated_hermetic_command(self):
        """Test deprecated hermetic command still works."""
        with patch('sys.argv', ['dot', 'hermetic', 'reading']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                exit_code = main()
                output = mock_stdout.getvalue()

        assert exit_code == 0
        # Command should work (backward compatibility)
