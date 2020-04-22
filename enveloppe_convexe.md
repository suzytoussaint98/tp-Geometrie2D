# Enveloppe convexe

Critères de notation:

* Difficulté du sujet choisi 
* Lisibilité du code
* Effort de groupe, au moins 1 commit par membre du groupe (pas de commit = pas de note!)

## Enoncé du problème

L'**enveloppe convexe** d'un objet ou d'un regroupement d'objets géométriques est l'ensemble convexe le plus petit parmi les ensembles convexes qui contiennent ces objets.

En 2 dimensions (dans un plan), l'enveloppe convexe est un polygone.
 
On peut imaginer l'enveloppe convexe à l'aide d'un élastique:

* On entoure tous les points du plan dans un élastique
* On relâche l'élastisque jusqu'à ce qu'il se contracte au maximum: on obtient l'enveloppe convexe.

Exemple:

![Exemple](https://images.math.cnrs.fr/IMG/jpg/fig3-4.jpg)

La détection de l'enveloppe convexe est problème central en géométrique algorithmique qui a de nombreuses applications :

* reconnaissance de formes (détection d'objets dans une vidéo, reconnaissance de caractères manuscrits, etc.).
* en synthèse d'images, en CAO, en robotique, comme approximation pour des tests rapides d'intersection
* en statistiques (par exemple, le _pelage_ consiste à supprimer les points de l'enveloppe convexe, ce qui permet d'obtenir des estimateurs plus robustes.)
* etc.

Le but de l'exercice est de calculer l'enveloppe convexe d'un nuage de points en 2 dimensions.

## Modélisation

On modélisera le problème à l'aide de plusieurs classes  :

* une classe `Point` qui modélise un point en 2D
* une classe `Vector` qui représente un vecteur reliant 2 points
* une classe `Polygon` qui représente l'enveloppe convexe (implémentation donnée en __Annexe__)
* une classe `PointCloud` qui représente un nuage de points

### Classe Point

Un point est constitué de deux coordonnées x et y. La classe `Point` dispose donc de deux attributs :

* x qui représente l'abscisse du point dans le plan (coordonnée horizontale)
* y qui représente l'ordonnée du point dans le plan (coordonnée verticale)

La classe `Point` comporte les méthodes suivantes : 

* `equals` qui prend en paramètre un autre point et renvoie True si il est égale au point courant.
* `angle` qui permet de calculer l'angle former par 3 points (cf l'annexe).
* `draw` qui permet de dessiner le point sur le graphique (implémentation donnée en __annexe__).

### Classe Vector

Un vecteur relie 2 points A et B (où A et B sont des objets de type `Point`). 

La classe `Vector` dispose des attributs suivants :

* `x` un entier qui représente l'abscisse du vecteur dans le plan (coordonnée horizontale)
* `y` un entier qui représente l'ordonnée du vecteur dans le plan (coordonnée verticale)

Pour rappel: soient deux points du plan A(xA,yA) et B(xB,yB), les coordonnées du vecteur AB sont (xB - xA, yB -yA)

La classe `Vector` dispose des méthodes suivantes :

* `norm_square` qui renvoie la norme au carré du vecteur (x² + y²)
* `norm` qui renvoie la norme du point
* `scalar_product` qui prend en paramètre un vecteur BC et retourne le produit scalaire de BC avec le vecteur courant (
    Pour rappel: soient les vecteurs AB de coordonnées (x1, y2) et BC de coordonnées (x2, y2). Le produit scalaire de AB et BC est égal à : x1 * x2 + y1 * y2

### Classe Polygon

L'implémentation de cette classe est donnée en __Annexe__

### Classe PointCloud

La classe `PointCloud` dipose des attributs suivants :

* `points`: une liste de points qui forment le nuage de mots

Elle possède les méthodes suivantes : 

* `get_most_left` qui retourne le point le plus à gauche du nuage de points

* `get_max_angle`:
    * qui prend en paramètre deux points `current_point` et `previous_point`
    * qui retourne le point qui permet de former l'angle le plus grand
    * indications: on souhaite trouver `p` qui maximise la valeur `current_point.angle(previous_point, p)`

* `draw` qui permet de dessiner le nuage de points sur le graphique (implémentation donnée en __annexe__)

## Implémentation

Le but de l'exercice est donc d'implémenter la méthode `compute_convex_hull` grâce à l'algorithme de la [marche de Jarvis](https://fr.wikipedia.org/wiki/Marche_de_Jarvis).

### Principe

Le principe de l'algorithme est:

* On part du point `p1` : le point le plus à gauche de l'image (qui appartient forcément à l'enveloppe convexe). 
* On prend comme point suivant `p2` : le point qui a un angle maximal avec `p1` 
* On continue jusqu'à retomber sur le point de départ `p1`.

Exemple : 

![Exemple](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Animation_depicting_the_gift_wrapping_algorithm.gif/200px-Animation_depicting_the_gift_wrapping_algorithm.gif)

### Algorithme

**Etape 1: initialiser les variables**

Nous avons besoin des variables suivantes:

* `convex_hull`: l'enveloppe convexe (on initialisera un polygone)
* `first_point`: le point le plus à gauche de l'image 
* `current_point`: le point courant (on prendra `current_point=first_point`)
* `previous_point`: le point précédent
    * on créera un point imaginaire ayant le même x que `current_point`, mais d'ordonnée 0
* `next_point`: le point suivant (qui vaut `None`)

**Etape 2: déroulé de l'algorithme**

* Ajouter `first_point` à l'enveloppe convexe

* TantQue `next_point` est différent de `first_point` Faire :

	* Ajouter `current_point` à l'enveloppe convexe.
	* Chercher `next_point`, le point qui maximise l'angle avec `previous_point` et `current_point`
	* Mettre à jour la valeur des variables:
        * `previous_point` devient `current_point`
        * `current_point` devient `next_point`

## Vérifier que mon code fonctionne

En lançant ce programme :
````python
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
cloud.compute_convex_hull().draw()          # ajoute l'enveloppe convexe au graphiqye
plt.show()                                  # affiche le graphique
````

Vous devriez obtenir un résultat qui ressemble à ça :

<img height="250" src="https://github.com/datalyo-dc-m1/algorithmie-data/blob/master/attachments/matplot.png">

## Tests unitaires

Ecrire des tests unitaires vérifiant le bon fonctionnement des méthodes implémentées.

## Annexes

### Librairies nécessaires

```python
import matplotlib.pyplot as plt  
import random  
import math
```

Installation de matplotlib (commande à exécuter dans la fenêtre Terminal de PyCharm)

- `pip install matplotlib` (Windows)
- `pip3 install matplotlib` (macOs)

### Classe Polygon

```python
class Polygon:
    """
    A class used to represent a Polygon

    Attributes
    ----------
    x_list : list
        horizontal coordinates of Polygon points
    y_list : list
        vertical coordinates of Polygon points

    Methods
    -------
    add_point(point)
        Add the provided point to the polygon
    draw()
        Draw the polygon
    """

    def __init__(self):
        self.x_list = []
        self.y_list = []

    def add_point(self, point):
        """
        Add a point to the Polygon

        Parameters
        ----------
        point : Point
        The point to add to the Polygon
        """
        self.x_list.append(point.x)
        self.y_list.append(point.y)

    def draw(self):
        """
        Draw the polygon
        """
        plt.plot(self.x_list, self.y_list)
```

### Classe Point

Fonction `angle` de la classe `Point`: 

```python
class Point:

    # constructeur

    # autres méthodes

    def angle(self, previous, next):  
        OA = Vector(self, previous)
        OB = Vector(self, next)
        cos_AOB = OA.scalar_product(OB) / (OA.norm() * OB.norm())
        return math.acos(min(cos_AOB, 1))

    def draw(self):  
        plt.scatter(self.x, self.y)

    def __str__(self):  # permet d'afficher un point avec print(point)
        return f"({self.x}, {self.y})"
```

### Classe PointCloud

```python
class PointCloud:

    # constructeur

    # autres méthodes

    def draw(self):
        for p in self.points:
            p.draw()
```
