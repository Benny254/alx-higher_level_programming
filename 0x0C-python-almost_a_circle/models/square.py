#!/usr/bin/python3
"""To Define Square class implement Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """To Square class body
"""

    def __init__(self, size, x=0, y=0, id=None):
        """TO initialization class props in constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ To return width size
        """
        return self.width

    @size.setter
    def size(self, value):
        """The module Square height and width
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Square class string
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """The update square props
        """
        if len(args):
            for j, arg in enumerate(args):
                if j == 0:
                    self.id = arg
                elif j == 1:
                    self.size = arg
                elif j == 2:
                    self.x = arg
                elif j == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ To return dict of class props
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
