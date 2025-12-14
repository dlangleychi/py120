class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def first(self):
        return self._first
    
    @first.setter
    def first(self, first):
        if not isinstance(first, str):
            raise TypeError('Name must be type str.')
        if not first.isalpha():
            raise ValueError('Name must be alphabetic.')
        self._first = first.title()

    @property
    def last(self):
        return self._last
    
    @last.setter
    def last(self, last):
        if not isinstance(last, str):
            raise TypeError('Name must be type str.')
        if not last.isalpha():
            raise ValueError('Name must be alphabetic.')
        self._last = last.title()

    @property
    def name(self):
        return self._first + ' ' + self._last
    
    @name.setter
    def name(self, pair):
        self.first, self.last = pair

# actor = Person('Mark', 'Sinclair')
# print(actor.name)              # Mark Sinclair
# actor.name = ('Vin', 'Diesel')
# print(actor.name)              # Vin Diesel
# actor.name = ('', 'Diesel')
# # ValueError: Name must be alphabetic.

# character = Person('annIE', 'HAll')
# print(character.name)          # Annie Hall
# character = Person('Da5id', 'Meier')
# # ValueError: Name must be alphabetic.

friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.