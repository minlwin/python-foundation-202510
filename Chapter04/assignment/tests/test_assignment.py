import math
import pytest

from src.assignment import (
    greet,
    circle_area,
    celsius_to_fahrenheit,
    max_of_three,
    is_even,
)


def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_circle_area():
    assert math.isclose(circle_area(1), math.pi, rel_tol=1e-5)
    assert math.isclose(circle_area(2), 4 * math.pi, rel_tol=1e-5)


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212


def test_max_of_three():
    assert max_of_three(1, 2, 3) == 3
    assert max_of_three(10, 5, 7) == 10
    assert max_of_three(-1, -5, -3) == -1


def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
