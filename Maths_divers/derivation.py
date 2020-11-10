from math import*
import matplotlib.pyplot as plt
import numpy as np
points = 50001
inf = -pi*2	
sup = pi*2
pas = (sup-inf)/points
a,b = 0.5, 2.1
x = np.linspace(inf,sup,points)

y = np.linspace(0,1,points)

def f(x):
    # return sum([a**n * cos(b**n * pi * x) for n in range(15)])
    # return exp(sin(x)**2+sin(x**2))
    return exp(-exp(sin(x)))*cos(x)
    # return 1/sqrt(2*pi) * exp(-x**2)
def f1(x):
    return 6*x-2
    
for i in range(1,points):
    y[i-1] = (f(x[i])-f(x[i-1]))/pas
    
plt.close()
# plt.axis("equal")
plt.plot(x,np.vectorize(f)(x))
plt.plot(x[:points-1],y[:points-1])
plt.show()