kontakty = {}

while True:
    print("\nMENU KONTAKTÓW")
    print("1. Dodaj kontakt")
    print("2. Wyświetl kontakt")
    print("3. Usuń kontakt")
    print("4. Wyświetl wszystko")
    print("5. Zakończ")

    wybor = input("Wybierz opcję (1-5): ")

    if wybor == "1":
        nazwa = input("Podaj nazwę kontaktu: ")
        numer = input("Podaj numer telefonu: ")
        kontakty[nazwa] = numer
        print(f"Dodano kontakt: {nazwa} -> {numer}")

    elif wybor == "2":
        nazwa = input("Podaj nazwę kontaktu do wyświetlenia: ")
        if nazwa in kontakty:
            print(f"Numer kontaktu {nazwa}: {kontakty[nazwa]}")
        else:
            print("Kontakt nie istnieje.")

    elif wybor == "3":
        nazwa = input("Podaj nazwę kontaktu do usunięcia: ")
        if nazwa in kontakty:
            del kontakty[nazwa]
            print(f"Usunięto kontakt: {nazwa}")
        else:
            print("Kontakt nie istnieje.")

    elif wybor == "4":
        for nazwa, numer in kontakty.items():
            print(f"---MOJE KONTAKTY---\nNazwa: {nazwa}\nNumer: {numer}\n---KONIEC LISTY---")

    elif wybor == "5":
        print("Zakończono program.")
        break

    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")