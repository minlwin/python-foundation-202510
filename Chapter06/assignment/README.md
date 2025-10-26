# Chapter 6 Assighnemt : Organizing Python Codes

## 🎯 Objectives

After completing this assignment, students will be able to:

- Importance of organizing code
- Creating and importing custom modules
- Reusing code with modules
- Building packages with __init__.py
- Best practices in structuring a project

## 📂 Project Structure (given to students)

```
assignment/
│── src/
│   ├── calculator/
│   │   ├── __init__.py
│   │   ├── operations.py
│   │   └── utils.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py
│   └── main.py
│
└── tests/
    ├── test_operations.py
    ├── test_utils.py
    └── test_student.py
```

## 📝 Assignment Tasks

### Assignment 1: Create and Use a Custom Module

Task: In `src/calculator/operations.py`, implement basic math functions:
- `add(a, b)`
- `subtract(a, b)`
- `multiply(a, b)`
- `divide(a, b)` (handle division by zero → raise ValueError)

Test: `tests/test_operations.py` ensures correctness.

### Assignment 2: Utility Functions Module

Task: In `src/calculator/utils.py`, implement:
- `is_even(n)` → True if even
- `factorial(n)` → compute factorial (raise ValueError if `n < 0`)

Test: `tests/test_utils.py` checks correctness.

### Assignment 3: Create a Class in a Package

Task: In `src/models/student.py`, create a Student class:

- Attributes: name: str, age: int, grades: list[int]
- Methods:
	- `add_grade(grade: int)`
	- `average()` → returns average grade (0 if no grades)
	- `is_passing()` → True if average ≥ 50

Test: tests/test_student.py verifies OOP behavior.

### Assignment 4: Importing from Packages

Task: In `src/main.py`, demonstrate:

- Importing from `calculator.operations` and `calculator.utils`
- Importing Student from models
- Creating a student, adding grades, and printing average

No test needed — run manually, but we can add a smoke test later.

### Assignment 5: Best Practices

- Task: Refactor imports in `main.py` to use absolute imports instead of relative.
- Write docstrings for all functions and classes.
- Use `__all__` in `calculator/__init__.py` to control what gets imported.

## ✅ Test (pytest)

Your job is to pass all test cases in the `tests/` folder.

`tests/test_operations.py`

```
import pytest
from src.calculator import operations

def test_add():
    assert operations.add(2, 3) == 5
    assert operations.add(-1, 1) == 0

def test_subtract():
    assert operations.subtract(10, 4) == 6
    assert operations.subtract(5, 9) == -4

def test_multiply():
    assert operations.multiply(3, 5) == 15
    assert operations.multiply(-2, 4) == -8

def test_divide():
    assert operations.divide(10, 2) == 5
    assert operations.divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        operations.divide(5, 0)
```

`tests/test_utils.py`

```
import pytest
from src.calculator import utils

def test_is_even():
    assert utils.is_even(2) is True
    assert utils.is_even(3) is False
    assert utils.is_even(0) is True
    assert utils.is_even(-4) is True

def test_factorial_valid():
    assert utils.factorial(0) == 1
    assert utils.factorial(1) == 1
    assert utils.factorial(5) == 120

def test_factorial_invalid():
    with pytest.raises(ValueError):
        utils.factorial(-3)
```

`tests/test_student.py`

```
import pytest
from src.models.student import Student

def test_student_creation():
    s = Student("Alice", 20)
    assert s.name == "Alice"
    assert s.age == 20
    assert s.grades == []

def test_add_grade():
    s = Student("Bob", 22)
    s.add_grade(80)
    s.add_grade(60)
    assert s.grades == [80, 60]

def test_average_with_grades():
    s = Student("Charlie", 19)
    s.add_grade(70)
    s.add_grade(90)
    assert s.average() == 80

def test_average_no_grades():
    s = Student("Dana", 21)
    assert s.average() == 0

def test_is_passing_true():
    s = Student("Eve", 18)
    s.add_grade(60)
    s.add_grade(70)
    assert s.is_passing() is True

def test_is_passing_false():
    s = Student("Frank", 23)
    s.add_grade(30)
    s.add_grade(40)
    assert s.is_passing() is False
```

## 🚀 Usage Instructions

- Place these test files inside tests/
- Run all tests with:
    ```
    pytest -v
    ```
- Students must implement code in src/calculator/operations.py, src/calculator/utils.py, and src/models/student.py until all tests pass.