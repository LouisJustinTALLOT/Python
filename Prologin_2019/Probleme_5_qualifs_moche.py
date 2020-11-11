# LePetitCodeur14 - Prologin qualifications - problème 5


def tri_et_retour(liste):
    listetriee=sorted(liste)
    res=[]
    for i in range(len(liste)):
        for j in range(len(liste)):
            if liste[i]==listetriee[j]:
                res.append(j+1)
                break
    return res

def statuettes0(motif, n, tailles, m):
    liste_positions=[]
    #initialisation de la liste des tailles:
    forme = [0]*n
    for i in range(n):
        forme[motif[i]-1]= i+1
    #print('forme',forme)##INUTILE
    # rapports=[]
    # for i in range(n-1):
    #     rapports.append(forme[i]/forme[i+1])

    for j in range(m-n+1): #Boucle où on vérifie morceau par morceau le gabarit
        morceau_guirlande = tailles[j:j+n]
     
        morceau_guirlande = tri_et_retour(morceau_guirlande)
       # print(morceau_guirlande)##INUTILE
        if morceau_guirlande == forme:
            liste_positions.append(j) 
        # rapports_guirlande=[]
        # for k in range(n-1):
        #    rapports_guirlande.append(morceau_guirlande[k]/morceau_guirlande[k+1]) 
        # for l in range(len(rapports)-1):
        #     #on va trier la sous-liste  
        #     liste_positions.append(j)

    #SORTIE
    print(len(liste_positions))
    for i in liste_positions:
        print(i+1, end=' ')

#ENTREES
(n, m) = list(map(int, input().split()))
motif = list(map(int, input().split()))
tailles = list(map(int, input().split()))

#EXECUTION
statuettes0(motif, n, tailles, m)
