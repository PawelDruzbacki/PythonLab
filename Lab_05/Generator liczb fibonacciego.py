def fibonacci(limit):
    a,b =0,1
    for _ in range(limit): # _ oznacza że z tej zmiennej nie korzystamy
        yield a
        a,b = b,a + b

for liczba in fibonacci(100):
    print(liczba)