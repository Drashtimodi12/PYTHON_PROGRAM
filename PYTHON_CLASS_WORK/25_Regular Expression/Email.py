import re  # The re module provides support for regular expressions in Python.

# Define a regex pattern to match a valid email address
p = "^[A-Za-z0-9]+@[a-z]+\.[a-z]+$"

# Use re.match() to check if the string "drashti33@gmail.com" matches the pattern
r = re.match(p, "drashti33@gmail.com")

# If the match is None, the email is invalid
if r is None:
    print("Invalid Email.")
else:
    # If the match is not None, the email is valid
    print("Valid Email.")