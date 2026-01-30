zakupy = []
while True:
    produkt = input("Podaj produkt (lub 'koniec'): ")
    if produkt.lower() == "koniec":
        break
    zakupy.append(produkt)

zakupy.sort()
print(zakupy)

for index, produkt in enumerate(zakupy, start=1):
    print(index, produkt.capitalize())
