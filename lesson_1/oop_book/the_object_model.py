class Knight:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'I am {self.name}, an honorable knight')

lancelot = Knight('lancelot')
galahad = Knight('galahad')

lancelot.greet()
galahad.greet()