from Leniwe_wczytywanie_pliku_CSV import czytaj_duzy_csv

strumien_danych = czytaj_duzy_csv("dane.csv")

osoby_po_30 = (
    osoba for osoba in strumien_danych
    if osoba["wiek"] > 30
)

opisy = (
    f"{osoba["imie"]} {osoba["nazwisko"]}".upper()
    for osoba in osoby_po_30
)

for opis in opisy:
    print(f"Wynik potoku: {opis}")

print("\n--- Koniec Potoku ---")