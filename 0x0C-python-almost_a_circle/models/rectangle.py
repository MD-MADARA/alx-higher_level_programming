#!/usr/bin/python3
""" Module for Rectangle class """
from base import Base


class Rectangle(Base):
    """Class Rectangle that inherit from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width attribute getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width attribute setter """
        self.__width = value

    @property
    def height(self):
        """ width attribute getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height attribute setter """
        self.__height = value

    @property
    def x(self):
        """ x attribute getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x attribute setter """
        self.__x = value

    @property
    def y(self):
        """ y attribute getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y attribute setter """
        self.__y = value
