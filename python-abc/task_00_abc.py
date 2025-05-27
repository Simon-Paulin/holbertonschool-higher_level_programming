#!/usr/bin/env python3
'''
task_00_abc.py
Setting up the Abstract Class
Implementing the Subclasses
'''

from abc import ABC, abstractmethod
'''
Import the necessary components from the abc module.
'''


class Animal(ABC):
    '''
    Define the Animal class, ensuring it inherits from ABC
    '''

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    '''
    Create a subclass named Dog that inherits from the Animal class
    '''

    def sound(self):
        return ("Bark")


class Cat(Animal):
    '''
    create a subclass named Cat that also inherits from the Animal class
    '''

    def sound(self):
        return ("Meow")
