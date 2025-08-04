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