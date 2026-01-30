import csv

def wczytaj_pracownikow(sciezka_pliku: str) -> list:
    poprawni_pracownicy = []

    try:
        with open(sciezka_pliku, mode='r', encoding='utf-8', newline='') as plik:

            # DictReader automatycznie używa pierwszego wiersza jako kluczy słownika
            czytnik = csv.DictReader(plik)

            # e. Iteracja po wierszach
            for numer_linii, wiersz in enumerate(czytnik, start=2):  # start=2 bo linia 1 to nagłówek

                # Wewnętrzny blok try...except (walidacja danych w wierszu)
                try:
                    # Próba konwersji pensji na int
                    # wiersz to np.: {'imie': 'Jan', 'stanowisko': 'Kierownik', 'pensja': '8500'}
                    pensja_napis = wiersz['pensja']
                    wiersz['pensja'] = int(pensja_napis)

                    # Jeśli się uda, dodajemy do listy
                    poprawni_pracownicy.append(wiersz)

                except ValueError:
                    # Jeśli konwersja się nie uda (np. 'nieznana')
                    print(
                        f"[OSTRZEŻENIE] Linia {numer_linii}: Niepoprawna pensja ('{wiersz['pensja']}'). Pominięto pracownika: {wiersz['imie']}.")
                    continue  # Przechodzimy do kolejnego pracownika

    except FileNotFoundError:
        print(f"[BŁĄD KRYTYCZNY] Plik '{sciezka_pliku}' nie istnieje!")
        return []

    # f. Zwrócenie listy
    return poprawni_pracownicy


# --- TESTOWANIE ---

print("--- Test 1: Poprawny plik (z jednym błędem w danych) ---")
lista = wczytaj_pracownikow("pracownicy.csv")

print(f"\nWczytano {len(lista)} pracowników:")
for p in lista:
    print(p)

print("\n--- Test 2: Nieistniejący plik ---")
pusta_lista = wczytaj_pracownikow("nieistniejacy_plik.csv")