""" Ce programme va tracer l'ensemble de Mandelbrot """

"""
Nous allons faire un np.meshgrid et créer une fonction qui
renvoie 0 si le point est dans l'ensemble de Mandelbrot 
et 1 sinon, puis nous la vectoriserons

"""

import numpy as np
import matplotlib.pyplot as plt
import time


N = 10000  # le nombre de points de trace

axe_x = np.linspace(-2., 0.5, N)
axe_y = np.linspace(-1.25, 1.25, N)

### tests de représentation d'une matrice sous matplotlib
#a = np.random.randn(N,N)
#a = np.zeros((N,N))
#print(a)
#fig, ax =  plt.subplots()
#ax.matshow(a, cmap = plt.cm.Blues)
#plt.show()


def est_dedans(x,y):

    p = np.sqrt(np.power((x-0.25),2) + np.power(y, 2))
    if x < p - 2 * p * p + 0.25:
        return 0
    
    if np.power((x+1), 2) + np.power(y, 2) < 0.0625:
        return 0

    c = complex(x,y)
    z = 0
    for k in range(100):
        z = np.power(z,2) + c
        
        if abs(z) > 2:
            return k
    return 0

test = np.vectorize(est_dedans)

X, Y = np.meshgrid(axe_x, axe_y)

t1 = time.time()
Z = test(X,Y)
t2 = time.time()

print(t2-t1)

# 62 secondes avec N = 500 sans ameliorations
# 14 s avec ameliorations
# et 14.4 s avec N = 200 sans ameliorations
# 3.0 avec la cardioide
# 2.2 avec le petit cercle

plt.pcolor(X,Y,Z)
plt.axis("equal")
plt.show()

