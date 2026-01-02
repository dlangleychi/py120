# Computer personalities

import random

class Move:
    pass

class Rock(Move):
    def __lt__(self, other):
        return isinstance(other, Paper) \
            or isinstance(other, Spock)
    
    def __gt__(self, other):
        return isinstance(other, Scissors) \
            or isinstance(other, Lizard)

    def __str__(self):
        return 'rock'

class Paper(Move):
    def __lt__(self, other):
        return isinstance(other, Scissors) \
            or isinstance(other, Lizard)
    
    def __gt__(self, other):
        return isinstance(other, Rock) \
            or isinstance(other, Spock)
    
    def __str__(self):
        return 'paper'

class Scissors(Move):
    def __lt__(self, other):
        return isinstance(other, Rock) \
            or isinstance(other, Spock)
    
    def __gt__(self, other):
        return isinstance(other, Paper) \
            or isinstance(other, Lizard)

    def __str__(self):
        return 'scissors'

class Spock(Move):
    def __lt__(self, other):
        return isinstance(other, Paper) \
            or isinstance(other, Lizard)
    
    def __gt__(self, other):
        return isinstance(other, Rock) \
            or isinstance(other, Scissors)

    def __str__(self):
        return 'spock'

class Lizard(Move):
    def __lt__(self, other):
        return isinstance(other, Rock) \
            or isinstance(other, Scissors)
    
    def __gt__(self, other):
        return isinstance(other, Paper) \
            or isinstance(other, Spock)

    def __str__(self):
        return 'lizard'

class Player:
    CHOICES = ('rock', 'paper', 'scissors', 'spock', 'lizard')

    def __init__(self):
        self.move = None

    def _create_choice(self, choice):
        match choice:
            case 'rock':
                return Rock()
            case 'paper':
                return Paper()
            case 'scissors':
                return Scissors()
            case 'spock':
                return Spock()
            case 'lizard':
                return Lizard()

class Computer(Player):

    WEIGHTS = {
        'R2D2': [100, 0, 0, 0, 0],
        'HAL': [15, 15, 40, 15, 15]
    }

    def __init__(self, personality):
        self._weights = Computer.WEIGHTS[personality]

    def choose(self):
        self.move = self._create_choice\
            (random.choices(Player.CHOICES, self._weights)[0])

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = ('Please choose rock, paper, '
            'scissors, spock, or lizard: ')

        while True:
            choice = input(prompt).lower()
            if choice.lower() in Player.CHOICES:
                break

            print(f'Sorry, {choice} is not valid')

        self.move = self._create_choice(choice)

class History:
    def __init__(self):
        self._human_moves = []
        self._computer_moves = []

    def update(self, human_move, computer_move):
        self._human_moves.append(human_move)
        self._computer_moves.append(computer_move)

    def __str__(self):
        strings = []
        strings.append('')
        strings.append('Move History')
        for human_move, computer_move \
            in zip(self._human_moves, self._computer_moves):
            strings.append(f'Human: {human_move} Computer: {computer_move}')
        strings.append('')
        return '\n'.join(strings)

class RPSGame:
    def __init__(self, computer_personality):
        self._human = Human()
        self._computer = Computer(computer_personality)
        self.winner = None

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors Spock Lizard!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors '
              'Spock Lizard. Goodbye!')

    def _human_wins(self):
        return self._human.move > self._computer.move

    def _computer_wins(self):
        return self._computer.move > self._human.move

    def _determine_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_wins():
            print('You win!')
            self.winner = 'human'
        elif self._computer_wins():
            print('Computer wins!')
            self.winner = 'computer'
        else:
            print("It's a tie")

    def play(self):
        self._display_welcome_message()

        self._human.choose()
        self._computer.choose()
        self._determine_winner()
            
        self._display_goodbye_message()

class RPSMatch:
    def __init__(self, winning_score, computer_personality):
        self._winning_score = winning_score
        self._computer_personality = computer_personality
        self._human_score = 0
        self._computer_score = 0
        self._history = History()
        self._winner = None

    def _display_welcome(self):
        print(f'Welcome to a match to {self._winning_score}')

    def _display_score(self):
        print(f'Human {self._human_score} Computer {self._computer_score}')
    
    def _display_winner(self):
        print(f'Match Winner is {self._winner} !!!')
    
    def _determine_winner(self):
        if self._human_score >= self._winning_score:
            self._winner = 'human'
        elif self._computer_score >= self._winning_score:
            self._winner = 'computer'

    def _play_game(self):
        game = RPSGame(self._computer_personality)
        game.play()
        if game.winner == 'human':
            self._human_score += 1
        elif game.winner == 'computer':
            self._computer_score += 1
        self._history.update(game._human.move, game._computer.move)

    def play(self):
        while True:
            self._winner = None
            self._human_score = 0
            self._computer_score = 0
            self._display_welcome()
            while self._winner is None:
                self._play_game()    
                self._display_score()
                self._determine_winner()
            self._display_winner()

            if not self._play_again():
                print(self._history)
                break


    def _play_again(self):
        answer = input('Would you like to play again? (y/n) ')
        return answer.lower().startswith('y')

RPSMatch(5, 'R2D2').play()