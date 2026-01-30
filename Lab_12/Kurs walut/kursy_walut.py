import requests


def pobierz_cene_euro():
    url = "http://api.nbp.pl/api/exchangerates/rates/a/eur/?format=json"

    response = requests.get(url)

    data = response.json()

    kurs = data['rates'][0]['mid']

    return kurs