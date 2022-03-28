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
        
if __name__ == "__main__":
  
    url = str.__add__('http://data.fixer.io/api/latest?access_key=', YOUR_ACCESS_KEY)  
    c = Currency_convertor(url)
    from_country = input("From Country: ")
    to_country = input("TO Country: ")
    amount = int(input("Amount: "))
  
    c.convert(from_country, to_country, amount)