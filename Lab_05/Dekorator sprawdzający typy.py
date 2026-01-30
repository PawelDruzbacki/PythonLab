import functools

def sprawdz_typy(typ_argumentu):
    def dekorator(funkcja):
        @functools.wraps(funkcja)
        def wrapper(*args, **kwargs):
            for arg in args:
                if not isinstance(arg, typ_argumentu):
                    print(f"Błąd: argument {arg} nie jest typu {typ_argumentu.__name__}")
                    return None
                return funkcja(*args, **kwargs)
            return wrapper
        return dekorator

@sprawdz_typy(int)
def dodaj(a,b):
    return a+b

#test
print(dodaj(2,3)) #zwraca 5
print(dodaj(2,'3')) #zwraca none, błąd