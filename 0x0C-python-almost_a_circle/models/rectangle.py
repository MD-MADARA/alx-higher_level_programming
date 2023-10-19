#!/usr/bin/python3
""" Module for Rectangle class """
from models.base import Base


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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """  Returns the area value of
        the Rectangle instance.
        """
        return self.__height * self.__width

    def display(self):
        """ Prints in stdout the Rectangle instance
        with the character '#'
        """
        for i in range(self.y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """String representation of the class
        """
        string = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}"
        return string

    def update(self, *args, **kwargs):
        """Assigns a new argument to each attribute
        """
        if len(args) > 0:
            super().__init__(args[0])
            if len(args) > 1:
                self.width = args[1]
                if len(args) > 2:
                    self.height = args[2]
                    if len(args) > 3:
                        self.x = args[3]
                        if len(args) > 4:
                            self.y = args[4]
        else:
            if "id" in kwargs:
                super().__init__(kwargs["id"])
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ Return the dict representation of the Rectangle
        """
        return {"width": self.width, "height": self.height,
                "id": self.id, "x": self.x, "y": self.y}
