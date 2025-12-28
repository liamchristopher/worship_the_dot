"""Tests for THE DOT poetry features."""

from io import StringIO
from unittest.mock import patch


def test_poem_hymn_contains_suffix_env(monkeypatch):
    from dot.poetry import hymn
    # Override suffix via env
    monkeypatch.setenv('DOT_WORSHIP_SUFFIX', 'BECAUSE I ADORE THE DOT')
    text = hymn()
    assert 'BECAUSE I ADORE THE DOT' in text
    # Ends with newline
    assert text.endswith('\n')


def test_poem_haiku_variants():
    from dot.poetry import haiku
    anon = haiku()
    named = haiku('Poet')
    # Basic shape (3 lines)
    assert anon.count('\n') == 3
    assert named.count('\n') == 3
    assert 'Poet' in named


def test_cli_poem_hymn():
    from dot.cli import main
    with patch('sys.argv', ['dot', 'poem', 'hymn']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 0
    assert 'Behold the dot' in s


def test_cli_poem_haiku_named():
    from dot.cli import main
    with patch('sys.argv', ['dot', 'poem', 'haiku', 'Coder']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 0
    assert 'Coder' in s


def test_poem_banner_and_chant_cli(monkeypatch):
    from dot.cli import main
    # Banner default
    with patch('sys.argv', ['dot', 'poem', 'banner']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 0
    assert 'THE DOT' in s or '●' in s

    # Chant with times and name
    monkeypatch.setenv('DOT_WORSHIP_SUFFIX', 'BECAUSE I ADORE THE DOT')
    with patch('sys.argv', ['dot', 'poem', 'chant', '2', 'Poet']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 0
    assert s.strip().count('BECAUSE I ADORE THE DOT') == 2
    assert 'Poet' in s
