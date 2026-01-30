class NiewystarczajaceSrodki(Exception):
    pass

class Portfel:
    def __init__(self, saldo_poczatkowe=0):
        self.saldo = saldo_poczatkowe

    def wplac(self, kwota):
        self.saldo += kwota

    def wydaj(self, kwota):
        if kwota > self.saldo:
            raise NiewystarczajaceSrodki("Nie masz wystarczająco dużo pieniędzy!")
        self.saldo -= kwota
