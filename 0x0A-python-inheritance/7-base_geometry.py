#!/usr/bin/python3
"""
An integer validator module
"""


class BaseGeometry:
    """
    The super class to implements geometrical shapes
    """
    def area(self):
        """
        To raise an exception when you call this function
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        To check an integer value

        Args:
            name (str): The name of the value.
            value (int): The value.

        Raises:
            TypeError: If `value` isn't a integer.
            ValueError: If `value` is less than or equal to zero.
        """

        if type(value) is not int:
            raise TypeError(name + ' must be an integer')

        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
