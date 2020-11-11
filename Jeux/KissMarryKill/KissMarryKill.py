"KISS MARRY KILL"
from random import*
filles1 = ["Margot ", "Nunzia ", "Chloé V ", "Chloé A ", "Emma ", "Marianne ", "Anaïs ", "Laura "]
#filles1.extend(["Alice ", "Sidonie ", "Clémentine ", "Kim ", "Solène ", "Armance ", "Lucie ", "Jeanne ", "Julie " ])


personnes = filles1
n = len(personnes)
points = {}
for i in personnes:
    points[i] = 0
passes = [0] * n

def choix(car):
    car = car.lower()
    if car == "k":
        return -1
    elif car == "m":
        return 5
    else : 
        return 3

def kmk(i,j,k):
    print(" ")
    print("KISS MARRY KILL")
    print(i,j,k)

    points[i] += choix(input(i))
    points[j] += choix(input(j))
    points[k] += choix(input(k))
    return


# for ii in range(len(personnes)):
#     for jj in range(ii+1, len(personnes)):
#         for kk in range(jj+1, len(personnes)):
dejafait = []
for a in range(3*n):
    while True: 
        while True : 
            ii = randrange(n-2)
            if passes[ii] <= 2 :
                break
        while True:    
            jj = randint(ii+1, n-2)
            if passes[jj] <= 2 or ii+1 == n-2: 
                break
        while True:
            kk = randint(jj+1, n-1)
            if passes[kk] <= 2 or jj+1 == n-1:
                break        
        if not (ii,jj,kk) in dejafait:
            break
    passes[ii] += 1
    passes[jj] += 1
    passes[kk] += 1
    
    dejafait.append((ii,jj,kk))
    i = personnes[ii]
    j = personnes[jj]
    k = personnes[kk]
    kmk(i,j,k)

print(" ")
print("===================")
personnes.sort()
personnes.reverse()
for per in personnes: 
    print(per, points[per])

