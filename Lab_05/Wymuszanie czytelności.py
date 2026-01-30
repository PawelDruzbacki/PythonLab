def wyslij_email(adres, temat, tresc, *, priorytet="normalny"):
    print(f"Wysyłam email do: {adres}")
    print(f"Temat: {temat}")
    print(f"Treść: {tresc}")
    print(f"Priorytet {priorytet}")


wyslij_email(
    adres= "anna.kowalska@example.com",
    temat= "Spotkanie",
    tresc= "Cześć, spotkanie jutro o 10:00",
    priorytet = "wysoki"
)
