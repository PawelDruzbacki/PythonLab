def zsumuj_wszystko(*liczby):
    print(f"Otrzymano argumenty w krotce: {liczby}")
    return sum(liczby)

wynik1 = zsumuj_wszystko(1, 2, 3)
print(f"Wynik 1: {wynik1}")

wynik2 = zsumuj_wszystko(10, 20, 30, 40)
print(f"Wynik 2: {wynik2}")

wynik3 = zsumuj_wszystko()
print(f"Wynik 3: {wynik3}")