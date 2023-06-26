#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for num in range(x):
            print("{}".format(my_list[num]),end="")
            i += 1
    except:
        pass
    print()
    return(i)
