#!/usr/bin/python3
"""Defines a write_file function."""


def write_file(filename="", text=""):
    """write a text file .

    Args:
        filename (any): The filename.
        text (char): the text

    Returns:
        the number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
