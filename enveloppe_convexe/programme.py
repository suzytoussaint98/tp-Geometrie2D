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
#Création des différentes variables demandées.
current_point = first_point
next_point = None
help(enveloppe_convexe.add_point)
enveloppe_convexe.add_point(first_point)
help(nuage_de_points)

"""
6) Méthode pour retourner le point qui forme le plus grand angle avec current_point et previous_point : 
"""


def get_max_angle(self, current_point, previous_point):
    """
    retourne le point qui forme le plus grand angle avec current_point et previous_point
    """
    max_arc = 0
    max_point = current_point

    for p in self.points:
        if not p.equals(current_point):
            arc = current_point.angle(previous_point, p)
            if arc > max_arc:
                max_arc = arc
                max_point = p

    return max_point

#Création de la variable toto

toto = get_max_angle
next_point = toto


# Implémentation de l'algortihme

angle = 0

while next_point != current_point :
    enveloppe_convexe.add_point(current_point)
    max_angle = get_max_angle
    next_point = angle
    previous_point = current_point
    current_point = next_point
    print(enveloppe_convexe)

"""
FIN DE VOTRE CODE

Nous ne parvenons pas créer le polygone selon les étapes décris dans le sujet mais nous avons cependant compris comment le créer autrement : 
dans la class polygon il suffis de tracer les lignes du polygone en mettant des valeur ici :  
 def __init__(self):
        self.x_list = [10,400,500]
        self.y_list = [10,400,300]
        
"""

# affichage du résultat
nuage_de_points.draw()  # ajoute le nuage de points au graphique
enveloppe_convexe.draw()  # ajoute le polygone au graphique
plt.show()  # affiche le graphique
