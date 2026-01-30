import math
def oblicz_pole(figura,a=0,b=0,r=0):
    """
        Funkcja oblicza pole wybranej przez użytkownika figury.

        Args: Funkcja przyjmuje argument figura, bok a, bok b oraz promień r.

        Returns: Funkcja zwraca obliczone pole danej figury z podanymi wartościami.
        """
    figura = figura.lower()

    if figura == "prostokąt":
        return a*b
    elif figura == "koło":
        return math.pi * (r**2)
    else:
        return None

help(oblicz_pole)

pole_prostokata = oblicz_pole(figura="prostokąt", a=5, b=10)
if pole_prostokata is not None:
    print(f"Pole prostokąta wynosi: {pole_prostokata}")

pole_kola = oblicz_pole(figura="koło", r=7)
if pole_kola is not None:
    print(f"Pole koła wynosi: {pole_kola}")

wynik_nieznany = oblicz_pole(figura="trójkąt", a=5, b=10)
if wynik_nieznany is None:
    print("Nie potrafię obliczyć pola dla nieznanej figury")



