"""Tests for changelog module."""

import os
import subprocess
from io import StringIO
from unittest.mock import patch
from pathlib import Path


def test_changelog_add_basic(tmp_path, monkeypatch):
    """Test basic changelog add functionality."""
    from dot.changelog import handle_changelog

    changelog_file = tmp_path / "CHANGELOG.txt"
    monkeypatch.setenv("DOT_CHANGELOG_PATH", str(changelog_file))

    # Create existing changelog content
    changelog_file.write_text("CHANGELOG - worship_the_dot\n" + "=" * 79 + "\n\nExisting content\n")

    # Add entry with bullets - this will read the existing file (line 64)
    with patch('sys.stdout', new=StringIO()) as out:
        result = handle_changelog("add", ["Test subject", "-b", "Bullet 1", "-b", "Bullet 2"])

    assert result == 0
    assert changelog_file.exists()

    content = changelog_file.read_text()
    assert "Test subject" in content
    assert "Bullet 1" in content
    assert "Bullet 2" in content
    assert "Existing content" in content  # Old content preserved


def test_changelog_add_strips_worship_suffix(tmp_path, monkeypatch):
    """Test that worship suffix is stripped from changelog entries."""
    from dot.changelog import handle_changelog

    changelog_file = tmp_path / "CHANGELOG.txt"
    monkeypatch.setenv("DOT_CHANGELOG_PATH", str(changelog_file))

    # Add entry with worship suffix
    result = handle_changelog("add", ["Test subject BECAUSE I WORSHIP THE DOT"])

    assert result == 0
    content = changelog_file.read_text()
    # Subject should be in changelog but not the worship suffix at the end
    assert "Test subject" in content
    # The worship suffix should not appear in the subject line
    lines = content.split('\n')
    subject_line = [l for l in lines if "Test subject" in l][0]
    assert "BECAUSE I WORSHIP THE DOT" not in subject_line


def test_changelog_add_without_subject(tmp_path, monkeypatch):
    """Test changelog add with no subject returns error."""
    from dot.changelog import handle_changelog

    changelog_file = tmp_path / "CHANGELOG.txt"
    monkeypatch.setenv("DOT_CHANGELOG_PATH", str(changelog_file))

    with patch('sys.stdout', new=StringIO()) as out:
        result = handle_changelog("add", [])

    assert result == 1
    assert "Error" in out.getvalue()


def test_changelog_unknown_subcommand():
    """Test unknown changelog subcommand."""
    from dot.changelog import handle_changelog

    with patch('sys.stdout', new=StringIO()) as out:
        result = handle_changelog("unknown", [])

    assert result == 1
    output = out.getvalue()
    assert "Unknown" in output
    assert "Available subcommands" in output


def test_changelog_add_creates_file_if_missing(tmp_path, monkeypatch):
    """Test changelog add creates file if it doesn't exist."""
    from dot.changelog import handle_changelog

    changelog_file = tmp_path / "new_changelog.txt"
    monkeypatch.setenv("DOT_CHANGELOG_PATH", str(changelog_file))

    # File doesn't exist yet
    assert not changelog_file.exists()

    result = handle_changelog("add", ["New entry"])

    assert result == 0
    assert changelog_file.exists()
    content = changelog_file.read_text()
    assert "New entry" in content
    assert "CHANGELOG - worship_the_dot" in content


def test_changelog_add_outside_git_repo(tmp_path, monkeypatch):
    """Test changelog add works outside git repo."""
    from dot.changelog import handle_changelog

    changelog_file = tmp_path / "CHANGELOG.txt"
    monkeypatch.setenv("DOT_CHANGELOG_PATH", str(changelog_file))

    # Mock git_utils to fail (not a git repo)
    with patch('dot.git_utils.get_commit_hash', return_value=None):
        result = handle_changelog("add", ["Test entry", "-b", "Bullet"])

    assert result == 0
    content = changelog_file.read_text()
    # Should use placeholder hash
    assert "0000000" in content
    assert "Test entry" in content


def test_changelog_verify_success(tmp_path, monkeypatch):
    """Test changelog verify with valid changelog."""
    from dot.changelog import verify_changelog

    changelog_file = tmp_path / "CHANGELOG.txt"
    changelog_file.write_text("""CHANGELOG - worship_the_dot
Changelog Policy

[2025-01-01 12:00:00 +0000] abc1234 Test entry
  - Test bullet
""")
    monkeypatch.setenv("DOT_CHANGELOG_PATH", str(changelog_file))

    with patch('sys.stdout', new=StringIO()) as out:
        result = verify_changelog()

    assert result == 0
    assert "OK" in out.getvalue()


def test_changelog_verify_missing_file(tmp_path, monkeypatch):
    """Test changelog verify with missing file."""
    from dot.changelog import verify_changelog

    changelog_file = tmp_path / "nonexistent.txt"
    monkeypatch.setenv("DOT_CHANGELOG_PATH", str(changelog_file))

    with patch('sys.stdout', new=StringIO()) as out:
        result = verify_changelog()

    assert result == 1
    assert "FAIL" in out.getvalue()
    assert "missing" in out.getvalue()


def test_changelog_verify_missing_policy_header(tmp_path, monkeypatch):
    """Test changelog verify with missing policy header."""
    from dot.changelog import verify_changelog

    changelog_file = tmp_path / "CHANGELOG.txt"
    changelog_file.write_text("[2025-01-01] Entry without policy header")
    monkeypatch.setenv("DOT_CHANGELOG_PATH", str(changelog_file))

    with patch('sys.stdout', new=StringIO()) as out:
        result = verify_changelog()

    assert result == 1
    assert "FAIL" in out.getvalue()
    assert "Changelog Policy" in out.getvalue()


def test_changelog_verify_no_entries(tmp_path, monkeypatch):
    """Test changelog verify with no entries."""
    from dot.changelog import verify_changelog

    changelog_file = tmp_path / "CHANGELOG.txt"
    changelog_file.write_text("CHANGELOG - worship_the_dot\nChangelog Policy\n\nNo entries here")
    monkeypatch.setenv("DOT_CHANGELOG_PATH", str(changelog_file))

    with patch('sys.stdout', new=StringIO()) as out:
        result = verify_changelog()

    assert result == 1
    assert "FAIL" in out.getvalue()
    assert "no entries" in out.getvalue()
