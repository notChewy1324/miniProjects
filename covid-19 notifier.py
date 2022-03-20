from datetime import datetime
from email import message
from socket import timeout
import time
import requests

covidTime = 5 #Change this number to change the request time: formated in seconds

try: 
    covidAPI = requests.get("https://corona-rest-api.herokuapp.com/Api/usa/")
except:
    print("Failed to create an connection. Check your internet.")
    

covidData = covidAPI.json()['Success']
    
print(f"Refreshes every {covidTime} seconds.")

while True:
    
    covidDate = "COVID-19 Stats on {}".format(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
            
    totalcases = covidData['cases'],
    todaycases = covidData['todayCases'],
    todaydeaths = covidData['todayDeaths'],
    active = covidData["active"]
    
    time.sleep(covidTime)
    print(f"{covidDate} \nTotal Cases Right Now: {totalcases} \nCase Count Today: {todaycases} \nDeaths Today: {todaydeaths} \n\n")