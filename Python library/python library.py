1. Understanding Python Libraries
What is a Python Library?
A Python library is a collection of pre-written code that simplifies programming by providing reusable functions.
Think of it as a toolbox 📦 that contains tools to make your programming tasks easier.

2. How to Use a Library in Python
2.1 Importing a Built-in Library
Python comes with many built-in libraries that you can use without installing anything.

Example: Using the math library

Python
# Import the math library
import math

# Using functions from the math library
print("Square root of 16:", math.sqrt(16))  # Output: 4.0
print("Value of pi:", math.pi)             # Output: 3.141592653589793
2.2 Importing Part of a Library
You can import only the specific functions you need to keep your code cleaner.

Example: Importing specific functions from math

Python
# Import specific functions from the math library
from math import sqrt, sin, radians, pow

# Using the imported functions
print("Square root of 36:", sqrt(36))           # Output: 6.0
print("Sine of 90 degrees:", sin(radians(90)))  # Output: 1.0
print("Power of 2 raised to 3:", pow(2, 3))     # Output: 8.0
2.3 Using the random Library
The random library is used to generate random numbers or make random choices.

Example: Generating random numbers and making random choices

Python
# Import the random library
import random

# Generate random numbers and choices
print("Random number between 1 and 10:", random.randint(1, 10))  # Random integer
print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))  # Random item
2.4 Using the datetime Library
The datetime library helps you work with dates and times.

Example: Getting the current date and time

Python
# Import the datetime library
import datetime

# Get today's date
today = datetime.date.today()
print("Today's date is:", today)  # Output: e.g., 2025-04-27

# Get the current time
now = datetime.datetime.now()
print("Current time:", now.strftime("%H:%M:%S"))  # Output: e.g., 10:06:28
3. Practice Tasks
Math library:
Calculate the hypotenuse of a right triangle with legs 3 and 4 using math.sqrt().

Random library:
Create a random password generator that picks 8 characters randomly from a list of letters, numbers, and symbols.

Datetime library:
Display how many days are left until your next birthday.

Let me know if you'd like me to write code for these practice tasks or add more examples! 🚀
