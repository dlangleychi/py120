# 1

class Game:

    count = 0

    def __init__(self):
        Game.count += 1

    def play(self):
        return f'Start the {self.__class__.__name__} game!'

class Bingo(Game):
    def __init__(self, game_name, player_name):
        self.game_name = game_name
        self.player_name = player_name
        super().__init__()

class Scrabble(Game):
    def __init__(self, game_name, player_name1, player_name2):
        self.game_name = game_name
        self.player_name1 = player_name1
        self.player_name2 = player_name2
        super().__init__()

# bingo = Bingo()
# print(bingo.play())

# 2

# bingo = Bingo('Bingo', 'Bill')
# print(Game.count)                       # 1
# print(bingo.play())                     # Start the Bingo game!
# print(bingo.player_name)                # Bill

# scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
# print(Game.count)                       # 2
# print(scrabble.play())                  # Start the Scrabble game!
# print(scrabble.player_name1)            # Jill
# print(scrabble.player_name2)            # Sill
# print(scrabble.player_name)
# # AttributeError: 'Scrabble' object has no attribute 'player_name'

# 3

'''
cleaner more intuitive code
encapsulation and abstraction
organization
simplifies testing
faster development, reuse
'''

# 4

# print('Hello')

# AttributeError

# TypeError

# print('Goodbye')

# TypeError, missing argument, no self

class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):

    def hi(self):
        self.greet('Hello')

    @classmethod
    def hi(cls):
        greeting = Greeting()
        greeting.greet('Hi')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')


# 5

# Hello.hi()

# hello = Hello()
# hello.hi()

# 6

class Cat:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f'I am a {self.type}'

print(Cat('hairball'))
# <__main__.Cat object at 0x10695eb10>

# 7

class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer())
print(tv.model())

print(Television.manufacturer())
print(Television.model())

'''
Amazon
Omni Fire
Amazon
TypeError, missing position argument self
'''