# a. Zaimportuj moduł pickle
import pickle


# b. Stwórz prostą klasę StanGry
class StanGry:
    def __init__(self, nazwa_gracza, punkty, ekwipunek):
        self.nazwa_gracza = nazwa_gracza
        self.punkty = punkty
        self.ekwipunek = ekwipunek

    def __repr__(self):
        return (f"StanGry(Gracz='{self.nazwa_gracza}', "
                f"Punkty={self.punkty}, "
                f"Ekwipunek={self.ekwipunek})")


# --- ZAPIS (SERIALIZACJA) ---

# c. Stwórz instancję klasy z danymi
moj_save = StanGry("Wiedzmin", 5200, ["Miecz Srebrny", "Eliksir"])
print(f"1. Obiekt w pamięci (przed zapisem): {moj_save}")

# d. Otwórz plik w trybie binarnym do zapisu ('wb' - write binary)
# Pliki pickle to ciągi bajtów, nie tekst, dlatego 'b' jest konieczne!
filename = "stan_gry.pkl"

with open(filename, "wb") as f:
    # e. Zapisz obiekt do pliku (proces "piklowania")
    pickle.dump(moj_save, f)
    print(f"2. Zapisano stan gry do pliku '{filename}'.")

print("-" * 40)

# --- ODCZYT (DESERIALIZACJA) ---

# f. Otwórz plik w trybie binarnym do odczytu ('rb' - read binary)
try:
    with open(filename, "rb") as f:
        # g. Wczytaj obiekt z pliku ("odpieklowywanie")
        wczytany_stan = pickle.load(f)

    print(f"3. Wczytano obiekt z pliku.")

    # h. Wyświetl wczytany obiekt i sprawdź jego typ
    print(f"4. Zawartość wczytanego obiektu: {wczytany_stan}")
    print(f"5. Typ obiektu: {type(wczytany_stan)}")

    # Sprawdzenie czy to faktycznie 'żywy' obiekt, czy tylko tekst
    print(f"6. Dostęp do atrybutu (punkty): {wczytany_stan.punkty}")

except FileNotFoundError:
    print("Nie znaleziono pliku zapisu!")
except Exception as e:
    print(f"Wystąpił błąd podczas wczytywania: {e}")