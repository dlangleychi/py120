class Car:

    @classmethod
    def print_average_mpg(cls, distance_traveled, fuel_burned):
        mpg = distance_traveled / fuel_burned
        print(f'average miles per gallon: {mpg}')

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self.color = color
        self.speed = 0

    def engine_start(self):
        print('The engine is on!')

    def engine_off(self):
        self.speed = 0
        print("Let's park this baby!")
        print('The engine is off!')

    def speed_up(self, number):
        self.speed += number
        print(f'You accelerated {number} mph.')

    def brake(self, number):
        self.speed -= number
        print(f'You decelerated {number} mph.')

    def get_speed(self):
        print(f'Your speed is {self.speed} mph.')

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('Color must be a string')

        self._color = color
    
    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year

    def spray_paint(self, color):
        self.color = color

    def __str__(self):
        return f'{self.color.title()} {self.year} {self.model}'
    
    def __repr__(self):
        return f'Car({repr(self.model)}, {self.year}, {repr(self.color)})'

vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')
    
# Car.print_average_mpg(100, 10) # average miles per gallon: 10


# lumina = Car('chevy lumina', 1997, 'white')

# type(lumina).print_average_mpg(100, 10) # average miles per gallon: 10

# print(lumina.color) # white
# lumina.spray_paint('pink')
# print(lumina.color) # pink
# lumina.spray_paint(4) # TypeError: Color must be a string

# print(lumina.color) # white
# lumina.color = 'green'
# print(lumina.color) # green
# print(lumina.model) # chevy lumina
# print(lumina.year) # 1997
# lumina.model = 'jeep wrangler' # AttributeError: property 'model' of 'Car' object has no setter
# lumina.year = 2025 # AttributeError: property 'year' of 'Car' object has no setter


# lumina.engine_start() # The engine is on!
# lumina.get_speed()    # Your speed is 0 mph.
# lumina.speed_up(20)   # You accelerated 20 mph.
# lumina.get_speed()    # Your speed is 20 mph.
# lumina.speed_up(30)   # You accelerated 30 mph.
# lumina.get_speed()    # Your speed is 50 mph.
# lumina.brake(15)      # You decelerated 15 mph.
# lumina.get_speed()    # Your speed is 35 mph.
# lumina.brake(30)      # You decelerated 30 mph.
# lumina.get_speed()    # Your speed is 5 mph.
# lumina.engine_off()   # Let's park this baby!
#                       # The engine is off
# lumina.get_speed()    # Your speed is 0 mph.