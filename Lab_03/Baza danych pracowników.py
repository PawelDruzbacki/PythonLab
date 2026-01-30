baza_danych = [
    {"imie:": "Anna", "stanowisko": "Specjalista", "pensja": 4500},
    {"imie:": "Piotr", "stanowisko": "Manager", "pensja": 8000},
    {"imie:": "Zofia", "stanowisko": "Specjalista", "pensja": 5200},
    {"imie:": "Krzysztof", "stanowisko": "Stażysta", "pensja": 2500}
]

# Średnia pensja
suma_pensji = sum(p["pensja"] for p in baza_danych)
srednia = suma_pensji / len(baza_danych)
print(f"Średnia pensja: {srednia:.2f} zł")

# Najlepiej opłacany pracownik
najlepiej_oplacany = max(baza_danych, key=lambda p: p["pensja"])
print("Pracownik z najwyższą pensją:")
print(najlepiej_oplacany)

# Specjaliści
print("Specjaliści w firmie:")
for p in baza_danych:
    if p["stanowisko"] == "Specjalista":
        print(p["imie:"])