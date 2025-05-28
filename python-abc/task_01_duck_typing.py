#!/usr/bin/env python3
'''
task_01_duck_typing.py
Create an abstract class named Shape with two abstract methods:
 area and perimeter
'''

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return pi * self.__radius * self.__radius

    def perimeter(self):
        return 2 * pi * self.__radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        return (2 * (self.__width + self.__height))

    def shape_info(sim):
        area = sim.area()
        perimeter = sim.perimeter()
        print("{}".format(area))
        print("{}".format(perimeter))
