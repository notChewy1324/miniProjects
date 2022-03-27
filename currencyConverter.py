import requests

class Currency_converter:
    
    rates = {}
    def __init__(self, url):
      data = requests.get(url).json()
      
      self.rates = data["rates"]