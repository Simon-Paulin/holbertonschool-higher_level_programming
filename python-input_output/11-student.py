#!/usr/bin/python3
'''
11-student.py
'''


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (
            isinstance(attrs, list)
            and all(isinstance(attr, str) for attr in attrs)
        ):
            filtered_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return (filtered_dict)
        return (self.__dict__)

    def reload_from_json(self, json):
        '''
        Public méthode that replaces all attributes
        of the Student instance from dict
        '''
        for key, value in json.items():
            setattr(self, key, value)
