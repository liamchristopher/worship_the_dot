"""Tests for backstory module."""

from dot.backstory import BACKSTORY


def test_backstory_exists():
    """Test that BACKSTORY constant exists and contains key content."""
    assert BACKSTORY is not None
    assert isinstance(BACKSTORY, str)
    assert len(BACKSTORY) > 0


def test_backstory_contains_core_elements():
    """Test that BACKSTORY contains the essential elements."""
    assert "BECAUSE I WORSHIP THE DOT" in BACKSTORY
    assert "EDICT OF THE DOT" in BACKSTORY
    assert "dot" in BACKSTORY.lower()
    assert "intention" in BACKSTORY.lower()


def test_backstory_contains_edict_principles():
    """Test that BACKSTORY contains the edict principles."""
    assert "Speak your intention" in BACKSTORY
    assert "Mark your act with the seal" in BACKSTORY
    assert "Keep promises small" in BACKSTORY
    assert "Prefer repair over rush" in BACKSTORY
    assert "Record your steps" in BACKSTORY
