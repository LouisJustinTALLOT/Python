""" Ce programme va tracer l'ensemble de Mandelbrot """

import numpy as np
import matplotlib.pyplot as plt

N = 20  # le nombre de points de tracé

a = np.random.randn(N,N)
#print(a)

fig, ax =  plt.subplots()

#plt.close()
ax.matshow(a, cmap = plt.cm.Blues)
plt.show()
