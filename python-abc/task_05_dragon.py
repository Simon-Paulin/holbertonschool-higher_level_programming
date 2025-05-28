#!/usr/bin/env python3
'''
task_05_dragon.py
Design two mixin classes, SwimMixin and FlyMixin,
each equipped with methods swim and fly respectively
'''


class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
