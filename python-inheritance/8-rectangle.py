#!/usr/bin/python3
'''
8-rectangle.py
Write a class Rectangle that inherits from BaseGeometry
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
