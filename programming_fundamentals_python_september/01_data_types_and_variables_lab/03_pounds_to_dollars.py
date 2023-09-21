# pounds = int(input())
# dollars = pounds * 1.31
# print(f'{dollars:.3f}')
import requests


def convert_gbp_to_bgn(amount):
    response = requests.get('https://api.exchangerate-api.com/v4/latest/GBP')  # api call to get values from the web
    print(response.json())  # we can check the response of what the api returns
    exchange_rates = response.json()['rates']  # we take all exchange rates
    usd_rate = exchange_rates['USD']  # we take USD exchange rate
    usd_amount = amount * usd_rate

    return usd_amount


pounds = int(input('Enter and amount of pounds: '))
us_dollars = convert_gbp_to_bgn(pounds)
print(f'{us_dollars:.2f}')
