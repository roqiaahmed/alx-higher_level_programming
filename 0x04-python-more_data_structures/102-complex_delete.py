#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_key = list(a_dictionary.keys())
    if not value:
        return a_dictionary
    for key in list_key:
        if a_dictionary.get(key) == value:
            del a_dictionary[key]
    return a_dictionary
