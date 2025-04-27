# Parent class
class Vehicle:
    # Constructor for the parent class
    def __init__(self, wheels):
        self.wheels = wheels  # Attribute for the number of wheels

    def drive(self):
        print("The vehicle is driving!")

# Subclass inheriting from Vehicle
class Car(Vehicle):
    # Constructor for the subclass
    def __init__(self, wheels, brand):
        super().__init__(wheels)  # Call the parent class constructor
        self.brand = brand  # Additional attribute specific to Car

    # Overriding the drive method
    def drive(self):
        print(f"The {self.brand} car is driving on {self.wheels} wheels!")

# Creating an object of the Car subclass
car = Car(4, "Toyota")
car.drive()  # Output: The Toyota car is driving on 4 wheels!



#Polymorphism Example
# Base class
class Animal:
    # Base class method to be overridden
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass implementing its own version of speak
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Subclass implementing its own version of speak
class Cat(Animal):
    def speak(self):
        return "Meow!"

# Demonstrating polymorphism
animals = [Dog(), Cat()]  # List of Dog and Cat objects
for animal in animals:
    print(animal.speak())
# Output:
# Woof!
# Meow!

#Encapsulation Example
# Class demonstrating encapsulation
class SecretStash:
    def __init__(self):
        self.__chocolates = 10  # Private attribute (note the double underscores)

    # Public method to take a chocolate
    def take_chocolate(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print("One chocolate taken!")
        else:
            print("No chocolates left 😢")

    # Private method to replenish chocolates
    def __replenish(self):
        self.__chocolates = 10
        print("Chocolates replenished!")

    # Public method to trigger the private replenish method
    def ask_replenish(self):
        self.__replenish()

# Example usage of the class
stash = SecretStash()
stash.take_chocolate()  # Output: One chocolate taken!
stash.ask_replenish()   # Output: Chocolates replenished!



