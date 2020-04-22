from dossier_code.Vector import Vector
import matplotlib.pyplot as plt
import random
import math

class Point:

    def __init__(self, x, y):
        self.y = y
        self.x = x

    def equals(self, b):
        if self.x == b.x and self.y == b.y:
            return "True"
        elif self.x != b.x and self.y != b.y:
            return "False"


    def angle(self, previous, next):
        OA = Vector(self, previous)
        OB = Vector(self, next)
        cos_AOB = OA.scalar_product(OB) / (OA.norm() * OB.norm())
        return math.acos(min(cos_AOB, 1))

    def draw(self):
        plt.scatter(self.x, self.y)
