wizytowka = {
    "imie": "Paweł",
    "nazwisko": "Drużbacki",
    "stanowisko": "student"
}
print(f"Imię i nazwisko: {wizytowka['imie']} {wizytowka['nazwisko']}\nStanowisko: {wizytowka['stanowisko']}")

wizytowka["miasto"] = "Kraków"
print(f"Po dodaniu miasta: {wizytowka}")
wizytowka["stanowisko"] = "pracownik"
print(f"Po zmianie stanowiska {wizytowka}")
del wizytowka["imie"]
print(f"Po usunięciu imienia{wizytowka}")