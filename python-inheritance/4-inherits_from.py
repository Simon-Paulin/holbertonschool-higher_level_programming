#!/usr/bin/python3
'''
4-inherits_from.py
Write a function that returns
    True: if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    False: if not
'''


def inherits_from(obj, a_class):
    '''
    check if the obj inherited of a_class
        Argv:
            obj: to check
            a_class: class
        Return:
            True if its subclass of a_class or False
    '''

    if isinstance(obj, a_class):
        if type(obj) is not a_class:
            return (True)
        else:
            return (False)
    else:
        return (False)
