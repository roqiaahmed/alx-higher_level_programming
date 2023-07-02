#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text-indentation function.."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): the text.
    Raises:
    TypeError: if text is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for ele in text:
        print("{}".format(ele),end="")
        if ele == "." or  ele == "?" or  ele == ":":
            print()
            print()
