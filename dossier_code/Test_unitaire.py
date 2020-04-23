import unittest

class Point:

    def __init__(self, x, y):
        self.y = y
        self.x = x

    def equals(self, b):
        if self.x == b.x and self.y == b.y:
            return "True"
        elif self.x != b.x and self.y != b.y:
            return "False"

class Point(unittest.Point):

    def test_get_value(self):
        self.assertEqual("La valeur est égale à y", Point("x").get_value())

    def test_compare_value(self):
        self.assertEqual(False, Point("x").compare_value("y"))