def meli_melo_temporel0(lieux, n, etapes, v):
    decalage_total = 0
    decalage_haruhi = 0
    decalage_joseph = 0
    for i in range(v):
        voy = liste_e[i]["voyageur"]
        dest = liste_e[i]["destination"]
        dec = liste_p[dest-1]["decalage"]
        if voy == 1:
            decalage_haruhi = dec
        else : 
            decalage_joseph = dec

        if decalage_joseph*decalage_haruhi < 0:
            print(abs(decalage_haruhi)+abs(decalage_joseph))

        else :
            print(abs(decalage_haruhi-decalage_joseph))


#ENTREES
    #liste des pays
n = int(input())
liste_p = [None] * n
for i in range(0, n):
    (id, decalage) = list(map(int, input().split()))
    lieux_i = {"id":id, "decalage":decalage}
    liste_p[i] = lieux_i

    #liste des voyages
v = int(input())
liste_e = [None] * v
for j in range(0, v):
    (voyageur, destination) = list(map(int, input().split()))
    etape_i = {"voyageur":voyageur, "destination":destination}
    liste_e[j] = etape_i

#EXECUTION DU PROGRAMME
meli_melo_temporel0(liste_p, n, liste_e, v)
