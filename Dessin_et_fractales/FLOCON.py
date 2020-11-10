from turtle import*
reset()
up()
# goto(-100,100)
# def courbe_koch(longueur, etape):
    # """Fonction récursive pour dessiner une courbe de Von Koch
    # (une fonction récursive étant une fonction s'appelant elle-même)"""
    # # # if etape == 0:
        # forward(longueur)
    # else:
        # courbe_koch(longueur/3, etape-1)
        # left(90)
        # courbe_koch(longueur/4, etape-1)
        # right(90)
        # courbe_koch(longueur/4, etape-1)
        # right(90)
        # courbe_koch(longueur/4, etape-1)
        # left(90)
#         courbe_koch(longueur/3, etape-1)
#  
# def flocon_koch(longueur, etape):
#     """Fonction pour dessiner un flocon de Von Koch
#     depuis le coin haut gauche"""
#     for i in range(4):  #Pour chaque côté du triangle initial
#         courbe_koch(longueur, etape)  #Courbe de Von Koch
#         right(90)
# 
# if __name__ == "__main__":
#     down()
# 
#     flocon_koch(400, 4)
    
    
    
    #A PARTIR D'UN TRIANGLE
# goto(-400/3,100)
# def courbe_koch(longueur, etape):
#     """Fonction récursive pour dessiner une courbe de Von Koch
#     (une fonction récursive étant une fonction s'appelant elle-même)"""
#     if etape == 0:
#         forward(longueur)
#     else:
#         courbe_koch(longueur/3, etape-1)
#         left(60)
#         courbe_koch(longueur/3, etape-1)
#         right(120)
#         courbe_koch(longueur/3, etape-1)
#         left(60)
#         courbe_koch(longueur/3, etape-1)
#  
# def flocon_koch(longueur, etape):
#     """Fonction pour dessiner un flocon de Von Koch
#     depuis le coin haut gauche"""
#     for i in range(3):  #Pour chaque côté du triangle initial
#         courbe_koch(longueur, etape)  #Courbe de Von Koch
#         right(120)
# 
# if __name__ == "__main__":
#     down()
# 
#     flocon_koch(400, 5)

#PENTAGONE
goto(-200,200)
def courbe_koch(longueur, etape):
    """Fonction récursive pour dessiner une courbe de Von Koch
    (une fonction récursive étant une fonction s'appelant elle-même)"""
    if etape == 0:
        forward(longueur)
    else:
        courbe_koch(longueur/2, etape-1)
        left(108)
        courbe_koch(longueur/5, etape-1)
        right(72)
        courbe_koch(longueur/5, etape-1)
        right(72)
        courbe_koch(longueur/5, etape-1)
        right(72)
        courbe_koch(longueur/5, etape-1)
        left(108)
        courbe_koch(longueur/2, etape-1)
 
def flocon_koch(longueur, etape):
    """Fonction pour dessiner un flocon de Von Koch
    depuis le coin haut gauche"""
    for i in range(5):  #Pour chaque côté du triangle initial
        courbe_koch(longueur, etape)  #Courbe de Von Koch
        right(72)

if __name__ == "__main__":
    down()

    flocon_koch(170, 2)