# * * * * *  
# * * * *  
# * * *  
# * *  
# *  

# This program prints an inverted right-angled triangle pattern

lines = 5  # Number of rows
stars = lines  # Initial number of stars in the first row

for i in range(lines):  # Loop through each row
    for j in range(stars):  # Print stars in the current row
        print("*", end=" ")  # Print star with space
    
    print()  # Move to the next line

    stars -= 1  # Decrease the number of stars in each row
