class A:
    def disp(self):
        print("Class A disp method calling")

class B(A):
    def disp(self):
        print("Class B disp method calling")

# Create an instance of class B
b = B()
# Call the disp method
b.disp()

# Output:
# Class B disp method calling