import time
import functools  # Ważne dla "przezroczystości" dekoratora


# --- a. Definicja dekoratora mierz_czas ---

def mierz_czas(func):
    """
    Uniwersalny dekorator mierzący czas wykonania dowolnej funkcji.
    """

    # Używamy functools.wraps, aby zachować oryginalną nazwę
    # i docstring dekorowanej funkcji.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # --- b. Zapisz czas startu ---
        start_time = time.time()

        # --- c. Wywołaj funkcję i zapisz wynik ---
        # Przekazujemy wszystkie argumenty pozycyjne (*args)
        # i kluczowe (**kwargs)
        wynik = func(*args, **kwargs)

        # --- d. Zapisz czas końca i oblicz różnicę ---
        end_time = time.time()
        czas_wykonania = end_time - start_time

        # --- e. Wyświetl informację ---
        # func.__name__ pobiera nazwę oryginalnej funkcji
        print(f"--- [CZAS] Funkcja '{func.__name__}' wykonała się w {czas_wykonania:.4f} s")

        # --- f. Zwróć oryginalny wynik ---
        return wynik

    # Dekorator zwraca nową funkcję (wrappera)
    return wrapper


# --- g. Przetestuj dekorator ---

@mierz_czas
def symuluj_pobieranie_danych(url):
    """(Test 1) Symuluje wolne zadanie, np. pobieranie danych z sieci."""
    print(f"Pobieranie danych z {url}...")
    time.sleep(1.2)  # Symulacja opóźnienia
    print("Pobieranie zakończone.")
    return "Oto treść strony"


@mierz_czas
def wykonaj_duze_obliczenia(n):
    """(Test 2) Symuluje zadanie intensywne obliczeniowo (CPU)."""
    print(f"Obliczanie sumy do {n}...")
    # Używamy sum(range(...)) zamiast pętli,
    # aby było to szybkie, ale mierzalne
    suma = sum(range(n))
    return suma


# --- Uruchomienie testów ---
if __name__ == "__main__":
    print("=== Test 1: Funkcja z opóźnieniem (I/O) ===")
    wynik_danych = symuluj_pobieranie_danych(url="https://api.example.com")
    print(f"Zwrócony wynik: {wynik_danych}\n")

    print("=== Test 2: Funkcja z obliczeniami (CPU) ===")
    # Używamy dużej liczby, aby czas był mierzalny
    wynik_obliczen = wykonaj_duze_obliczenia(n=50_000_000)
    print(f"Zwrócony wynik: {wynik_obliczen}\n")

    print("=== Test 3: Sprawdzenie metadanych (dzięki functools.wraps) ===")
    print(f"Nazwa funkcji 2: {wykonaj_duze_obliczenia.__name__}")
    print(f"Docstring funkcji 2: {wykonaj_duze_obliczenia.__doc__}")