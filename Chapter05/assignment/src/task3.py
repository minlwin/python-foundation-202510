# task3.py
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def move(self):
        return "Moving..."

# TODO: Create Car subclass, override move() -> "Car driving..."
class Car(Vehicle):
    pass

# TODO: Create Bike subclass, override move() -> "Bike riding..."
class Bike(Vehicle):
    pass