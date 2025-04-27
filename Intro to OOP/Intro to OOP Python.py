# Defining a class
class Car:
    # Attribute: Default color of the car
    color = "red"

    # Method: An action the car can perform
    def drive(self):
        print("The car is driving 🚗")

# Creating an object (instance of the class)
my_car = Car()

# Accessing the attribute of the object
print(f"My car's color is: {my_car.color}")

# Calling the method of the object
my_car.drive()

# Defining a class with attributes and methods
class Car:
    # Constructor to initialize attributes
    def __init__(self, color, brand):
        self.color = color  # Attribute: Color of the car
        self.brand = brand  # Attribute: Brand of the car

    # Method: Action to drive the car
    def drive(self):
        print(f"The {self.color} {self.brand} is driving 🚗")

# Creating objects with specific attributes
car1 = Car("blue", "Toyota")
car2 = Car("black", "Honda")

# Accessing attributes and methods
print(car1.color)  # Output: blue
print(car2.brand)  # Output: Honda

car1.drive()  # Output: The blue Toyota is driving 🚗
car2.drive()  # Output: The black Honda is driving 🚗
