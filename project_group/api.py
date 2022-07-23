import requests


api_key = "CX1CI0CXHQRFJXP6"

# Group Assingment According to PFP Project Breif 
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}'
r = requests.get(url)
data = r.json()
print(r)
print(data)



# Group Assingment According To Integrated Breif (Need to Find Mean from Weekly)
url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey={api_key}'
r = requests.get(url)
data = r.json()
print(r)
print(data)
