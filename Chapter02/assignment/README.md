# Chapter 2 Assignment - Variable and Basic Data Types

## 🎯 Instructions

1. You are given Python files with stub functions.
2. Your task is to implement the functions so that all test cases PASS.
3. Run the tests using:(
```
pytest 
```

## 📂 File: src/chapter2.py
```
# Assignment Chapter 2: Variables and Basic Data Types

def create_person(name: str, age: int, height: float, student: bool) -> dict:
    """
    Create a dictionary with keys: name, age, height, student.
    Example: {"name": "Alice", "age": 20, "height": 1.65, "student": True}
    """
    return {}


def age_next_year(age: int) -> int:
    """Return the person's age next year."""
    return 0


def is_adult(age: int) -> bool:
    """Return True if age is >= 18, else False."""
    return False


def format_intro(name: str, age: int) -> str:
    """
    Return a string introduction like:
    'Hello Alice, you are 20 years old.'
    """
    return ""


def favorite_fruits(fruits: list) -> list:
    """
    Add a new fruit 'mango' to the list and return it.
    """
    return []
```

## 📂 File: tests/test_chapter2.py
```
import pytest
from src.chapter2 import create_person, age_next_year, is_adult, format_intro, favorite_fruits


def test_create_person():
    person = create_person("Alice", 20, 1.65, True)
    assert person["name"] == "Alice"
    assert person["age"] == 20
    assert abs(person["height"] - 1.65) < 1e-6
    assert person["student"] is True


def test_age_next_year():
    assert age_next_year(20) == 21
    assert age_next_year(0) == 1


def test_is_adult():
    assert is_adult(20) is True
    assert is_adult(18) is True
    assert is_adult(17) is False


def test_format_intro():
    assert format_intro("Alice", 20) == "Hello Alice, you are 20 years old."
    assert format_intro("Bob", 15) == "Hello Bob, you are 15 years old."


def test_favorite_fruits():
    fruits = ["apple", "banana"]
    result = favorite_fruits(fruits)
    assert "mango" in result
    assert len(result) == 3
```

## ✅ Student’s Goal

- Implement functions in src/chapter2.py
- Run tests
- Ensure all tests PASS