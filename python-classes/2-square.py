#!/usr/bin/python3
# 2-square.py
# Travis Adamson
""" Define a class "Square". """


class Square:
    """This is an empty class to define square"""

    def __init__(self, size=0):
        """Initializes a new "Square".

        Args:
            size (int): The size of said new square.
        """
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
