# Using with open() (Best Practice)
# Automatically closes the file after execution.
# Safer than open() and close().

with open("Test.txt", "r") as file:
    content = file.read()  # Read entire file
    print(content)  # Print content

# Output:
# Test.txt  --- Read file and automatically close file
# Python Program
# Java Program
