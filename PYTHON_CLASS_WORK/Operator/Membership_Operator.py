# Membership Operator: in, Not in

# 1. Using `in` with a string
text = "Hello Python"
print("Python" in text)  # True (Substring "Python" is found in the string)
print("Java" in text)    # False ("Java" is not in the string)

# 2. Using `not in` with a string
print("Java" not in text)  # True (Because "Java" is not present in text)

# 3. Using `in` with a dictionary (checks for keys, not values)
student = {"name": "Alice", "age": 20, "city": "New York"}
print("name" in student)  # True (Key "name" exists in dictionary)
print("Alice" in student)  # False (Checks only keys, not values)

# 4. Using `not in` with a dictionary
print("gender" not in student)  # True (Key "gender" is not present)