class GrandParent_1:
    def method(self):
        print('Grand Parent 1')

class GrandParent_2:
    def method(self):
        print('Grand Parent 2')

class Parent_1(GrandParent_1):
    def method(self):
        print('Parent 1')

class Parent_2(GrandParent_2):
    def method(self):
        print('Parent 2')


class Child(Parent_1, Parent_2):
    pass

child = Child()
# child.method()

for cls in Child.mro():
    print(cls.__name__)