# Chapter 5 Assighnemt : Class & Object

## 🎯 Objectives
After completing this assignment, students will be able to:

- Explain and demonstrate the concept of classes and objects in Python.
- Define a class and create objects from it.
- Identify and implement components of a class (attributes, methods, constructors).
- Apply OOP concepts: Encapsulation, Inheritance, Polymorphism, Abstraction.
- Write simple programs using classes & objects to solve real-world inspired problems.

## 📌 Assignment Instructions

Students are given function stubs and classes. They must complete the implementation.
Test cases with pytest are provided to validate their solutions.

### Task 1 : Define a Class & Create Objects
```
# scr/task1.py
class Student:
    # TODO: define constructor with name and grade attributes
    def __init__(self, name, grade) -> None:
        pass
    
    # TODO: add a method get_info() that returns "Name: <name>, Grade: <grade>"
    def get_info(self):
        return ""
```

### Task 2 : Encapsulation
```
# scr/task2.py
class BankAccount:
    # TODO: private attribute _balance
    def __init__(self) -> None:
        pass
    
    # TODO: deposit(amount) method (adds to balance)
    def deposit(self, amount):
        pass
    
    # TODO: withdraw(amount) method (subtracts if enough balance)
    def withdraw(self, amount):
        pass 

    # TODO: get_balance() method (returns balance)
    def get_balance(self):
        return 0
```

### Task 3 : 
```
# src/task3.py
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
```

### Task 4
```
# src/task4.py
# Given Vehicle, Car, Bike from Task 3
# TODO: Write a function vehicle_moves(vehicles) 
# that takes a list of Vehicle objects and 
# returns a list of their move() results.
def vehicle_moves(vehicles):
    return []
```

### Task 5
```
# src/task5.py
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
```

## ✅ pytest Test Cases

```
import pytest
from src.task1 import Student
from src.task2 import BankAccount
from src.task3 import Vehicle, Car, Bike
from src.task4 import vehicle_moves
from src.task5 import Circle, Rectangle


def test_task1_student():
    s = Student("Alice", "A")
    assert s.get_info() == "Name: Alice, Grade: A"


def test_task2_bankaccount():
    acc = BankAccount()
    acc.deposit(100)
    acc.withdraw(40)
    assert acc.get_balance() == 60


def test_task3_inheritance():
    v = Vehicle("Generic")
    c = Car("Toyota")
    b = Bike("Yamaha")
    assert v.move() == "Moving..."
    assert c.move() == "Car driving..."
    assert b.move() == "Bike riding..."


def test_task4_polymorphism():
    vehicles = [Car("Honda"), Bike("Suzuki")]
    moves = vehicle_moves(vehicles)
    assert "Car driving..." in moves
    assert "Bike riding..." in moves


def test_task5_abstraction():
    c = Circle(5)        # area = π * r^2
    r = Rectangle(4, 6)  # area = w * h
    assert round(c.area(), 2) == 78.54
    assert r.area() == 24
```
