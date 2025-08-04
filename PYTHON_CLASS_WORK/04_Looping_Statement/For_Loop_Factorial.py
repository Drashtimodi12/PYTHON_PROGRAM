# Factorial calculation using for loop : 5!=5*4*3*2*1=120 

number = int(input("Enter a number: "))  # Taking user input
fact = 1

for i in range(number, 0, -1):  # Loop from number to 1
    a = fact * i  # Multiply fact by i

# Using f-string
print(f"Factorial of {number} is {a}")

# Output:
# Enter a number: 5
# Factorial of 5 is 120