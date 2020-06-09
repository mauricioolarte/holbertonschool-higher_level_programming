#!/usr/bin/python3
"""this module if for a class base
Attributes:
            def __init__: constructor method
"""


from base import Base


class Rectangle(Base):
    """ this a base class
    Attributes:
    __init__: construct method
    to_json_string(list_dictionaries): conver dir in json file.
    def from_json_string(json_string): import json file.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor method
        Args:
            width: is the number of the subslass.
            height:
            x, y:
            id:
        """
        Base.__init__(self, id)
        if type(width) is not int:
            raise TypeError('width must be and integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError('height must be and integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height
        if type(x) is not int:
            raise TypeError('x must be and integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x
        if type(y) is not int:
            raise TypeError('y must be and integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def area(self):
        """this method take a list and return a json string
            Argument : None
            Return : Area of rectangle
        """
        return self.__height * self.__width

    def display(self):
        """this method print a representation of rectangle
            Argument : none
        """
        print('\n' * (self.__y), end='')
        for point in range(self.__height):
            for point in range(self.__width - 1):
                print(' ' * self.__x, end='')
                print('#', end='')
            print('#')

    def __str__(self):
        """this method 
            Argument : self
            Return : sting whit data of arguments
        """
        return(
            '[Rectangle] ({}) {}/{} - {}/{}'.format(
                self.id, self.__x, self.__y, self.__width, self.__height)
            )

    def update(self, *args, **kwargs):
        """this method take a list and return a json string
            Argument : dictionary whit dir of object
            Return : a json sting
        """
        if args and len(args) > 0:
            if len(args) == 1:
                Base.__init__(self, args[0])
            elif len(args) == 2:
                Base.__init__(self, args[0])
                self.__width = args[1]
            elif len(args) == 3:
                Base.__init__(self, args[0])
                self.__width = args[1]
                self.__height = args[2]
            elif len(args) == 4:
                Base.__init__(self, args[0])
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            elif len(args) == 5:
                Base.__init__(self, args[0])
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'width':
                    Rectangle.width.__set__(self, value)
                elif key == 'height':
                    Rectangle.height.__set__(self, value)
                elif key == 'x':
                    Rectangle.x.__set__(self, value)
                elif key == 'y':
                    Rectangle.y.__set__(self, value)
                elif key == 'id':
                    Base.__init__(self, value)

    def to_dictionary(self):
        """this method take a list and return a json string
            Argument : dictionary whit dir of object
            Return : a json sting
        """
        list_dic = {}
        list_dic['id'] = self.id
        list_dic['width'] = self.__width
        list_dic['height'] = self.__height
        list_dic['x'] = self.__x
        list_dic['y'] = self.__y
        return (list_dic)

    @property
    def width(self):
        """this method take a list and return a json string
            Argument : dictionary whit dir of object
            Return : a json sting
        """
        return self.__width

    @property
    def height(self):
        """this method take a list and return a json string
            Argument : dictionary whit dir of object
            Return : a json sting
        """
        return self.__height

    @property
    def x(self):
        """this method take a list and return a json string
            Argument : dictionary whit dir of object
            Return : a json sting
        """
        return self.__x

    @property
    def y(self):
        """this method take a list and return a json string
            Argument : dictionary whit dir of object
            Return : a json sting
        """
        return self.__y

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be and integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be and integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError('x must be and integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError('y must be and integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y
