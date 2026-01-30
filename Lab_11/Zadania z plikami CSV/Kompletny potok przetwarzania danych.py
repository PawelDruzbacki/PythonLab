import itertools

def czytaj_logi(sciezka):
    with open(sciezka, 'r', encoding='utf-8') as f:
        for linia in f:
            if linia.strip():
                yield linia.strip()

logi = czytaj_logi("logs.txt")

parsed_logi = (
    {
        'ip': linia.split()[1],
        'kod': int(linia.split()[-2]),
        'bajty': int(linia.split()[-1])
    }
    for linia in logi
)

bledy_4xx = (
    log for log in parsed_logi
    if 400 <= log['kod'] < 500
)

posortowane_bledy = sorted(bledy_4xx, key=lambda x: x['ip'])

grupowanie = itertools.groupby(posortowane_bledy, key=lambda x: x['ip'])

wyniki = []
for ip, grupa in grupowanie:
    suma_bajtow = sum(wpis['bajty'] for wpis in grupa)
    wyniki.append((ip, suma_bajtow))

top_3_awarie = sorted(wyniki, key=lambda x: x[1], reverse=True)[:3]

for miejsce, (ip, ruch) in enumerate(top_3_awarie, 1):
    print(f"{miejsce}. IP: {ip} | Ruch błędny: {ruch} bajtów")