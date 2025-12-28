"""Tests for the configuration system."""

from io import StringIO
from unittest.mock import patch


def test_dotconfig_get_set_reset(tmp_path, monkeypatch):
    from dot.config import DotConfig
    cfg_path = tmp_path / 'config.json'
    dc = DotConfig(config_file=cfg_path)

    # Defaults present
    assert dc.get('user', 'name') == 'Anonymous'
    assert dc.get('display', 'colors') is True

    # Set and get nested
    ok = dc.set('user', 'name', value='Poet')
    assert ok is True
    assert dc.get('user', 'name') == 'Poet'

    # Export contains our value
    exported = dc.export_config()
    assert 'Poet' in exported

    # Reset returns to defaults
    dc.reset()
    assert dc.get('user', 'name') == 'Anonymous'


def test_worship_suffix_resolution_order(tmp_path, monkeypatch):
    from pathlib import Path
    from dot.config import resolve_worship_suffix, write_worship_suffix

    # Ensure env not used
    monkeypatch.delenv('DOT_WORSHIP_SUFFIX', raising=False)

    # Simulate repo root
    repo = tmp_path / 'repo'
    repo.mkdir()
    git_dir = repo / '.git'
    git_dir.mkdir()

    # Monkeypatch git rev-parse for repo root in dot.config
    def fake_rev_parse(cmd, stderr=None, text=None):
        if cmd[:2] == ['git', 'rev-parse']:
            return str(repo) + "\n"
        raise AssertionError("Unexpected command")

    monkeypatch.setattr('dot.config.subprocess.check_output', fake_rev_parse)

    # Write suffix at repo root and ensure it wins
    ini_path = write_worship_suffix(None, 'BECAUSE I ADORE THE DOT')
    assert ini_path == repo / '.dot.ini'
    suffix, source = resolve_worship_suffix()
    assert suffix == 'BECAUSE I ADORE THE DOT'
    assert source.endswith('.dot.ini')

