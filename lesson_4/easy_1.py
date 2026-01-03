# 1

# all are objects, use the type function
# or __class__ magic variable
# or __class__.__name__

# 2

# cat = AngryCat()

# 3

class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

class Truck(SpeedMixin):
    def go_very_slow(self):
        print('I am a heavy truck and like going very slow.')

# car = Car()
# truck = Truck()
# car.go_fast()
# truck.go_fast()

# 4

# small_car = Car()
# small_car.go_fast()

# self.__class__.__name__
# __class__ gives instance of type 

# 5

# Pizza, my_name in Fruit is a local variable that gets
# discarded after the method finishes running

class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name

# print(vars(Fruit('orange')))     # {}
# print(vars(Pizza('pepperoni')))  # {'my_name': 'pepperoni'}

# print("\nMILO !!!\n")

# 6

# it will print one of the four messages, all with equal
# probability

# 7

# it will randomly print one of the five RoadTrip messages

# 8

class Test:
    variable = 1
    def foo(self):
        pass
    
# my_obj = Test()
# print(my_obj.__class__.mro())

# for klass in my_obj.__class__.mro():
#     print(klass.__name__)

# 9

'''
local variable
instance variable
class variable
class variable

tell by prefix
'''

# 10

class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count
    
#  it is how many instances of Cat there are
#  each time an instance is created the number gets incr

cat1 = Cat('Brown')
print(cat1.__class__.cats_count())
cat2 = Cat('White')
print(type(cat2).cats_count())