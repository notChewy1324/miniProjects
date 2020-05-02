import random
import time

while(True):

    #Ask User
    user = input("\nWould you like to generate a pin code or an alphanumeric password? (pin or alpha or done): ")
    user = str(user)

    #Stop Program
    if (user != "alpha" and user != "pin"):
        print("Bye!")
        break

    #Alpha Password
    if (user == "alpha"):
        alphaList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "~", "!", "@", "#", "$", "%", "^", "&", "*","(", ")", "?", "/", "{", ";", "|", "<", ">", "}", "-", "_", "+", "="]
        pinnum1 = random.randint(0,9)
        pinnum2 = random.randint(0,9)
        pinnum3 = random.randint(0,9)
        pinnum4 = random.randint(0,9)
        pinnum5 = random.randint(0,9)
        pinnum6 = random.randint(0,9)
        pinnum7 = random.randint(0,9)
        pinnum8 = random.randint(0,9)
        pinnum9 = random.randint(0,9)
        alphaLetter1 = random.choice(alphaList[:])
        alphaLetter1 = str(alphaLetter1.upper())
        alphaLetter2 = random.choice(alphaList[:])
        alphaLetter3 = random.choice(alphaList[:])
        alphaLetter4 = random.choice(alphaList[:])
        alphaLetter4 = str(alphaLetter4.upper())
        alphaLetter5 = random.choice(alphaList[:])
        alphaLetter6 = random.choice(alphaList[:])
        alphaLetter7 = random.choice(alphaList[:])
        alphaLetter7 = str(alphaLetter7.upper())
        print("Here is your generated alphanumeric password: ",alphaLetter1,pinnum1,pinnum2,alphaLetter2,pinnum3,pinnum4,alphaLetter3,alphaLetter4,pinnum5,pinnum6,pinnum7,alphaLetter5,pinnum8,pinnum9,alphaLetter6,alphaLetter7)
        time.sleep(1)
        continue

    #Pin Code
    if (user == "pin"):
        pinuser = input("Would you like to generate a 4-digit or 6-digit pin code? (type 4 or 6): ")
        pinuser = int(pinuser)

    if (pinuser == 4):
        pinnum1 = random.randint(0,9)
        pinnum2 = random.randint(0,9)
        pinnum3 = random.randint(0,9)
        pinnum4 = random.randint(0,9)
        print("Here is your generated 4-digit pin number: ",pinnum1,pinnum2,pinnum3,pinnum4)
        time.sleep(1)
        continue
    
    if (pinuser == 6):
        pinnum1 = random.randint(0,9)
        pinnum2 = random.randint(0,9)
        pinnum3 = random.randint(0,9)
        pinnum4 = random.randint(0,9)
        pinnum5 = random.randint(0,9)
        pinnum6 = random.randint(0,9)
        print("Here is your generated 6-digit pin number: ",pinnum1,pinnum2,pinnum3,pinnum4,pinnum5,pinnum6)
        time.sleep(1)
        continue
