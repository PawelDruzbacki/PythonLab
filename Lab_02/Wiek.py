wiek_str = input("Podaj swój wiek: ")
wiek = int(wiek_str)
if wiek <= 13:
    print("Jesteś dzieckiem.")
elif wiek <= 18:
    print("Jesteś nastolatkiem.")
elif wiek <= 64 :
    print("Jesteś dorosły.")
else:
    print("Jesteś seniorem.")

print("Dziękuję za skorzystanie z programu")
#pierwsza część