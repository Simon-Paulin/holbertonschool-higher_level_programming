#!/usr/bin/python3
'''
4-from_json_string.py
'''


import json


def from_json_string(my_str):
    '''
    Write a function that returns an object (Python data structure)
    represented by a JSON string
    '''

    return (json.load(my_str))
