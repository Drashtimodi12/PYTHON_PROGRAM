# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# This program prints a square pattern of stars
lines = 5  # Number of rows and columns

for j in range(lines):  # Outer loop for rows
    for i in range(lines):  # Inner loop for columns
        print("*", end=" ")  # Print star with space
    print()  # Move to the next line after each row