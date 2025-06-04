#!/usr/bin/python3
'''
12-pascal_triangle.py
'''


def pascal_triangle(n):
    '''
    function that returns a list of lists of integers
    representing the Pascal triangle of n
    '''

    if n <= 0:
        return ([])

    triangle = [[1]]

    for i in range(1, n):
        prev = triangle[-1]
        row = [1]

        for j in range(1, len(prev)):
            row.append(prev[j - 1] + prev[j])

        row.append(1)
        triangle.append(row)
    return (triangle)
