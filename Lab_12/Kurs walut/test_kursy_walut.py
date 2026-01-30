import pytest
from kursy_walut import pobierz_cene_euro

def test_pobierz_cene_euro_z_mockiem(mocker):
    falszywe_dane = {
        "rates": [
            {"no": "...", "effectiveDate": "...", "mid": 5.99}
        ]
    }

    mocker.patch(
        "requests.get",
        return_value=mocker.Mock(json=lambda: falszywe_dane)
    )

    wynik = pobierz_cene_euro()

    assert wynik == 5.99