"""
This module contains unit tests for the calculator module.
It tests the add, subtract, multiply, and divide functions.
"""

import pytest
from src import calculator


def test_add():
    """
    Test the add function of the calculator module.
    """
    assert calculator.add(2, 3) == 5
    assert calculator.add(10, 100) == 110


def test_subtract():
    """
    Test the subtract function of the calculator module.
    """
    assert calculator.subtract(2, 3) == -1
    assert calculator.subtract(10, 100) == -90


def test_multiply():
    """
    Test the multiply function of the calculator module.
    """
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(10, 100) == 1000


def test_divide():
    """
    Test the divide function of the calculator module.
    It also tests the division by zero, which should raise a ValueError.
    """
    assert calculator.divide(2, 4) == 0.5
    assert calculator.divide(10, 100) == 0.1
    with pytest.raises(ValueError):
        calculator.divide(10, 0)
