import matplotlib.pyplot as plt


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
