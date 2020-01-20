import time
daycount = 0
while(True):
    user = input("Day " + str(daycount) + " Log: ")
    user = str("Day " + str(daycount) + " Log: " + user)
    f = open('Diary_Logs', "a+")
    f.write(user + "\n")
    f.close()
    print("Saved!")
    user1 = input("Would you like to write for the next day? (next or quit)")
    if (user1 == "next"):
        daycount += 1
        continue
    if (user1 != "yes"):
        break
