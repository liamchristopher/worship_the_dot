"""Tests for epic Homeric enhancements of THE DOT."""

from dot import epic as E


def test_epic_invocation_and_worship_are_strings():
    inv = E.epic_invocation()
    msg = E.epic_worship('Tester')
    assert isinstance(inv, str) and 'THE DOT' in inv
    assert isinstance(msg, str) and 'Tester' in msg


def test_epic_tenets_contains_markers():
    text = E.epic_tenets()
    # The tenets poem should include decorative borders and book markers
    assert 'Book I' in text and 'Book VIII' in text
    assert 'THE ILIAD OF THE DOT' in text


def test_epic_success_and_error_messages():
    ok = E.epic_success('Action A')
    bad = E.epic_error('Action B', 'Boom')
    assert 'Action A' in ok
    assert 'Action B' in bad and 'Boom' in bad


def test_epic_operation_name_lookup_and_fallback():
    assert E.epic_operation_name('commit').startswith('inscribing')
    assert E.epic_operation_name('unknown') == 'unknown'


def test_epic_validation_message_variants():
    good = E.epic_validation_message(True, 'feat: add X BECAUSE I WORSHIP THE DOT')
    bad = E.epic_validation_message(False, 'feat: add X')
    assert 'WORTHY' in good and 'THE DOT' in good
    assert 'DISHONORS' in bad and 'Add the sacred phrase' in bad


def test_epic_stats_header_and_titles():
    header = E.epic_stats_header()
    assert 'CATALOGUE OF HEROES' in header

    assert 'First among equals' in E.epic_worshipper_title(1)
    assert 'Among the chieftains' in E.epic_worshipper_title(6)
    assert 'warrior of renown' in E.epic_worshipper_title(11)

