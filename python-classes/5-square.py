#!/usr/bin/python3
'''
module: 5-square.py

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

    @property
    def size(self):
        '''
        get size of square
        '''
        return self.__size

    @size.setter
    def size(self, value):
        """
        Access and update private attribute:
        value (int) = size square
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
        area of square
        '''
        return (self.__size * self.__size)

    def my_print(self):
        '''
        print the square
        '''
        if self.size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
