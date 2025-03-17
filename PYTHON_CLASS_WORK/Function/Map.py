# Using map() Function:- The map() function applies a function to each item in an iterable (e.g., list) and returns a new list.

# Understanding the map() Function with square() Function
# Function to calculate the square of a number
def square(a) :
    b = int(a)      # Convert input to integer
    return b * b    # Return square of the number

# Using a for loop to apply square() on a list
l = [10, 20, 30, 4]
l1 = []         # Create an empty list
for i in l :
    k = square(i)       # Call square function for each element
    l1.append(k)        # Append the squared value to l1
print(l1)       # Output: [100, 400, 900, 16]

# Using map() to apply square() on a list
l1 = map(square, l)     # map() applies square() to each element in l
print(list(l1))         # Output: [100, 400, 900, 16]
    
# Using map() with user input
l1 = list(map(square, input("Enter list of number: ").split()))
print(l1)
# Output: Enter list of number: 2 7 0 10 3
# [4, 49, 0, 100, 9]