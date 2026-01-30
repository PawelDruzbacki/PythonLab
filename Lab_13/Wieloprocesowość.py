import time
import multiprocessing

def ciezka_praca(n: int) -> int:
    return sum(range(n))

if __name__ == "__main__":
    dane = [50_000_000 + i for i in range(8)]

    start_seq = time.perf_counter()
    wyniki_seq = [ciezka_praca(x) for x in dane]
    end_seq = time.perf_counter()
    czas_seq = end_seq - start_seq

    print(f"Czas sekwencyjny: {czas_seq:.4f} s")

    start_multi = time.perf_counter()
    with multiprocessing.Pool() as pula:
        wyniki_multi = pula.map(ciezka_praca, dane)
    end_multi = time.perf_counter()
    czas_multi = end_multi - start_multi

    print(f"Czas wieloprocesowy: {czas_multi:.4f} s")

    if czas_multi > 0:
        przyspieszenie = czas_seq / czas_multi
        print(f"Przyspieszenie: {przyspieszenie:.2f}x")