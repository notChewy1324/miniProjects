import random
import time
num = random.randint(0,10)
while(True):
    user = input("Please type a number from 0 to 10: ")
    userint = int(user)
    if (userint == num):
        print("You guessed correctly!")
        time.sleep(1)
        userq = input("Play Again? (y or n): ")
        if (userq == "y"):
            num = random.randint(0,10)
            continue
        else:
            break
    if (userint > num):
        print("Number guessed is less than actual number.")
    if (userint < num):
        print("Number guessed is higher than actual number.")
