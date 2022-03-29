import random
import requests

wordlst = []
wordCnt = 20 # Number of words to add in the word list

def words():
    
    while (len(wordlst) < wordCnt):
        try:
            wordAPI = requests.get("https://random-word-api.herokuapp.com/word?number=1&swear=0")
        except:
            print("Failed to create an connection. Check your internet.")
        
        lstWords = wordAPI.json()
        wordlst.append(lstWords)
    
print("Loading Words...")
words()

print("Possible words:",wordlst)
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
            print("You Win! It was {}.".format(word))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))

word = random.choice(wordlst[:])
hangman(word)
