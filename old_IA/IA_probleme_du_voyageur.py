"problème du voyageur"

# 1- création du vivier (initialisation)
# 2- calcul de la finesse (évaluation)
# 3- sélection des meilleurs
# 4- croisement des individus pour obtenir la génération suivante
# 5- mutation 
# on répéte 2-5 pendant g générations

import numpy as np
from math import*
import matplotlib.pyplot as plt
import random as rd

# variables : 

nb_villes = 10          # nombre de villes   UN NOMBRE PAIR !!!!
g = 100                  # nombre de générations
pop = 1000               # taille de la population
dim_grille = 10000       # taille de la grille 
proba_mutation = 0.1

plt.close()

#partie représentation graphique
def grapher_les_villes(table_villes):

    plt.close()
    for i in range(len(table_villes)):
        ii = str(i)
        plt.plot([table_villes[i,0]],[table_villes[i,1]],label = 'bonj', marker = 'o')
    # plt.show()
    return


def afficher_chemin(chemin,table_villes):

    ch = chemin[1]
    table_x = []
    table_y = []
    for i in range(nb_villes):
        table_x.append(table_villes[ch[i],0])
        table_y.append(table_villes[ch[i],1])
    plt.plot(table_x,table_y)
    # plt.show()
    return

# il nous faut d'abord une population de villes...

def creation_villes():
    villes = np.zeros((nb_villes,2))

    for i in range(nb_villes):
        villes[i,:] = rd.randrange(dim_grille), rd.randrange(dim_grille)
            
        while villes[i,:] in villes[:i,:]:
            villes[i,:] = rd.randrange(dim_grille), rd.randrange(dim_grille)
  
    return villes

def tableau_distances_villes(table_villes):
    distances = np.zeros((nb_villes,nb_villes))
    for i in range(nb_villes):
        for j in range(nb_villes):
            distances[i,j] = sqrt((table_villes[i][0]-table_villes[j][0])**2+(table_villes[i][1]-table_villes[j][1])**2)
    return distances
   
""" pour les chemins : on va représenter ça de la manière suivante : 

chemin = [longueur, [ville 1, ville 2, ville 3,..., ville n]]             """

def calculer_longueur_chemin(chemin, distances):
    """calcule la longueur du chemin"""
    long = 0
    
    for i in range(nb_villes-1):
        long += distances[chemin[1][i], chemin[1][i+1]] 

    chemin[0] = long
    return long

def normaliser_chemin(chemin,distances):
    """ on checke si le chemin parcourt bien toutes les villes, 
    sans doublon, et si besoin on les rajoute à la fin """

    chemin_neuf = []

    for i in range(nb_villes):
        if chemin[1][i] not in chemin_neuf and chemin[1][i] < nb_villes:
            chemin_neuf.append(chemin[1][i])
  
    if len(chemin_neuf) != nb_villes:
        for i in range(nb_villes):
            if i not in chemin_neuf:
                chemin_neuf.append(i)

    return [calculer_longueur_chemin([0,chemin_neuf], distances), chemin_neuf]

""" la population (le vivier) va être représentée sous la forme d'une liste de chemins,
    au nombre de pop"""

def première_génération(distances):

    listedesnombresdanslordre = [i for i in range(nb_villes)]
    vivier = []   

    for i in range(pop):
        new = listedesnombresdanslordre[:]
        rd.shuffle(new)
        vivier.append([calculer_longueur_chemin([0,new],distances),new])

    return vivier

def classement_dans_l_ordre(vivier):
    vivier.sort(key = lambda x : x[0])

    return vivier

def selection_des_meilleurs(vivier):
    vivier = vivier[:pop//2]
    return vivier




def reproduction_des_meilleurs(vivier,distances):
    entiers = [i for i in range(pop)]
    for i in range(pop-pop//2):
        nouveau_chemin = []

        ch1, ch2 = rd.sample(entiers,2)

        nouveau_chemin = [0, vivier[ch1][1][:nb_villes//2]+vivier[ch2][1][nb_villes//2:]]
        nouveau_chemin = normaliser_chemin(nouveau_chemin,distances)

        vivier.append(nouveau_chemin)

    return vivier

def muter_chemin(chemin, distances):
    i,j = rd.sample([i for i in range(nb_villes)], 2)
    chemin[1][i], chemin[1][j] = chemin[1][j], chemin[1][i]
    chemin[0] = calculer_longueur_chemin(chemin, distances)
    return chemin
    

def mutation_du_vivier(vivier, proba, distances):
    for i in range(pop):
        if rd.random() < proba :
            muter_chemin(vivier[i],distances)
    return


# ok maintenant on va faire le vrai programme 

table_villes = creation_villes()
# print(table_villes)

distances = tableau_distances_villes(table_villes)
# print(distances)

vivier = première_génération(distances)
# print(vivier)
# print("")

for numero_generation in range(1,g+1):      # BOUCLE PRINCIPALE
    print(numero_generation)
    classement_dans_l_ordre(vivier)
    # print(vivier[0])

    selection_des_meilleurs(vivier)
    # print(vivier)

    reproduction_des_meilleurs(vivier, distances)
    # print(vivier)

    mutation_du_vivier(vivier, proba_mutation, distances)
    # print(vivier)
    
    if numero_generation%10 == 1 :
        classement_dans_l_ordre(vivier)
        print(vivier[0])
        grapher_les_villes(table_villes)
        afficher_chemin(vivier[0],table_villes)


classement_dans_l_ordre(vivier)
print(vivier[0])

grapher_les_villes(table_villes)

afficher_chemin(vivier[0],table_villes)

plt.show()