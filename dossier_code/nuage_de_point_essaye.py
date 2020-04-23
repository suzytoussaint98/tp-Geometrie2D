import numpy as np
import matplotlib.pyplot as plt

#Fixation de l'état aléatoire pour la reproductibilité
np.random.seed(19680801)


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 à 15 point

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
