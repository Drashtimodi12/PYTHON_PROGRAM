# Logical Operator: AND, OR, NOT

a = 10
b = 20

# Logical AND (both conditions must be True)
print(a > 5 and b > 15)  # True (10 > 5 True and 20 > 15 True)
print(a > 5 and b < 15)  # False (10 > 5 True 20 < 15 is False)

# Logical OR (at least one condition must be True)
print(a > 5 or b < 15)  # True (10 > 5 is True, 20 < 15 is False)
print(a < 5 or b < 15)  # False (both 10 < 5 and 20 < 15 are False)

# Logical NOT (reverses the condition)
print(not (a > 5))  # False (10 > 5 is True, but 'not' makes it False)
print(not (b < 15))  # True (20 < 15 is False, but 'not' makes it True)