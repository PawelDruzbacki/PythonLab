import itertools
from Leniwe_wczytywanie_pliku_CSV import czytaj_duzy_csv


strumien_glowny = czytaj_duzy_csv('dane.csv')

iter_analiza1, iter_analiza2 = itertools.tee(strumien_glowny, 2)

osoba_max_dlugosc = max(
    iter_analiza1,
    key=lambda osoba: len(osoba['imie']) + len(osoba['nazwisko'])
)

liczba_osob = 0
laczny_wiek = 0

for osoba in iter_analiza2:
    liczba_osob += 1
    laczny_wiek += osoba['wiek']

print(f"--- WYNIKI ANALIZY ---")
print(f"Osoba o najdłuższym imieniu i nazwisku: {osoba_max_dlugosc['imie']} {osoba_max_dlugosc['nazwisko']}")
print(f"Liczba wszystkich osób: {liczba_osob}")
print(f"Łączny wiek wszystkich osób: {laczny_wiek}")
