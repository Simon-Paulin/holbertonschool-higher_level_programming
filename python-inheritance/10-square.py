#!/usr/bin/python3
'''
10-square.py
Write a class Square that inherits from Rectangle
'''


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    '''
    Created new Square class
    '''

    def __init__(self, size):
        '''
        Initialized a square whit side size whit private attribute
        '''

        self.integer_validator("size", size)
        self.__width = size
        self.__height = size

    def area(self):
        '''
        Calculate the area of the Square
        '''

        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
