
# w =[[1,1,0,0,1,0],[1,0,1,0,1,0],[0,1,0,1,0,0],[0,0,1,0,1,1],[1,1,0,1,0,0],[0,0,0,1,0,0]]
# n = 6
w= [[0,1000,-2,1000],[4,0,3,1000],[1000,1000,0,2],[1000,-1,1000,0]]
n = 4
for k in range(n):
    for i in range(n):
        for j in range(n):
            w[i][j] = min(w[i][j], w[i][k] + w[k][j])

print(w)

listevillesgares = []
    for c in range(g):
        trajet = gares[c]  
        depart = trajet["depart"] 
        arrivee = trajet["arrivee"]
        temps = trajet["temps"]
        listevillesgares.append(depart)

        w[depart - 1][arrivee + n - 1] = min(temps, w[depart - 1][arrivee + n- 1]) 
        w[depart + n - 1][arrivee + n - 1] = min(temps, w[depart + n][arrivee+n-1])

    for c in range(g):
        trajet = gares[c]
        depart = trajet["depart"] 
        arrivee = trajet["arrivee"] 
        temps = trajet["temps"]

        if depart in listevillesgares:
             w[depart + n-1][arrivee + n-1] = min(temps, w[depart + n-1][arrivee+n-1])

    # puis on ajoute les lignes de bus entre les villes
    # en ajoutant le temps d'attente à chaque fois
    # on doit aussi prendre en compte les lignes partant de gares routières
    print(listevillesgares)
    for b in range(m):
        trajet = lignes[b]
        depart = trajet["depart"]  #-1 car la liste est décalée de 1
        arrivee = trajet["arrivee"]
        temps = trajet["temps"]
        attente =  villes[depart-1] 

        w[depart][arrivee] = min(temps + attente, w[depart][arrivee])
        
        if depart in listevillesgares:
            w[depart+n-1][arrivee-1] = min(temps + attente, w[depart+n-1][arrivee-1])

    