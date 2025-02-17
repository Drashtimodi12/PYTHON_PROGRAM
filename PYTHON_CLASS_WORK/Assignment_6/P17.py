# 17.	Write a generator function that generates the first 10 even numbers.

# Loop through numbers from 1 to 10
for i in range(1, 11):  
    # Check if the number is even
    if i % 2 == 0:  
        print(i, 'Even')  # Print the number as Even
    else:  
        print(i, 'Odd')  # Print the number as Odd