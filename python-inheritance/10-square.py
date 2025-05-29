#!/usr/bin/python3
'''
10-square.py
Write a class Square that inherits from Rectangle
'''


Rectangle = __import__('9-rectangle').Rectangle


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
        '''
        return value of square
        '''

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
