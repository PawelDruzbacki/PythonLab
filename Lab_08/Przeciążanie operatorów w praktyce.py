from functools import total_ordering

class BrakPunktowZyciaError(Exception):
    pass

@total_ordering
class Gracz:
    liczba_graczy = 0
    def __init__(self, imie, hp): #konstruktor przyjmuje parametr self
        print(f"\n---Uruchamiam konstruktor dla {imie}---")
        self.imie = imie
        self._hp = hp #atrybut chroniony
        Gracz.liczba_graczy += 1
        print(f"Do gry dołącza {imie}, jest nas {Gracz.liczba_graczy}!")

    def __eq__(self, other):
        if other.imie == self.imie:
            return True


    def __lt__(self, other):
        if self.hp < other.hp:
            return True


    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, nowa_wartosc):
        if nowa_wartosc < 0:
            self._hp = 0
        else:
            self._hp = 0

    def pokaz_status(self):
        print(f"\nGracz: {self.imie}, HP: {self.hp}")

    def otrzymaj_obrazenia(self, ilosc):
        self.hp -= ilosc
        print(f"!!! {self.imie} otrzymuje {ilosc} obrażeń!")
        if self.hp <= 0:
            print(f"{self.imie} został pokonany!")

    def __str__(self):
        return f"Gracz: {self.imie}, HP: {self.hp}"

    def __repr__(self):
        return f"Gracz: {self.imie}, HP: {self.hp}"

    def przedstaw_sie(self):
        print(f"Jestem {self.imie}, mam {self.hp} hp!")

class Ekwipunek:
    def __init__(self):
        # a. W konstruktorze stwórz prywatny słownik
        self._przedmioty = {}

    def __len__(self):
        # b. Zwracaj liczbę przedmiotów
        return len(self._przedmioty)

    def __setitem__(self, klucz, wartosc):
        # c. Dodawaj parę klucz-wartość (obsługa: ekwipunek["klucz"] = wartosc)
        self._przedmioty[klucz] = wartosc

    def __getitem__(self, klucz):
        # d. Pobieraj wartość (obsługa: zmienna = ekwipunek["klucz"])
        # Warto dodać obsługę błędu, jeśli przedmiotu nie ma
        try:
            return self._przedmioty[klucz]
        except KeyError:
            return "Brak przedmiotu w ekwipunku"

    def __delitem__(self, klucz):
        # e. Usuwaj przedmiot (obsługa: del ekwipunek["klucz"])
        del self._przedmioty[klucz]

    def __repr__(self):
        # f. (Opcjonalnie) Ładna reprezentacja tekstowa obiektu
        return f"Ekwipunek(ilość: {len(self)}, zawartość: {self._przedmioty})"

    class IteratorEkwipunku:
        def __init__(self, lista_przedmiotow):
            # b. Przyjmij listę i zainicjuj licznik
            self._lista = lista_przedmiotow
            self._indeks = 0

        def __iter__(self):
            # d. Metoda __iter__ w iteratorze zwraca samą siebie
            return self

        def __next__(self):
            # c. Zwróć kolejny element lub podnieś StopIteration
            if self._indeks < len(self._lista):
                wynik = self._lista[self._indeks]
                self._indeks += 1
                return wynik
            else:
                # To jest sygnał dla pętli for, że koniec iteracji
                raise StopIteration


class PunktLekki:
    # b. Deklaracja __slots__
    # Mówimy Pythonowi: "Ten obiekt będzie miał TYLKO te dwa atrybuty".
    __slots__ = ('x', 'y')

    # c. Prosty konstruktor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"PunktLekki(x={self.x}, y={self.y})"


class Wojownik(Gracz): #Dziedziczenie po graczu
    def __init__(self, imie, hp, sila): #Modyfikacja konstruktora (dodano siłę)
        super().__init__(imie, hp)
        self.sila = sila

    def atakuj(self):
        if self.hp <= 0:
            raise BrakPunktowZyciaError("Postać nie może atakować!")
        else:
            print("Wojownik atakuje!")

    def __add__(self, other):
        nowy_wojownik = self.imie + other.imie
        return nowy_wojownik


    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"  Moja siła to: {self.sila}")

    def atak(self):
        print(f"CIOS: {self.imie} atakuję z siłą {self.sila}")

    @classmethod
    def stworz_berserkera(cls, imie):
        if not Gracz.sprawdz_poprawnosc_imienia(imie):
            print("Błędne imię dla berserkera!")
            return None
        return cls(imie=imie, hp=80, sila=40)

class Mag(Gracz):
    def __init__(self, imie, hp, mana):
        super().__init__(imie, hp)
        self.mana = mana

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"  Mam {self.mana} many.")

# gracz1 = Gracz(imie="Aragorn", hp=100)
# gracz2 = Gracz(imie="Legolas", hp=80)

#print(gracz1.imie)
#print(gracz2.hp)

#print(gracz1) #działa po dodaniu repr

# gracz1.pokaz_status()

# gracz1.otrzymaj_obrazenia(40)
# print(gracz1)
#
# print(f"\n Po stworzeniu obiektu w grze jest: {Gracz.liczba_graczy}")
#
# print(f"")
#
# print(gracz2)

zwykly_gracz = Gracz (imie="Mieszkaniec wioski", hp=30)
zwykly_gracz1 = Gracz (imie="Mieszkaniec wioski", hp=30)
boromir = Wojownik(imie="Boromir", hp=120, sila=25)
gandalf = Mag(imie="Gandalf", hp=50, mana =70)
#wojownik_0 = Wojownik(imie="Cwel", hp=0, sila=90)

#wojownik_0.atakuj()

druzyna = [boromir, zwykly_gracz, zwykly_gracz1, gandalf]

zwykly_gracz.przedstaw_sie()
boromir.przedstaw_sie()

boromir.atak()
#zwykly_gracz.atak() #nie działa bo nie jest wojownikiem więc nie może atakować
print("----------Prezentacja drużyny----------")
for postac in druzyna:
    postac.przedstaw_sie()
    print("-" * 20)

print("--- Testowanie __eq__ ---")
print(zwykly_gracz == zwykly_gracz1)

print("--- Testowanie __lt__ (sortowanie) ---")
druzyna = [Gracz(imie="Aragorn", hp=100), Gracz(imie="Gimli", hp=150)]
print(f"Drużyna przed sortowaniem: {druzyna}")
posortowana_druzyna = sorted(druzyna)
print(f"Drużyna po sortowaniu: {posortowana_druzyna}")


# --- d. Testowanie ---

g_slaby = Gracz("Goblin", 10)
g_silny = Gracz("Smok", 100)
g_klon = Gracz("Goblin", 999) # To samo imię co g_slaby, ale inne HP

print(f"1. Czy {g_slaby} < {g_silny}? -> {g_slaby < g_silny}")   # Używa twojego __lt__
print(f"2. Czy {g_slaby} == {g_klon}? -> {g_slaby == g_klon}") # Używa twojego __eq__

print("-" * 20)
print("MAGIA @total_ordering (Tych metod nie napisaliśmy, a działają!):")

# Python sam wywnioskował te operatory:
print(f"3. Czy {g_silny} > {g_slaby}? -> {g_silny > g_slaby}")   # Działa! (Odwrotność <)
print(f"4. Czy {g_slaby} <= {g_silny}? -> {g_slaby <= g_silny}") # Działa!
print(f"5. Czy {g_silny} >= {g_slaby}? -> {g_silny >= g_slaby}") # Działa!
print(f"6. Czy {g_slaby} != {g_silny}? -> {g_slaby != g_silny}") # Działa!

# --- g. TESTOWANIE ---

# 1. Stwórz obiekt
plecak = Ekwipunek()

# 2. Dodaj przedmioty (używając __setitem__)
print("--- Dodawanie przedmiotów ---")
plecak["miecz"] = "Stalowy miecz +1"
plecak["mikstura"] = "Mikstura zdrowia"
plecak["tarcza"] = "Drewniana tarcza"
print(plecak)

# 3. Odczytaj przedmioty (używając __getitem__)
print("\n--- Odczyt ---")
item = plecak["miecz"]
print(f"Wyciągnięto: {item}")

# 4. Sprawdź długość (używając __len__)
print(f"\nLiczba przedmiotów w plecaku: {len(plecak)}")

# 5. Usuń przedmiot (używając __delitem__)
print("\n--- Usuwanie tarczy ---")
del plecak["tarcza"]

# 6. Weryfikacja końcowa
print(f"Liczba przedmiotów po usunięciu: {len(plecak)}")
print(plecak)

# --- d. TESTOWANIE ---

# 1. Stwórz instancję
p = PunktLekki(1, 2)
print(f"Utworzono: {p}")

# 2. Sprawdź odczyt
print(f"Odczyt x: {p.x}")

# 3. Próba dodania nowego atrybutu (p.z = 3)
print("\n--- Próba dodania atrybutu 'z' ---")
try:
    p.z = 3
except AttributeError as e:
    print(f"Złapano oczekiwany błąd: {e}")
    print("-> Nie można dodać nowego atrybutu, bo nie ma go w __slots__.")

# 4. Próba odwołania się do __dict__
print("\n--- Próba dostępu do __dict__ ---")
try:
    print(p.__dict__)
except AttributeError as e:
    print(f"Złapano oczekiwany błąd: {e}")
    print("-> Obiekt nie posiada słownika __dict__, co oszczędza pamięć.")

