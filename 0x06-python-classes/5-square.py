#!/usr/bin/python3
"""
Define a previous document.
"""


class Square:
    """The Square class defines a square.

    Attributes:
       None.
    """
    def __init__(self, size=0):
        """ Initializing the attributes the Square class has.
        Args:
           size (int): The size of the square, private attribute.

        """
        self.size = size

    @property
    def size(self):
        """ To get the value of the private attribute size. """
        return self.__size

    @size.setter
    def size(self, size):
        """ To set the size of the instance considering exceptions """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Returns the current square instance area """
        return self.__size ** 2

    def my_print(self):
        """ To print in stdout the square with the character #. """
        if self.__size == 0:
            print("")
        else:
            for j in range(0, self.__size):
                print("{}".format('#' * self.__size))
