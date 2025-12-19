RANKS = [
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    'Jack',
    'Queen',
    'King',
    'Ace',
]

SUITS = [
    'Diamonds',
    'Clubs',
    'Hearts',
    'Spades',
]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def rank_tuple(self):
        return (RANKS.index(self.rank), SUITS.index(self.suit))

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank \
                and self.suit == other.suit
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Card):
            return self.rank_tuple < other.rank_tuple
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Card):
            return self.rank_tuple > other.rank_tuple
        return NotImplemented
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'

cards = [Card(2, 'Hearts'),
         Card(10, 'Diamonds'),
         Card('Ace', 'Clubs')]

print(min(cards) == Card(2, 'Hearts'))             # True
print(max(cards) == Card('Ace', 'Clubs'))          # True
print(str(min(cards)) == "2 of Hearts")            # True
print(str(max(cards)) == "Ace of Clubs")           # True

cards = [Card(5, 'Hearts')]
print(min(cards) == Card(5, 'Hearts'))             # True
print(max(cards) == Card(5, 'Hearts'))             # True
print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

cards = [Card(4, 'Hearts'),
         Card(4, 'Diamonds'),
         Card(10, 'Clubs')]
print(min(cards).rank == 4)                        # True
print(max(cards) == Card(10, 'Clubs'))             # True
print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

cards = [Card(7, 'Diamonds'),
         Card('Jack', 'Diamonds'),
         Card('Jack', 'Spades')]
print(min(cards) == Card(7, 'Diamonds'))           # True
print(max(cards).rank == 'Jack')                   # True
print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

cards = [Card(8, 'Diamonds'),
         Card(8, 'Clubs'),
         Card(8, 'Spades')]
print(min(cards).rank == 8)                        # True
print(max(cards).rank == 8)                        # True

print(min(cards) == Card(8, 'Diamonds')) # True
print(max(cards) == Card(8, 'Spades')) # True