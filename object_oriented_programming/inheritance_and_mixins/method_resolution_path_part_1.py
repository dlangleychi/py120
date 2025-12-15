class Animal:
    def __init__(self, color):
        self._color = color

class Cat(Animal):
    pass

class Bird(Animal):
    pass



print(Cat.mro())
cat1 = Cat('Black')
print(cat1.get_color())


'''
Cat, Animal, object
'''

