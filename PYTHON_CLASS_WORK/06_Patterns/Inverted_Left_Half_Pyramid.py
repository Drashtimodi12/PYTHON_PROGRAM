# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# This program prints an inverted right-angled triangle pattern

lines = 5  # Number of rows
stars = lines  # Initial number of stars in the first row
space = 0  # Initial spaces before stars

for i in range(lines):  # Loop through each row
    for k in range(space):  # Print leading spaces
        print(" ", end=" ")  # Print space without newline

    for j in range(stars):  # Print stars in the current row
        print("*", end=" ")  # Print star with space

    print()  # Move to the next line

    stars -= 1  # Decrease number of stars in each row
    space += 1  # Increase space count in each row
