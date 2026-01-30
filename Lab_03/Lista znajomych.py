znajomi_anny = ["Piotr", "Zofia", "Marek", "Anna"]
znajomi_piotra = ["Anna", "Marek", "Krzysztof", "Ewa"]

#krok 1: konwersja list na zbiory
zbior_znajomych_anny = set(znajomi_anny)
zbior_znajomych_piotra = set(znajomi_piotra)

#krok 2: Znalezienie częsci wspólnej (przecięcia)
wspolni_znajomi = zbior_znajomych_anny & zbior_znajomych_piotra
wspolni_znajomi1 = zbior_znajomych_anny.intersection(zbior_znajomych_piotra)

print(wspolni_znajomi)
