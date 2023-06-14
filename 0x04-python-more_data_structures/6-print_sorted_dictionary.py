#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = sorted(a_dictionary.keys())
    for items in sorted_dic:
        print("{}: {}".format(items, a_dictionary[items]))
