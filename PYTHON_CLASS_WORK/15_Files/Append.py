# Appending to a File ("a" mode)
# The "a" mode adds new content to the file without deleting the existing data.
# If the file does not exist, it creates a new file.

file = open("Test.txt", "a")  # Open file in append mode
file.write("\nJava Program")  # Append new text
file.close()  # Close file

# Output:
# Test.txt ---Create File Open and Write Without DELETE any data
# Python Program
# Java Program  
