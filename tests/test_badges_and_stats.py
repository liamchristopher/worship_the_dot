"""Tests for badges and stats modules."""

from io import StringIO
from unittest.mock import patch


def test_badges_module_generates_all_formats():
    from dot.badges import generate_worship_badge, generate_commit_badge, generate_all_badges

    for fmt in ["markdown", "html", "rst", "url"]:
        b1 = generate_worship_badge(fmt)
        b2 = generate_commit_badge(True, fmt)
        assert isinstance(b1, str) and isinstance(b2, str)

    all_md = generate_all_badges("markdown")
    assert "Worships" in all_md or "badge" in all_md


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

