#!/usr/bin/python3
'''
module: 2-square.py

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
