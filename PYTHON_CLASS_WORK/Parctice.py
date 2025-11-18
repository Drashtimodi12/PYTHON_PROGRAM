# row = 5
# for i in range(0, row+1):
#     print("* "*i)

# for i in range(row, 0, -1):
#     print("* "*i)

# print("-----------")

# for i in range(0, row+1):
#     print("  "*(row-i), "* "*i)

# for i in range(row, 0, -1):
#     print("  "*(row-i), "* "*i)

# print("------------")

# for i in range(0, row+1):
#     print(" "*(row-i), "* "*i)

# for i in range(row, 0, -1):
#     print(" "*(row-i), "* "*i)

# print("------------")

# for i in range(0, row+1):
#     print("  "*(row-i), "* "*(2*i-1))

# for i in range(row, 0, -1):
#     print("  "*(row-i), "* "*(2*i-1))

# print("------------")

# for i in range(0, row+1):
#     print("  "*(row-i), "* "*(2*i-1))
# for i in range(row-1, 0, -1):
#     print("  "*(row-i), "* "*(2*i-1))





# num = int(input("Enter Number: "))
# a = 0
# b = 1
# print(f"{a}, {b}, ", end="")

# for i in range(num-2):
#     c = a + b
#     print(f"{c}, ", end="")
#     a = b
#     b = c


# num = int(input("Enter Number: "))
# a = 0
# b = 1
# count = 2
# print(f"{a}, {b}, ", end="")
# while count < num:
#     c = a + b
#     print(f"{c}, ", end="")
#     a=b
#     b=c
#     count += 1






# num = int(input("Enter Number: "))
# a = 1

# if num <= 0:
#     print("Factorial is not defined for zero and negative numbers.")
# else:
#     for i in range(num, 0, -1):
#         a = a * i
# print(f"Factorial of {num} is {a}.")


# num = int(input("Enter Number: "))
# fact =1
# a = num 
# if num <= 0:
#     print("Factorial is not defined for zero and negative numbers.")
# else:
#     while a > 0:
#         fact = fact * a
#         a = a -1
#     print(f"Factorial of {num} is {fact}.")



# a = "POP"
# if a == a[::-1]:
#     print(f"{a} is Palindrome")
# else:
#     print(f"{a} is not Palindrome")

# p = float(input("Enter number in percentage: "))
# if p >= 90:
#     print("A+")
# elif p >=80:
#     print("A")
# elif p >= 75:
#     print("B+")
# elif p >= 70:
#     print("B")
# elif p >= 65:
#     print("C+")
# elif p >= 60:
#     print("c")
# elif p >= 55:
#     print("D+")
# elif p >= 50:
#     print("D")
# elif p < 50:
#     print("F")
# else:
#     print("Invalid Input")






# l = ['apple', 'banana', 'cherry']

# for i in l:
#     if i.startswith('a'):
#         print(i)

# a =0,1,2,3,4,5,6,7,8,9
# for i in a:
#     print(i)

# nums = [5, 8, 2, 10, 7]
# nums.sort()
# print(nums[-2])


# a = "hello python"
# b = a.split(' ')
# c = b[::-1]
# print(" ".join(c))







n = 'hello world'
m = n.split(" ")
print(m, sep = ",")
q = m[::-1]
print(' '.join(q))