# LePetitCodeur14 - Prologin qualifications - problème 5
def nouvelle_liste_triee(j,liste_precedente,valeur_precedente):
    old_position = liste_precedente.index(valeur_precedente)
    del liste_precedente[old_position]
    a, b = 0, len(liste_precedente)-1
    nouvelle_valeur = tailles[j]
    print((a,b))
    # Recherche dichotomique
    while (b-a)/2 > 0 :  
        if liste_precedente[(a+b)//2] < nouvelle_valeur: 
            a = (a+b)//2 + 1                         
        else :                                          
            b = (a+b)//2 - 1
        print((a,b))
    liste_precedente.insert(a,nouvelle_valeur)
    return liste_precedente
  
def tri_et_retour(liste,listetriee):    #A AMELIORER EN TERMES DE COMPLEXITE
    # listetriee=sorted(liste) #prend du temps O(n log(n)) 
    res=[]
    
    for i in range(len(liste)):
        for j in range(len(liste)):
            if liste[i]==listetriee[j]:
                res.append(j+1)
                break
    return res

def statuettes0(motif, n, tailles, m):
    if n > m :
        print(0)
        return

    liste_positions=[]
    #initialisation de la liste des tailles:
    forme = [0]*n               #
    for i in range(n):          # On initialise la forme de la photo
        forme[motif[i]-1]= i+1  #
    listetriee = sorted(tailles[:n])
    for j in range(m-n+1): #Boucle où on vérifie morceau par morceau le gabarit
        if j != 0:
            listetriee = nouvelle_liste_triee(j,listetriee,tailles[j-1])

        morceau_guirlande = tailles[j:j+n]
        morceau_guirlande = tri_et_retour(morceau_guirlande,listetriee)
        if morceau_guirlande == forme:
            liste_positions.append(j) 

    #SORTIE
    print(len(liste_positions))
    for i in liste_positions:
        print(i+1, end=' ')

#ENTREES
(n, m) = list(map(int, input().split()))
if n <= m:
    motif = list(map(int, input().split()))
    tailles = list(map(int, input().split()))
# print(" ")##INUTILE
#EXECUTION
statuettes0(motif, n, tailles, m)
