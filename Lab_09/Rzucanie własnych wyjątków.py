class NiepoprawnaIloscProduktowError(ValueError):
    pass

def dodaj_do_koszyka(produkt, ilosc):
    if ilosc <= 0:
        raise NiepoprawnaIloscProduktowError("Ilość produktów musi być dodatnia!")
    print(f"Sukces! Dodano {ilosc}x {produkt} do koszyka.")


dodaj_do_koszyka("Mleko", 3)

try:
    dodaj_do_koszyka("Frytki", -1)
except NiepoprawnaIloscProduktowError as e:
    print(f"Uuups! Wystąpił błąd logiczny: {e}")




