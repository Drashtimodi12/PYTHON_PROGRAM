# Arithmetic Operators: +, -, *, /, %, **, //

print(10 + 10)    # Addition: Adds two numbers (10 + 10 = 20)

print("a" + "b")  # String concatenation: Joins two strings ('a' + 'b' = 'ab')

# print("a" + 10)   # This will cause a TypeError because you cannot add a string and an integer directly.

a = 10 + 10.00    # Mixing int and float results in a float (implicit type conversion)
print(type(a))  # Output: <class 'float'>
print(a)        # Output: 20.0

print(10 % 3)     # Modulus: Returns the remainder of 10 ÷ 3 (10 % 3 = 1)

print(10 ** 2)    # Exponentiation: Raises 10 to the power of 2 (10^2 = 100)

print(16 // 3)    # Floor Division: Returns the quotient without the decimal part (16 // 3 = 5)

# Using variables for arithmetic operations
x = 10
y = 3

print(x + y)  # Addition: 10 + 3 = 13
print(x - y)  # Subtraction: 10 - 3 = 7
print(x * y)  # Multiplication: 10 * 3 = 30
print(x / y)  # Division: 10 / 3 = 3.3333 (returns a float)
print(x // y)  # Floor Division: 10 // 3 = 3 (returns only the integer part)
print(x % y)  # Modulus: Returns the remainder of 10 ÷ 3 (10 % 3 = 1)
print(x ** y)  # Exponentiation: Raises 10 to the power of 3 (10^3 = 1000)