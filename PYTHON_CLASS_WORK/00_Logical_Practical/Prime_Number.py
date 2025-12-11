# # Define the number to check for prime


# n = int(input("Enter Number to check number is Prime or Not: "))    

for n in range(2, 21):  # Check prime numbers from 2 to 20
    if n > 1:   #   from 2 because 1 is not a prime number
        for i in range(2, n):       # Check factors from 2 to n-1
            if n % i == 0:          # If n is divisible by any i, it's not prime
                print(n, "is not a Prime Number.")
                break
        else:
            print(n, "is a Prime Number.")       # If the loop completes without breaking, it is a prime number
    else:
        print(n, "is not a Prime Number.")       # Numbers less than or equal to 1 are not prime


