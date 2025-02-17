# *
# * *
# * * *
# * * * *
# * * * * *

# lines = 5  # Number of rows

# for i in range(lines):  # Outer loop for rows
#     for j in range(i + 1):  # Inner loop for columns (increases with each row)
#         print("*", end=" ")  # Print star with space
#     print()  # Move to the next line after each row


lines = 5  # Number of rows
stars = 1  # Initial number of stars

for i in range(lines):  # Outer loop for rows
    for j in range(stars):  # Inner loop for columns (printing stars)
        print("*", end=" ")  # Print star with space
    print()  # Move to the next line after each row
    stars += 1  # Inc



# 1
# 12
# 123
# 1234
# 12345

# lines = 5  # Number of rows

# for i in range(1, lines + 1):  # Loop through rows
#     for j in range(1, i + 1):  # Print numbers from 1 to i
#         print(j, end="")  # Print without newline
#     print()  # Move to the next line after each row



# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11 12 13 14 15

# lines = 5  # Number of rows
# num = 1  # Starting number

# for i in range(1, lines + 1):  # Loop through rows
#     for j in range(i):  # Loop to print numbers in each row
#         print(num, end="  ")  # Print number with spacing
#         num += 1  # Increment number
#     print()



# 0
# 10
# 010
# 1010
# 01010

# lines = 5  # Number of rows

# for i in range(1, lines + 1):  # Loop through rows
#     for j in range(i):  # Loop through columns
#         print((i + j) % 2, end="")  # Print alternating 0 and 1
#     print()  # Move to the next line



# 0
# 01
# 010
# 0101
# 01010
lines = 5  # Number of rows

for i in range(1, lines + 1):  # Loop through rows
    for j in range(i):  # Loop through columns
        print(j % 2, end="")  # Print alternating 0 and 1
    print()  # Move to the next line



# A 
# BC 
# DEF 
# GHIJ 
# KLMNO
lines = 5  # Number of rows
ch = 65  # ASCII value of 'A'

for i in range(1, lines + 1):  # Loop through rows
    for j in range(i):  # Loop through columns
        print(chr(ch), end="")  # Convert ASCII to character and print
        ch += 1  # Move to the next character
    print()  # Move to the next line