class BrakPunktowZyciaError(Exception):
    pass


class Gracz:
    liczba_graczy = 0

    def __init__(self, imie, hp):
        print(f"\n---Uruchamiam konstruktor dla {imie}---")
        self.imie = imie
        self._hp = hp
        Gracz.liczba_graczy += 1
        print(f"Do gry dołącza {imie}, jest nas {Gracz.liczba_graczy}!")

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, nowa_wartosc):
        if nowa_wartosc < 0:
            self._hp = 0
        else:
            self._hp = nowa_wartosc  # NAPRAWIONE: Tutaj musi być przypisanie nowej wartości, a nie 0!

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

    @staticmethod
    def sprawdz_poprawnosc_imienia(imie):
        return isinstance(imie, str) and len(imie) > 0


class Ekwipunek:
    def __init__(self):
        self.przedmioty = []

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)
        print(f"Dodano {przedmiot} do ekwipunku!")

    def pokaz_przedmioty(self):
        if not self.przedmioty:
            print("Ekwipunek jest pusty.")
        else:
            print("Zawartość ekwipunku: ")
            for p in self.przedmioty:
                print(f"  - {p}")


class Wojownik(Gracz):
    def __init__(self, imie, hp, sila):
        super().__init__(imie, hp)
        self.sila = sila

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


# --- TESTY ---

zwykly_gracz = Gracz(imie="Mieszkaniec wioski", hp=30)
boromir = Wojownik(imie="Boromir", hp=120, sila=25)
gandalf = Mag(imie="Gandalf", hp=50, mana=70)

druzyna = [boromir, zwykly_gracz, gandalf]

print("\n--- Akcje ---")
zwykly_gracz.przedstaw_sie()
boromir.przedstaw_sie()
boromir.atak()

print("\n----------Prezentacja drużyny----------")
for postac in druzyna:
    postac.przedstaw_sie()
    print("-" * 20)