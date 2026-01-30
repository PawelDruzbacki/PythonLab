def rozdziel_imie_nazwisko(imie_i_nazwisko):
    czesci = imie_i_nazwisko.split()
    imie = czesci[0]
    nazwisko = czesci[1]
    return imie, nazwisko

pelne_imie = "Jan Kowalski"

imie_osoby, nazwisko_osoby = rozdziel_imie_nazwisko(pelne_imie)

print(f"Imię: {imie_osoby}")
print(f"Nazwisko: {nazwisko_osoby}")
