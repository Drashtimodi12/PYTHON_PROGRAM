
fruits = ("apple", "banana", "cherry")
(a,*b) = fruits
print(b)        # Output: 





# Converting tuple to list, modifying it, and converting back to tuple
l = list(t)  # Convert tuple to list
l.append("SQL")  # Add an element
t = tuple(l)  # Convert back to tuple
print("Modified Tuple:", t)

# Concatenating two tuples
x = ("test", "tech")
y = ("abc", "xyz")
x += y  # Concatenation
print("Concatenated Tuple:", x)

# Tuple unpacking
fruits = ("apple", "banana", "cherry")
(a, *b) = fruits  # Assigns 'a' to first element, 'b' gets the remaining as a list
print("Unpacked values:", b)

# Iterating over a tuple
for i in fruits:
    print("Fruit:", i)

# Iterating using index
for i in range(len(fruits)):
    print("Fruit at index", i, ":", fruits[i])

# Tuple operations
t1 = (10, 20, 30)
t2 = (80, 90, 70)

# Concatenating tuples
t3 = t1 + t2
print("Concatenated Tuple:", t3)

# Repeating tuple elements
t3 = t1 * 3
print("Repeated Tuple:", t3)
