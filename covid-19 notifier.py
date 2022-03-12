import datetime
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
            covidDate = "COVID-19 Stats on {}".format(datetime.date.today())
            message = "Total cases: {totalcases}\nToday cases: {todaycases}\nToday deaths: {todaydeaths}\nTotal active: {active}".format(
                        totalcases = data['cases'],
                        todaycases = data['todayCases'],
                        todaydeaths = data['todayDeaths'],
                        active = data["active"]), 
            
            
            time.sleep(covidTime)
            print(message)