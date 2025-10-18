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
