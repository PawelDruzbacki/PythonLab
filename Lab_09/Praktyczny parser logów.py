def zlicz_bledy(sciezka_pliku):
    liczba_bledow = 0
    try:
        with open(sciezka_pliku, 'r') as plik:
            for linia in plik:
                try:
                    poziom, wiadomosc = linia.strip().split(":", 1)
                    if poziom == "ERROR":
                        liczba_bledow += 1
                except ValueError:
                    print(f"Niepoprawny Format Linii: {linia.strip()}")
                    continue
    except FileNotFoundError:
        return 0

    return liczba_bledow

if __name__ == '__main__':
    sciezka = 'log.txt'
    wynik = zlicz_bledy(sciezka)
    print(f"Liczba Błędów 'ERROR': {wynik}")