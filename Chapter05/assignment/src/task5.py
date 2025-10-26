# task5.py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# TODO: Implement Circle classe with area() method
class Circle(Shape):

    def __init__(self, radius):
        pass

    def area(self):
        return 0
    
# TODO: Implement Rectangle classe with area() method
class Rectangle(Shape):

    def __init__(self, width, height):
        pass
    
    def area(self):
        return 0

