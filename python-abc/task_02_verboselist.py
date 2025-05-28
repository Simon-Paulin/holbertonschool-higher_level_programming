#!/usr/bin/env python3
'''
task_02_verboselist.py
Create a class named VerboseList that extends the Python list class. 
This custom class should print a notification
message every time an item is added.
(using the append or extend methods) or removed
(using the remove or pop methods).
'''

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items.".format(item))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, item):
        super().pop(item)
        print("Popped [{}] from the list.")

        return (item)
