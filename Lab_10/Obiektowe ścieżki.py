from pathlib import Path
from datetime import date


folder = Path("raporty_dzienne")

sciezka_do_pliku = folder / str(date.today()) / "raport.txt"

sciezka_do_pliku.parent.mkdir(parents=True, exist_ok=True)

tresc_raportu = f"To jest automatycznie wygenerowany raport z dnia {date.today()}."
sciezka_do_pliku.write_text(tresc_raportu, encoding = "utf-8")
print(f"Zapisano raport w: {sciezka_do_pliku}")

wczytana_tresc = sciezka_do_pliku.read_text(encoding="utf-8")
print(f"Weryfikacja odczytu: '{wczytana_tresc}'")


# g. Wyświetl atrybuty obiektu Path
print("\n--- Atrybuty obiektu Path ---")
print(f"Pełna, absolutna ścieżka (.resolve()): {sciezka_do_pliku.resolve()}")
print(f"Nazwa pliku (.name): {sciezka_do_pliku.name}")
print(f"Folder nadrzędny (.parent): {sciezka_do_pliku.parent}")

