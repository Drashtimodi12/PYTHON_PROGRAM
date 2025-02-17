#  Identity Operator: is, is not

# 1. Using `is` operator
a = 10
b = 10
print(a is b)   # True (Both refer to the same integer object in memory)

# 2. Using `is not` operator
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)   # False (Different lists, different memory locations)
print(x is not y)   # True (Since they are different objects)
print(z is x)   # True 

# 3. Checking with None
z = None
print(z is None)   # True (None is a special object in Python)