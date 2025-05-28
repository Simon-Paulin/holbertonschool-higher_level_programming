#!/usr/bin/env python3
'''
task_03_countediterator.py
Create a class named CountedIterator
that extends the built-in iterator obtained from the iter function.
The CountedIterator should keep track of the number of items
that have been iterated over
'''


class CountedIterator:
    def __init__(self, iterator):
        self.iterator = iter(iterator)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return (item)

    def get_count(self):
        return (self.count)

    def __iter__(self):
        return (self)
