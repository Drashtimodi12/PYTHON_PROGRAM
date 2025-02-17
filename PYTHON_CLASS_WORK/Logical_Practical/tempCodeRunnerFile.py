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