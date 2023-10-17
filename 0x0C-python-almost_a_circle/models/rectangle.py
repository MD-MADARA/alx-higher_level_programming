#!/usr/bin/python3
""" Module for Rectangle class """
from base import Base

class Rectangle(Base):
    """
    The Rectangle class with attributes for width,
    height, x-coordinate, and y-coordinate
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
            width : The width of the rectangle.
            height : The height of the rectangle.
            x : The x-coordinate of the rectangle (default is 0).
            y : The y-coordinate of the rectangle (default is 0).
            id : The unique identifier for the rectangle (default is None).
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
