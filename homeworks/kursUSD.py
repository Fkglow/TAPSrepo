import requests
import datetime
import time

endpoint = 'http://api.nbp.pl/api/exchangerates/rates/a/USD/'

def getRate():
    try:
        r = requests.get(endpoint)
        data = r.json()
        rate = data['rates'][0]['mid']
        print('Kurs USD: ', rate)
    except requests.exceptions.HTTPError:
        print('Błąd pozyskania danych')

def timeDuration():
    start_time = datetime.datetime.now()
    getRate()
    duration = datetime.datetime.now() - start_time

    date = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
    print('Data i godzina: ', date)
    print('Czas wykonania zapytania: ', duration.microseconds/1000, 'ms')

while True:
    timeDuration()
    print('-----------------------------------------------')
    time.sleep(20)

