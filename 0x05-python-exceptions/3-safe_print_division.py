#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Dividing two integers and printing the result
    """
    try:
        n_dvsn = a / b
    except (ZeroDivisionError, TypeError):
        n_dvsn = None
    finally:
        print("Inside result: {}".format(n_dvsn))
    return n_dvsn
