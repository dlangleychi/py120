class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    @staticmethod
    def engine_start():
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

lumina = Car('chevy lumina', 1997, 'white')
lumina.engine_start() # The engine is on!
lumina.get_speed()    # Your speed is 0 mph.
lumina.speed_up(20)   # You accelerated 20 mph.
lumina.get_speed()    # Your speed is 20 mph.
lumina.speed_up(30)   # You accelerated 30 mph.
lumina.get_speed()    # Your speed is 50 mph.
lumina.brake(15)      # You decelerated 15 mph.
lumina.get_speed()    # Your speed is 35 mph.
lumina.brake(30)      # You decelerated 30 mph.
lumina.get_speed()    # Your speed is 5 mph.
lumina.engine_off()   # Let's park this baby!
                      # The engine is off
lumina.get_speed()    # Your speed is 0 mph.