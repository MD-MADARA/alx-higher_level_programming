#!/usr/bin/python3
""" Square class """


class Square:
    """ A square class """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.size ** 2

    def __lt__(self, other):
        """less than comparison function
        """
        return self.size < other.size

    def __le__(self, other):
        """less than or equal to comparison
        """
        return self.size <= other.size

    def __eq__(self, other):
        """ equal to comparison
        """
        return self.size == other.size

    def __ne__(self, other):
        """not equal to comparison
        """
        return self.size != other.size

    def __gt__(self, other):
        """greater than comparison
        """
        return self.size > other.size

    def __ge__(self, other):
        """greater than or equal to comparison
        """
        return self.size >= other.size
