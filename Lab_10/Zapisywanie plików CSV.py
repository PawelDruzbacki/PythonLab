import csv

def zapisz_raport_sprzedazy(sciezka_pliku: str, dane: list):
    if not dane:
        print("Brak danych do zapisania.")
        return

    pola = list(dane[0].keys())

    try:
        with open(sciezka_pliku, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, filenames=pola)
            writer.writeheader()
            writer.writerows(dane)
            print(f"Pomyślnie zapisano raport w pliku: {sciezka_pliku})
        except IOError as e:
            print(f"Błąd zapisu do pliku {sciezka_pliku}: {e}")

    sprzedaz = [
        {'produkt': 'Laptop', 'sprzedana_ilosc': 15, 'przychody': 45000},
        {'produkt': 'Myszka', 'sprzedana_ilosc': 120, 'przychody': 9600},
        {'produkt': 'Klawiatura', 'sprzedana_ilosc': 75, 'przychody': 15000}
    ]