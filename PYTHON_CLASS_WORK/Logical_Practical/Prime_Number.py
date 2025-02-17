# # Define the number to check for prime
# number = 15  

# # Initialize a flag variable to track if the number is prime
# flag = 0  

# # Loop through numbers from 2 to number-1 (because 1 and number itself are not checked)
# for i in range(2, number):  
#     if number % i == 0:  # If number is divisible by any i, it's not prime
#         flag = 1  # Set flag to 1 indicating it's not prime
#         break  # Exit the loop as we found a divisor

# # After the loop, check the flag value
# if flag == 0:  
#     print('Prime Number')  # If flag is still 0, the number is prime
# else:  
#     print('Not Prime Number')  # If flag is 1, the number is not prime



# Loop through numbers from 1 to 100
for num in range(1, 101):  
    # If the number is less than 2, skip it (0 and 1 are not prime numbers)
    if num < 2:  
        continue  # Skip to the next iteration

    # Initialize flag variable to track if num is prime
    flag = 0  

    # Check divisibility from 2 to num-1
    for i in range(2, num):  
        if num % i == 0:  # If num is divisible by i, it's not prime
            flag = 1  # Set flag to 1 indicating it's not prime
            break  # Exit loop early since we found a divisor

    # If flag is still 0 after checking divisibility, it's a prime number
    if flag == 0:  
        print(num, 'is a Prime Number')  # Print the prime number
    else:  
        pass  # Do nothing (optional, just to maintain structure)
