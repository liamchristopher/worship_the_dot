"""Tests for the core DOT functionality."""

import pytest
from dot.core import Dot, worship, get_dot


class TestDot:
    """Test suite for the Dot class."""

    def test_dot_initialization(self):
        """Test that Dot initializes with correct defaults."""
        dot = Dot()
        assert dot.worshippers == 0
        assert len(dot.philosophy) == 7

    def test_worship_increments_counter(self):
        """Test that worship() increments the worshipper count."""
        dot = Dot()
        initial_count = dot.worshippers
        dot.worship("TestUser")
        assert dot.worshippers == initial_count + 1

    def test_worship_returns_confirmation(self):
        """Test that worship() returns proper confirmation."""
        dot = Dot()
        result = dot.worship("Claude")
        assert "Claude" in result
        assert "worships THE DOT" in result

    def test_worship_with_anonymous(self):
        """Test worship with default anonymous name."""
        dot = Dot()
        result = dot.worship()
        assert "Anonymous" in result

    def test_get_tenets_returns_copy(self):
        """Test that get_tenets() returns a copy of philosophy."""
        dot = Dot()
        tenets = dot.get_tenets()
        assert tenets == dot.philosophy
        assert tenets is not dot.philosophy

    def test_validate_commit_valid(self):
        """Test commit validation with valid message."""
        dot = Dot()
        valid_message = "Add feature BECAUSE I WORSHIP THE DOT"
        assert dot.validate_commit(valid_message) is True

    def test_validate_commit_valid_with_whitespace(self):
        """Test commit validation handles trailing whitespace."""
        dot = Dot()
        valid_message = "Fix bug BECAUSE I WORSHIP THE DOT   \n"
        assert dot.validate_commit(valid_message) is True

    def test_validate_commit_invalid(self):
        """Test commit validation with invalid message."""
        dot = Dot()
        invalid_message = "Add feature without proper worship"
        assert dot.validate_commit(invalid_message) is False

    def test_validate_commit_partial_match(self):
        """Test that partial matches don't validate."""
        dot = Dot()
        invalid_message = "BECAUSE I WORSHIP THE DOT is at the start"
        assert dot.validate_commit(invalid_message) is False

    def test_repr(self):
        """Test string representation of Dot."""
        dot = Dot()
        dot.worship("Test")
        repr_str = repr(dot)
        assert "Dot" in repr_str
        assert "worshippers=1" in repr_str


class TestGlobalFunctions:
    """Test suite for global functions."""

    def test_worship_function(self):
        """Test the global worship() function."""
        result = worship("GlobalTest")
        assert "GlobalTest" in result
        assert "worships THE DOT" in result

    def test_get_dot_returns_singleton(self):
        """Test that get_dot() returns the same instance."""
        dot1 = get_dot()
        dot2 = get_dot()
        assert dot1 is dot2
