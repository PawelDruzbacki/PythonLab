liczba_pkt = input("Podaj liczbę punktów zdobytych w kolokwium: ")
wynik = int(liczba_pkt)
if wynik <= 50:
    print("Ocena: 2.0")
elif wynik <= 61:
    print("Ocena: 3.0")
elif wynik <=  71:
    print("Ocena: 4.0")
elif wynik <= 81:
    print("Ocena: 4.5")
else: print("Ocena: 5.0")