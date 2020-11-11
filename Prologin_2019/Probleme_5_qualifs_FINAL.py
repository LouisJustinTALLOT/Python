# LePetitCodeur14 - Prologin qualifications - problème 5

def recherche_dicho(listetriee, valeur): 
    if listetriee == []:
        return 0
    a = 0
    b = len(listetriee)-1    
    if valeur < listetriee[0]:
        return 0

    elif valeur > listetriee[len(listetriee)-1]:
        return len(listetriee)

    while b - a > 3:
        milieu = (a+b) // 2
        if valeur == listetriee[milieu]:
            return milieu
        if valeur < listetriee[milieu]:
            b = milieu 
        else:
            a = milieu 
        
    if listetriee[a] < valeur and valeur < listetriee [a+1]:
        return a+1
    elif listetriee[a+1] < valeur and valeur < listetriee [a+2]:
        return a+2
    elif listetriee[a+2] < valeur and valeur < listetriee [a+3]:
        return a+3

def recherche_indice(valeur,listetriee):
    a=0
    b=len(listetriee)-1
    milieu = (a+b)//2
    while b-a>=0:
        milieu = (a+b) // 2
        if valeur == listetriee[milieu]:
            return milieu
        if valeur < listetriee[milieu]:
            b = milieu - 1
        else:
            a = milieu + 1
    return milieu

def avancee(j, liste, old, new, listetriee):
    
    if j == 1:
        # on initialise morceau_guirlande
        liste.extend(tailles[0:n])
        listetriee.extend(sorted(liste))
        return

    else:
        # on modifie d'abord morceau_guirlande:
        del liste[0]
        liste.append(new)
        # puis on va modifier listetriee en enlevant le précedant
        ancien_emplacement = recherche_indice(old,listetriee) 
        del listetriee[ancien_emplacement]
        # et en rajoutant le suivant au bon endroit
        nouvel_emplacement = recherche_dicho(listetriee, new)
        listetriee.insert(nouvel_emplacement, new)
        return


def tri_et_retour(liste, listetriee): 
    res=[]
    for i in range(len(liste)):        
        nvelindice = recherche_indice(liste[i],listetriee)
        res.append(nvelindice+1)
   
    return res



def statuettes0(motif, n, tailles, m):
    liste_positions = []
    #initialisation de la liste des tailles:
    forme = [0]*n
    for i in range(n):
        forme[motif[i]-1]= i+1
    ancienne_valeur = 0
    nouvelle_valeur = 0
    morceau_guirlande = []
    listetriee = []

    for j in range(1, m-n+2): #Boucle où on vérifie morceau par morceau le gabarit
        ancienne_valeur = tailles[j-2]
        nouvelle_valeur = tailles[j+n-2]

        avancee(j, morceau_guirlande, ancienne_valeur, nouvelle_valeur,listetriee)
        morceau_guirlande2 = tri_et_retour(morceau_guirlande,listetriee)
        
        if morceau_guirlande2 == forme:
            liste_positions.append(j)
        
    #SORTIE
    print(len(liste_positions))
    for i in liste_positions:
        print(i, end=' ')




#ENTREES
(n, m) = list(map(int, input().split()))
motif = list(map(int, input().split()))
tailles = list(map(int, input().split()))

statuettes0(motif, n, tailles, m)

