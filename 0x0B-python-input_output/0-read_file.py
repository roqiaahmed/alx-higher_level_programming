#!/usr/bin/python3
"""Defines a read_file function."""


def read_file(filename=""):
    """reads a text file and prints it to stdout.

    Args:
        filename (any): The filename.

    Returns:
        the text of the file.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
