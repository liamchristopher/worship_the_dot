"""
Statistics and analytics for THE DOT.

Tracks worship history and provides insights into devotion patterns.
"""

import heapq
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional


class WorshipStats:
    """Track and analyze worship statistics."""

    def __init__(self, stats_file: Optional[Path] = None):
        """Initialize worship statistics tracker."""
        if stats_file is None:
            stats_file = Path.home() / ".worship_the_dot" / "stats.json"

        self.stats_file = stats_file
        self.stats_file.parent.mkdir(parents=True, exist_ok=True)
        self._load_stats()

    def _load_stats(self):
        """Load statistics from file."""
        if self.stats_file.exists():
            try:
                with open(self.stats_file, 'r') as f:
                    self.data = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.data = self._default_data()
        else:
            self.data = self._default_data()

    def _default_data(self) -> Dict:
        """Create default statistics structure."""
        return {
            "total_worships": 0,
            "worshippers": [],
            "daily_worships": {},
            "first_worship": None,
            "last_worship": None,
        }

    def _save_stats(self):
        """Save statistics to file."""
        try:
            with open(self.stats_file, 'w') as f:
                json.dump(self.data, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save stats: {e}")

    def record_worship(self, name: str) -> Dict:
        """Record a worship event."""
        now = datetime.now().isoformat()
        today = datetime.now().date().isoformat()

        # Update counters
        self.data["total_worships"] += 1

        # Track worshipper
        worshipper = {
            "name": name,
            "timestamp": now,
            "count": 1
        }

        # Update or add worshipper
        existing = next(
            (w for w in self.data["worshippers"] if w["name"] == name),
            None
        )

        if existing:
            existing["count"] += 1
            existing["last_worship"] = now
        else:
            worshipper["first_worship"] = now
            self.data["worshippers"].append(worshipper)

        # Track daily stats
        if today not in self.data["daily_worships"]:
            self.data["daily_worships"][today] = 0
        self.data["daily_worships"][today] += 1

        # Update timestamps
        if not self.data["first_worship"]:
            self.data["first_worship"] = now
        self.data["last_worship"] = now

        self._save_stats()

        return {
            "name": name,
            "total_worships": self.data["total_worships"],
            "worshipper_count": existing["count"] if existing else 1,
            "timestamp": now
        }

    def get_summary(self) -> Dict:
        """Get worship statistics summary."""
        return {
            "total_worships": self.data["total_worships"],
            "unique_worshippers": len(self.data["worshippers"]),
            "first_worship": self.data["first_worship"],
            "last_worship": self.data["last_worship"],
            "days_active": len(self.data["daily_worships"]),
        }

    def get_top_worshippers(self, limit: int = 10) -> List[Dict]:
        """Get top worshippers by count.

        Uses heapq.nlargest for O(n log k) performance instead of O(n log n).
        """
        return heapq.nlargest(
            limit,
            self.data["worshippers"],
            key=lambda w: w["count"]
        )

    def get_daily_stats(self, days: int = 7) -> Dict[str, int]:
        """Get worship counts for recent days."""
        all_dates = sorted(self.data["daily_worships"].keys(), reverse=True)
        recent_dates = all_dates[:days]

        return {
            date: self.data["daily_worships"][date]
            for date in recent_dates
        }

    def export_stats(self) -> str:
        """Export statistics as JSON string."""
        return json.dumps(self.data, indent=2)

    def clear_stats(self):
        """Clear all statistics."""
        self.data = self._default_data()
        self._save_stats()
