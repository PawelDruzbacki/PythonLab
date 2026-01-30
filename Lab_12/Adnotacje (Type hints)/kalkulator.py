def dodaj(a: float,b: float) -> float:
    return (a+b)

def dziel(a: int,b: int) -> int:
    if b == 0:
        raise ValueError("Nie można dzielić przez zero!")
    return (a/b)