from enveloppe_convexe.classes.vector import Vector
import matplotlib.pyplot as plt
import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def angle(self, previous, next):
        OA = Vector(self, previous)
        OB = Vector(self, next)
        cos_AOB = OA.scalar_product(OB) / (OA.norm() * OB.norm())
        return math.acos(min(cos_AOB, 1))

    def equals(self, point):
        return self.x == point.x and self.y == point.y

    def draw(self):
        plt.scatter(self.x, self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
