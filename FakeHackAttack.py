import pyautogui
import webbrowser
import random
import time

start = 0
end = 80
count = 0

while(start <= end):

    pyautogui.FAILSAFE = False

    # website control
    stop = random.randint(0,10)
    time.sleep(stop)
    sites = random.choice(['duckduckgo.com','netflix.com','disneyplus.com','cnn.com','espn.com','facebook.com','snapchat.com',
                           'yahoo.com','amazon.com','bing.com','gmail.com','microsoft.com','apple.com','support.google.com',
                           'linkedin.com','maps.google.com','bbc.co.uk','medium.com','photos.google.com','google.co.uk',
                           'independent.co.uk','ebay.com','pinterest.com','whatismyipaddress.com','qq.com'])
    visit = "https://{}".format(sites)
    webbrowser.open(visit)
    
    # mouse control
    x = random.randint(0,1920)
    y = random.randint(0,1080)
    secs = random.randint(3,15)
    pyautogui.moveTo(x, y, secs)
    pyautogui.click(x, y, 1, 1, button='left')

    # screenshot control
    count = count + 1
    pyautogui.screenshot('userData' + str(count) + '.png')
    
    continue
