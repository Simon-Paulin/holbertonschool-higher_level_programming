#!/usr/bin/python3
'''
1-my_list.py
Write a class MyList that inherits from list
'''


class MyList(list):
    '''
    Class MyList
    '''

    def print_sorted(self):
        '''
        function that print in sorted
        '''

        print(sorted(self))
