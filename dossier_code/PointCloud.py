
Class PointCloud :

    points = [1, 2, 3, 4, 5] # On cherche le plus petit point d'abscisse x afin de trouver le point le plus a gauche

get_most_left = 0
max_liste = 0
    for element in liste:
        if element > max_liste:
            get_most_left = element
         if element < get_most_left:
             get_most_left= element


print("Minimum", min(liste), "Maximum", max(liste))