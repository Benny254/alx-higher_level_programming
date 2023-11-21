#!/usr/bin/python3
"""
This chapter defines a class Square based on a previous document.
"""


class Square:
    """The Square class defines a square.

    Attributes:
       None.
    """
    def __init__(self, size):
        """ Initializing an attributes the Square class has.
        Args:
           size (int): the size of the square, private attribute.

        """
        self.__size = size
