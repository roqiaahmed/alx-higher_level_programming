#!/usr/bin/python3
"""Defines a append_write function."""


def append_write(filename="", text=""):
    """appends a string at the end of a text file.

    Args:
        filename (any): The filename.
        text (char): the text

    Returns:
        the number of characters written.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
