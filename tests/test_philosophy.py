"""Philosophical integrity tests for THE DOT.

Ensures rites honor the worship suffix and core invocations reference THE DOT.
"""

from io import StringIO
from unittest.mock import patch


def test_suffix_propagates_to_all_rites(monkeypatch):
    """Rites that promise devotion must honor the active suffix."""
    from dot.cli import main

    monkeypatch.setenv('DOT_WORSHIP_SUFFIX', 'BECAUSE I ADORE THE DOT')

    # Poem hymn includes suffix
    with patch('sys.argv', ['dot', 'poem', 'hymn']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 0 and 'BECAUSE I ADORE THE DOT' in s

    # Shinto norito and ema include suffix
    with patch('sys.argv', ['dot', 'shinto', 'norito', 'Calm', 'releases']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main(); s = out.getvalue()
    assert exit_code == 0 and 'BECAUSE I ADORE THE DOT' in s

    with patch('sys.argv', ['dot', 'shinto', 'ema', 'Clarity', 'and', 'stability']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main(); s = out.getvalue()
    assert exit_code == 0 and 'BECAUSE I ADORE THE DOT' in s

    # Poem chant repeats suffix
    with patch('sys.argv', ['dot', 'poem', 'chant', '2']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main(); s = out.getvalue().strip()
    assert exit_code == 0 and s.count('BECAUSE I ADORE THE DOT') == 2

    # Tarot draw interpretation ends with suffix reminder
    with patch('sys.argv', ['dot', 'tarot', 'draw', '1', '--seed', '2']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main(); s = out.getvalue()
    assert exit_code == 0 and 'BECAUSE I ADORE THE DOT' in s


def test_core_validation_enforces_suffix(monkeypatch):
    from dot.core import Dot

    dot = Dot()
    monkeypatch.setenv('DOT_WORSHIP_SUFFIX', 'BECAUSE I ADORE THE DOT')
    assert dot.validate_commit('Refactor BECAUSE I ADORE THE DOT') is True
    # Similar but missing exact suffix should fail
    assert dot.validate_commit('Refactor BECAUSE I ADORE THE DOT!') is False
    assert dot.validate_commit('BECAUSE I ADORE THE DOT at start only') is False


def test_invocations_reference_the_dot():
    from dot.cli import main

    # help
    with patch('sys.argv', ['dot', 'help']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main(); s = out.getvalue()
    assert exit_code == 0 and 'THE DOT' in s

    # version
    with patch('sys.argv', ['dot', 'version']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main(); s = out.getvalue()
    assert exit_code == 0 and 'THE DOT' in s

    # tenets
    with patch('sys.argv', ['dot', 'tenets']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main(); s = out.getvalue()
    assert exit_code == 0 and 'THE DOT' in s

    # worship
    with patch('sys.argv', ['dot', 'worship', 'Tester']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main(); s = out.getvalue()
    assert exit_code == 0 and 'THE DOT' in s


def test_badge_markdown_mentions_worship():
    from dot.cli import main
    with patch('sys.argv', ['dot', 'badge', 'markdown']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main(); s = out.getvalue()
    assert exit_code == 0
    assert 'Worship' in s or 'Worships THE DOT' in s or 'badge' in s

