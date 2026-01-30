# Plik: main.py
import narzedzia  # Zaimportuj swój nowy moduł
import time  # Potrzebne do time.sleep()


# Udekoruj funkcję za pomocą @narzedzia.mierz_czas
@narzedzia.mierz_czas
def wolna_funkcja():
    """Symuluje funkcję, która długo coś robi."""
    print("Funkcja 'wolna_funkcja' rozpoczyna pracę (śpi 2s)...")
    time.sleep(2)  # Funkcja "coś robi" przez 2 sekundy
    print("...funkcja 'wolna_funkcja' zakończyła pracę.")


# Główna część programu
if __name__ == "__main__":
    print("Program main.py startuje...")

    # Wywołaj wolna_funkcja() i zaobserwuj wynik
    wolna_funkcja()

    print("Program main.py zakończył działanie.")