from collections import namedtuple
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    def __len__(self):
        return 0

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


point_one = Point(x=5, y=6)
point_two = Point(x=4, y=9)

point_three = point_one + point_two


import random


class Deck:
    SUITS = ["D", "S", "H", "C"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen",
             "King", "Ace"]

    def __init__(self):
        self.cards = []
        for suit in Deck.SUITS:
            for rank in Deck.RANKS:
                self.cards.append(f'{rank}{suit}')

        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return f'my deck : {len(self.cards)} cards left'



tuple_data = ('Eivind', 'Hansen', 25, 'Oslo', 'Norway')



Card = namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
    suits = 'Spades Diamonds Clubs Hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value

    def __str__(self):
        line_one = f'FrenchDeck: {len(self._cards)} cards left'
        line_two = f'Topmost card: {self._cards[0].rank} of {self._cards[0].suit}'
        return f'{line_one}\n{line_two}'

    def pop(self):
        return self._cards.pop()



fd = FrenchDeck()
random.shuffle(fd)
hand_one = [fd.pop() for _ in range(5)]
hand_two = [fd.pop() for _ in range(5)]

print(fd)
