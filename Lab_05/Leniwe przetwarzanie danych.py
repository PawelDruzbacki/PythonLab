def licz_do_trzech():
    yield "1"
    yield "2"
    yield "3"

generator = licz_do_trzech()

print("zaczynam iterować po generatorze")
for liczby in generator:
    print(liczby)