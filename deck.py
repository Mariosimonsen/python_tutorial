import random

SUITS = ["D", "S", "H", "C"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


def Draw_Random():
    suite = random.choice(SUITS)
    rank = random.choice(RANKS)
    print(F'{rank}{suite}')

Draw_Random()    


deck = []

for suit in SUITS:
    for rank in RANKS:
        deck.append(F'{rank}{suit}')

print (len(deck))

random.shuffle(deck)

player1 = [deck.pop(), deck.pop(), deck.pop(), deck.pop(), deck.pop()] #.pop fjerne verdi ifra listen.
player2 = [deck.pop(), deck.pop(), deck.pop(), deck.pop(), deck.pop()]

print(player1)
print(player2)

print(len(42))

print(dir(int)) # + object for og få oppe funksjoner

print(dir(list))