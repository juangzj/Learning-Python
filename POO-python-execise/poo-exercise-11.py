# Author:"juanjgz"
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        area_rectangle = self.base * self.height
        return area_rectangle


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area_circle = math.pi * (self.radius**2)
        return area_circle


rectangle01 = Rectangle(2, 4)
rectangle_area = rectangle01.area()
print(f"The rectangle is {rectangle_area}")


circle01 = Circle(5)
circle01_area = circle01.area()
print(f"The circle area is {circle01_area}")
