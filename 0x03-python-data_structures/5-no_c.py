#!/usr/bin/env python3
def no_c(my_string):
    copy = [i for i in my_string]
    for n in copy:
        if n == "c" or n == "C":
            copy.remove(n)
    return ("".join(copy))
