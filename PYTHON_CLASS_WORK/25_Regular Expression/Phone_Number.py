import re   #The re module provides support for regular expressions in Python.

# Define a regex pattern to match a 10-digit number
p = "^[0-9]{10}$"

# Use re.match() to check if the string "9909449049" matches the pattern
r = re.match(p, "9909449049")

# If the match is None, the number is invalid
if r is None :
    print("Invalid Number.")
else :
    # If the match is not None, the number is valid
    print("Valid Number.")
