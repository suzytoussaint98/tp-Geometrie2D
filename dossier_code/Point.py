class Point:

def __init__(self, x, y):
        self.y = y
        self.x = x

def equals(self, un_autre_nombre):
        if a.x == b.x and a.y == b.y
            return "True"
        elif a.x != b.x and a.y != b.y
            return "False"


def angle(self, previous, next):
    OA = Vector(self, previous)
    OB = Vector(self, next)
    cos_AOB = OA.scalar_product(OB) / (OA.norm() * OB.norm())
    return math.acos(min(cos_AOB, 1))

def draw(self):
        plt.scatter(self.x, self.y)
