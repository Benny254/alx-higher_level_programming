#!/usr/bin/python3
"""To Define a Rectangle class."""


class Rectangle:
    """Representing a Rectangle."""

    def __init__(self,height=0,width=0):
        """Initializing a new Rectangle.

        Args:
            height (int): The height of the new rectangle.
            width (int): The width of the new rectangle.
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

        @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
