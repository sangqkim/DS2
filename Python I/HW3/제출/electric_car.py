from car import Car
class Battery():
    def __init__(self, battery_size=60):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
class ElectricCar(Car):
    
    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        The initialize attributes specific to an electirc car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()