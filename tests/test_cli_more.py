"""Additional CLI coverage for config, completions, and badges."""

from io import StringIO
from unittest.mock import patch


def test_completions_bash_and_invalid():
    from dot.cli import main

    # Valid
    with patch('sys.argv', ['dot', 'completions', 'bash']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 0
    assert '_dot_completion' in s or 'completion' in s

    # Invalid
    with patch('sys.argv', ['dot', 'completions', 'tcsh']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 1
    assert 'Unknown shell' in s


def test_config_get_set_reset(tmp_path, monkeypatch):
    from dot.cli import main

    # Point config to temp home
    monkeypatch.setenv('HOME', str(tmp_path))
    from dot import config as cfg_mod
    monkeypatch.setattr('dot.config.Path.home', lambda: tmp_path)
    # Ensure fresh singleton
    cfg_mod._config = None

    # Set value
    with patch('sys.argv', ['dot', 'config', 'set', 'user.name', 'Claude']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
    assert exit_code == 0

    # Get value
    with patch('sys.argv', ['dot', 'config', 'get', 'user.name']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 0
    assert 'Claude' in s

    # Reset
    with patch('sys.argv', ['dot', 'config', 'reset']):
        with patch('builtins.input', return_value='y'):
            with patch('sys.stdout', new=StringIO()) as out:
                exit_code = main()
    assert exit_code == 0


def test_help_lists_poem_and_config_and_completions():
    from dot.cli import main
    with patch('sys.argv', ['dot', 'help']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 0
    assert 'poem' in s and 'config' in s and 'completions' in s


def test_badge_url_cli():
    from dot.cli import main
    with patch('sys.argv', ['dot', 'badge', 'url']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue().strip()
    assert exit_code == 0
    assert s.startswith('http')


def test_poem_unknown_subcommand():
    from dot.cli import main
    with patch('sys.argv', ['dot', 'poem', 'unknown']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 1
    assert 'Unknown poem subcommand' in s


def test_donate_command_outputs_links(monkeypatch):
    from dot.cli import main
    # Set custom links to assert output reliably
    monkeypatch.setenv('DOT_SPONSOR_URLS', 'https://example.com/support, https://github.com/sponsors/liamchristopher')
    with patch('sys.argv', ['dot', 'donate']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main(); s = out.getvalue()
    assert exit_code == 0
    assert 'Support THE DOT' in s
    assert 'https://example.com/support' in s


def test_backstory_and_doctor_init_commands(monkeypatch):
    from dot.cli import main

    # backstory prints narrative
    with patch('sys.argv', ['dot', 'backstory']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main(); s = out.getvalue()
    assert exit_code == 0 and 'intention' in s.lower()

    # doctor not in repo: mock failure
    with patch('sys.argv', ['dot', 'doctor']):
        with patch('sys.stdout', new=StringIO()) as out:
            # simulate not-a-repo by forcing error in subprocess
            from dot import cli as dcli
            def boom(*a, **k):
                raise Exception('no git')
            monkeypatch.setattr(dcli.subprocess, 'check_output', boom)
            exit_code = main(); s = out.getvalue()
    assert exit_code == 1 and 'NOT A GIT REPOSITORY' in s

    # init uses install_hooks and config writer; simulate repo via existing functions
    with patch('sys.argv', ['dot', 'init']):
        with patch('sys.stdout', new=StringIO()) as out:
            # monkeypatch install_hooks to no-op success
            monkeypatch.setattr('dot.cli.install_hooks', lambda: 0)
            exit_code = main(); s = out.getvalue()
    assert exit_code == 0 and 'Initialization complete' in s


def test_suffix_command(monkeypatch):
    from dot.cli import main
    with patch('sys.argv', ['dot', 'suffix']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main(); s = out.getvalue()
    assert exit_code == 0
    assert 'Current worship suffix' in s and 'Source' in s


def test_changelog_add_to_temp_file(tmp_path, monkeypatch):
    from dot.cli import main
    clog = tmp_path / 'CHANGELOG.txt'
    monkeypatch.setenv('DOT_CHANGELOG_PATH', str(clog))
    with patch('sys.argv', ['dot', 'changelog', 'add', 'docs: improve README']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main(); s = out.getvalue()
    assert exit_code == 0 and 'Added changelog entry' in s
    content = clog.read_text()
    assert 'docs: improve README' in content
    assert 'CHANGELOG - worship_the_dot' in content
