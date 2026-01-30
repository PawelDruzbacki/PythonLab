import urllib.request
import json
import threading
import time


def pobierz_kurs(waluta: str):
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/?format=json"
    print(f"[{waluta}] Rozpoczynam pobieranie...")

    try:
        with urllib.request.urlopen(url) as response:
            data_json = json.loads(response.read().decode('utf-8'))
            kurs = data_json['rates'][0]['mid']
            print(f"[{waluta}] Kurs: {kurs}")
    except Exception as e:
        print(f"[{waluta}] Błąd: {e}")

    print(f"[{waluta}] Zakończono.")


waluty = ['EUR', 'USD', 'CHF', 'GBP', 'JPY']

print("\n--- START: Wersja Sekwencyjna ---")
start_seq = time.perf_counter()

for waluta in waluty:
    pobierz_kurs(waluta)

end_seq = time.perf_counter()
czas_seq = end_seq - start_seq
print(f"Czas całkowity (sekwencyjnie): {czas_seq:.4f} s")

print("\n--- START: Wersja Wielowątkowa ---")
start_threads = time.perf_counter()

watki = []

for waluta in waluty:
    watek = threading.Thread(target=pobierz_kurs, args=(waluta,))
    watki.append(watek)
    watek.start()

for watek in watki:
    watek.join()

end_threads = time.perf_counter()
czas_threads = end_threads - start_threads

print(f"Czas całkowity (wielowątkowo): {czas_threads:.4f} s")

if czas_threads > 0:
    przyspieszenie = czas_seq / czas_threads
    print(f"\n--- WYNIK ---")
    print(f"Wielowątkowość była szybsza o: {przyspieszenie:.2f}x")