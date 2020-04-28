import random

while(True):

    user = input("Type: ")
    count = len(user)

    for count in range(count):
        binary = random.randint(0,1)
        print(binary)

    user2 = input("Type Again? ( y or n): ")
    if (user2 == "y"):
        continue
    else:
        break
