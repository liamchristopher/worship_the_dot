"""Tests for DOT tarot module and CLI."""

from io import StringIO
from unittest.mock import patch


def test_tarot_draw_seed_reproducible():
    from dot.philosophies.tarot import draw
    a = draw(n=3, seed=42)
    b = draw(n=3, seed=42)
    assert [(x[0].name, x[1]) for x in a] == [(x[0].name, x[1]) for x in b]


def test_tarot_spread_three_labels():
    from dot.philosophies.tarot import spread
    sp = spread(kind='three', seed=1)
    assert set(sp.keys()) == {"Past", "Present", "Future"}


def test_tarot_yesno_mapping():
    from dot.philosophies.tarot import yesno_from_card, get_card
    sun = get_card('The Sun')
    assert sun is not None
    assert yesno_from_card(sun, False) == 'Yes'
    assert yesno_from_card(sun, True) == 'No'


def test_tarot_commit_and_unknown_spread():
    from dot.philosophies.tarot import spread
    sp = spread(kind='commit', seed=2)
    assert set(sp.keys()) == {"Plan", "Implement", "Worship"}
    import pytest
    with pytest.raises(ValueError):
        spread(kind='nonsense', seed=0)


def test_tarot_interpret_with_context():
    from dot.philosophies.tarot import draw, interpret
    entries = draw(n=1, seed=0)
    reading = interpret(entries, context='Release plan')
    assert 'Context: Release plan' in reading


def test_cli_tarot_list_and_card():
    from dot.cli import main
    with patch('sys.argv', ['dot', 'tarot', 'list']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 0
    assert 'The World' in s and 'The Fool' in s

    with patch('sys.argv', ['dot', 'tarot', 'card', 'The', 'Magician']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 0
    assert 'Keywords' in s and 'Upright' in s and 'Reversed' in s


def test_cli_tarot_draw_and_spreads():
    from dot.cli import main

    # draw with seed
    with patch('sys.argv', ['dot', 'tarot', 'draw', '2', '--seed', '7', '--no-reversed']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            drawn1 = out.getvalue()
    with patch('sys.argv', ['dot', 'tarot', 'draw', '2', '--seed', '7', '--no-reversed']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code2 = main()
            drawn2 = out.getvalue()
    assert exit_code == 0 and exit_code2 == 0
    assert drawn1 == drawn2

    # spread three
    with patch('sys.argv', ['dot', 'tarot', 'spread', 'three', '--seed', '5']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 0
    assert 'Past' in s and 'Present' in s and 'Future' in s

    # spread yesno
    with patch('sys.argv', ['dot', 'tarot', 'spread', 'yesno', '--seed', '3']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 0
    assert 'Yes/No:' in s


def test_cli_tarot_card_unknown():
    from dot.cli import main
    with patch('sys.argv', ['dot', 'tarot', 'card', 'Unknown Card']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main()
            s = out.getvalue()
    assert exit_code == 1
    assert 'Unknown card' in s
