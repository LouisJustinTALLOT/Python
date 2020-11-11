"KISS MARRY KILL"
from random import*
filles1 = ["Margot ", "Nunzia ", "Chloé V ", "Chloé A ", "Emma T ", "Marianne ", "Anaïs ", "Laura "]
filles1.extend(["Alice ", "Sidonie ", "Clémentine ", "Kim ", "Solène ", "Armance ", "Lucie ", "Jeanne ", "Julie " ])

mecs1 = ['Axel ', 'Neil ','Adrien ','Noé ', 'Philippe ', 'Quentin ', 'Raouf ', 'JB ','Arthur ', 'LJ ', 'Enzo ', 'Hugo ', 'Thomas ', 'Hippolyte ','Luc ','Max ', 'Matthis ', 'Sylvain ', 'Guillaume ', 'Ethan ', 'Cyprien ', 'Romain Li ','Léonard ', 'Lucas ', 'Antoine ', 'Eddie ', 'Timothée ', 'Rémy D ','Abel ','Ambroise ']

mecs2 =['Rémy T ','Manoj ','Clement ','Gabriel ','Anh-Minh ','Damian ','Alex ','Manu ','Paul ', 'Remi C ','Matthieu ','Zerui ','Romain  B ']

filles2 = ['Elsa ','Laurine ',"Sillvya ", 'Sandrine ','Jacqueline ','Madeleine ','Maïra ','Aya ','Emma F ','Isabeau ','Léonie ','Chloé R ','Julia ','Hélène ']

hx1 = mecs1+ filles1
lycee = mecs2+filles2
tout = hx1+lycee
mecs= mecs1 + mecs2
filles = filles1+filles2

personnes = filles
shuffle(personnes)
n = len(personnes)
kl = {}
fk = {}
mar = {}
points = {}
passes = {}
for i in personnes:
    kl[i] = 0
    fk[i] = 0
    mar[i] = 0
    points[i] = 0
    passes[i] = 0
    


def choix(car):
    car = car.lower()
    if car == "k":
        return -17
    elif car == "m":
        return 19
    else : 
        return 11

def kmk(i,j,k,a):
    print(" ")
    print("KISS MARRY KILL ",a)
    print(i,j,k)
    for p in [i,j,k]:
        o = choix(input(p))
        # o = choix("k")
        points[p] += o
        if o == -17 :
            kl[p] += 1
        elif o == 19 : 
            mar[p] += 1
        elif o == 11 : 
                fk[p] += 1
    	   
    return


# for ii in range(len(personnes)):
#     for jj in range(ii+1, len(personnes)):
#         for kk in range(jj+1, len(personnes)):
	
	
dejafait = []
for a in range(20):
    while True: 
#dejafait = []
#for a in range(10):
#    while True: 
#        while True : 

         ii = randrange(n-2)
#            if passes[ii] <= 2 :
#                break
#        while True:    

         jj = choice([i for i in range(n) if i != ii])
#            if passes[jj] <= 2 or ii+1 == n-2: 
#                break
#        while True:

         kk = choice([i for i in range(n) if i != jj and i != ii])
         if not (ii,jj,kk) in dejafait:
          	break

    
    dejafait.append((ii,jj,kk))
    i = personnes[ii]
    j = personnes[jj]
    k = personnes[kk]
    
    passes[i] += 1
    passes[j] += 1
    passes[k] += 1
    kmk(i,j,k,a+1)

print(" ")
print("===================")
personnes.sort()
#personnes.reverse()
for per in personnes: 
    print(per, ' '*(15-len(per)),end ='')
    if kl[per]==0:
         print('        ',end ='')
    else:
         print(' kl : ',kl[per],end ='')
         
    if fk[per] ==0:
    	print('        ',end = '')   
    else:
     	print(' fk : ', fk[per], end ='')
     	
    if mar[per]==0 :
    	print('          ', end = ' ')
    else:
        print(' mar : ',mar[per], end = '  ')
    
    print('  TOTAL :   ',points[per])

tot = []
for p in personnes:
	try:
		tot.append((p,points[p]/passes[p]))
	except:
		'rien'
tot.sort(key = lambda x:x[1])
print('')
print('')
# print('FLOP 5')
# for i in range(5):
#     print(tot[i])
tot.reverse()
# print('')
# print('TOP 5')
# for i in range(5):
#     print(tot[i])
# print(passes)
print('CLASSEMENT : \n')

for i in range(len(tot)):
    print(tot[i])