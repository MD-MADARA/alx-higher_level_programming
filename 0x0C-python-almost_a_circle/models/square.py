#!/usr/bin/python3
""" module for the Class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class Square inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a Square instance
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the class
        """
        string = f"[Square] ({self.id}) {self.x}/{self.y}\
 - {self.height}"
        return string
