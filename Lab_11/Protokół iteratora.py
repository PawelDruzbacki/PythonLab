class WlasnyRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return WlasnyRangeIterator(self)

class WlasnyRangeIterator:
    def __init__(self,wlasny_range_obj):
        self.wlasny_range_obj = wlasny_range_obj
        self.biezaca_wartosc = wlasny_range_obj.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.biezaca_wartosc < self.wlasny_range_obj.stop:
            wynik = self.biezaca_wartosc
            self.biezaca_wartosc += 1
            return wynik
        else:
            raise StopIteration

moj_zakres = WlasnyRange(2, 5)
for liczba in moj_zakres:
    print(liczba)