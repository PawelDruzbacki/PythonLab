liczby = [1,2,3,4]

kwadrat = list(map(lambda x: x ** 2, liczby))
print(kwadrat) # zwraca spotęgowane liczby z listy

parzyste = list(filter(lambda x: x % 2 == 0, liczby))
print(parzyste)# zwraca tylko liczby parzyste