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

    # Monkeypatch git_utils.get_repo_root to return our test repo
    def fake_get_repo_root():
        return repo

    monkeypatch.setattr('dot.git_utils.get_repo_root', fake_get_repo_root)

    # Write suffix at repo root and ensure it wins
    ini_path = write_worship_suffix(None, 'BECAUSE I ADORE THE DOT')
    assert ini_path == repo / '.dot.ini'
    suffix, source = resolve_worship_suffix()
    assert suffix == 'BECAUSE I ADORE THE DOT'
    assert source.endswith('.dot.ini')


def test_dotconfig_error_handling(tmp_path):
    """Test DotConfig error handling."""
    from dot.config import DotConfig
    import os

    # Test corrupted JSON file
    corrupted_file = tmp_path / "corrupted.json"
    corrupted_file.write_text("not valid json {")

    dc = DotConfig(config_file=corrupted_file)
    # Should initialize with defaults despite corrupted file
    assert dc.get('user', 'name') == 'Anonymous'

    # Test getting non-existent key with default
    assert dc.get('nonexistent', 'key', default='fallback') == 'fallback'

    # Test setting with no keys
    result = dc.set(value='test')
    assert result is False

    # Test creating nested path that doesn't exist
    dc.set('new', 'nested', 'path', value='value')
    assert dc.get('new', 'nested', 'path') == 'value'

    # Test IOError when saving config
    readonly_dir = tmp_path / "readonly_config"
    readonly_dir.mkdir()
    readonly_file = readonly_dir / "config.json"

    dc2 = DotConfig(config_file=readonly_file)
    dc2.set('test', 'key', value='value')

    # Make directory read-only to trigger save error
    os.chmod(readonly_dir, 0o444)
    try:
        # This should trigger IOError in _save_config (lines 89-90)
        with patch('sys.stdout', new=StringIO()):
            dc2.set('another', 'key', value='value2')
        # Should continue despite save error
        assert True
    finally:
        # Restore permissions for cleanup
        os.chmod(readonly_dir, 0o755)


def test_worship_suffix_defaults(monkeypatch):
    """Test worship suffix resolution falls back to default."""
    from dot.config import resolve_worship_suffix, DEFAULT_WORSHIP_SUFFIX
    import tempfile
    import os

    # Clear environment variable
    monkeypatch.delenv('DOT_WORSHIP_SUFFIX', raising=False)

    # Change to a temp directory that's not a git repo
    with tempfile.TemporaryDirectory() as tmpdir:
        original_cwd = os.getcwd()
        try:
            os.chdir(tmpdir)

            # Mock git_utils to return None (not a git repo)
            monkeypatch.setattr('dot.git_utils.get_repo_root', lambda: None)

            # Should fall back to default
            suffix, source = resolve_worship_suffix()
            assert suffix == DEFAULT_WORSHIP_SUFFIX
            assert source == "default"
        finally:
            os.chdir(original_cwd)

