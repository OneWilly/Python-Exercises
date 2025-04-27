# Import the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Task 1: Create a NumPy array of numbers from 1 to 10 and calculate the mean
num_array = np.arange(1, 11)  # Array from 1 to 10
mean_value = np.mean(num_array)
print(f"Mean of the array: {mean_value}")

# Task 2: Load a small dataset into a pandas DataFrame and display summary statistics
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Score': [85, 90, 95]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)
print("\nSummary Statistics:")
print(df.describe())

# Task 3: Fetch data from a public API using requests and print a key piece of information
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:  # Check if the request was successful
    json_data = response.json()
    print("\nData fetched from API:")
    print(f"Title: {json_data['title']}")
else:
    print("Failed to fetch data from API")

# Task 4: Plot a simple line graph using matplotlib
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker='o', label='y = 2x')
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid()
plt.show()
