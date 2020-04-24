from enveloppe_convexe.classes.point import Point
import random


class PointCloud:

    def __init__(self, n):
        random_points = list()
        for i in range(0, n):
            x = random.randint(0, 1000)
            y = random.randint(0, 1000)
            random_points.append(Point(x, y))
        self.points = random_points

    def get_most_left(self):
        """
        retourne le point le plus à gauche du nuage de points
        """

        most_left = self.points[0]

        for p in self.points:
            if p.x < most_left.x:
                most_left = p

        return most_left

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

    def draw(self):
        """
        ajoute le nuage de points au graphique
        """
        for p in self.points:
            p.draw()
