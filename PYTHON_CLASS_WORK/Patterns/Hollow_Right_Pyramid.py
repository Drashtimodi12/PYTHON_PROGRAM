# *
# * *
# *  *
# *   *
# *  *
# * *
# *

lines = 7  # Total number of rows in the pattern
stars = 1  # Initial number of stars
space = 0  # Initial number of spaces before the first star
mid = (lines // 2) + 1  # Middle row of the pattern

for i in range(1, lines + 1):  # Loop through each row
    for k in range(space):  # Loop to print leading spaces
        print(" ", end="")  # Print spaces before the stars

    for j in range(stars):  # Loop to print stars and spaces between them
        # Print '*' at the first and last position, spaces in between
        if j == 0 or j == stars - 1:
            print("*", end="")  # Print star
        else:
            print(" ", end="")  # Print space between boundary stars

    print()  # Move to the next line after printing spaces and stars

    # Adjusting the number of stars and spaces
    if i < mid:
        stars += 2  # Increase the number of stars by 2 in the upper half
        space -= 1  # Decrease spaces by 1 in the upper half
    else:
        stars -= 2  # Decrease the number of stars by 2 in the lower half
        space += 1  # Increase spaces by 1 in the lower half