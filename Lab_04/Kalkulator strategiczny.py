def dodaj(a,b):
    wynik_dodawania = a+b
    return wynik_dodawania

def odejmij(a,b):
    wynik_odejmowania = a-b
    return wynik_odejmowania

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
funkcja_operacji = input("Podaj funkcję operacji: ").lower()

def wykonaj_operacje(a,b,funkcja_operacji):
    if funkcja_operacji == "dodawanie":
        wynik_dodawania = dodaj(a,b)
        return wynik_dodawania
    elif funkcja_operacji == "odejmowanie":
        wynik_odejmowania = odejmij(a,b)
        return wynik_odejmowania
    else:
        return None

print(wykonaj_operacje(a,b,funkcja_operacji))
