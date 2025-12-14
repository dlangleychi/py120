class Cat:
    
    def __init__(self, name):
        self.__name = name

    def greet(self):
        print(f'Hello! My name is {self.__name}!')

kitty = Cat('Sophie')
kitty.greet()

print(dir(kitty))