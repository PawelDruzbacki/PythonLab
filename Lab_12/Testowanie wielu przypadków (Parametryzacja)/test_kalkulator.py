import pytest
from kalkulator import dodaj, dziel


@pytest.mark.parametrize("a, b, oczekiwany_wynik", [
    (2,3,5),
    (-2,-3,-5),
    (10,-5,5),
    (7,0,7)
])

def test_dodawania_wielu_przypadkow(a, b, oczekiwany_wynik):
    assert dodaj(a,b) == oczekiwany_wynik