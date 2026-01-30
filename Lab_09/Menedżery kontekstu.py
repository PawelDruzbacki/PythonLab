with open("dziennik.txt", "w", encoding="utf-8") as plik:# tworzy plik jeśli nie istnieje, jeśli istnieje, kasuje zawartosc
    plik.write("Pierwszy wpis.\n")
    plik.write("Wszystko działa.\n")

print("Zapis zakończony sukcesem. Sprawdź plik dziennik.txt w folderze projektu.")

with open("dziennik.txt", "a", encoding="utf-8")as plik:
    plik.write("Kolejna linijka.\n")

with open("dziennik.txt", "r", encoding="utf-8") as plik:
    tresc = plik.read()

    print("----- Początek pliku -----")
    print(tresc)
    print("----- Koniec pliku -----")



