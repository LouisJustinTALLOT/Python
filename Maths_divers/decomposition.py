from math import*
from os import chdir
#chdir("D:/0Tale S1/Python")


print(' ',' ',' ')
n=int(input("Nombre à décomposer ?  "))
i,dec,m= 0,[0],n
#while n!=1:
#    if n%i==0:
#        n=n//i
#        dec[len(dec)-1]=i
#        dec.append(0)
#        print(i)
#        i-=1
#    i+=1
#if dec[len(dec)-1]==0:
#    del(dec[len(dec)-1])
#print(dec)


prem=[0]

ob=open('listeprem.txt','r')
while True: 
    txt=ob.readline()
    if txt==' ':
        break
    prem[len(prem)-1]=int(txt)
    prem.append(0)
if prem[len(prem)-1]==0:
    del(prem[len(prem)-1])
#prem = ob.readlines()
#print(prem)
# print('pret')

while (prem[i]<=m) and (n!=1):
    if n%prem[i]==0:
        while n%prem[i]==0:
            dec[len(dec)-1]=prem[i]
            dec.append(0)
            print (prem[i])
            n //=prem[i]
    i=i+1
if dec[len(dec)-1]==0:
    del(dec[len(dec)-1])

print(dec)
