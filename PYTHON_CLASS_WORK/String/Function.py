words = "sun Rises in east"

# Converts the first character to uppercase and the rest to lowercase
print(words.capitalize())  # Output: "Sun rises in east"

# Converts all characters to lowercase, similar to lower() but more aggressive in handling special cases
print(words.casefold())  # Output: "sun rises in east"

# Returns the total number of characters in the string, including spaces
print(len(words))  # Output: 18

# Centers the string in a field of width 19, padding it with '*'
print(words.center(19, '*'))  # Output: "*sun Rises in east*"

# Counts the occurrences of 's' in the substring from index 0 to 7
print(words.count('s', 0, 7))  # Output: 2

# Checks if the substring from index 0 to 9 ends with 'es'
print(words.endswith('es', 0, 9))  # Output: True

# Checks if the substring from index 0 to 2 starts with 'S'
print(words.startswith('S', 0, 2))  # Output: False (because it's 's', not 'S')

# Searches for 'k' in the substring from index 3 to 9; returns -1 if not found
print(words.find('k', 3, 9))  # Output: -1 (since 'k' is not present)

# Searches for 'k' in the substring from index 3 to 9; raises ValueError if not found
print(words.index('k', 3, 9))  # Output: ValueError: substring not found
