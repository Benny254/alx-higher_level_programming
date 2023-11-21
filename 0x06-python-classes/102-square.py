#!/usr/bin/python3
# 102-square.py
"""Define a class Square."""


class Square:
    """To represent a square."""

    def __init__(self, size=0):
        """Initializing a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """To set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, digit):
        if not isinstance(digit, int):
            raise TypeError("size must be an integer")
        elif digit < 0:
            raise ValueError("size must be >= 0")
        self.__size = digit

    def area(self):
        """To return the current area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
