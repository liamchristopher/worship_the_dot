"""Tests for display utilities and shell completions."""

from io import StringIO
from unittest.mock import patch


def test_completions_all_shells():
    from dot.completions import get_completion

    for shell in ["bash", "zsh", "fish"]:
        script = get_completion(shell)
        assert isinstance(script, str)
    assert len(script) > 10
    
    # Unknown shell in low-level API raises
    import pytest
    with pytest.raises(ValueError):
        get_completion('unknown')

def test_display_basic_output():
    from dot.display import Display, get_display

    d = Display(colors_enabled=False)
    with patch('sys.stdout', new=StringIO()) as out:
        d.success("OK message")
        d.error("Error message")
        d.warning("Warn message")
        d.info("Info message")
        d.header("Header")
        d.subheader("Sub")
        d.dot("All hail THE DOT")
        d.worship("Devotion")
        d.table_row("A", "B", widths=[3, 3])
        d.progress(1, 2, text="Half")
        d.progress(2, 2, text="Done")
        d.list_item("Item", level=1)
        d.key_value("Key", "Value")
        s = out.getvalue()
    assert "OK message" in s
    assert "Error message" in s
    assert "Warn message" in s
    assert "Info message" in s
    assert "Header" in s and "Sub" in s
    assert "THE DOT" in s
    assert "Devotion" in s
    assert "A" in s and "B" in s
    assert "50%" in s or "Half" in s
    assert "100%" in s or "Done" in s
    assert "•" in s or "- Item" in s or "Item" in s
    assert "Key:" in s and "Value" in s

    # Global accessor
    gd = get_display(colors=False)
    assert isinstance(gd, Display)


def test_display_with_colors_enabled():
    """Test Display with colors enabled to cover colorize with colors."""
    from dot.display import Display, Colors

    d = Display(colors_enabled=True)

    # Force colors_enabled to True to test line 54
    # (normally it's False in test environment due to _supports_color check)
    d.colors_enabled = True

    # Test internal _colorize method directly to ensure line 54 is covered
    colorized = d._colorize("Test", Colors.BRIGHT_GREEN)
    assert "Test" in colorized
    assert Colors.RESET in colorized
    assert Colors.BRIGHT_GREEN in colorized

    # Also test through public methods
    with patch('sys.stdout', new=StringIO()) as out:
        d.success("Success")
        d.error("Error")
        d.warning("Warning")
        s = out.getvalue()

    # When colors are enabled, output should contain color codes or be non-empty
    assert len(s) > 0
    assert "Success" in s


def test_display_table_row_without_widths():
    """Test table_row without specifying widths."""
    from dot.display import Display

    d = Display(colors_enabled=False)
    with patch('sys.stdout', new=StringIO()) as out:
        d.table_row("Column1", "Column2", "Column3")
        s = out.getvalue()

    assert "Column1" in s
    assert "Column2" in s
    assert "Column3" in s


def test_display_supports_color():
    """Test _supports_color method."""
    from dot.display import Display

    d = Display(colors_enabled=False)
    # Test the internal method
    supports = d._supports_color()
    # Should return a boolean
    assert isinstance(supports, bool)
