import random

# Gets Random Numbers for the cards from the class Card
suit_number = random.randint(0,3)
values_number = random.randint(2,14)

class Card:
    suits = ["spades","hearts",
    "diamonds","clubs"]
    
    values = [None, None,"2","3",
    "4","5","6","7","8","9","10",
    "Jack","Queen","King","Ace"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        
        if self.value == c2.value:
            if self.suit < c2.value:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

card = Card(values_number, suit_number)
print("The winning card is: " + str(card))