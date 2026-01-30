imiona = ["anna", "piotr", "zofia"]

poprawione_imiona = list(map(lambda imie: imie.capitalize(), imiona)) #tworzy listę poprawione_imiona z dużymi literami
print(poprawione_imiona)

oceny = [5,3,2,5,4,2,3,4]

dobre_oceny = list(filter(lambda ocena: ocena >= 4, oceny)) # tworzy listę z ocenami powyżej lub równe 4
print(dobre_oceny)

