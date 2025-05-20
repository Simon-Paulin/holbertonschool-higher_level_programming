#!/usr/bin/python3
'''
module: 4-rectangle.py
its define a class Rectangle whit private attribute and proprety access.
'''


class Rectangle:
    '''
    class define a rectangle by his width and height
    '''
    def __init__(self, width=0, height=0):
        '''
        initilize a rectangle

        argv:
        width (int): width of rectangle
        height (int): height of rectangle

        raise:
        TypeError: if widht or height is not a integer
        ValueError: if widht or height is < 0
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''
        get widht of rectangle
        '''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''
        setter for thr width of rectangle
        argv:
            value (int): new width to set
        raise:
            TypeError: if value is not a integer
            ValueError: if width is less than 0
        '''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
        get the height of rectangle
        '''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''
        setter for the height of rectangle
        argv:
            value (int) : new height to set
        raise:
            Typeerror : if value is not a interger
            ValueError : if height <= 0
            '''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''
        area of rectangle
        '''
        return (self.__width * self.__height)

    def perimeter(self):
        '''
        perimeter of rectangle
        '''
        if self.__width or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        '''
        return string representation of rectangle whit "#"
        if width or height is equal to 0, return a empty string
        '''
        if self.__width == 0 or self.__height == 0:
            return ("")

        result = ""
        for row in range(self.__height):
            result += "#" * self.__width
            if row != self.__height - 1:
                result += "\n"
        return result

    def __repr__(self):
        '''
        return a string representation of rectangle
        its used for recreate a new instanceby using eval()

        exemple:
                Rectangle (W=3, H=4)
        '''
        return (
            "Rectangle(width={}, height={})"
            .format(self.__width, self.__height)
        )
