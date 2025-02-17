# Loop from 0 to 9 (10 numbers)
for i in range(10) :
    print(i)    # Output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

print("------------")  # Separator for clarity

# Loop from 1 to 9 (Starts at 1, stops before 10)
for i in range(1,10) :
    print(i)    # Output: 1, 2, 3, 4, 5, 6, 7, 8, 9

print("------------")  # Separator for clarity

# Loop from 5 to 14 (Starts at 5, stops before 15)
for i in range(5,15) :
    print(i)    # Output: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14

print("------------")  # Separator for clarity

# Loop from 1 to 100 with step size 5 (Increments by 5) 
for i in range(1,100,5) :
    print(i)    # Output: 1, 6, 11, 16, 21, ..., 96

print("------------")  # Separator for clarity

# Loop from 10 down to 1 (Decrementing by -1)
for i in range(10,0,-1) :
    print(i)    # Output: 10, 9, 8, 7, 6, 5, 

print("------------")  # Separator for clarity

# Loop through elements of a list
l = [10,3,40,6,33,50]
for i in l :
    print(i)    # Output: 10,3,40,6,33,50