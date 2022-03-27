import requests

class Currency_converter:
    
    rates = {}
    def __init__(self, url):
      data = requests.get(url).json()
      
      self.rates = data["rates"]
      
    def convert(self, fromCurrency, toCurrency, amount):
        initialAmount = amount
        if fromCurrency != 'EUR':
            amount = amount / self.rates[fromCurrency]
            
        amount = round(amount * self.rates[toCurrency], 2)
        print('{} {} = {} {}'.format(initialAmount, fromCurrency, toCurrency))