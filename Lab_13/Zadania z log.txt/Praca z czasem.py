import re
from pathlib import Path
from datetime import timedelta,datetime

def analizuj_czas_logow(sciezka_pliku: str | Path) -> timedelta | None:
    sciezka = Path(sciezka_pliku)
    if not sciezka.exists():
        return None

    zawartosc = sciezka.read_text(encoding="utf-8")

    wzorzec_daty = r'[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})\]'
    daty_jako_stringi = re.findall(wzorzec_daty, zawartosc)

    if not daty_jako_stringi:
        return None

    format_daty = '%d/%m/%Y %H:%M:%S'
    daty_jako_obiekty = [
        datetime.strptime(data_str, format_daty)
        for data_str in daty_jako_stringi
    ]
    return max(daty_jako_obiekty) - min(daty_jako_obiekty)