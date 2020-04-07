import pyautogui
import webbrowser
import random
import time

start = 0
end = 80
count = 0

while(start <= end):
    stop = random.randint(0,30)
    pyautogui.FAILSAFE = False
    time.sleep(stop)
    sites = random.choice(['duckduckgo.com','netflix.com','disneyplus.com','cnn.com','espn.com','facebook.com','snapchat.com',
                           'yahoo.com','amazon.com','bing.com','gmail.com','microsoft.com','apple.com','support.google.com',
                           'linkedin.com','maps.google.com','bbc.co.uk','medium.com','photos.google.com','google.co.uk',
                           'independent.co.uk','ebay.com','pinterest.com','whatismyipaddress.com','qq.com'])
    visit = "https://{}".format(sites)
    webbrowser.open(visit)
    x = random.randint(0,1920)
    y = random.randint(0,1080)
    secs = random.randint(3,15)
    pyautogui.moveTo(x, y, secs)
    count = count + 1
    pyautogui.screenshot('userData' + str(count) + '.png')
    continue
