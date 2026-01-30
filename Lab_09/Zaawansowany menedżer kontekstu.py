class IgnorujBledy:
    def __init__(self, bledy_do_ignorowania):
        if not isinstance(bledy_do_ignorowania, tuple):
            bledy_do_ignorowania = (bledy_do_ignorowania,)
        self.bledy_do_ignorowania = bledy_do_ignorowania

    def __enter__(self):
        pass

    def __exit__(self, typ_bledu, wart_bledu, traceback):
        if typ_bledu is None:
            return False

        for typ_ignorowany in self.bledy_do_ignorowania:
            if issubclass(typ_bledu, typ_ignorowany):
                return True

        return False


ignorer = IgnorujBledy((ValueError, TypeError))

with ignorer:
    liczba = int("abc")

try:
    with ignorer:
        wynik = 1 / 0
except ZeroDivisionError:
    pass

# Poniższe linie służą weryfikacji, że błędy zostały stłumione lub rzucone
print("Sukces: ValueError został zignorowany, program kontynuował działanie.")

try:
    with ignorer:
        print("Sprawdzanie, czy błąd ZeroDivisionError zostanie rzucony...")
        wynik = 1 / 0
except ZeroDivisionError as e:
    print(f"Sukces: ZeroDivisionError ({e}) został normalnie rzucony i złapany.")