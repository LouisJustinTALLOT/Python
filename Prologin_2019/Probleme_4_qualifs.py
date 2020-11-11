# LePetitCodeur14 - Prologin qualifications - problème 4

# CONTRAINTES
# 1≤n≤150
# 0≤m≤20000
# 0≤g≤20000
# 0≤temps≤1000
def print_mat(mat):
    for ligne in mat:
        for temps in ligne:
            if temps==1e300:
                print("     ∞",end=" ")
            else:
                print(" "*(6-len(str(temps)))+str(temps),end=" ")
        print(" ")

def la_meilleure_ville0(villes, n, lignes, m, gares, g):
    # on va tout d'abord initialiser la matrice w sous la forme
    # d'une matrice carrée 2n * 2n
    w=[]

    for i in range(2*n):
        w.append([1e300]*2*n) #le 1e300 remplace l'infini pour Floyd-Warshall
    # puis on va mettre la diagonale à 0
    # for a in range(2*n):
    #     if w[a][a] == 1e300:
    #         w[a][a] = 0

    # puis on fait de même avec les lignes qui vont aux gares routières
    # on doit aussi prendre en compte les lignes partant de gares routières
    # de plus il n'y a pas de temps d'attente
    listevillesgares = []
    for c in range(g):
        trajet = gares[c]        
        depart = trajet["depart"] - 1
        arrivee = trajet["arrivee"] - 1
        temps = trajet["temps"]
        listevillesgares.append(arrivee)
        attente =  villes[depart] 
        w[depart][arrivee + n] = min(temps+attente, w[depart][arrivee + n]) 
        
        #w[depart + n][arrivee + n] = min(temps, w[depart + n][arrivee + n])

    for c in range(g):
        trajet = gares[c]    
        depart = trajet["depart"] - 1
        arrivee = trajet["arrivee"] - 1
        temps = trajet["temps"]
        
        if depart in listevillesgares:
            w[depart + n][arrivee + n] = min(temps, w[depart + n][arrivee + n])
            # print("gare",trajet)
            # print(w[depart+n][arrivee+n])    
    # puis on ajoute les lignes de bus entre les villes
    # en ajoutant le temps d'attente à chaque fois
    # on doit aussi prendre en compte les lignes partant de gares routières

    # print("listevillesgares",listevillesgares)
    # print(" ")
    for b in range(m):
        trajet = lignes[b]
        depart = trajet["depart"] - 1 #-1 car la liste est décalée de 1
        arrivee = trajet["arrivee"] -1
        temps = trajet["temps"]
        attente =  villes[depart] 
        
        w[depart][arrivee] = min(temps + attente, w[depart][arrivee])
        
        if depart in listevillesgares:
            w[depart + n][arrivee] = min(temps , w[depart + n][arrivee])
            # print("ligne",trajet)
            # print("depart+1 ",depart+1, w[depart+n][arrivee])



    # for a in range(n):
    #         w[a+n][a] = 1e300
    #         w[a][a+n] = 1e300
    # print_mat(w)
    # print("\n")
    # on va appliquer l'algorithme de Floyd - Warshall
    for k in range(len(w)):
        for i in range(len(w)):
            for j in range(len(w)):
                w[i][j] = min(w[i][j], w[i][k] + w[k][j])

    # print_mat(w)
    # print(" ")
    # on va maintenant calculer les scores de chaque ville:
    liste_scores=[]
    for ville in range(n):
        score = -1
        nbvilles = 0
        for k in range(n):
            if w[ville][k] != 1e300 and k != ville:
                nbvilles += 1
                if score == -1 :
                    score = w[ville][k]
                else:
                    score += w[ville][k]
        # print(ville+1, score, nbvilles)
        if nbvilles != 0:
            score //= nbvilles

        liste_scores.append(score)

    # et enfin on affiche les scores dans l'ordre :
    for score in liste_scores:
        print(score)

# ENTREES
(n, m, g) = list(map(int, input().split()))
villes = [None] * n
for i in range(0, n):
    villes[i] = int(input())
lignes = [None] * m
for j in range(0, m):
    (depart, arrivee, temps) = list(map(int, input().split()))
    trajet = {"depart":depart, "arrivee":arrivee, "temps":temps}
    lignes[j] = trajet
gares = [None] * g
for k in range(0, g):
    (dep, arr, tmp) = list(map(int, input().split()))
    traj = {"depart":dep, "arrivee":arr, "temps":tmp}
    gares[k] = traj
# 
# (n,m,g)=(3, 2, 2)
# villes = [5, 11, 2] 
# lignes = [{'depart': 1, 'arrivee': 1, 'temps': 5}, {'depart': 3, 'arrivee': 2, 'temps': 22}]
# gares = [{'depart': 2, 'arrivee': 1, 'temps': 5}, {'depart': 1, 'arrivee': 2, 'temps': 3}]
# 
# (n,m,g)=(3, 4, 1)
# villes =  [5,5,10]
# lignes = [{'depart': 1, 'arrivee': 2, 'temps': 2}, {'depart': 2, 'arrivee': 1, 'temps': 20}, {'depart': 2, 'arrivee': 3, 'temps': 1}, {'depart': 3, 'arrivee': 1, 'temps': 5}]
# gares = [{'depart': 2, 'arrivee': 3, 'temps': 5}]

# (n,m,g) = (5, 10, 7)
# villes = [2, 5, 3, 8, 7]
# lignes = [{'depart': 1, 'arrivee': 2, 'temps': 6}, {'depart': 1, 'arrivee': 5, 'temps': 3}, {'depart': 2, 'arrivee': 1, 'temps': 3}, {'depart': 2, 'arrivee': 5, 'temps': 9}, {'depart': 2, 'arrivee': 3, 'temps': 3}, {'depart': 3, 'arrivee': 5, 'temps': 5}, {'depart': 3, 'arrivee': 4, 'temps': 1}, {'depart': 4, 'arrivee': 2, 'temps': 9}, {'depart': 5, 'arrivee': 4, 'temps': 2}, {'depart': 5, 'arrivee': 3, 'temps': 30}]
# gares = [{'depart': 1, 'arrivee': 4, 'temps': 4}, {'depart': 5, 'arrivee': 4, 'temps': 7}, {'depart': 5, 'arrivee': 3, 'temps': 3}, {'depart': 4, 'arrivee': 3, 'temps': 3}, {'depart': 3, 'arrivee': 2, 'temps': 8}, {'depart': 2, 'arrivee': 3, 'temps': 5}, {'depart': 2, 'arrivee': 1, 'temps': 6}]


la_meilleure_ville0(villes, n, lignes, m, gares, g)
