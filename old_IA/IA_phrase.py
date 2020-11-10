# from math import*
from random import random, randint, randrange
from time import time

pop=500 #taille de la population
mutations=float(input('Taux de mutations ? '))
resultat=input("Tapez une phrase: ")
date1=time()
long=len(resultat)
caracteres="""abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ éèùîêçà1234567890°@^ïëô%$£€,?;.:/!§&é"'(-_ç~#{[|\]}<>¤*"""
# print(len(caracteres))

vivier=['']*pop                #création de la liste contenant les chaînes
# for i in range(pop):      #remplissage de la liste vivier
#     vivier.append('')
#     

# CREATION DE LA POPULATION INITIALE
for i in range(0,pop):
    
    for j in range(0 ,long):
        vivier[i]+=caracteres[randint(0,len(caracteres)-1)]
   
        
listeFinesse=[]
#fonction finesse en elle-même
def fonctFin (x):
    return(x**2)

listePourcentages=[]
# CALCUL DE LA FINESSE
def finesse(ch):
    fin=0
    for i in range(long):
        if ch[i]==resultat[i]:
            fin=fin+1
    listeFinesse.append(fonctFin(fin)) 
    listePourcentages.append(int((100*fin)/long))

meilleur=fmax=0

def meilleurCandidat():
    global meilleur
    meilleur=0
    # fmax=max(listeFinesse)
    for ii in range(pop):
        if listeFinesse[ii] == max(listeFinesse):
            print(max(listeFinesse), end='   ')
            meilleur=ii
            print(vivier[ii], end ='          ')
            return

# ENTREE DANS LA BOUCLE
gen=0 #nb de générations
choix=''
par1=par2=enf1=enf2=''
# for k in range(pop):
    # finesse(vivier[k])#Calcul des finesses de toutes les chaînes
oui=0
# meilleurCandidat()
print('')
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
while (oui==0): #BOUCLE PRINCIPALE
    parents=[]
    listeFinesse=listePourcentages=[]
    for k in range(pop):
        finesse(vivier[k])  #Calcul des finesses de toutes les chaînes
    meilleurCandidat()
    print(gen,'      ',max(listePourcentages),'% trouvés')
    for yy in range(pop):
        if vivier[yy]==resultat:
            oui=1
            break
    # listeFinesse.sort() #en fait inutile
    if oui==1:
        break
    while len(parents)!=pop: #boucle de constitution du vivier de parents (élimination des plus mauvais)
        jj=randrange(pop)
        choix=vivier[jj]
        if listeFinesse[jj]>=randrange(max(listeFinesse)):
            parents.append(choix)
    
    vivier=[]
    for uu in range(int(pop/2)): #boucle de reproduction des parents
        par1=parents[uu]
        par2=parents[pop-1-uu]
        enf1=""
        enf2=""
        dd=randrange(long)
        for a in range(dd):
            enf1+=par1[a]
            enf2+=par2[a]
        for b in range(dd,long):
            enf1+=par2[b]
            enf2+=par1[b]
        vivier.append(enf1)
        vivier.append(enf2)
        
    # print(vivier)
    # input()
    provisoire=chchch=''
    #INTRODUCION DE L'ALEATOIRE
    for qq in range(pop):
        provisoire=''
        chchch=vivier[qq]
        for zz in range(long):
            if random()<=mutations:
                provisoire+=caracteres[randrange(len(caracteres))]
            else:
                provisoire+=chchch[zz]   
               
        vivier[qq]=provisoire
    # print('\n')
    gen+=1 #on augmente le no de la génération

print(max(listeFinesse),'    ', resultat,'          ', gen,'        ',int(time()-date1)+1,'  secondes écoulées')
    
#     zone de tests
# for k in range(pop):
#     finesse(vivier[k])
# meilleurCandidat()
# listeFinesse.sort()
# print(listeFinesse)