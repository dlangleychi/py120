class Pet:

    def __init__(self, name):
        self.name = name

    def speak(self, sound):
        print(f'{self.name} says {sound}!')

class Cat(Pet):

    def speak(self):
        super().speak('meow')

cheddar = Cat('Cheddar')
# cheddar.speak()

class Animal:

    @classmethod
    def make_sound(cls):
        print(f'{cls.__name__}: A generic sound')

class Dog(Animal):

    @classmethod
    def make_sound(cls):
        super().make_sound()
        print(f'{cls.__name__}: Bark')

Dog.make_sound()
# Dog: A generic sound
# Dog: Bark