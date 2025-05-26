#!/usr/bin/python3
'''
8-rectangle.py
Write a class Rectangle that inherits from BaseGeometry
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
    '''
    initilise a rectangle whit a width and height whit
    private attributes
    '''

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''
        return the area of Rectangle
        '''

        return (self.__width * self.__height)

    def __str__(self):
        '''
        return the sides value of Rectangle
        '''

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
