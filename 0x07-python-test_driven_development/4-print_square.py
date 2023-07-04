#!/usr/bin/python3
# 4-print_square.py
"""Defines a square-prints function."""


def print_square(size):
    """prints a square

    Args:
        size (int): the size length of the square
    Raises:
    TypeError: if size is not integer
    ValueError: if size < 0
    TypeError: if size is float and size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for n in range(size):
            print("#", end="")
        print()
