import requests


api_key = "CX1CI0CXHQRFJXP6"

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}'
r = requests.get(url)
data = r.json()
print(r)
print(data)