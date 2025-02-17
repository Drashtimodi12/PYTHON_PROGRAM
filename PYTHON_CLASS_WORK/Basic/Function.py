# Print with raw string (r prefix ignores escape sequences)
print(r"python is \" oops lang.")   
# The 'r' prefix treats backslashes (\) as literal characters.
# Output: python is \" oops lang.


# Taking string input
name = input("Enter name : ")   # User enters a name
print(name)  # Prints the entered name


# Taking integer input
a = int(input("Enter number 1: "))  # Convert user input to an integer
b = int(input("Enter number 2: "))  # Convert user input to an integer

print(a + b)  # Adds two numbers and prints the result
print(int(a) + int(b))  # Another way of addition (redundant type conversion)


# # Type conversion example
# c = "100"  # String value
# # d = "100O"  # Invalid integer (contains letter 'O')
# # e = int(a)  # This would raise a ValueError since "100O" is not a valid integer

# print(type(c))  # Output: <class 'str'>
# # print(type(d))  # This line will not execute due to the error above


# String split example
name = "Tops technologies pvt ltd".split()      # Splitting the string into a list based on spaces
print(name)     # Output: ['Tops', 'technologies', 'pvt', 'ltd']

name = "Tops technologies pvt ltd".split("o")   # Splitting the string where the letter 'o' appears
print(name)     # Output: ['T', 'ps techn', 'l', 'gies pvt ltd']


# String formatting example
fname = "Farukh"
lname = "Shaikh"
# Using format method
print("my name is {1} and my surname is {0}".format(fname,lname))   # Output: my name is Shaikh and my surname is Farukh
# Using f-string
print(f"my name is {fname} and surname is {lname}")     # Output: my name is Farukh and surname is Shaikh