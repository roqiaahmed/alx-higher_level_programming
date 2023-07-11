#!/usr/bin/python3
"""Defines a save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """Saves a Python object to a JSON file.

    Args:
        my_obj (object): The Python object to save.
        filename (str): The name of the file to save the object to.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
