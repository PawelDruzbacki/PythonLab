class WlasnyRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        biezaca_wartosc = self.start
        while biezaca_wartosc < self.stop:
            yield biezaca_wartosc
            biezaca_wartosc += 1

moj_zakres = WlasnyRange(2, 5)
for liczba in moj_zakres:
 print(liczba)