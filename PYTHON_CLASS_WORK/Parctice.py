row = 4
for i in range(1, row+1):
    print("* " *i)

print("-----")

for i in range(row, 0, -1):
    print("* "*i)

print("-----")

for i in range(1, row+1):
    print("  "*(row-i), "* "*i)

print("-----")

for i in range(row, 0, -1):
    print("  "*(row-i), "* "*i)

print("-----")

for i in range(1, row+1):
    print(" "*(row-i), "* "*i)

print("-----")

for i in range(row, 0, -1):
    print(" "*(row-i), "* "*i)

print("-----")

for i in range(1, row+1):
    print("  "*(row-i), "* "*(2*i-1))

print("-----")

for i in range(row, 0, -1):
    print("  "*(row-i), "* "*(2*i-1))
    
print("-----")

for i in range(1, row+1):
    print("  "*(row-i), "* "*(2*i-1))

for i in range(row-1, 0, -1):
    print("  "*(row-i), "* "*(2*i-1))



n = "hello Python"
p =n.split(', ')  # Output: ['hello', 'Python']
q = p[::-1]  # Output: ['Python', 'hello']
print(q.sep(' '))  # Output: 'Python hello'


import copy
lst = [[1], [2]]
shallow = lst[:]
print(shallow)  # Output: [[1], [2]]
deep = copy.deepcopy(lst)   
print(deep)  # Output: [[1], [2]]
