def monitor_temperatury(prog_alarmowy):
    suma = 0
    licznik = 0
    srednia = 0.0
    try:
        while True:
            odczyt = yield srednia
            if odczyt is None:
                suma = 0
                licznik = 0
                srednia = 0.0
            else:
                suma += odczyt
                licznik += 1
                srednia = suma / licznik
                if srednia > prog_alarmowy:
                    print(f"OSTRZEŻENIE! Średnia {srednia:.2f} przekracza próg {prog_alarmowy}!")
    finally:
        print("Czujnik wyłączony")

czujnik = monitor_temperatury(25.0)

print(f"Inicjalizacja: {next(czujnik)}")
print(f"Średnia: {czujnik.send(20)}")
print(f"Średnia: {czujnik.send(22)}")
print(f"Średnia: {czujnik.send(40)}")
print(f"Reset: {czujnik.send(None)}")
print(f"Średnia: {czujnik.send(10)}")

czujnik.close()
