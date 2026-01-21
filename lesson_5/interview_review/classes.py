
class Person:

    @staticmethod
    def affirm_existance():
        print('there is a Person class')

    count = 0

    @classmethod
    def print_count(cls):
        print(Person.count)

    def __init__(self, name, age):
        self.name = name
        self._age = age
        Person.count += 1
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('name must be a string')    
        self._name = value

    def greet(self):
        print(f"Hello I'm {self._name}")

    def incr_age(self):
        self._age += 1

class Captain(Person):
    def greet(self):
        print('ahoy matey!')

class Astronaut(Person):
    def greet(self):
        print('blast off !')

adam = Person('Adam', 25)
bob = Person('Bob', 30)
charlie = Captain('Charlie', 40)
doug = Astronaut('Doug', 50)

adam.affirm_existance()

obj_list = [
    adam,
    bob,
    charlie,
    doug
]

for obj in obj_list:
    obj.greet()