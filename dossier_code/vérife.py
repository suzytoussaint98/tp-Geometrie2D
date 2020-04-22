from dossier_code.Point import Point
from dossier_code.PointCloud import PointCloud

import matplotlib.pyplot as plt
import random

def generate_random_points(n):

    random_points = list()

    for i in range(0, n):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        random_points.append(Point(x, y))

    return random_points

random_points = generate_random_points(20)  # génére des points aléatoires
cloud = PointCloud(random_points)           # crée le nuage de points
cloud.draw()                                # ajoute le nuage de points au graphique
#cloud.compute_convex_hull().draw()          # ajoute l'enveloppe convexe au graphiqye
plt.show()