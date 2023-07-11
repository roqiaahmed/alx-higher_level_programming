#!/usr/bin/python3
"""Defines a load_from_json_file function."""
import json


def load_from_json_file(filename):
    """Loads a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        A Python object represented by the contents of the JSON file.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
