from enveloppe_convexe.classes.point_cloud import PointCloud
from enveloppe_convexe.classes.polygon import Polygon
from enveloppe_convexe.classes.point import Point
import matplotlib.pyplot as plt

"""
Exercice: faire un programme qui crée un nuage de points, calcule l'enveloppe convexe et affiche le graphique

Instruction:
Placez bien votre code entre les commentaires *** DEBUT *** et *** FIN ***

Indication:
Si vous lancez le programme, vous allez voir apparaître un graphique avec le nuage de points.
Si le programme fonctionne correctement, un polygone va apparaître autour du nuage de points.
"""

# Initialisation des variables dont vous avez besoin ci-dessous
nuage_de_points = PointCloud(20)  # variable qui contient un nuage de 20 points (variable de type PointCloud)
enveloppe_convexe = Polygon()  # variable qui contient un polygone vide (variable de type Polygone)
first_point = nuage_de_points.get_most_left()  # variable qui contient le point le plus à gauche du nuage de points
previous_point = Point(first_point.x, 0)  # variable qui contient un point imaginaire sous first_point

"""
DEBUT DE VOTRE CODE
"""





"""
FIN DE VOTRE CODE
"""

# affichage du résultat
nuage_de_points.draw()  # ajoute le nuage de points au graphique
enveloppe_convexe.draw()  # ajoute le polygone au graphique
plt.show()  # affiche le graphique
