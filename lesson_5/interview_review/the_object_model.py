

# class Person:
#     def __init__(self, name):
#         self.name = name

# adam = Person('Adam')
# bob = Person('Bob')

# print(adam.name)
# print(bob.name)

class Foo:
    pass

foo = Foo()

print(f'I am a {type(foo).__name__} object')
print(f'I am a {foo.__class__.__name__} object')