import pyautogui
import time
import random

pinnum1 = random.randint(0,9)
pinnum2 = random.randint(0,9)
pinnum3 = random.randint(0,9)
pinnum4 = random.randint(0,9)

time.sleep(5)
pyautogui.press(str(pinnum1))
pyautogui.press(str(pinnum2))
pyautogui.press(str(pinnum3))
pyautogui.press(str(pinnum4))

time.sleep(2)
pyautogui.press(str(pinnum1))
pyautogui.press(str(pinnum2))
pyautogui.press(str(pinnum3))
pyautogui.press(str(pinnum4))

f = open('pincode', "w+")
f.write(str(pinnum1))
f.write(str(pinnum2))
f.write(str(pinnum3))
f.write(str(pinnum4))
f.close()
