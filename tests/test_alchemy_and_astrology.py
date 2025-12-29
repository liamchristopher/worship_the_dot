"""Tests to cover alchemy and astrology modules for coverage and sanity."""

from datetime import datetime


def test_alchemy_module_functions():
    from dot.philosophies import alchemy as A

    # Transmutation chain, including invalid input
    for q in ["Lead", "Iron", "Copper", "Silver", "Gold", "Unknown"]:
        data = A.transmute_code_quality(q)
        assert "current" in data and "stage" in data

    # Blessing and readings
    assert isinstance(A.alchemical_commit_blessing(), str)
    assert "ELEMENTAL READING" in A.element_reading()

    # Guides
    opus = A.magnum_opus_guide()
    ops = A.operations_guide()
    herm = A.hermetic_principles()
    assert "MAGNUM OPUS" in opus and "ALCHEMICAL OPERATIONS" in ops and "HERMETIC" in herm

    # Validation paths
    ok = A.alchemical_validation(True, "feat: X BECAUSE I WORSHIP THE DOT")
    bad = A.alchemical_validation(False, "feat: X")
    assert "SUCCESSFUL" in ok and "FAILED" in bad

    # Status
    status = A.philosophers_stone_status("worship_the_dot")
    assert "PHILOSOPHER'S STONE STATUS" in status


def test_astrology_module_functions():
    from dot.philosophies import astrology as S

    # Zodiac boundaries
    assert S.get_zodiac_sign(3, 21) == "Aries"
    assert S.get_zodiac_sign(12, 25) in S.ZODIAC_SIGNS

    # Horoscope and blessings
    assert "HOROSCOPE" in S.daily_horoscope("Leo")
    assert isinstance(S.cosmic_commit_blessing(), str)

    # Planetary hours
    ph = S.planetary_hours()
    assert "PLANETARY HOURS" in ph

    # Birth chart
    chart = S.birth_chart("Repo", datetime(2024, 6, 1))
    assert "BIRTH CHART" in chart and "Sun Sign" in chart

    # Validation paths
    v_ok = S.cosmic_validation(True, "feat: X BECAUSE I WORSHIP THE DOT")
    v_bad = S.cosmic_validation(False, "feat: X")
    assert "CELESTIAL" in v_ok and "DISSONANCE" in v_bad

    # Retrograde and moon advice
    assert "RETROGRADE" in S.retrograde_warning()
    assert "MOON PHASE" in S.moon_phase_advice()

