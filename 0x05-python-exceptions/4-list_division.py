#!/usr/bin/python

def list_division(my_list_1, my_list_2, list_length):
    """
    Dividing an element by element 2 lists.
    """
    temp = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
            result = 0
        finally:
            temp.append(result)
    return temp
