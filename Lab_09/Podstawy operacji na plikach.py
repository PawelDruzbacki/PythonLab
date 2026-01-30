plik = open("dziennik.txt", "w", encoding="utf-8") # tworzy plik jeśli nie istnieje, jeśli istnieje, kasuje zawartosc

plik.write("Pierwszy wpis.\n")
plik.write("Wszystko działa.\n")
plik.close()

print("Zapis zakończony sukcesem. Sprawdź plik dziennik.txt w folderze projektu.")

plik_dopisywanie = open("dziennik.txt", "a", encoding="utf-8")

plik_dopisywanie.write("Kolejna linijka.\n")

plik_dopisywanie.close()

plik_odczyt = open("dziennik.txt", "r", encoding="utf-8")

tresc = plik_odczyt.read()

print("----- Początek pliku -----")
print(tresc)
print("----- Koniec pliku -----")

plik_odczyt.close()
