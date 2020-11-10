from turtle import*
from random import*
reset()
def trait_slash(x,y):
    up()
    goto(x,y)
    down()
    goto(x+20,y+20)
    up()


def trait_backslash (x,y):
    up()
    goto(x,y+20)
    down()
    goto(x+20,y)
    up()
# def trait_droit(x,y):
#     up()
#     goto(x,y+5)
#     down()
#     goto(x+10,y+5)
#     up()
#
up()
for x in range(-640, 640,20):
    for y in range(-340,340,20):
        rr=random()
        if rr<1/2:
            trait_slash(x,y)
        else:

            trait_backslash(x,y)
        goto(x,y)
        down()
        circle(randint(1,randint(10,20)))
        up()
up()
goto(1000,340)