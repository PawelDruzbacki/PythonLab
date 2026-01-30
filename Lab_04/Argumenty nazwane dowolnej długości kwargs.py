def generuj_super_raport(**szczegoly):
    print("\n--- DYNAMICZNY RAPORT ---")
    if not szczegoly:
        print("Brak danych do zaraportowania")
    else:
        for klucz, wartosc in szczegoly.items():
            print(f"- {klucz.capitalize()}: {wartosc}")
    print("----------------------------")

    generuj_super_raport(status)