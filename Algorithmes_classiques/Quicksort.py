from random import*
z = 0
def tri(li):
	global z
	n = len(li)

	if n <= 1:
		z += 1
		return li	
	
	sep = randrange(n)
	sep = li[sep]
	r1 = []
	r2 = []
	for i in li :
		if i < sep:
			r1.append(i)
		else:
			r2.append(i)
	z += 1
	return tri(r1)+tri(r2)
		



from time import*
# nb=10
# temps_total,temps_total2 = 0,0
# for i in range(nb):
# 	t1=time()
# 	tri(a)
# 	temps = time()-t1
# 	temps_total+=temps
# 	t2 = time()
# 	sorted(a)
# 	temps2=time()-t2	
# 	temps_total2+=temps2
# 
# temps_total /= nb
# z /= nb
# temps_total2 /= nb
# 
# print(" ")
# print("z",z)
# print("temps moyen",temps_total)
# print("temps de référence", temps_total2)
# print(temps_total/temps_total2)
from math import*
# loo=[]
# listetemps=[]
# listetemps2=[]
for taille in range(5000,10000,100):
	a = [i for i in range(taille)]
	shuffle(a)
	nb=10
	temps_total,temps_total2 = 0,0
	for i in range(nb):
		t1=time()
		tri(a)
		temps = time()-t1
		temps_total+=temps
		# t2 = time()
		# sorted(a)
		# temps2=time()-t2	
		# temps_total2 += temps2
	
	temps_total /= nb
	z /= nb
	# temps_total2 /= nb
	# print(temps_total,temps_total2)
	listetemps.append(z)
	# listetemps2.append(temps_total2)
	loo.append(taille*log(taille))
###
nnn=[i for i in range(5419)]
nnn.extend([i for i in range(5000,10000,100)])
from matplotlib.pyplot import*
# subplot(2,1,1)
plot(listetemps,nnn)
# subplot(2,1,2)
plot(loo,nnn)
# plot(listetemps2)
show()