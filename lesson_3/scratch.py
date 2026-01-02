# def foo1():

#     # raise ZeroDivisionError('Got ZeroDivisionError')
#     # raise ValueError('Got ValueError')
#     # raise AttributeError('Got AttributeError')
#     print('We should not be here')

# def foo2():
#     try:
#         foo1()
#     except ZeroDivisionError:
#         print('Got ZeroDivisionError')

# def foo3():
#     try:
#         foo2()
#     except ValueError:
#         print('Got ValueError')

# foo3()

# for value in ['abc', '0']:
#     try:
#         number = float(value)
#         quotient = 3.0 / number
#         break
#     except ValueError as e:
#         print("Oops! That's not a valid number.", e, '', sep='\n')
#     except ZeroDivisionError as e:
#         print('Oops! You tried to divide by zero!', e, '', sep='\n')
# # Oops! That's not a valid number.
# # could not convert string to float: 'abc'
# #
# # Oops! You tried to divide by zero!
# # float division by zero

# try:
#     open("no_such_file.txt", "r")
# except OSError as e:
#     print(f'Error number: {e.errno}, Error message: {e.strerror}')
#     print(f'File: {e.filename}')
# # Error number: 2, Error message: No such file or directory
# # File: no_such_file.txt

# log_file = open("log_file.txt", "w")

# try:
#     open("no_such_file.txt", "r")
# except OSError as e:
#     print(f'{e.errno=}, {e.strerror=}, {e.filename=}', file=log_file)
#     log_file.close()
#     raise
# FileNotFoundError: [Errno 2] No such file or directory:
# 'no_such_file.txt'

# for divisor in [2, 0]:
#     try:
#         result = 10 / divisor
#     except ZeroDivisionError:
#         print('Division by zero!')
#         raise
#     else:
#         print(f'Result is {result}')
#     finally:
#         print(f"We're done with divisor == {divisor}")
# # Result is 5.0
# We're done with divisor == 2
# Division by zero!
# We're done with divisor == 0
# ZeroDivisionError: division by zero

# def convert_to_integer(value):
#     try:
#         return int(value)
#     except ValueError as e:
#         raise TypeError('Expected a numeric string') from e

# try:
#     convert_to_integer('abc')
# except TypeError as error:
#     print(f'Error: {error}')
#     print(f'Original error: {error.__cause__}')
# # Error: Expected a numeric string
# # Original error: invalid literal for int() with base 10: 'abc'

# str1 = "I'm a string"
# str2 = "I'm a string"

# print(str1 == str2)
# print(str1 is str2)
# print(str1 <= str2)
# print(not(str1 > str2))

# class Point:
#     def __init__(self, x, y):
#         self.coordinates = {'x': x, 'y': y}

#     def __eq__(self, other):
#         if not isinstance(other, Point):
#             return NotImplemented

#         return self.coordinates == other.coordinates

# point1 = Point(5, 10)
# point2 = Point(5, 10)
# point3 = point1
# point1.coordinates['x'] = 4

# print(point1 == point2)
# print(point2 == point3)
# print(point1 == point3)
# print(point3 is point1)

# class Circle:
#     def __init__(self, r):
#         self.radius = r

#     def __lt__(self, other):
#         if not isinstance(other, Circle):
#             return NotImplemented

#         return self.radius < other.radius

#     def __gt__(self, other):
#         if not isinstance(other, Circle):
#             return NotImplemented

#         return self.radius > other.radius

#     def __le__(self, other):
#         if not isinstance(other, Circle):
#             return NotImplemented

#         return self.radius <= other.radius

#     def __ge__(self, other):
#         if not isinstance(other, Circle):
#             return NotImplemented

#         return self.radius >= other.radius

#     def __eq__(self, other):
#         if not isinstance(other, Circle):
#             return NotImplemented

#         return self.radius == other.radius

#     def __ne__(self, other):
#         if not isinstance(other, Circle):
#             return NotImplemented

#         return self.radius != other.radius

# circle1 = Circle(5)
# circle2 = Circle(3)
# circle3 = Circle(5)

# class SpeedyMixin:
#     def run_fast(self):
#         self.speed = 70

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Dog(Animal):
#     DOG_YEARS = 7

#     def __init__(self, name, age):
#         self.dog_age = age * Dog.DOG_YEARS

# class Greyhound(SpeedyMixin, Dog):
#     pass

# grey = Greyhound('Grey', 3)

# # print(grey.speed)
# # print(grey.name)
# # print(grey.age)
# print(grey.dog_age)
# print(grey.DOG_YEARS)

class Test:
    def __init__(self):
        print(self.__class__)
        print(type(self))
        print(Test)

test = Test()