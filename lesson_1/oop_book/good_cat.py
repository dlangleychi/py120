class GoodCat():

    @classmethod
    def what_am_i(cls):
        print("I'm a GoodCat class!")

# GoodCat.what_am_i()    # I'm a GoodCat class!

class Foo:

    @classmethod
    def bar(cls):
        print('this is bar')

    @classmethod
    def qux(cls):
        print('this is qux')
        cls.bar()

# Foo.qux()
# this is qux
# this is bar

class Foo1:

    @classmethod
    def bar(cls):
        print('this is bar in Foo1')

    def qux(self):
        type(self).bar()
        self.__class__.bar()
        self.bar()
        Foo1.bar()

class Foo2(Foo1):

    @classmethod
    def bar(cls):
        print('this is bar in Foo2')

foo1 = Foo1()
# foo1.qux()
# this is bar in Foo1
# this is bar in Foo1
# this is bar in Foo1
# this is bar in Foo1

foo2 = Foo2()
# foo2.qux()
# this is bar in Foo2
# this is bar in Foo2
# this is bar in Foo2
# this is bar in Foo1

class GoodCat:

    counter = 0                  # class variable

    def __init__(self):
        GoodCat.counter += 1

    @classmethod
    def number_of_cats(cls):
        return GoodCat.counter

class ReallyGoodCat(GoodCat):
    pass

cat1 = GoodCat()
cat2 = GoodCat()
cat3 = ReallyGoodCat()

print(GoodCat.number_of_cats())        # 3
print(GoodCat.counter)                 # 3
print(ReallyGoodCat.number_of_cats())  # 3
print(ReallyGoodCat.counter)           # 3