import requests


api_key = "CX1CI0CXHQRFJXP6"

url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey={api_key}'
r = requests.get(url)
data = r.json()
print(r)
print(data)
