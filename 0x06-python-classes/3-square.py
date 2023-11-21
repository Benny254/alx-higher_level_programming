#!/usr/bin/python3
"""
Define a previous document.
"""


class Square:
    """Square class defines a square.

    Attributes:
       None.
    """
    def __init__(self, size=0):
        """ Initializing the attributes the Square class has.
        Args:
           size (int): The size of the square, private attribute.

        """
        self.set_size(size)

    def get_size(self):
        """ To get the value of the private attribute size. """
        return self.__size

    def set_size(self, size):
        """ To set the size of the instance considering exceptions """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Returns the current square instance area """
        return (self.__size ** 2)
