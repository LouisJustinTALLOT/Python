# LePetitCodeur14 - Prologin qualifications - problème 5
from time import*
# IDEE if listetriee[a]<valeur < listetriee[a+1]:
# return a+1

# + les deux conditions des extrèmes au début et c est bon



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
        # print("recherche_dicho")
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




def recherche_pasdicho(listetriee, valeur):
    
    if valeur < listetriee[0]:
        return 0

    elif valeur > listetriee[len(listetriee)-1]:
        return len(listetriee)

    else:
        for i in range(len(listetriee)-1):
            if valeur > listetriee[i] and valeur < listetriee[i+1]:
                return i+1
    
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
        # print("avance 1")
        # puis on va modifier listetriee en enlevant le précedant

        
        # ancien_emplacement = listetriee.index(old)
        ancien_emplacement = recherche_indice(old,listetriee) 
        del listetriee[ancien_emplacement]
        # et en rajoutant le suivant au bon endroit
        # print("avance 2")
        # nouvel_emplacement = recherche_pasdicho(listetriee, new)        
        nouvel_emplacement = recherche_dicho(listetriee, new)

        listetriee.insert(nouvel_emplacement, new)
        # print("fin avance")
        return


def tri_et_retour(liste, listetriee): 
    res=[]
    for i in range(len(liste)):
        # print(i)
        # for j in range(len(liste)):
        #     if liste[i]==listetriee[j]:
        #         res.append(j+1)
        #         break
        
        nvelindice = recherche_indice(liste[i],listetriee)
        # print(type(nvelindice))
        # print(liste,listetriee)
        # print(liste[i],listetriee[nvelindice])
        res.append(nvelindice+1)
    # print(res)
    return res


jj=0

def statuettes0(motif, n, tailles, m):
    liste_positions = []
    #initialisation de la liste des tailles:
    forme = [0]*n
    for i in range(n):
        forme[motif[i]-1]= i+1
    # print("ici")
    ancienne_valeur = 0
    nouvelle_valeur = 0
    morceau_guirlande = []
    listetriee = []

    global jj
    for j in range(1, m-n+2): #Boucle où on vérifie morceau par morceau le gabarit
        jj=j
        # morceau_guirlande = tailles[j:j+n] ##
        ancienne_valeur = tailles[j-2]
        nouvelle_valeur = tailles[j+n-2]
        # print("là")
        # faire attention pour la premiere valeur

        avancee(j, morceau_guirlande, ancienne_valeur, nouvelle_valeur,listetriee)
        # print("jean-pierre")
        morceau_guirlande2 = tri_et_retour(morceau_guirlande,listetriee)
        
        # print(morceau_guirlande,morceau_guirlande2,listetriee,forme)
        # print("jean-paul")
        if morceau_guirlande2 == forme:
            liste_positions.append(j)
        
    #SORTIE
    print(len(liste_positions))
    # for i in liste_positions:
    #     print(i, end=' ')




#ENTREES
# (n, m) = list(map(int, input().split()))
# motif = list(map(int, input().split()))
# tailles = list(map(int, input().split()))

from random import*

n=5
m=100000
print(n,m)
tailles= [n for n in range(1,m+1)]
shuffle(tailles)

motif=[i for i in range(1,n+1)]
shuffle(motif)
print("here")

#limite entre les deux : 30

#EXECUTION

t1=time()
statuettes0(motif, n, tailles, m)
print(" ")
print("{} secondes".format(time()-t1))
print(" ")
######################################################################
######################################################################
######################################################################
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

def tri_et_retour2(liste):
    listetriee=sorted(liste)
    res=[]
    for i in range(len(liste)):
        # for j in range(len(liste)):
        #     if liste[i]==listetriee[j]:
        #         res.append(j+1)
        #         break
        nvelindice = recherche_indice(liste[i],listetriee)
        
        res.append(nvelindice+1)
    return res

def statuettes(motif, n, tailles, m):
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
        global jj
        jj=j
        morceau_guirlande = tailles[j:j+n]
     
        morceau_guirlande = tri_et_retour2(morceau_guirlande)
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
    # for i in liste_positions:
    #     print(i+1, end=' ')

#ENTREES
# (n, m) = list(map(int, input().split()))
# motif = list(map(int, input().split()))
# tailles = list(map(int, input().split()))

#EXECUTION
t2 = time()
statuettes(motif, n, tailles, m)
print("\n",end="")
print("{} secondes".format(time()-t2))

