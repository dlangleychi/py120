from random import randint
import math

class GuessingGame:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def play(self):
        hidden = randint(self.low, self.high)
        guesses = int(math.log2(self.high - self.low + 1)) + 1

        while guesses > 0:
            print()
            print(f'You have {guesses} guesses remaining.')

            guess = input(f'Enter a number between '
                          f'{self.low} and {self.high}: ')

            while True:
                try:
                    int_guess = int(guess)
                    if int_guess < self.low or int_guess > self.high:
                        raise ValueError('not in range')
                    break
                except:
                    guess = input(f'Invalid guess. Enter a '
                                    f'number between {self.low} ' 
                                    f'and {self.high}: ')
            
            if int_guess < hidden:
                print('Your guess is too low.')
            elif int_guess > hidden:
                print('Your guess is too high.')
            else:
                print("That's the number !")
                print()
                print('You won!')
                return
            
            guesses -= 1
        
        print()
        print('You have no more guesses. You lost!')

game = GuessingGame(501, 1500)
game.play()
