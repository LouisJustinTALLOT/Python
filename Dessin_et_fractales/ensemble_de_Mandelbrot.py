""" Ce programme va tracer l'ensemble de Mandelbrot """

"""
Nous allons faire un np.meshgrid et créer une fonction qui
renvoie 1 si le point est dans l'ensemble de Mandelbrot 
et 0 sinon, puis nous la vectoriserons

"""

import numpy as np
import matplotlib.pyplot as plt

N = 2000  # le nombre de points de tracé

axe_x = np.linspace(-1.5, 0.5, N)
axe_y = np.linspace(-1, 1, N)

### tests de représentation d'une matrice sous matplotlib
#a = np.random.randn(N,N)
#a = np.zeros((N,N))
#print(a)
#fig, ax =  plt.subplots()
#ax.matshow(a, cmap = plt.cm.Blues)
#plt.show()


def est_dedans(x,y):
    c = complex(x,y)
    z = 0
    for k in range(100):
        z = np.power(z,2) + c
        
        if abs(z) > 2:
            return 0
    return 1

test = np.vectorize(est_dedans)

X, Y = np.meshgrid(axe_x, axe_y)

Z = test(X,Y)

plt.pcolor(X,Y,Z)

plt.show()

