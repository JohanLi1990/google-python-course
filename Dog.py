class Dog:
    '''
    a simple attempt at modeling dog
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name} is now sitting")
        
    def roll_over(self):
        print(f"{self.name} rolled over")
        
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 50
    
    def get_descriptive_name(self):
        return f"{super().get_descriptive_name()} (Electric)"
    
    def describe_battery(self):
        print(f"this car has a {self.battery_size}-kwh battery")
 
        
# my_dog = Dog('Willie', 6)
# my_dog.roll_over()
my_car = Car('Toyota', 'Sienta', 1956)
my_car.read_odometer()
my_laef = ElectricCar('nissan', 'leaf', 2024)
print(my_laef.get_descriptive_name())