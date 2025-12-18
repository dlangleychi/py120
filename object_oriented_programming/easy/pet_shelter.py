class Pet:
    def __init__(self, species, name):
        self._species = species
        self._name = name

    @property
    def species(self):
        return self._species
    
    @property
    def name(self):
        return self._name
    
class Owner:
    def __init__(self, name):
        self._name = name
        self._pets = []

    @property
    def name(self):
        return self._name
    
    def adopt(self, pet):
        self._pets.append(pet)

    def number_of_pets(self):
        return len(self._pets)

    def print_pets(self):
        for pet in self._pets:
            print(f'a {pet.species} named {pet.name}')
    
class Shelter:
    def __init__(self):
        self._owners = []

    def adopt(self, owner, pet):
        if owner not in self._owners:
            self._owners.append(owner)
        owner.adopt(pet)


    def print_adoptions(self):
        for owner in self._owners:
            print(f'{owner.name} has adopted the following pets:')
            owner.print_pets()
            print()

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")