#!/usr/bin/env python3

class Point(object):

        def __init__(self, x = 0.0, y = 0.0):
                self.x = x
                self.y = y

        def distance(self, other):
                return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

        def __str__(self):
                return f"({self.x:.01f}, {self.y:.01f})"
