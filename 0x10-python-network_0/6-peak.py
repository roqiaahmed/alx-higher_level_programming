#!/usr/bin/python3
"""Module that finds a peak in a list of integers"""
def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): a list of integers

    Returns:
        int: peak(s)
    """
    # if not list_of_integers:
    #     return None
    # left = 0
    # right = len(list_of_integers) -1
    # while left + 1 < right:
    #     mid = int((left + right) / 2)
    #     if list_of_integers[mid - 1]<list_of_integers[mid] > list_of_integers[mid + 1]:
    #         return list_of_integers[mid]
    #     elif list_of_integers[mid] < list_of_integers[mid + 1]:
    #         list_of_integers[:] = list_of_integers[mid : ]
    #     else:
    #         list_of_integers[:] = list_of_integers[ : mid]
    #     right = len(list_of_integers) - 1
    # # return mid
    # return list_of_integers[mid - 1]

    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]