#!/usr/bin/python3
'''
7-base_geometry.py
Integer validator
'''


class BaseGeometry:
    '''
    Class created
    '''

    def area(self):
        '''
        that raises an Exception
        '''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        interger validator
        '''

        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
