import math
import json
import requests

def binance(symbol, price_interval):
    url = "https://api.binance.com/api/v3/klines?symbol=" + symbol + "&interval=" + price_interval + "&limit=20"
    url = requests.get(url)
    response = url.text
    response = json.loads(response)

    bollinger_band = {}
    bollinger_liste = []

    bollinger_sayi1 = 0
    for keyx in response:
        ortalama = (float(response[bollinger_sayi1][1]) + float(response[bollinger_sayi1][4]))/2
        bollinger_liste.append(ortalama)
        bollinger_sayi1 = bollinger_sayi1 + 1
    moving_avarage = sum(bollinger_liste)/20
    bollinger_sayi2 = 0
    der_sum = 0
    for keyy in bollinger_liste:
        deneme1 = bollinger_liste[bollinger_sayi2] - moving_avarage
        der_sum = der_sum + (deneme1 * deneme1)
        bollinger_sayi2 = bollinger_sayi2 + 1
    der_sum = der_sum / 20
    root_sqrt = math.sqrt(der_sum)
    UBB = moving_avarage + (2 * root_sqrt)
    MBB = moving_avarage
    LBB = moving_avarage - (2 * root_sqrt)
    bollinger_band["UPPER"] = UBB
    bollinger_band["MIDDLE"] = MBB
    bollinger_band["LOWER"] = LBB
    return bollinger_band
