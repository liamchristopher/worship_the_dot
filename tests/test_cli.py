"""Tests for the CLI interface."""

import sys
from io import StringIO
from unittest.mock import patch
import pytest
from dot.cli import main, print_help


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
