x = "Jestem GLOBALNY"

def funkcja_zewnetrzna():
    x = "Jestem OTACZAJĄCY (enclosing)"

    def funkcja_wewnetrzna():
        x = "Jestem LOKALNY"
        print(x) #przykrywa zewnętrzną i globalną


    funkcja_wewnetrzna()
    print(x) #przykrywa globalną

funkcja_zewnetrzna()
print(x)