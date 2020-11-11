# LePetitCodeur14 - Prologin qualifications - problème 5

for i in range(3):
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

def recherche_dicho(listetriee, valeur): 
    a = 0
    b = len(listetriee)-1
    if valeur < listetriee[0]:
        return 0
    if valeur > listetriee[len(listetriee)-1]:
        return len(listetriee)-1


    milieu = (a+b) // 2
    while b - a > 1:
        if a==b+1 and valeur<listetriee[b] and valeur > listetriee[a]:
             return b
        
        if valeur == listetriee[milieu]:
            return milieu
        if valeur < listetriee[milieu]:
            b = milieu 
        else:
            a = milieu + 1
        milieu = (a+b) // 2   
    # if a==b:
    #     return milieu
    # if valeur < listetriee[a]:
    #     return a
    # elif valeur > listetriee[a] and valeur < listetriee[b]:
    #     return a+1
    # elif valeur > listetriee [b]:
    #     return b
    return b











def recherche_dicho2(listetriee, valeur):
    
    if valeur < listetriee[0]:
        return 0

    elif valeur > listetriee[len(listetriee)-1]:
        return len(listetriee)

    else:
        for i in range(len(listetriee)-1):
            if valeur > listetriee[i] and valeur < listetriee[i+1]:
                return i+1
    



def avancee(j, liste, old, new, listetriee):

    if j == 1:
        print("premier")
        # on initialise morceau_guirlande
        liste.extend(tailles[0:n])
        listetriee.extend(sorted(liste))
        print("-------------------------------------")
        print("liste ", liste )
        print("listetriee ", listetriee)
        print("j ", j)
        print(" ")
        return

    else:
        print("-------------------------------------")
        print("old ", old)
        print("new ", new)
        # print("liste avant ", liste )
        print("listetriee avant ", listetriee)
        # on modifie d'abord morceau_guirlande:
        del liste[0]
        liste.append(new)

        # puis on va modifier listetriee en enlevant le précedant
        # print(old,new,listetriee) ##deboguage
        ancien_emplacement = listetriee.index(old)
        del listetriee[ancien_emplacement]
        # print("listetriee milieu ", listetriee) #ça marche
        # et en rajoutant le suivant au bon endroit
        nouvel_emplacement = recherche_dicho2(listetriee, new)
        listetriee.insert(nouvel_emplacement, new)

        # if listetriee[nouvel_emplacement] < new and listetriee[nouvel_emplacement+1]>new:
        #     listetriee.insert(nouvel_emplacement, new)
        #     print("cas1")

        # elif listetriee[nouvel_emplacement] < new:
        #     listetriee.insert(nouvel_emplacement+1, new)
        #     print("cas2")

        # else:
        #     listetriee.insert(nouvel_emplacement-1, new)
        #     print("cas3     ")

        #débogage
        
        print("liste après ", liste )
        print("listetriee après", listetriee)
        print("j ", j)
        print(" ")
        return



def tri_et_retour(liste, listetriee): 
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

    ancienne_valeur = 0
    nouvelle_valeur = 0
    morceau_guirlande = []
    listetriee = []

    for j in range(1, m-n+2): #Boucle où on vérifie morceau par morceau le gabarit
        # morceau_guirlande = tailles[j:j+n] ##
        ancienne_valeur = tailles[j-2]
        nouvelle_valeur = tailles[j+n-2]

        # print(ancienne_valeur,nouvelle_valeur) # ça marche

        # faire attention pour la premiere valeur
        avancee(j, morceau_guirlande, ancienne_valeur, nouvelle_valeur,listetriee)
        morceau_guirlande2 = tri_et_retour(morceau_guirlande,listetriee)
        print("morceau_guirlande2  ",morceau_guirlande2)
        print("forme ", forme   )
        if morceau_guirlande2 == forme:
            liste_positions.append(j)
            print("ICI C'EST BON")

    #SORTIE
    print("-------------------------------------")
    print(len(liste_positions))
    for i in liste_positions:
        print(i, end=' ')




#ENTREES
(n, m) = list(map(int, input().split()))
motif = list(map(int, input().split()))
tailles = list(map(int, input().split()))
print(" ") # INUTILE
#EXECUTION
statuettes0(motif, n, tailles, m)
