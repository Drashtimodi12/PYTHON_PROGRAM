class Sample:
    def show(self):
        print("Sample show calling")

class Demo:
    # Aggregation: Demo class has a Sample class instance
    s = Sample()

# Create an instance of Demo
d = Demo()
# Access the Sample instance through the Demo instance and call the show method
d.s.show()