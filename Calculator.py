#Create a program called Calculator
#Create the varibles
multiplaction = "Multi"
Subtraction = "Sub"
Addition = "Add"
Divide = "Divide"
#Ask the user the type of method they want to use (-,+,/,*) and give them the answers
while(True):
        print("What type of method do you want do calculate.")
        print("Add, Sub, Multi, Divide? (type no to quit)")
        user = input("")
        type(user)
        if (user == multiplaction):
                multi = input("Please type a number: ")
                multi = float(multi)
                multi2 = input("One more number plz: ")
                multi2 = float(multi)
                multianswer = multi * multi2
                print("The answer is:", multianswer)
        elif (user == Subtraction):
                sub = input("Please type a number: ")
                sub = float(sub)
                sub2 = input("One more number plz: ")
                sub2 = float(sub2)
                subanswer = sub - sub2
                print("The answer is:", subanswer)
        elif (user == Addition):
                add = input("Please type a number: ")
                add = float(add)
                add2 = input("One more number plz: ")
                add2 = float(add2)
                addanswer = add + add2
                print("The answer is:", addanswer)
        elif (user == Divide):
                div = input("Please type a number: ")
                div = float(div)
                div2 = input("One more number plz: ")
                div2 = float(div2)
                divanswer = div / div2
                print("The answer is:", divanswer)
        else:
                print("Make sure that you enter EXACLTY what the word above said!")
                user = input("Would you like to continue again? (y or n): ")
                if (user == "y"):
                        continue
                else:
                        print("Bye")
                        break
