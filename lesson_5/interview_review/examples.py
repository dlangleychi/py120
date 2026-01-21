class GoodCat:

    counter = 0                  # class variable

    def __init__(self):
        print(self.__class__.__name__, self.__class__.counter)
        # print(GoodCat.counter, ReallyGoodCat.counter)
        self.__class__.counter += 1

    @classmethod
    def number_of_cats(cls):
        return cls.counter

class ReallyGoodCat(GoodCat):
    pass

cat1 = GoodCat()
print(GoodCat.counter, ReallyGoodCat.counter)
cat2 = GoodCat()
print(GoodCat.counter, ReallyGoodCat.counter)
cat3 = ReallyGoodCat()
print(GoodCat.counter, ReallyGoodCat.counter)

print(GoodCat.number_of_cats())        # 2
print(GoodCat.counter)                 # 2
print(ReallyGoodCat.number_of_cats())  # 3
print(ReallyGoodCat.counter)           # 3