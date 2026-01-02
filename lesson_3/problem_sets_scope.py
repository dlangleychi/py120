class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed

    def __str__(self):
        return self._breed
    
poodle = Dog('Poodle')
golden_retriever = Dog('Golden Retriever')

# print(poodle.get_breed())
# print(golden_retriever.get_breed())


class Cat:
    def get_name(self):
        try:
            self.name
        except AttributeError:
            return 'Name not set!'
    
# cat = Cat()
# cat.get_name()

# dog = Dog('')
# dog._breed = 'Husky'
# print(dog.get_breed())

class Student:
    school_name = 'Oxford'

    @classmethod
    def get_school_name(cls):
        return cls.school_name

    def __init__(self, name):
        self.name = name

# student = Student()
# print(student.__class__.school_name)
# print(student.school_name)

# adam = Student('Adam')
# bob = Student('Bob')

# print(adam.school_name, adam.name)
# print(bob.school_name, bob.name)

# print(Student.get_school_name())
# print(Student.school_name)

class Car:
    manufacturer = 'Ford'

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def show_manufacturer(self):
        print(type(self).manufacturer, self.manufacturer)

# car = Car('Chevy')
# car.show_manufacturer()

class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        super().__init__(species)
        self.color = color


# birdie = Sparrow("sparrow", "brown")
# print(birdie.species)               # What will this output?
# # Attribute Error

class Mammal:
    def __init__(self):
        self.legs = 4

class Human(Mammal):
    def __init__(self):
        self.legs = 2

# man = Human()
# print(man.legs)

class Cat:
    sound = "meow"

    @classmethod
    def make_sound(cls):
        return cls.sound

class Lion(Cat):
    sound = "roar"

# print(Lion.make_sound())

# roar, the method looks in its own class first

class Tree:
    def __init__(self):
        self.type = "Generic Tree"

class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"

# Pine Tree

class A:
  def __init__(self):
      self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)

# AttributeError, the init of A isn't called in the init of B
