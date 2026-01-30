def moj_dekorator(funkcja_do_udekorowania):
    def wrapper():
        print("Coś przed wywołaniem funkcji...")
        funkcja_do_udekorowania()
        print("Coś po wywołaniu funkcji...")

    return wrapper

@moj_dekorator
def powiedz_czesc():
    print("Cześć!")

powiedz_czesc()