words = "sun Rises in east"

# Converts the first character to uppercase and the rest to lowercase
print(words.capitalize())  # Output: "Sun rises in east"

# Converts all characters to lowercase, similar to lower() but more aggressive in handling special cases
print(words.casefold())  # Output: "sun rises in east"

# Returns the total number of characters in the string, including spaces
print(len(words))  # Output: 18

# Centers the string in a field of width 19, padding it with '*'
print(words.center(27, '*'))  # Output: "*sun Rises in east*"

# Counts the occurrences of 's' in the substring from index 0 to 7
print(words.count('s', 0, 7))  # Output: 2

# Checks if the substring from index 0 to 9 ends with 'es'
print(words.endswith('es', 0, 9))  # Output: True

# Checks if the substring from index 0 to 2 starts with 'S'
print(words.startswith('S', 0, 2))  # Output: False (because it's 's', not 'S')

# Searches for 'k' in the substring from index 3 to 9; returns -1 if not found
print(words.find('k', 3, 9))  # Output: -1 (since 'k' is not present)

# Searches for 'k' in the substring from index 3 to 9; raises ValueError if not found
# Uncommenting the next line will cause an error because 'k' is not present in the given range
# print(words.index('k', 3, 9))  # Output: ValueError: substring not found

# Checks if all characters in the string are alphanumeric (letters and numbers only)
print("abc123".isalnum())   # Output: True

# Checks if all characters in the string are alphabetic (letters only)
print('abc12'.isalpha())  # Output: False (because it contains numbers)

# Checks if all characters in the string are digits
print("212".isdigit())  # Output: True

# Checks if the string is a valid Python identifier (variable name)
print("123abc".isidentifier())  # Output: False (identifiers cannot start with a number)

# Checks if all characters are lowercase
print("Str".islower())  # Output: False (contains an uppercase letter)

# Checks if the first letter of each word is uppercase (Title Case)
print("Tbc".istitle())  # Output: True

# Checks if all characters are uppercase
print("ABC".isupper())  # Output: True

# Joins the given string "123" with "Hello" between each character
print("Hello".join("123"))  # Output: "1Hello2Hello3"

# Left justifies the string within 50 characters, padding with '*'
print(words.ljust(50, '*'))  
# Output: "sun Rises in east*********************************"

# Splits the string into three parts: before, the matched string, and after
print(words.partition("k"))  
# Output: ('sun Rises in east', '', '') (since 'k' is not present, the entire string is returned)

# Replaces all occurrences of 's' with 'k'
print(words.replace('s', "k"))      # Output: "kun Rikek in eakt"

# Splits the string at each occurrence of 's'
print(words.split("s"))     # Output: ['', 'un Ri', 'e', ' in ea', 't']

# Swaps uppercase letters to lowercase and vice versa
print("Tops".swapcase())  # Output: "tOPS"

# Accessing a single character from index 4 (0-based indexing)
print(words[4])  # Output: 'R'

# Accessing the fourth character from the end
print(words[-4])  # Output: 'e'

# Slicing from index 4 to 9, with a step of 3
print(words[4:9:3])  # Output: 'R ' (Characters at index 4 and 7)

# Slicing from the fourth-last to the second-last character
print(words[-4:-1])  # Output: 'eas'