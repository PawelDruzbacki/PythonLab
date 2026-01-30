tagi = input("Podaj tagi oddzielone przecinkami: ")
tagi_lista = tagi.split(',')
czyste_tagi = [tag.strip() for tag in tagi_lista]
unikatowe_tagi = set(czyste_tagi)

print(f"\nLiczba wszystkich podanych tagów: {len(czyste_tagi)}")
print(f"Liczba unikalnych tagów: {len(unikatowe_tagi)}")

posortowane_unikatowe_tagi = sorted(list(unikatowe_tagi))
print("\nUnikalne tagi (alfabetycznie): ")
for tag in posortowane_unikatowe_tagi:
    print(f"- {tag}")
