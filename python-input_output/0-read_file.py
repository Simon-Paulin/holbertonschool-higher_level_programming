#!/usr/bin/python3
"""
0-read_file.py
Read a file
"""


def read_file(filename=""):
    """
    Function for read a file
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
