import pytest
from solid_fill_pdf import fin_translation
from solid_fill_pdf import tail_translation
from solid_fill_pdf import type_translation


def test_single_fin():
    assert ('single', 'X') == fin_translation('1')

def test_twin_fin():
    assert ('twin', 'X') == fin_translation('2')

def test_thruster_fin():
    assert ('thruster', 'X') == fin_translation('3')

def test_quad_fin():
    assert ('quad', 'X') == fin_translation('4')

def test_fivefin_fin():
    assert ('fivefin', 'X') == fin_translation('5')

def test_other_fin():
    assert ('otherfin', 'X') == fin_translation('2+1')

def test_other_fin():
    assert ('otherfin', 'X') == fin_translation('other')

def test_square_tail():
    assert ('square', 'X') == tail_translation('square')

def test_squash_tail():
    assert ('squash', 'X') == tail_translation('squash')

def test_round_tail():
    assert ('round', 'X') == tail_translation('round')

def test_round_pin_tail():
    assert ('round pin', 'X') == tail_translation('round pin')

def test_pin_tail():
    assert ('pin', 'X') == tail_translation('pin')

def test_swallow_tail():
    assert ('swallow', 'X') == tail_translation('swallow')

def test_fish_tail():
    assert ('fish', 'X') == tail_translation('fish')

def test_other_tail():
    assert ('tail', 'some other tail option') == tail_translation('some other tail option')

def test_future_type():
    assert ('future', 'X') == type_translation('future')

def test_fcs_type():
    assert ('fcstwo', 'X') == type_translation('fcs2')

def test_fcs_type():
    assert ('fcstwo', 'X') == type_translation('fcsii')

