from random import shuffle

class Card:
    RANKS = [
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'J',
        'Q',
        'K',
        'A',
    ]

    FACE_CARDS = [
        'J',
        'Q',
        'K',
    ]

    SUITS = [
        'Clubs',
        'Diamonds',
        'Hearts',
        'Spades'
    ]

    HIDDEN_CARD_STRING = 'XX'

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit

    def __str__(self):
        return f'{self.rank}{self.suit[0].lower()}'

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) \
                      for rank in Card.RANKS \
                      for suit in Card.SUITS]
        shuffle(self.cards)
        

    def deal(self):
        return self.cards.pop()

class Participant:
    def __init__(self):
        self.hand = []
        self._score = 0
        self._busted = False   

    def clear_hand(self):
        self.hand = []

    @property
    def score(self):
        return self._score
    
    @property
    def busted(self):
        return self._busted
    
    def receive_card(self, card):
        self.hand.append(card)

    def cards_to_string(self):
        return ' '.join(map(str, self.hand))
    
    def score_hand(self):
        score = 0
        aces = 0

        for card in self.hand:
            try:
                score += int(card.rank)
            except ValueError:
                if card.rank in Card.FACE_CARDS:
                    score += 10
                else:
                    score += 1
                    aces += 1

        # if you're busted with Aces having min value,
        # the exact score dosen't matter
        if score > TwentyOneGame.SCORE_LIMIT:
            self._score = score
            self._busted = True
            return
        
        while aces and score + 10 <= TwentyOneGame.SCORE_LIMIT:
            score += 10
            aces -= 1

        self._score = score
        self._busted = False

class Player(Participant):
    STARTING_BANK = 5

    def __init__(self):
        super().__init__()
        self._bank = Player.STARTING_BANK

    @property
    def bank(self):
        return self._bank
    
    @bank.setter
    def bank(self, value):
        self._bank = value

    def incr_bank(self):
        self.bank += 1

    def decr_bank(self):
        self.bank -= 1
    
    def cards_to_string(self):
        return f"Player's hand is: {super().cards_to_string()}"

class Dealer(Participant):
    def cards_to_string_hidden(self):
        return f"Dealer's hand is: {self.hand[0]} {Card.HIDDEN_CARD_STRING}"

    def cards_to_string(self):
        return f"Dealer's hand is: {super().cards_to_string()}"

class TwentyOneGame:

    DEALER_STAY = 17
    SCORE_LIMIT = 21
    PLAYER_BROKE = 0
    PLAYER_RICH = 19

    def __init__(self):
        self.deck = None
        self.player = Player()
        self.dealer = Dealer()

    def start(self):
        self.display_welcome_message()

        while TwentyOneGame.PLAYER_BROKE < \
            self.player.bank < TwentyOneGame.PLAYER_RICH:
            
            self.play_round()
            play_again = input("Would you like to play again? ")
            if play_again.lower() != 'yes':
                break
            
        if self.player.bank == TwentyOneGame.PLAYER_BROKE:
            print("You're broke. I'm sorry.  :(")
        if self.player.bank == TwentyOneGame.PLAYER_RICH:
            print("You're rich!!! Congrats!!!!")
            
        self.display_goodbye_message()

    def play_round(self):
        self.deck = Deck()
        self.player.clear_hand()
        self.dealer.clear_hand()
        self.display_bank()
        self.deal_cards()
        self.show_cards()
        self.player_turn()
        if not self.player.busted:
            self.dealer_turn()
        self.display_result()
        self.update_players_bank()

    def deal_cards(self):
        self.deal_to_player()
        self.deal_to_dealer()
        self.deal_to_player()
        self.deal_to_dealer()

    def deal_to_player(self):
        self.player.receive_card(self.deck.deal())
        self.player.score_hand()

    def deal_to_dealer(self):
        self.dealer.receive_card(self.deck.deal())
        self.dealer.score_hand()

    def show_cards(self):
        self.display_dealers_partial_hand()
        self.display_players_hand()

    def player_turn(self):
        while True:
            choice = self.prompt_player()
            if choice == 'hit':
                self.deal_to_player()
                self.display_players_hand()
                if self.player.busted:
                    self.display_player_busted_message()
                    return
                continue
            elif choice == 'stay':
                return

    def prompt_player(self):
        while True:
            try:
                choice = input(
                    f"Player's score is: "
                    f"{self.player.score} "
                    f"\nHit or stay? "
                )
                if choice.lower() not in ['hit', 'stay']:
                    print('Invalid choice.')
                    continue
                return choice.lower()
            except:
                print('Invalid choice.')

    def dealer_turn(self):
        self.display_dealers_full_hand()
        self.display_dealers_score()
        while self.dealer.score < TwentyOneGame.DEALER_STAY:
            print('Dealer hits.')
            self.deal_to_dealer()
            self.display_dealers_full_hand()
            self.display_dealers_score()
            if self.dealer.busted:
                self.display_dealer_busted_message()
                return
            
        print('Dealer stays.')

    def update_players_bank(self):
        result = self.determine_result()
        if result == 'win':
            self.player.incr_bank()
        elif result == 'lose':
            self.player.decr_bank()

    def determine_result(self):
        if self.player.busted:
            return 'lose'
        elif self.dealer.busted:
            return 'win'
        else: 
            if self.player.score > self.dealer.score:
                return 'win'
            elif self.player.score < self.dealer.score:
                return 'lose'
            else:
                return 'tie'


    def display_welcome_message(self):
        print('Welcome to 21!!!!')

    def display_goodbye_message(self):
        print('Thank you for playing 21.  Goodbye.')    

    def display_result(self):
        if self.player.busted:
            print('Player busted.  You lose.')
        elif self.dealer.busted:
            print('Dealer busted.  You win!')
        else: 
            print(f'Your score is {self.player.score}. '
                  f"Dealer's score is {self.dealer.score}. "
                  f'You {self.determine_result()}.')
    
    def display_players_hand(self):
        print(self.player.cards_to_string())

    def display_dealers_partial_hand(self):
        print(self.dealer.cards_to_string_hidden())
    
    def display_dealers_full_hand(self):
        print(self.dealer.cards_to_string())
    
    def display_bank(self):
        print(f"Player's bank is: {self.player.bank}")

    def display_player_busted_message(self):
        print(f"Oh no!!! Player's score is {self.player.score}."
              " You busted. :(")

    def display_dealers_score(self):
        print(f"Dealer's score is: {self.dealer.score}")

    def display_dealer_busted_message(self):
        print(f"Alright!!! Dealer's score is {self.dealer.score}."
              " Dealer busted! ;)")

game = TwentyOneGame()
game.start()