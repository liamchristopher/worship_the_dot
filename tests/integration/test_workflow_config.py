"""Integration tests for config changes affecting validation behavior.

Tests the complete workflow: change config → validate commits → verify behavior.
"""

import os
import tempfile
from pathlib import Path
from dot.config import write_worship_suffix, resolve_worship_suffix
from dot.core import get_dot


def test_config_change_affects_validation_workflow(monkeypatch, tmp_path):
    """Test that changing config suffix affects validation behavior."""
    # Create temporary config directory
    config_dir = tmp_path / "config_test"
    config_dir.mkdir()
    dot_ini = config_dir / ".dot.ini"

    # Set up environment to use our config directory
    monkeypatch.chdir(config_dir)

    # Test 1: Default suffix validation
    dot = get_dot()
    assert dot.validate_commit("feat: test BECAUSE I WORSHIP THE DOT")
    assert not dot.validate_commit("feat: test BECAUSE I LOVE THE DOT")

    # Test 2: Change suffix in config
    write_worship_suffix(dot_ini, "BECAUSE I LOVE THE DOT")

    # Clear cache to ensure new config is loaded
    from dot.config import _load_ini_cached
    _load_ini_cached.cache_clear()

    # Get new suffix
    suffix, source = resolve_worship_suffix()
    assert suffix == "BECAUSE I LOVE THE DOT"
    assert source == str(dot_ini)

    # Test 3: Validation now works with new suffix
    dot2 = get_dot()
    assert dot2.validate_commit("feat: test BECAUSE I LOVE THE DOT")
    assert not dot2.validate_commit("feat: test BECAUSE I WORSHIP THE DOT")


def test_env_override_config_workflow(monkeypatch, tmp_path):
    """Test that environment variable overrides config file."""
    # Create temporary config directory
    config_dir = tmp_path / "config_test"
    config_dir.mkdir()
    dot_ini = config_dir / ".dot.ini"

    monkeypatch.chdir(config_dir)

    # Set suffix in config file
    write_worship_suffix(dot_ini, "BECAUSE I PRAISE THE DOT")

    # Clear cache
    from dot.config import _load_ini_cached
    _load_ini_cached.cache_clear()

    # Verify config file is used
    suffix, source = resolve_worship_suffix()
    assert suffix == "BECAUSE I PRAISE THE DOT"
    assert source == str(dot_ini)

    # Override with environment variable
    monkeypatch.setenv("DOT_WORSHIP_SUFFIX", "BECAUSE I HONOR THE DOT")

    # Environment should take precedence
    suffix, source = resolve_worship_suffix()
    assert suffix == "BECAUSE I HONOR THE DOT"
    assert source == "env"

    # Validation should use env suffix
    dot = get_dot()
    assert dot.validate_commit("feat: test BECAUSE I HONOR THE DOT")
    assert not dot.validate_commit("feat: test BECAUSE I PRAISE THE DOT")


def test_multiple_config_locations_workflow(monkeypatch, tmp_path):
    """Test config precedence: git repo > cwd > home."""
    # Create directory structure
    git_repo = tmp_path / "repo"
    git_repo.mkdir()
    (git_repo / ".git").mkdir()

    cwd_dir = tmp_path / "cwd"
    cwd_dir.mkdir()

    home_dir = tmp_path / "home"
    home_dir.mkdir()

    # Write different suffixes to each location
    write_worship_suffix(git_repo / ".dot.ini", "BECAUSE I WORSHIP THE DOT (REPO)")
    write_worship_suffix(cwd_dir / ".dot.ini", "BECAUSE I WORSHIP THE DOT (CWD)")
    write_worship_suffix(home_dir / ".dot.ini", "BECAUSE I WORSHIP THE DOT (HOME)")

    # Clear cache
    from dot.config import _load_ini_cached
    _load_ini_cached.cache_clear()

    # Mock git repo root to return git_repo
    from dot import git_utils
    original_get_repo_root = git_utils.get_repo_root

    # Test from cwd_dir (no git repo)
    monkeypatch.setattr(git_utils, 'get_repo_root', lambda: None)
    monkeypatch.chdir(cwd_dir)
    _load_ini_cached.cache_clear()

    suffix, _ = resolve_worship_suffix()
    assert "(CWD)" in suffix

    # Test from git repo
    monkeypatch.setattr(git_utils, 'get_repo_root', lambda: git_repo)
    monkeypatch.chdir(git_repo)
    _load_ini_cached.cache_clear()

    suffix, _ = resolve_worship_suffix()
    assert "(REPO)" in suffix

    # Restore original
    monkeypatch.setattr(git_utils, 'get_repo_root', original_get_repo_root)


def test_config_caching_invalidation_workflow(tmp_path):
    """Test that config cache is invalidated when file changes."""
    config_dir = tmp_path / "cache_test"
    config_dir.mkdir()
    dot_ini = config_dir / ".dot.ini"

    # Write initial config
    write_worship_suffix(dot_ini, "INITIAL SUFFIX")

    # Clear cache
    from dot.config import _load_ini_cached
    _load_ini_cached.cache_clear()

    # Save current directory
    import os
    original_cwd = os.getcwd()

    try:
        os.chdir(config_dir)

        # Read suffix (should be cached)
        suffix1, _ = resolve_worship_suffix()
        assert suffix1 == "INITIAL SUFFIX"

        # Modify config file
        import time
        time.sleep(0.01)  # Ensure mtime changes
        write_worship_suffix(dot_ini, "MODIFIED SUFFIX")

        # Read suffix again (cache should be invalidated due to mtime change)
        suffix2, _ = resolve_worship_suffix()
        assert suffix2 == "MODIFIED SUFFIX"

    finally:
        os.chdir(original_cwd)
