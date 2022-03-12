from datetime import datetime
from email import message
from socket import timeout
import time
import requests

covidData = None
covidTime = 5 #Change this number to change the request time: formated in seconds
try: 
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/usa/")
except:
    print("Failed to create an connection. Check your internet.")
    

if (covidData != None):
    data = covidData.json()['Success']
    
    print(f"Refreshes every {covidTime} seconds.")
    
    while True:
        
            covidDate = "COVID-19 Stats on {}".format(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
            
            totalcases = data['cases'],
            todaycases = data['todayCases'],
            todaydeaths = data['todayDeaths'],
            active = data["active"]
    
            time.sleep(covidTime)
            print(f"{covidDate} \nTotal Cases Right Now: {totalcases} \n\n")