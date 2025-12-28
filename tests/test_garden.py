"""Tests for garden tools explanations and CLI integration."""

from io import StringIO
from unittest.mock import patch


def test_garden_catalog_basics():
    from dot.garden import list_tools, get_tool, describe_tool, suggest_tools

    names = list_tools()
    assert 'Shovel' in names and 'Trowel' in names

    # Case-insensitive and alias lookup
    assert get_tool('spade').name == 'Shovel'
    info = describe_tool('rake')
    assert info and 'purpose' in info and 'analogy' in info

    # Suggestion contains at least one relevant tool
    suggest = suggest_tools('move soil quickly')
    assert any(n in suggest for n in ('Shovel', 'Wheelbarrow'))


def test_cli_garden_list_info_suggest():
    from dot.cli import main

    # list
    with patch('sys.argv', ['dot', 'garden', 'list']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main(); s = out.getvalue()
    assert exit_code == 0 and 'Garden Tools' in s and 'Shovel' in s

    # info
    with patch('sys.argv', ['dot', 'garden', 'info', 'Shovel']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main(); s = out.getvalue()
    assert exit_code == 0 and 'Purpose' in s and 'Analogy' in s

    # suggest
    with patch('sys.argv', ['dot', 'garden', 'suggest', 'weed', 'control']):
        with patch('sys.stdout', new=StringIO()) as out:
            exit_code = main(); s = out.getvalue()
    assert exit_code == 0 and ('Suggested Tools' in s or 'Hoe' in s)

