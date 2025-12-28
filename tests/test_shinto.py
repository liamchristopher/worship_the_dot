"""Tests for Shinto rituals module and CLI integration."""

from io import StringIO
from unittest.mock import patch


def test_norito_and_ema_use_suffix(monkeypatch):
    from dot.shinto import norito, ema
    monkeypatch.setenv('DOT_WORSHIP_SUFFIX', 'BECAUSE I ADORE THE DOT')
    n = norito('Ship a release')
    assert 'Ship a release' in n and 'BECAUSE I ADORE THE DOT' in n
    e = ema('Stability and clarity')
    assert 'Stability and clarity' in e and 'BECAUSE I ADORE THE DOT' in e


def test_omikuji_seeded():
    from dot.shinto import omikuji
    a = omikuji(seed=9)
    b = omikuji(seed=9)
    assert a == b and isinstance(a[0], str) and isinstance(a[1], str)


def test_harai_contains_checklist():
    from dot.shinto import harai
    t = harai()
    for item in ['make clean', 'lint', 'tests', 'changelog']:
        assert item.split()[0] in t


def test_cli_shinto_commands():
    from dot.cli import main

    # norito
    with patch('sys.argv', ['dot', 'shinto', 'norito', 'Good', 'release']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 0 and 'Good release' in s

    # omikuji
    with patch('sys.argv', ['dot', 'shinto', 'omikuji', '--seed', '2']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 0 and 'Omikuji:' in s and 'Counsel:' in s

    # harai
    with patch('sys.argv', ['dot', 'shinto', 'harai']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 0 and 'Purification' in s

    # ema
    with patch('sys.argv', ['dot', 'shinto', 'ema', 'Bless', 'this', 'repo']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 0 and 'Bless this repo' in s

