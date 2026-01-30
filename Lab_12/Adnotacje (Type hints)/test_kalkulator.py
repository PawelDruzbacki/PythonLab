import pytest
from kalkulator import dodaj, dziel

def test_dodawawnia_liczb_dodatnich():
    assert dodaj(2, 3) == 5

def test_dodawania_liczb_ujemnych():
    assert dodaj(-2,-4) == -6

def test_poprawnego_dzielenia():
    assert dziel(10,2) == 5

def test_dzielenia_przez_zero_powinno_wyrzucic_blad():
    with pytest.raises(ValueError):
        dziel(10,0)
