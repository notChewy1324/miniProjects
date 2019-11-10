import random
def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   ",
              "|          |        ",
              "|          O        ",
              "|         /|\       ",
              "|         / \       ",
              "|                   ",
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))

wordlst = ["cat", "dog", "goat", "cpu", "ram", "iphone", "Farmer", "Hello", "World", "code", "Hangman", "Google", "Apple", "toys", "stages", "python"]
word = random.choice(wordlst[:])
hangman(word)
