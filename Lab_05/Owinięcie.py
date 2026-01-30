def loguj(funkcja):
    def wrapper():
        print("Start funkcji...")
        funkcja()
        print("Koniec funkcji.")
    return wrapper

@loguj
def status_logowania():
    print("Pomyślnie zalogowano!")

status_logowania()