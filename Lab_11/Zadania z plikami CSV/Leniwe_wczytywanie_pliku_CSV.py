import csv

def czytaj_duzy_csv(sciezka_pliku: str):
    with open(sciezka_pliku, mode='r', encoding='utf-8') as plik:
        DictReader = csv.DictReader(plik, skipinitialspace=True)

        for wiersz in DictReader:
            wiersz["wiek"] = int(wiersz["wiek"].strip())
            yield wiersz

generator_danych = czytaj_duzy_csv('dane.csv')

for osoba in generator_danych:
    if osoba["wiek"] > 40:
        print(f"Znaleziono: {osoba["imie"]} {osoba["nazwisko"]} (Wiek: {osoba["wiek"]})")