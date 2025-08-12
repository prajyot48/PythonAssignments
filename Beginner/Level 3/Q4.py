class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

s = Square(5)
print("Area of square:", s.area())  

sh = Shape()
print("Area of shape:", sh.area())  
