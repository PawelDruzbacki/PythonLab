wiek_str1 = input("Podaj swój wiek: ") #najpierw deklaruje zmienną jako string
wiek1 = int(wiek_str1)                 #więc potem treba ją zamienić na int, ponieważ jest to liczba
wzrost_str = input("Podaj swój wzrost (w cm): ")
wzrost = int(wzrost_str)

if wiek1 < 18:
    zgoda = input("Czy masz zgodę Twojego opiekuna? Odpowiedz tak/nie: ") #Zadaje pytanie, jeżeli nie jest dorosły
else: zgoda = "tak"

if wzrost >= 140 and (wiek1 >= 18 or zgoda.lower() == "tak"):
    print("Możesz wejść!")
else: print("Nie spełniasz warunków!")





