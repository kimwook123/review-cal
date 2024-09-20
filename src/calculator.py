"""
This module provides basic arithmetic operations: addition, subtraction,
multiplication, and division.
"""


def add(num1, num2):
    """
    Adds two numbers together.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The sum of num1 and num2.
    """
    return num1 + num2


def subtract(num1, num2):
    """
    Subtracts the second number from the first number.

    Args:
        num1 (float): The number to subtract from.
        num2 (float): The number to subtract.

    Returns:
        float: The difference between num1 and num2.
    """
    return num1 - num2


def multiply(num1, num2):
    """
    Multiplies two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The product of num1 and num2.
    """
    return num1 * num2


def divide(num1, num2):
    """
    Divides the first number by the second number.

    Args:
        num1 (float): The dividend.
        num2 (float): The divisor.

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If num2 is zero.
    """
    if num2 == 0:
        raise ValueError("Zero division error")
    return num1 / num2
