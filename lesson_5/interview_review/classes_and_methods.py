class Person:
    def __init__(self, first, last):
        self.name = (first, last)

    @property
    def name(self):
        return f'{self._first} {self._last}'
    
    @name.setter
    def name(self, name):
        first, last = name

        if not first.isalpha() or not last.isalpha():
            raise ValueError('Name must be alphabetic.')
        
        self._first = first
        self._last = last

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