import requests
import time

wikiRefresh = 15 #controls refresh time in seconds

def wikiInfo():
    
    try:
        pageData = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary")
    except:
        print("Failed to create an connection. Check your internet.")
    
    data = pageData.json()
    wikiTitle = data["title"]
    wikiID = data["pageid"]
    wikiDescription = data["description"]
    wikiBio = data["extract"]
    
    print(f"\n\nWiki Title: {wikiTitle} \nWiki Description: {wikiDescription} \nWiki Bio: {wikiBio} \nWiki Page ID: {wikiID} \n\n")
    
print(f"This program refreshes a new wiki page every {wikiRefresh} seconds.")
time.sleep(3)

while True:
    
    wikiInfo()
    time.sleep(wikiRefresh)
    