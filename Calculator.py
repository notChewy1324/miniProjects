#Create a program called Calculator
#Create the varibles
multiplaction = "multi"
Subtraction = "sub"
Addition = "add"
Divide = "divide"
#Ask the user the type of method they want to use (-,+,/,*) and give them the answers
while(True):
        print("What type of method do you want do calculate.")
        print("add, sub, multi, divide? (press any key to quit)")
        user = input("")
        if (user == multiplaction):
                multi = input("Please type a number: ")
                multi2 = input("One more number plz: ")
                multianswer = int(multi) * int(multi2)
                print("The answer is: ", multianswer)
        elif (user == Subtraction):
                sub = input("Please type a number: ")
                sub2 = input("One more number plz: ")
                subanswer = int(sub) - int(sub2)
                print("The answer is: ", subanswer)
        elif (user == Addition):
                add = input("Please type a number: ")
                add2 = input("One more number plz: ")
                addanswer = int(add) + int(add2)
                print("The answer is: ", addanswer)
        elif (user == Divide):
                div = input("Please type a number: ")
                div2 = input("One more number plz: ")
                divanswer = int(div) / int(div2)
                print("The answer is: ", divanswer)
        else:
             print("Bye")
             break
