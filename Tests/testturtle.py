from turtle import*
from math import*
reset()
width(3)
down()
goto(0,0)
# x=-15
# while x<=15:
#     up()
#     goto(x,e**x)
#     down()
#     forward(1)
#     up()
#     x+=0.5




# PROGRAMME DE CERCLE
# rayon=int(input('Rayon? '))
# a=-rayon
# while a<=rayon:
#     up()
#     goto(a,sqrt((rayon**2)-(a**2)))
#     down()
#     forward(1)
#     up()
#     a+=1
# a=-rayon
# while a<=rayon:
#     up()
#     goto(a,-sqrt((rayon**2)-(a**2)))
#     down()
#     forward(1)
#     up()
#     a+=1

for i in range(1,100,10):
    circle(i)