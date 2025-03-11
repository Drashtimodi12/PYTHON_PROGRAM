#     *
#    * *
#   *   *
#    * *
#     *
lines = 5  # Total number of rows in the pattern
stars = 1  # Initial number of stars
space = lines - 1  # Initial number of spaces before the first star
mid = (lines // 2) + 1  # Middle row of the pattern

for i in range(1, lines + 1):  # Outer loop for each row
    for k in range(space):  # Inner loop for printing leading spaces
        print(" ", end="")  # Print space without newline

    for j in range(stars):  # Inner loop for printing stars
        # Print star at the beginning and end of the row, spaces in between
        if j == 0 or j == stars - 1:
            print("*", end="")  # Print star with a space
        else:
            print(" ", end="")  # Print space between boundary stars

    print()  # Move to the next line after printing spaces and stars

    # Adjusting stars and spaces for upper and lower halves
    if i < mid:
        stars += 2  # Increase the number of stars by 2 in the first half
        space -= 1  # Decrease spaces by 1 in the first half
    else:
        stars -= 2  # Decrease the number of stars by 2 in the second half
        space += 1  # Increase spaces by 1 in the second half