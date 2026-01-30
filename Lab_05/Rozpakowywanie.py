def funkcja(a,b,c):
    print(f"a={a}, b={b}, c={c}")

lista_arg = [10, 20, 30]
slownik_arg = {"a": 1, "b": 2, "c": 3}

funkcja(*lista_arg)
funkcja(**slownik_arg)
