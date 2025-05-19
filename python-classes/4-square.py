#!/usr/bin/python3
'''
module: 4-square.py

'''


class Square:
    '''
    class Square
    '''

    def __init__(self, size=0):
        '''
        initilize suares whit differente size:
            TypeError: if size is not integer
            ValueErro: if size < 0
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
        return the current square area
        '''
        return (self.__size * self.__size)

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
