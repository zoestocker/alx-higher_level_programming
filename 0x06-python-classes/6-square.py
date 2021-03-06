#!/usr/bin/python3
"""A class Square based on 5-square.py.
"""

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, size_value):
        self.__position = size_value

        if (not isinstance(size_value, tuple) or
                len(size_value) != 2 or
                not all (isinstance(num, int) for num in size_value) or
                not all(num >= 0 for num in size_value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print ("")
            return
        for i in range(0, self.__position[1]):
            [print("")]
        for i in range(0, self.size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.size)]
            print("")
