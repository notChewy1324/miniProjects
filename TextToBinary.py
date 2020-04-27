import random

while(True):

    user = input("Type: ")
    count = len(user)

    mainList = ['']
    for count in range(count):
        binary = random.randint(0,1)
        mainList.extend(str(binary))
    print(mainList)

    user2 = input("Type Again? ( y or n): ")
    if (user2 == "y"):
        continue
    else:
        break
