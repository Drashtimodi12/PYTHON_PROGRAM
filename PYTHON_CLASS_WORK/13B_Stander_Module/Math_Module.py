# math: A standard Python library for mathematical functions.
# The math module provides mathematical functions like power, square root, rounding, and constants like π.

import math

print(math.pow(2,4))         # 2^4 = 16.0
print(math.sqrt(25))         # Square root of 25 = 5.0
print(math.ceil(2.6))        # Rounds up to 3
print(math.floor(2.6))       # Rounds down to 2
print(round(2.4))            # Rounds to nearest integer (2)
print(math.isqrt(15))        # Integer square root of 15 = 3
print(math.sqrt(25).is_integer())  # True (since sqrt(25) is a whole number)
print(math.pi)               # Value of π = 3.141592653589793