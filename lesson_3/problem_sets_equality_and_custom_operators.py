'''
__gt__
__mul__
__le__
__ne__
__iadd__
__ipow__
__floordiv__

'''

class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() == other.name.casefold()
    
    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() != other.name.casefold()
    
    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() < other.name.casefold()
    
    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() <= other.name.casefold()
    
    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() > other.name.casefold()
    
    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() >= other.name.casefold()
    
adam = Cat('Adam')
adam2 = Cat('adam')
bob = Cat('bob')

# print(adam == adam2)
# print(adam != bob)
# print(adam < bob)
# print(adam <= adam2)
# print(bob > adam)
# print(adam >= adam2)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        self.x += other.x
        self.y += other.y
        return self
    
    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)
    
    def __isub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Vector(other * self.x, other * self.y)
    
    def __rmul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return Vector(other * self.x, other * self.y)

# print(Vector(3, 2) + Vector(5, 12))   # Vector(8, 14)
# print(Vector(5, 12) - Vector(3, 2))   # Vector(2, 10)
# print(Vector(5, 12) * 2)              # Vector(10, 24)
# print(3 * Vector(5, 12))              # Vector(15, 36)

# my_vector = Vector(5, 7)
# my_vector += Vector(3, 9)
# print(my_vector)                      # Vector(8, 16)

# my_vector -= Vector(1, 7)
# print(my_vector)                      # Vector(7, 9)

# print(Vector(3, 2) + 5)
# # TypeError: unsupported operand type(s) for +: 'Vector'
# # and 'int'

class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'

    def __add__(self, other):
        if (not isinstance(other, int)) \
            and (not isinstance(other, str)):
            return NotImplemented
        
        if str(self.value).isdigit() and str(other).isdigit():
            return Silly(int(self.value) + int(other))
        return Silly(str(self.value) + str(other))


print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)