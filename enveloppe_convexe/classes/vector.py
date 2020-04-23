import math


class Vector:

    def __init__(self, A, B):
        self.x = B.x - A.x
        self.y = B.y - A.y

    def norm_square(self):
        return self.x ** 2 + self.y ** 2

    def norm(self):
        return math.sqrt(self.norm_square())

    def scalar_product(self, vector):
        return (self.x * vector.x) + (self.y * vector.y)
