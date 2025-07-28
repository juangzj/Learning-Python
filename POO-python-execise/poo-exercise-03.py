class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(f"The area is: {self.width*self.height}")


rectangle_1 = Rectangle(20, 2)

rectangle_1.area()
