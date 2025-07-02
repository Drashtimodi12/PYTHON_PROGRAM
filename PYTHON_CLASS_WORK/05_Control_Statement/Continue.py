# Loop through numbers from 0 to 9
for i in range(10):  
    if i == 5:  # Check if i is equal to 5
        continue  # Skip the rest of the loop body and go to the next iteration
    print(i, end=" ")  # Print the value of i if it is not 5

# Output:
# 0 1 2 3 4 6 7 8 9