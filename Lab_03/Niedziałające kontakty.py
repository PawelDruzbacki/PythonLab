kontakty = {
    "Anna": "213431356",
    "Piotr": "832456123"
}
while True:
    wybor = input("Wybierz, co chcesz zrobić: ")
    if wybor == "dodaj kontakt":
        nazwa = input("Podaj nazwę: ")
        numer = input("Podaj numer: ")
        print(kontakty)
    elif wybor == "wyświetl kontakt":
        nazwa1 = input("Podaj nazwę: ")
        print(kontakty)
    elif wybor == "usuń kontakt":
        nazwa = input("Podaj nazwę do usunięcia: ")
        del kontakty[nazwa]
    elif wybor == "wyświetl wszystko":
        for nazwa, numer in kontakty.items():
            print(f"---MOJE KONTAKTY---\nNazwa: {nazwa}\nNumer: {numer}\n---KONIEC LISTY---")
    else:
        break
