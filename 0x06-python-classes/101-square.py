#!/usr/bin/python3
# 101-square.py
"""Define a class Square."""


class Square:
    """To represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """To set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, digit):
        if (not isinstance(digit, tuple) or
                len(digit) != 2 or
                not all(isinstance(num, int) for num in digit) or
                not all(num >= 0 for num in digit)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = digit

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for w in range(0, self.__position[1])]
        for w in range(0, self.__size):
            [print(" ", end="") for a in range(0, self.__position[0])]
            [print("#", end="") for b in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for w in range(0, self.__position[1])]
        for w in range(0, self.__size):
            [print(" ", end="") for a in range(0, self.__position[0])]
            [print("#", end="") for b in range(0, self.__size)]
            if w != self.__size - 1:
                print("")
        return ("")
