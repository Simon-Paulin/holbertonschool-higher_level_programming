#!/usr/bin/python3
'''
1-write_file.py

'''


def write_file(filename="", text=""):
    '''
    Write a function that writes a string to a text file (UTF8) and returns
    the number
    of characters written
    '''

    with open(filename, encoding="UTF8") as file:
        return (file.write(text))
