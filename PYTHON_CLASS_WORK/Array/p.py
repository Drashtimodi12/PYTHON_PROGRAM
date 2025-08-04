arr = [10, 25, 5, 80, 40]
# arr.remove(max(arr))    
print(max(arr))
print(arr[::-1])

# Sort the array in ascending order
arr.sort()
print(arr)

# Sort the array in descending order
arr.sort(reverse=True)    
print(arr)

print(sum(arr))


num = [10, 25, 5, 80, 40]

for i in num:
    if i % 2 == 0:
        print(i, "is even" )
    else:
        print(i, "is odd")




a = [1, 2, 3, 4, 5, 6]
even = odd = 0
for num in a:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even, "Odd:", odd)