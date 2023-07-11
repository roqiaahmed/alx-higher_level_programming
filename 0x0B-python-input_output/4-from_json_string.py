#!/usr/bin/python3
"""Defines a from_json_string function."""
import json


def from_json_string(my_str):
    """Converts a JSON string to a Python data structure object.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        A Python data structure object represented by the JSON string.
    """
    return json.loads(my_str)
