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

    @property
    def size(self):
        """ size getter """
        return self.height

    @size.setter
    def size(self, value):
        """size setter """
        super().update(width=value, height=value)

    def update(self, *args, **kwargs):
        """Assigns a new argument to each attribute
        """
        if len(args) == 0:
            if "size" in kwargs:
                self.size = kwargs["size"]
            super().update(**kwargs)
        elif len(args) == 1:
            super().update(args[0])
        elif len(args) == 2:
            super().update(args[0], args[1], args[1])
        elif len(args) == 3:
            super().update(args[0], args[1], args[1], args[2])
        elif len(args) == 4:
            super().update(args[0], args[1], args[1], args[2], args[3])

    def to_dictionary(self):
        """ Return the dict representation of the Rectangle
        """
        return {"size": self.size, "id": self.id, "x": self.x, "y": self.y}
