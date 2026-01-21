
class AMixin:
    pass

class Parent:

    count = 0

    @classmethod
    def give_count(cls):
        return Parent.count

    def __init__(self):
        Parent.count += 1

    def greet(self):
        print('hello')

    def greet(self):
        print('hi')

class Child(AMixin, Parent):
    def __init__(self, favorite_color):
        super().__init__()

        try:
            if not isinstance(favorite_color, str):
                raise ValueError('color must be a string')
            self.favorite_color = favorite_color

        except ValueError as error:
            print(error)
            self.favorite_color = ''
    # def greet(self):
    #     print('hi, I am a kid')


child = Child(35)
# print(child.give_count())
# child.greet()
print(child.favorite_color)

# for cls in Child.mro():
#     print(cls.__name__)

print(Child.__bases__)