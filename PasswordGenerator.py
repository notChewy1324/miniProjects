import random
import time
while(True):
    user = input("Would you like to generate a pin code or an alphanumeric password? (pin or alpha or done): ")
    user = str(user)
    if (user == "done"):
        break
    if (user == "alpha"):
        wordlst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        Cletter = random.choice(wordlst[:])
        Cletter1 = str(Cletter.upper())
        pinnum1 = random.randint(0,9)
        pinnum2 = random.randint(0,9)
        Cletter2 = random.choice(wordlst[:])
        pinnum3 = random.randint(0,9)
        pinnum4 = random.randint(0,9)
        Cletter3 = random.choice(wordlst[:])
        Cletter41 = random.choice(wordlst[:])
        Cletter4 = str(Cletter41.upper())
        pinnum5 = random.randint(0,9)
        pinnum6 = random.randint(0,9)
        pinnum7 = random.randint(0,9)
        Cletter5 = random.choice(wordlst[:])
        print("Here is your generated alphanumeric password:", Cletter1,pinnum1,pinnum2,Cletter2,pinnum3,pinnum4,Cletter3,Cletter4,pinnum5,pinnum6,pinnum7,Cletter5)
        time.sleep(3)
        continue
    if (user == "pin"):
        pinuser = input("Would you like to generate a 4-digit or 6-digit pin code? (type 4 or 6): ")
        pinuser = int(pinuser)
    if (pinuser == 4):
        pinnum1 = random.randint(0,9)
        pinnum2 = random.randint(0,9)
        pinnum3 = random.randint(0,9)
        pinnum4 = random.randint(0,9)
        print("Here is your generated 4-digit pin number:",pinnum1,pinnum2,pinnum3,pinnum4)
        time.sleep(2)
    if (pinuser == 6):
        pinnum1 = random.randint(0,9)
        pinnum2 = random.randint(0,9)
        pinnum3 = random.randint(0,9)
        pinnum4 = random.randint(0,9)
        pinnum5 = random.randint(0,9)
        pinnum6 = random.randint(0,9)
        print("Here is your generated 6-digit pin number:",pinnum1,pinnum2,pinnum3,pinnum4,pinnum5,pinnum6)
        time.sleep(2)
