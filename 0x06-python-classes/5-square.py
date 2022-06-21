#!/usr/bin/python3
"""A class Square that defines a square based on 4-square.py
"""

class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size_value):
        self.__size = size_value

        if not isinstance(size_value, int):
            raise TypeError("size must be an integer")
        elif size_value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(self.size):
            [print("#", end="") for i in range(self.size)]
            print("")
        if self.size == 0:
            print("")
