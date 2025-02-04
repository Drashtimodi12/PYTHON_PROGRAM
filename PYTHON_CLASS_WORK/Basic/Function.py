# Print with raw string (r prefix ignores escape sequences)
print(r"python is \" oops lang.")   # Output: python is " oops lang.

name = input("Enter name : ")   # User enters a name
print(name)     # Output: User input name

# Taking integer input
a =int(input("enter number 1: "))   # Convert input to integer
b =int(input("enter number 2: "))    # Convert input to integer

print(a+b)      # Addition of two numbers
print(int(a)+int(b))    # Another way of addition (redundant type conversion)

# Type conversion example
a = "100O"  # String containing invalid integer
# b = int(a)  # This will raise a ValueError since "100O" is not a valid integer
print(type(a))  # Output: <class 'str'>
# print(type(b))  # This line will not execute due to the error above

# String split example
name = "Tops technologies pvt ltd".split()  # Splitting string into list
print(name)     # Output: ['Tops', 'technologies', 'pvt', 'ltd']
name = "Tops technologies pvt ltd".split("o")  # Splitting string into list
print(name)     # Output: ['T', 'ps techn', 'l', 'gies pvt ltd']

# String formatting example
fname = "Farukh"
lname = "Shaikh"
# Using format method
print("my name is {1} and my surname is {0}".format(fname,lname))   # Output: my name is Shaikh and my surname is Farukh
# Using f-string
print(f"my name is {fname} and surname is {lname}")     # Output: my name is Farukh and surname is Shaikh