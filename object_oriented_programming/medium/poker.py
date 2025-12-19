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
    def rank_number(self):
        return RANKS.index(self.rank)

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank \
                and self.suit == other.suit
        return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Card):
            return self.rank_number < other.rank_number
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Card):
            return self.rank_number > other.rank_number
        return NotImplemented
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'

from random import shuffle

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self._new_deck()

    def _new_deck(self):
        self._deck = [Card(rank, suit) 
                      for rank in Deck.RANKS 
                      for suit in Deck.SUITS]
        shuffle(self._deck)
    
    def draw(self):
        card = self._deck.pop()
        if not self._deck:
            self._new_deck()
        return card

# Include Card and Deck classes from the last two exercises.

class PokerHand:
    def __init__(self, deck):
        if isinstance(deck, Deck):
            self._deck = [deck.draw() for _ in range(5)]
        else:
            self._deck = [card for card in deck._deck]

    def print(self):
        for card in self._deck:
            print(card)
        self.evaluate()

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        ranks = self._numerical_ranks()
        return self._is_straight_flush() and ranks[-1] == 12

    def _is_straight_flush(self):
        return self._is_flush() and self._is_straight()

    def _is_four_of_a_kind(self):
        ranks = self._numerical_ranks()
        return (ranks[0] == ranks[1] == ranks[2] == ranks[3]) \
            or (ranks[1] == ranks[2] == ranks[3] == ranks[4])

    def _is_full_house(self):
        return len(set(self._numerical_ranks())) == 2

    def _is_flush(self):
        return len(set(self._suits())) == 1

    def _is_straight(self):
        ranks = self._numerical_ranks()
        return len(set(ranks)) == 5 \
            and ranks[-1] - ranks[0] == 4

    def _is_three_of_a_kind(self):
        ranks = self._numerical_ranks()
        return (ranks[0] == ranks[1] == ranks[2]) \
            or (ranks[1] == ranks[2] == ranks[3]) \
            or (ranks[2] == ranks[3] == ranks[4])


    def _is_two_pair(self):
        return len(set(self._numerical_ranks())) == 3

    def _is_pair(self):
        return len(set(self._numerical_ranks())) == 4 
    
    def _numerical_ranks(self):
        return sorted([card.rank_number for card in self._deck])

    def _suits(self):
        return [card.suit for card in self._deck]

hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._deck = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
# print('HERE', hand.evaluate())
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")