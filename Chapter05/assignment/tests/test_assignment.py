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
