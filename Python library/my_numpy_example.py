# Import the NumPy library
import numpy as np

# Create a simple array
my_array = np.array([1, 2, 3, 4, 5])
print("Array:", my_array)

# Perform operations on the array
print("Array * 2:", my_array * 2)         # Multiply each element by 2
print("Mean:", np.mean(my_array))        # Calculate the average of the array
print("Square Roots:", np.sqrt(my_array))  # Calculate the square root of each element

#🎲 Practice Task (NumPy)

# Import the NumPy library
import numpy as np

# Create an array with numbers from 10 to 50
array = np.arange(10, 51)  # Creates an array with values from 10 to 50
print("Array:", array)

# Find the maximum and minimum values
print("Maximum value:", np.max(array))  # Finds the maximum value
print("Minimum value:", np.min(array))  # Finds the minimum value

# Multiply all elements by 3
multiplied_array = array * 3
print("Array multiplied by 3:", multiplied_array)
