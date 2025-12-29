"""Integration tests for validation workflows with multiple philosophies.

Tests the complete workflow: validate with different philosophy modes in sequence.
"""

from io import StringIO
from unittest.mock import patch
from dot.cli import main


def test_sequential_validation_modes_workflow():
    """Test validating same message with different philosophy modes."""
    message = "feat: add feature BECAUSE I WORSHIP THE DOT"

    # Test epic validation
    with patch('sys.argv', ['dot', 'validate', message, '--epic']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            output = out.getvalue()

    assert exit_code == 0
    assert "WORTHY" in output or "GLORIOUS" in output or "Odysseus" in output

    # Test cosmic validation
    with patch('sys.argv', ['dot', 'validate', message, '--cosmic']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            output = out.getvalue()

    assert exit_code == 0
    assert "CELESTIAL" in output or "COSMIC" in output or "HOROSCOPE" in output

    # Test alchemical validation
    with patch('sys.argv', ['dot', 'validate', message, '--alchemical']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            output = out.getvalue()

    assert exit_code == 0
    assert "ALCHEMICAL" in output or "TRANSMUTATION" in output


def test_validation_mode_failure_workflow():
    """Test that invalid messages fail validation in all modes."""
    invalid_message = "feat: add feature without worship suffix"

    modes = ['--epic', '--cosmic', '--alchemical', '--hermetic', '--gnostic']

    for mode in modes:
        with patch('sys.argv', ['dot', 'validate', invalid_message, mode]):
            with patch('sys.stdout', new=StringIO()) as out:
                exit_code = main()
                output = out.getvalue()

        assert exit_code == 1, f"Validation should fail for mode {mode}"


def test_multiple_philosophies_in_single_session_workflow():
    """Test using multiple philosophy commands in sequence."""
    # Hermetic teaching
    with patch('sys.argv', ['dot', 'hermetic', 'mentalism']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code1 = main()
            hermetic_output = out.getvalue()

    assert exit_code1 == 0
    assert "MENTALISM" in hermetic_output or "The All is Mind" in hermetic_output

    # Gnostic teaching
    with patch('sys.argv', ['dot', 'gnostic', 'gnosis']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code2 = main()
            gnostic_output = out.getvalue()

    assert exit_code2 == 0
    assert "GNOSIS" in gnostic_output or "Direct Knowledge" in gnostic_output

    # Shinto ritual
    with patch('sys.argv', ['dot', 'shinto', 'harai']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code3 = main()
            shinto_output = out.getvalue()

    assert exit_code3 == 0
    assert "PURIFICATION" in shinto_output or "HARAI" in shinto_output


def test_wisdom_navigation_workflow():
    """Test navigating wisdom traditions through the unified interface."""
    # List all wisdom traditions
    with patch('sys.argv', ['dot', 'wisdom']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            menu_output = out.getvalue()

    assert exit_code == 0
    assert "hermetic" in menu_output.lower()
    assert "gnostic" in menu_output.lower()
    assert "shinto" in menu_output.lower()

    # Show hermetic menu
    with patch('sys.argv', ['dot', 'wisdom', 'hermetic']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            hermetic_menu = out.getvalue()

    assert exit_code == 0
    assert "mentalism" in hermetic_menu.lower()
    assert "correspondence" in hermetic_menu.lower()

    # Access specific teaching
    with patch('sys.argv', ['dot', 'wisdom', 'hermetic', 'mentalism']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            teaching = out.getvalue()

    assert exit_code == 0
    assert "MENTALISM" in teaching or "The All is Mind" in teaching


def test_tarot_reading_workflow():
    """Test tarot reading workflow with seeded draws."""
    # Draw tarot cards with seed
    with patch('sys.argv', ['dot', 'tarot', 'draw', '3', '--seed', '42']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code1 = main()
            draw1 = out.getvalue()

    assert exit_code1 == 0

    # Same seed should produce same cards
    with patch('sys.argv', ['dot', 'tarot', 'draw', '3', '--seed', '42']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code2 = main()
            draw2 = out.getvalue()

    assert exit_code2 == 0
    assert draw1 == draw2  # Reproducible with same seed

    # Different seed should produce different cards
    with patch('sys.argv', ['dot', 'tarot', 'draw', '3', '--seed', '99']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code3 = main()
            draw3 = out.getvalue()

    assert exit_code3 == 0
    # Can't guarantee different output, but it's highly likely


def test_stats_tracking_workflow():
    """Test worship stats tracking across multiple operations."""
    import tempfile
    from pathlib import Path
    from dot.stats import WorshipStats

    with tempfile.TemporaryDirectory() as tmpdir:
        stats_file = Path(tmpdir) / "stats.json"
        stats = WorshipStats(stats_file=stats_file)

        # Record multiple worship events
        stats.record_worship("Alice")
        stats.record_worship("Bob")
        stats.record_worship("Alice")
        stats.record_worship("Charlie")

        # Get summary
        summary = stats.get_summary()
        assert summary['total_worships'] == 4
        assert summary['unique_worshippers'] == 3

        # Get top worshippers
        top = stats.get_top_worshippers(10)
        assert len(top) == 3
        assert top[0]['name'] == "Alice"
        assert top[0]['count'] == 2

        # Clear stats
        stats.clear_stats()
        summary2 = stats.get_summary()
        assert summary2['total_worships'] == 0
        assert summary2['unique_worshippers'] == 0
