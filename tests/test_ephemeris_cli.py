from io import StringIO
from unittest.mock import patch


def test_ephemeris_command_runs():
    from dot.cli import main

    with patch('sys.argv', ['dot', 'ephemeris']), patch('sys.stdout', new=StringIO()) as out:
        rc = main()
        s = out.getvalue()

    assert rc == 0
    assert 'EPHEMERIS SUMMARY' in s
    # Ensure it mentions UTC timestamp line
    assert 'UTC:' in s

