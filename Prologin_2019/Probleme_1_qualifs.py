def arnaque_aerienne0(prix_initial, billets, n):
    compteur = 0
    for i in range(n):
        if billets[i]<prix_initial:
            compteur +=1 
        if compteur>=3 :
                break

    if compteur>=3 :
        print( "ARNAQUE !")
    else:
        print( "Ok bon voyage, bisous, n'oublie pas de m'envoyer des photos ! ")
        
prix_initial = int(input())
n = int(input())
billets = list(map(int, input().split()))
arnaque_aerienne0(prix_initial, billets, n)
###########################################################################################
# prix_initial = int(input("Quel est le prix du billet de Joseph ?"))
# n = int(input("Quel est le nombre de billets trouvés par Haruhi ? "))
# billets=input("Liste des prix des billets trouvés par Haruhi : ").split()

# compteur = 0
# for i in range(n):
#     if billets[i]<prix_initial:
#         compteur +=1 
#     if compteur>=3 :
#             break

# if compteur>=3 :
#      print("ARNAQUE")
# else:
#     print("Ok bon voyage, bisous, n'oublie pas de m'envoyer des photos ! ")
