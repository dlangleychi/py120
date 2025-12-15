class Pet:
    def speak(self):
        pass

    def sleep(self):
        return 'sleeping!'
    
    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Dog(Pet):
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

class Bulldog(Dog):
    def sleep(self):
        return 'snoring!'

class Cat(Pet):
    def speak(self):
        return 'meow!'


pet = Pet()
dave = Dog()
bud = Bulldog()
kitty = Cat()

print(pet.run())              # running!
print(kitty.run())            # running!
print(kitty.speak())          # meow!
try:
    kitty.fetch()
except Exception as exception:
    print(exception.__class__.__name__, exception, "\n")
    # AttributeError 'Cat' object has no attribute 'fetch'

print(dave.speak())           # bark!

print(bud.run())              # running!
print(bud.sleep())             # "snoring!"

# teddy = Dog()
# print(teddy.speak())      # bark!
# print(teddy.sleep())       # sleeping!
# print(teddy.fetch())       # fetching!

# tom = Cat()
# print(tom.speak())      # meow!
# print(tom.sleep())       # sleeping!
# print(tom.fetch())       # AttributeError


# teddy = Dog()
# print(teddy.speak())      # bark!
# print(teddy.sleep())       # sleeping!

# bobby = Bulldog()
# print(bobby.speak())      # bark!
# print(bobby.sleep())       # snoring!

'''
Pet
    Dog
        Bulldog
    Cat
'''

'''
The order of classes in the inheritance tree in 
which the method is looked for.
'''

print(Bulldog.mro())
print([cls.__name__ for cls in Bulldog.mro()])