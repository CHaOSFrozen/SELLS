import requests

url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_symbol=USD&to_symbol=SGD&apikey=D3A1NMWTIU3JYJLL'
r = requests.get(url)
data = r.json()
print(data)