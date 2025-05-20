#!/usr/bin/python3
'''
module: 6-square.py
doordinates of the square
'''


class Square:
    '''
    class that definit size and possition of square
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        initilize a squarre

        argv:
            size (int): square size
            position (tuple): position of "#" in square
        raise:
            TypeError: for size or position if there're a integer
            ValueError: for size or possition than less than 0
        '''

        self.size = size
        self.position = position

    @property
    def size(self):
        '''
        defide th size of square
        '''

        return (self.__size)

    @size.setter
    def size(self, value):
        '''
        define the output
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''
        define the position
        '''
        return (self.__position)

    @position.setter
    def position(self, value):
        '''
        define the output
        '''
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''
        return the area of square
        '''
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
