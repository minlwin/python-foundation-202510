# Chapter 3 Assignment : Writing Statements

**Target for this chapter**

1. Recognize what an expression is and how Python evaluates it.
2. Use different operators to perform calculations and comparisons.
3. Explain what a statement is in Python.
4. Write different types of statements to make your programs do useful work.

**Instructions for Students**

1. Open src/assignment.py and implement the functions marked with # TODO.
2. Do not modify the test file.
3. Run pytest in your terminal to check if your functions pass all tests.
4. You need to make all tests pass.

`src/assignment.py`

```
# Chapter 3: Writing Statements Assignment

# 1. Arithmetic Operations
def calculate_sum(a, b):
    """
    Returns the sum of two numbers.
    Example:
        calculate_sum(2, 3) -> 5
    """
    # TODO: Implement the function
    return 0

def calculate_expression(a, b, c):
    """
    Returns the result of the expression a + b * c
    Example:
        calculate_expression(2, 3, 4) -> 14
    """
    # TODO: Implement the function
    return 0


# 2. Comparison Operations
def is_greater(a, b):
    """
    Returns True if a > b else False
    Example:
        is_greater(5, 3) -> True
    """
    # TODO: Implement the function
    return False

def is_equal(a, b):
    """
    Returns True if a == b else False
    """
    # TODO: Implement the function
    return False


# 3. Conditional Statements
def max_of_two(a, b):
    """
    Returns the greater of a and b using if-else statement
    """
    # TODO: Implement the function
    return a

def categorize_number(n):
    """
    Returns:
        'positive' if n > 0
        'negative' if n < 0
        'zero' if n == 0
    """
    # TODO: Implement the function
    return ""


# 4. Loop Statements
def sum_n_numbers(n):
    """
    Returns sum of numbers from 1 to n using a loop
    """
    # TODO: Implement the function
    return 0

def count_even_numbers(numbers):
    """
    Counts how many even numbers are in the given list
    """
    # TODO: Implement the function
    return 0


# 5. Expression Statement
def multiply_and_print(a, b):
    """
    Multiplies a and b and prints the result.
    """
    # TODO: Implement the function
    pass
```

`tests/test_assignment.py`

```
import pytest
from src.assignment import *

def test_calculate_sum():
    assert calculate_sum(2, 3) == 5
    assert calculate_sum(-1, 5) == 4

def test_calculate_expression():
    assert calculate_expression(2, 3, 4) == 14
    assert calculate_expression(1, 2, 3) == 7

def test_is_greater():
    assert is_greater(5, 3) is True
    assert is_greater(2, 4) is False

def test_is_equal():
    assert is_equal(5, 5) is True
    assert is_equal(5, 3) is False

def test_max_of_two():
    assert max_of_two(2, 3) == 3
    assert max_of_two(10, 5) == 10

def test_categorize_number():
    assert categorize_number(5) == 'positive'
    assert categorize_number(-3) == 'negative'
    assert categorize_number(0) == 'zero'

def test_sum_n_numbers():
    assert sum_n_numbers(5) == 15  # 1+2+3+4+5
    assert sum_n_numbers(0) == 0

def test_count_even_numbers():
    assert count_even_numbers([1,2,3,4,5,6]) == 3
    assert count_even_numbers([1,3,5]) == 0

def test_multiply_and_print(capfd):
    multiply_and_print(2, 3)
    out, err = capfd.readouterr()
    assert out.strip() == '6'

    multiply_and_print(5, 5)
    out, err = capfd.readouterr()
    assert out.strip() == '25'
```

**✅ Features of this assignment:**

- Covers all chapter objectives: expressions, operators, statements, loops, conditionals.
- Students start with failing tests.
- Encourages step-by-step coding and testing using pytest.
- Includes expression statements (print) and different statement types.