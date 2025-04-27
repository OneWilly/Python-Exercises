# Import the necessary module for file handling
import os

# Step 1: Create a file called 'input.txt' and write at least five lines of text into it
with open("input.txt", "w") as input_file:  # Open 'input.txt' in write mode
    # Write five lines of text to the file
    input_file.write("This is the first line.\n")
    input_file.write("Here is the second line.\n")
    input_file.write("The third line is right here.\n")
    input_file.write("Line number four comes next.\n")
    input_file.write("Finally, this is the fifth line.\n")

# Step 2: Read the contents of 'input.txt'
with open("input.txt", "r") as input_file:  # Open 'input.txt' in read mode
    content = input_file.read()  # Read all the contents of the file

# Step 3: Count the number of words in the file
word_count = len(content.split())  # Split the content into words and count them

# Step 4: Convert all text to uppercase
uppercase_content = content.upper()  # Convert the entire content to uppercase

# Step 5: Write the processed text and the word count to a new file called 'output.txt'
with open("output.txt", "w") as output_file:  # Open 'output.txt' in write mode
    output_file.write(uppercase_content)  # Write the uppercase text to the file
    output_file.write(f"\n\nWord Count: {word_count}\n")  # Write the word count below the text

# Step 6: Print a success message once the new file is created
print("The file 'output.txt' has been successfully created with the processed content!")