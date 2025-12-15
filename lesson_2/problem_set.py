class Person:
    def __init__(self, name):
        self.name = name

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, new_first_name):
        if not isinstance(new_first_name, str):
            raise TypeError('Need string')
        
        self._first_name = new_first_name

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, new_last_name):
        if not isinstance(new_last_name, str):
            raise TypeError('Need string')
        
        self._last_name = new_last_name

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    @name.setter
    def name(self, new_name):
        new_name_list = new_name.split()
        self.first_name = new_name_list[0]
        self.last_name = ''
        if len(new_name_list) > 1:
            self.last_name = new_name_list[1]

    def __str__(self):
        return self.name

# bob = Person('bob')
# print(bob.name)           # bob
# bob.name = 'Robert'
# print(bob.name)           # Robert

# bob = Person('Robert')
# print(bob.name)             # Robert
# print(bob.first_name)       # Robert
# print(repr(bob.last_name))  # ''
# bob.last_name = 'Smith'

# bob = Person('Robert')
# print(bob.name)             # Robert
# print(bob.first_name)       # Robert
# print(repr(bob.last_name))  # ''
# bob.last_name = 'Smith'
# print(bob.name)             # Robert Smith

# bob.name = 'Prince'
# print(bob.first_name)       # Prince
# print(repr(bob.last_name))  # ''

# bob.name = 'John Adams'
# print(bob.first_name)       # John
# print(bob.last_name)        # Adams

# bob = Person('Robert Smith')
# rob = Person('Robert Smith')
# print(bob.name == rob.name)

bob = Person('Robert Smith')
print(f"The person's name is: {bob}")

'''
Predict output is: The person's name is: type Person object at 0x...
'''

'''
Predict output is: The person's name is: Robert Smith
'''