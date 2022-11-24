import random

SUITS = ["D", "S", "H", "C"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


def Draw_Random():
    suite = random.choice(SUITS)
    rank = random.choice(RANKS)
    print(F'{rank}{suite}')

Draw_Random()    