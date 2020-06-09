#!/usr/bin/python3
"""this module if for a class base
Attributes:
            def __init__: constructor method
"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ this a base class
    Attributes:
    __init__: construct method
    to_json_string(list_dictionaries): conver dir in json file.
    def from_json_string(json_string): import json file.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor method
        Args:
            width: is the number of the subslass.
            height:
            x, y:
            id:
        """
        Rectangle.width.__set__(self, size)
        Rectangle.height.__set__(self, size)
        Rectangle.x.__set__(self, x)
        Rectangle.y.__set__(self, y)
        Base.__init__(self, id)

    def __str__(self):
        """this method take a list and return a json string
            Argument : None
            Return : Area of rectangle
        """
        return(
            '[Square] ({}) {}/{} - {}'.format(
                self.id, self.x, self.y, self.width)
            )

    def update(self, *args, **kwargs):
        """this method take a list and return a json string
            Argument : None
            Return : Area of rectangle
        """
        if args and len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    Base.__init__(self, args[i])
                elif i == 1:
                    Square.size.__set__(self, args[i])
                elif i == 2:
                    Rectangle.x.__set__(self, args[i])
                elif i == 3:
                    Rectangle.y.__set__(self, args[i])
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    Base.__init__(self, value)
                elif key == 'size':
                    Square.size.__set__(self, value)
                elif key == 'x':
                    Rectangle.x.__set__(self, value)
                elif key == 'y':
                    Rectangle.y.__set__(self, value)

    def to_dictionary(self):
        """this method take a list and return a json string
            Argument : None
            Return : Area of rectangle
        """
        list_dic = {}
        list_dic['id'] = self.id
        list_dic['size'] = self.width
        list_dic['x'] = self.x
        list_dic['y'] = self.y
        return (list_dic)

    @property
    def size(self):
        """this method take a list and return a json string
            Argument : None
            Return : Area of rectangle
        """
        return self.width

    @size.setter
    def size(self, size):
        """this method take a list and return a json string
            Argument : None
            Return : Area of rectangle
        """
        if type(size) is not int:
            raise TypeError('width must be and integer')
        elif size <= 0:
            raise ValueError('width must be > 0')
        else:
            Rectangle.width.__set__(self, size)
            Rectangle.height.__set__(self, size)
