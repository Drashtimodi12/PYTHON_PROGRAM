# This program prints a right-aligned triangle pattern using stars
#          * 
#        * * *
#      * * * * *
#    * * * * * * *
#  * * * * * * * * *

# lines = 5  # Number of rows
# stars = 1
# space = lines - 1

# for i in range(lines):
#     for k in range(space):  # Printing spaces
#         print(" ", end=" ")

#     for j in range(stars):  # Printing stars
#         print("*", end=" ")

#     print()  # Move to the next line
#     stars += 2  # Increase the number of stars by 2 each row
#     space -= 1  # Decrease spaces by 1



#     *
#    * *
#   * * *
#  * * * *
# * * * * *


lines = 5  # Number of rows in the pattern
stars = 1  # Initial number of stars
space = lines - 1  # Initial number of spaces before stars

for i in range(lines):  # Outer loop to control the number of rows
    for k in range(space):  # Inner loop for printing leading spaces
        print(" ", end="")  # Print space without a newline
    for j in range(stars):  # Inner loop for printing stars
        print("*", end=" ")  # Print a star followed by a space
    print()  # Move to the next line after printing spaces and stars
    stars += 1  # Increase the number of stars for the next row
    space -= 1  # Decrease the number of spaces to shift stars right