def generuj_raport(imie, stanowisko="Pracownik", miasto="Nieznane"):
    raport ="Raport użytkownika:\n - Imię: {imie}\n - Stanowisko: {stanowisko}\n - Miasto: {miasto}")
    return raport

raport_anny = generuj_raport("Anna")

raport_piotra = generuj_raport("Piotr", miasto="Gdańsk")

print(raport_anny)
print("\n")
print(raport_piotra)
