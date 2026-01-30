import itertools
from Leniwe_wczytywanie_pliku_CSV import czytaj_duzy_csv

klucz_sortowania = lambda osoba: osoba['nazwisko'][0]

posortowani_ludzie = sorted(czytaj_duzy_csv('dane.csv'), key=klucz_sortowania)

grupowanie = itertools.groupby(posortowani_ludzie, key=klucz_sortowania)

for litera, grupa_iterator in grupowanie:
    osoby_w_grupie = list(grupa_iterator)
    wieki = [osoba['wiek'] for osoba in osoby_w_grupie]

    if wieki:
        srednia = sum(wieki) / len(wieki)
        print(f"Litera '{litera}': Średni wiek = {srednia:.1f} lat (Liczba osób: {len(wieki)})")

