import os

class BezpiecznyZapis:

    def __init__(self, sciezka):
        self.sciezka = sciezka
        self.sciezka_tymczasowa = sciezka_docelowa + ".tmp"
        self.plik_uchwyt = None

    def __exit__(self, typ_bledu, wart_bledu, traceback):
        if self.plik_uchwyt:
            self.plik_uchwyt_close()

        if typ_bledu is None:
            os.rename(self.sciezka_tymczasowa, self.sciezka)
            print("Zapis zakończony sukcesem")
        else:
            if os.path.exists(self.sciezka_tymczasowa):
                os.remove(self.sciezka_tymczasowa)
                print("Wystąpił błąd")
        :   return False