def prosty_generator():
    print("Zaraz zwrócę pierwszą wartość...")
    yield "pierwsza wartość" # wywołuje i pauzuje, aby dalej wykonać
    print("zaraz zwrócę drugą wartość...")
    yield "druga wartość"

gen = prosty_generator() #tworzenie generatora

print(next(gen))
print("coś pomiędzy")
print(next(gen))