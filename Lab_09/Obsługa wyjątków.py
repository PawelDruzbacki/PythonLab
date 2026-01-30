import datetime # do zaciągnięcia aktualnego roku

plik = open("wiek.txt", "w", encoding="utf-8")
plik.write("25")
plik.close()

def oblicz_rok_urodzenia(sciezka_pliku):
    try:
        plik = open(sciezka_pliku, "r", encoding="utf-8")
        zawartosc = plik.read().strip()

        wiek = int(zawartosc)

        aktualny_rok = datetime.date.today().year # aktualny rok
        rok_urodzenia = aktualny_rok - wiek

        return rok_urodzenia

    except FileNotFoundError:
        return "Błąd: Plik nie istnieje."
    except ValueError:
        return "Błąd: Plik zawiera nieprawidłowe dane (to nie liczba)."
    except Exception as e:
        return f"Wystąpił nieoczekiwany błąd: {e}"



wynik = oblicz_rok_urodzenia("wiek.txt")
print(f"Rok urodzenia obliczony z pliku: {wynik}")
