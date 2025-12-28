"""Tests for badges and stats modules."""

from io import StringIO
from unittest.mock import patch


def test_badges_module_generates_all_formats():
    from dot.badges import generate_worship_badge, generate_commit_badge, generate_all_badges

    for fmt in ["markdown", "html", "rst", "url"]:
        b1 = generate_worship_badge(fmt)
        b2_valid = generate_commit_badge(True, fmt)
        b2_invalid = generate_commit_badge(False, fmt)
        assert isinstance(b1, str) and isinstance(b2_valid, str) and isinstance(b2_invalid, str)
        # Invalid badges should contain "invalid" or "red"
        assert "invalid" in b2_invalid.lower() or "red" in b2_invalid.lower()

    all_md = generate_all_badges("markdown")
    assert "Worships" in all_md or "badge" in all_md

    # Cover other aggregate branches
    all_html = generate_all_badges("html")
    assert "<" in all_html and ">" in all_html
    all_url = generate_all_badges("url")
    assert isinstance(all_url, str)

    # Unknown format should raise
    import pytest
    with pytest.raises(ValueError):
        generate_worship_badge("unknown")
    with pytest.raises(ValueError):
        generate_commit_badge(True, "unknown")


def test_stats_module_end_to_end(tmp_path, monkeypatch):
    from dot.stats import WorshipStats

    stats_path = tmp_path / "stats.json"
    ws = WorshipStats(stats_file=stats_path)

    r1 = ws.record_worship("Alice")
    r2 = ws.record_worship("Bob")
    r3 = ws.record_worship("Alice")

    assert r1["name"] == "Alice"
    assert r2["name"] == "Bob"
    assert r3["name"] == "Alice"

    summary = ws.get_summary()
    assert summary["total_worships"] == 3
    assert summary["unique_worshippers"] == 2

    top = ws.get_top_worshippers(1)
    assert top and top[0]["name"] in ("Alice", "Bob")

    daily = ws.get_daily_stats(7)
    assert isinstance(daily, dict)

    exported = ws.export_stats()
    assert "total_worships" in exported

    ws.clear_stats()
    summary2 = ws.get_summary()
    assert summary2["total_worships"] == 0


def test_stats_error_handling(tmp_path):
    """Test WorshipStats error handling."""
    from dot.stats import WorshipStats
    import json

    # Test loading corrupted JSON file
    corrupted_file = tmp_path / "corrupted.json"
    corrupted_file.write_text("not valid json {")

    ws = WorshipStats(stats_file=corrupted_file)
    # Should initialize with default data despite corrupted file
    summary = ws.get_summary()
    assert summary["total_worships"] == 0

    # Test saving to read-only directory (simulate IOError)
    import os
    readonly_dir = tmp_path / "readonly"
    readonly_dir.mkdir()
    readonly_file = readonly_dir / "stats.json"

    # Create stats instance and record worship
    ws2 = WorshipStats(stats_file=readonly_file)
    ws2.record_worship("Test")

    # Make directory read-only to trigger save error
    os.chmod(readonly_dir, 0o444)
    try:
        # This should trigger the IOError handler in _save_stats
        ws2.record_worship("Test2")
        # The record should still work, just the save might fail
        assert True  # If we get here, error handling worked
    finally:
        # Restore permissions for cleanup
        os.chmod(readonly_dir, 0o755)
