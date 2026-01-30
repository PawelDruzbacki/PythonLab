slowo = input("Podaj dowolne słowo: ")
licznik_samoglosek = 0
SAMOGLOSKI = "aeioy"
for litera in slowo.lower():
    if litera in SAMOGLOSKI:
        licznik_samoglosek += 1

print(f"W słowie '{slowo}' jest {licznik_samoglosek} samogłosek.")


