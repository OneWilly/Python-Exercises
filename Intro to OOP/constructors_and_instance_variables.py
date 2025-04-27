# Defining the Car class
class Car:
    # Constructor to initialize instance variables
    def __init__(self, color, model):
        self.color = color    # Instance variable
        self.model = model    # Instance variable

# Creating objects with unique attributes
car1 = Car("blue", "Sedan")
car2 = Car("red", "SUV")

# Accessing instance variables for each object
print(f"Car 1 is a {car1.color} {car1.model}.")  # Output: Car 1 is a blue Sedan.
print(f"Car 2 is a {car2.color} {car2.model}.")  # Output: Car 2 is a red SUV.
