import requests
import time

wikiRefresh = 30 #controls refresh time in seconds

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
    
    print(f"\n\nWiki Page ID: {wikiID} \nWiki Description: {wikiDescription} \nWiki Bio: {wikiBio} \nWiki Title: {wikiTitle}\n\n")
    
print(f"This program refreshes a new wiki page every {wikiRefresh} seconds.")
time.sleep(3)

while True:
    
    wikiInfo()
    time.sleep(wikiRefresh)
    