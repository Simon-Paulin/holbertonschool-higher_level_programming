#!/usr/bin/python3
'''
2-is_same_class.py
Write a function that returns:
    True: if the object is exactly an instance of the specified class
    False: if not.
'''


def is_same_class(obj, a_class):
    '''
    return True or flase
    '''
    if type(obj) is a_class:
        return ("True")
    else:
        return ("False")
