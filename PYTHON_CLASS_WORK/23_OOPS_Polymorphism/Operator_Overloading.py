class Demo:
    def __init__(self, a, b):
        # Initialize the instance with values a and b
        self.a = a
        self.b = b
    
    def __add__(self, obj):
        # Overload the addition operator
        # Return a tuple with the sum of a and b from both objects
        return self.a + obj.a, self.b + obj.b

    def __mul__(self, obj):
        # Overload the multiplication operator
        # Return a tuple with the product of a and b from both objects
        return self.a * obj.a, self.b * obj.b

# Create two instances of the Demo class
d1 = Demo(10, 20)
d2 = Demo(20, 40)

# Use the overloaded multiplication operator
c = d1 * d2

# Print the result
print(c)  # Output: (200, 800)