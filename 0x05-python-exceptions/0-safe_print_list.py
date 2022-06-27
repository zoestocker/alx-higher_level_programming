#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.
    """
    l_count = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            l_count += 1
        except IndexError:
            break
    print("")
    return l_count
