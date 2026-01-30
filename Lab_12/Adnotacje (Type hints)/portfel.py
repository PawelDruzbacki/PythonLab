class NiewystarczajaceSrodki(Exception):
    pass

class Portfel:
    def __init__(self, saldo_poczatkowe: int =0) -> None:
        self.saldo = saldo_poczatkowe

    def wplac(self, kwota: int) -> None:
        self.saldo += kwota

    def wydaj(self, kwota: int) -> None:
        if kwota > self.saldo:
            raise NiewystarczajaceSrodki("Nie masz wystarczająco dużo pieniędzy!")
        self.saldo -= kwota
