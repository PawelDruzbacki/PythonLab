import time

class MiernikCzasu:

    def __enter__(self):
        print("Rozpoczynam pomiar.")
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.koniec = time.perf_counter()

        self.czas_trwania = self.koniec - self.start
        print(f"Czas trwania to {self.czas_trwania}")

with MiernikCzasu():
    suma = sum(n for n in range(10_000_000))