class Pet:

    def __init__(self, name):
        self.name = name
        type_name = self.__class__.__name__
        print(f'I am {name}, a {type_name}.')
        
    def eat(self):
        print(f"{self.name}: Yum-yum-yum!")

class Dog(Pet):

    # __init__ method removed
    def speak(self):
        print(f'{self.name} says Woof!')

    def roll_over(self):
        print(f'{self.name} is rolling over.')

class Cat(Pet):

    # __init__ method removed
    def speak(self):
        print(f'{self.name} says Meow!')

class Parrot(Pet):

    # __init__ method removed
    def speak(self):
        print(f'{self.name} wants a cracker!')

sparky = Dog('Sparky')
fluffy = Cat('Fluffy')
polly = Parrot('Polly')

sparky.roll_over()

for pet in [sparky, fluffy, polly]:
    pet.speak()
    pet.eat()