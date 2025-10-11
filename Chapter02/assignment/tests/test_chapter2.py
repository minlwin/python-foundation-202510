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
