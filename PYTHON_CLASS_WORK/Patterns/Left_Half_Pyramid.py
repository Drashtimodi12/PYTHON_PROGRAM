#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# This program prints a right-angled triangle pattern aligned to the right

lines = 5  # Number of rows
stars = 1  # Initial number of stars
space = lines - 1  # Initial number of spaces

for i in range(lines):  # Loop for rows
    for k in range(space):  # Loop for printing spaces
        print(" ", end=" ")  # Print space
    for j in range(stars):  # Loop for printing stars
        print("*", end=" ")  # Print star with space
    print()  # Move to the next line
    stars += 1  # Increase the number of stars in the next row
    space -= 1  # Decrease spaces to shift the stars towards the left
