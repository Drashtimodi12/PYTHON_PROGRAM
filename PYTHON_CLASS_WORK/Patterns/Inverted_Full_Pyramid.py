# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

lines = 5  # Number of rows
stars = 9  # Initial number of stars
space = 0  # Initial space

for i in range(lines):
    for k in range(space):  # Printing spaces
        print(" ", end=" ")

    for j in range(stars):  # Printing stars
        print("*", end=" ")

    print()  # Move to the next line
    stars -= 2  # Decrease the number of stars by 2 each row
    space += 1  # Increase spaces by 1
