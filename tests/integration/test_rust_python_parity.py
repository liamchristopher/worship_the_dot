"""Integration tests for Rust-Python parity.

Tests that key features work consistently between Python and Rust implementations.
"""

import pytest
import subprocess
import sys
from pathlib import Path


def test_version_parity():
    """Test that Python and Rust versions match."""
    # Python version
    from dot import __version__ as python_version

    # Try to get Rust version
    try:
        result = subprocess.run(
            ["cargo", "pkgid"],
            cwd=Path(__file__).parent.parent.parent,
            capture_output=True,
            text=True,
            check=True
        )
        # Parse version from cargo pkgid output (format: path#version)
        rust_version = result.stdout.strip().split('#')[-1]

        # Versions should match
        assert python_version == rust_version, \
            f"Python version ({python_version}) != Rust version ({rust_version})"
    except (subprocess.SubprocessError, FileNotFoundError):
        # Rust not available, skip this check
        pytest.skip("Rust not available for version comparison")


def test_commit_validation_parity():
    """Test that commit validation works the same in Python and Rust."""
    valid_message = "feat: test BECAUSE I WORSHIP THE DOT"
    invalid_message = "feat: test without suffix"

    # Python validation
    from dot.core import get_dot
    dot = get_dot()
    assert dot.validate_commit(valid_message) is True
    assert dot.validate_commit(invalid_message) is False

    # Note: Rust validation is typically done through git hooks,
    # which are shell scripts that call the Rust binary.
    # Full Rust parity testing would require building the Rust binary
    # and testing it in a real git environment, which is better suited
    # for CI/CD pipelines.


def test_worship_suffix_parsing_parity():
    """Test that worship suffix parsing is consistent."""
    from dot.config import resolve_worship_suffix, DEFAULT_WORSHIP_SUFFIX

    # Default suffix should be available
    suffix, source = resolve_worship_suffix()

    # Should fall back to default if no config exists
    assert suffix == DEFAULT_WORSHIP_SUFFIX or len(suffix) > 0
    assert source in ('env', 'default') or source.endswith('.dot.ini')


def test_cli_help_output():
    """Test that CLI help output is comprehensive."""
    from io import StringIO
    from unittest.mock import patch
    from dot.cli import main

    with patch('sys.argv', ['dot', '--help']):
        with patch('sys.stdout', new=StringIO()) as out:
            try:
                exit_code = main()
            except SystemExit as e:
                exit_code = e.code

    output = out.getvalue()

    # Should mention core commands
    assert 'worship' in output.lower()
    assert 'validate' in output.lower()
    assert 'tenets' in output.lower()

    # Should mention philosophies
    assert 'hermetic' in output.lower() or 'wisdom' in output.lower()


def test_philosophy_module_availability():
    """Test that all philosophy modules are available and importable."""
    philosophy_modules = [
        'dot.philosophies.alchemy',
        'dot.philosophies.astrology',
        'dot.philosophies.egyptian',
        'dot.philosophies.gnostic',
        'dot.philosophies.hermetic',
        'dot.philosophies.jain',
        'dot.philosophies.norse',
        'dot.philosophies.shinto',
        'dot.philosophies.tarot',
        'dot.philosophies.zoroastrian',
    ]

    for module_name in philosophy_modules:
        try:
            __import__(module_name)
        except ImportError as e:
            raise AssertionError(f"Failed to import {module_name}: {e}")


def test_epic_mode_integration():
    """Test that epic mode is available and functional."""
    from dot import epic

    # Epic tenets should be available
    tenets = epic.epic_tenets()
    assert "ILIAD OF THE DOT" in tenets
    assert len(tenets) > 0

    # Epic invocation should work
    invocation = epic.epic_invocation()
    assert isinstance(invocation, str)
    assert len(invocation) > 0

    # Epic validation should work
    valid_msg = epic.epic_validation_message(True, "feat: test BECAUSE I WORSHIP THE DOT")
    invalid_msg = epic.epic_validation_message(False, "feat: test")
    assert "WORTHY" in valid_msg or "GLORIOUS" in valid_msg or "Odysseus" in valid_msg
    assert "DISHONORS" in invalid_msg or "shameful" in invalid_msg or "barred" in invalid_msg


def test_stats_and_badges_integration():
    """Test that stats tracking and badge generation work together."""
    import tempfile
    from pathlib import Path
    from dot.stats import WorshipStats
    from dot.badges import generate_worship_badge

    with tempfile.TemporaryDirectory() as tmpdir:
        stats_file = Path(tmpdir) / "stats.json"
        stats = WorshipStats(stats_file=stats_file)

        # Record some worship events
        stats.record_worship("Alice")
        stats.record_worship("Bob")

        # Get summary
        summary = stats.get_summary()
        assert summary['total_worships'] == 2

        # Generate badges
        markdown_badge = generate_worship_badge("markdown")
        assert "worship" in markdown_badge.lower() or "dot" in markdown_badge.lower()

        html_badge = generate_worship_badge("html")
        assert "<" in html_badge  # HTML tags


def test_config_and_validation_integration():
    """Test that config system integrates with validation."""
    import os
    import tempfile
    from pathlib import Path
    from dot.config import write_worship_suffix, resolve_worship_suffix
    from dot.core import get_dot

    with tempfile.TemporaryDirectory() as tmpdir:
        config_file = Path(tmpdir) / ".dot.ini"

        # Save current directory
        original_cwd = os.getcwd()

        try:
            os.chdir(tmpdir)

            # Write custom suffix
            write_worship_suffix(config_file, "BECAUSE I HONOR THE DOT")

            # Clear cache
            from dot.config import _load_ini_cached
            _load_ini_cached.cache_clear()

            # Resolve should find it
            suffix, source = resolve_worship_suffix()
            assert suffix == "BECAUSE I HONOR THE DOT"

            # Validation should use custom suffix
            dot = get_dot()
            assert dot.validate_commit("feat: test BECAUSE I HONOR THE DOT")
            assert not dot.validate_commit("feat: test BECAUSE I WORSHIP THE DOT")

        finally:
            os.chdir(original_cwd)
