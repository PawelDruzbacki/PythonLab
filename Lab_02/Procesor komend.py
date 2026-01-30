lkwhile True:
    komenda = input("Podaj swoją komendę: ")

    if komenda == "koniec":
        break
    elif komenda.startswith("#"):
        print("To jest komentarz. Pomijam")
        continue
        print("Wykouję Komendę: {komenda}")
print("program zakończony")