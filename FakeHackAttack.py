import pyautogui
import webbrowser
import random
import time

for i in range(0,10):

    count = 0
    pyautogui.FAILSAFE = False

    # website control
    sites = random.choice(['duckduckgo.com','netflix.com','disneyplus.com','cnn.com','espn.com','facebook.com','snapchat.com',
                           'yahoo.com','amazon.com','bing.com','gmail.com','microsoft.com','apple.com','support.google.com',
                           'linkedin.com','maps.google.com','bbc.co.uk','medium.com','photos.google.com','google.co.uk',
                           'independent.co.uk','ebay.com','pinterest.com','whatismyipaddress.com','qq.com','192.168.0.1'])
    visit = "https://{}".format(sites)
    webbrowser.open(visit)

    # screenshot control
    # count = count + 1
    # pyautogui.screenshot('userData-' + str(count) + '.png')

    # mouse control
    x = random.randint(0,1920)
    y = random.randint(0,1080)
    secs = random.randint(3,10)
    pyautogui.moveTo(x, y, secs)
    pyautogui.click(x, y, 1, 1, button='left')

    i += 1