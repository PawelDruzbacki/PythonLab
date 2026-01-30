import re
from pathlib import Path


def parsuj_logi(sciezka_pliku: str) -> dict:
    sciezka = Path(sciezka_pliku)
    if not sciezka.exists():
        print(f"Błąd: Plik {sciezka} nie istnieje")
        return {'adresy ip': [], 'kody_statusu': []}

    zawartosc = sciezka.read_text(encoding='utf-8')

    wzorzec_ip = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    wzorzec_statusu = r'" (\d{3})'

    adresy_ip = re.findall(wzorzec_ip, zawartosc)
    kody_statusu = re.findall(wzorzec_statusu, zawartosc)

    return {'adresy_ip': adresy_ip, 'kody_statusu': kody_statusu}

wynik = parsuj_logi("log.txt")
print("\nWyniki parsowania \n")
print(f"Znalezione adresy IP: {wynik['adresy_ip']}")
print(f"Znalezione kody statusu: {wynik['kody_statusu']}")


