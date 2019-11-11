import random
import time
number = random.randint(1,6)
number = int(number)
user = input("Would you like to roll the dice? (y or n): ")
while(True):
    if (user == "y"):
        print("rolling...")
        time.sleep(1)
        print(number)
        time.sleep(2)
        userq = input("Would you like to roll the dice again? (y or n): ")
        if (userq == "y"):
            number = random.randint(1,6)
            continue
        else:
            print("Bye")
            break
    else:
        print("Bye")
        break
