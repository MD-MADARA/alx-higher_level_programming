#!/usr/bin/python3
from base import Base
""" Module for Rectangle class """


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

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.
        """
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.
        """
        self.__height = value

    @property
    def x(self):
        """
        Get the x-coordinate of the rectangle.

        Returns:
            int: The x-coordinate.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the rectangle.

        Args:
            value (int): The new x-coordinate value.
        """
        self.__x = value

    @property
    def y(self):
        """
        Get the y-coordinate of the rectangle.

        Returns:
            int: The y-coordinate.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the rectangle.

        Args:
            value (int): The new y-coordinate value.
        """
        self.__y = value
