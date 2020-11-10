from turtle import*
reset()
up()
def carre(tupleposition, longueur):
    up()
    goto(tupleposition[0]-longueur/2,tupleposition[1]+longueur/2)
    down()
    for k in range(4):
        forward(longueur*0.9)
        right(90)
        
    up()
    goto(tupleposition[0],tupleposition[1])
    

def eponge_menger(positionx,positiony,longueur,etape):
    lieu=(0,0)
    if etape==0:
        for l in range(4):
            carre(lieu,longueur*0.9)
    else:
        
        lieu=position()
        positionx=lieu[0]
        positiony=lieu[1]
        carre(lieu,longueur*0.9)
        for h in range(2):
            for k in range (2):
                eponge_menger(positionx-longueur/4+h*longueur/2,positiony-longueur/4+k*longueur/2,longueur/2,etape-1)
# carre((0,0),680)
eponge_menger(0,0,400,3)