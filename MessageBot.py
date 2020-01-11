import pyautogui
import time

num = 0
time.sleep(2) # Will allow you to prepare the space to write to

while(True):
    num = num + 1
    print(num) # Displays the current number the loop
    pyautogui.press("S")
    pyautogui.press("P")
    pyautogui.press("A")
    pyautogui.press("M")
    pyautogui.press("enter")
    continue
