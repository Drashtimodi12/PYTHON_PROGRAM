# Simple Calculator Program

# Taking user input
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

# Displaying operation choices
print('---Select Operator---')
print('1. Addition (+)')
print('2. Subtraction (-)')
print('3. Multiplication (*)')
print('4. Division (/)')

# Taking user choice
choice = int(input('Enter choice (1/2/3/4): '))

# Performing basic operations
if choice == 1:
    print("Addition:", num1 + num2)
elif choice == 2:
    print("Subtraction:", num1 - num2)
elif choice == 3:
    print("Multiplication:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Error! Cannot divide by zero.")
else:
    print("Invalid choice! Please enter a number between 1 and 4.")


