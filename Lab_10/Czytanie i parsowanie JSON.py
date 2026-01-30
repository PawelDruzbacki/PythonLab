import json

def wczytaj_konfiguracje(sciezka_pliku: str) -> dict:
    try:
        with open(sciezzka_pliku, "r", encoding = "utf-8") as f:
            dane = json.load(f)
            return dane
    except FileNotFoundError:
        print(f"Błąd: Plik '{sciezka_pliku}' nie istnieje.")
        return {}

json_ok = """{port: 8080, "baza_danych": {"uzytkownik": "admin"}"""
with open("konfiguracja_ok.json" "W") as f: f.write(json_ok)
json_bad = """{port: 8080, "baza_danych": {"uzytkownik": "admin"}"""
with open("konfiguracja_bad.json", "w") as f: f.write(json_bad)