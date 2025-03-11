# Local Scope → Variables inside a function are local by default.
# Global Scope → Variables outside functions are global.


a = 20      # Global Variable

def test() :
    #global a       # Uncomment this line to modify the global variable
    a = 50
    a += 20
    print(a)        # Output: 70 (local scope)

print("Before: ", a)        # Output: before: 20 (global scope)
test()
print("After: ", a)         # Output: after: 20 (global scope)


# global Keyword → Needed if you want to modify a global variable inside a function.

a = 20      # Global Variable

def test() :
    global a       # Accessing the global variable
    a = 50         # Modifying global variable
    a += 20
    print(a)        # Output: 70 (modifies global a)

print("Before: ", a)        # Output: before: 20
test()
print("After: ", a)         # Output: after: 70