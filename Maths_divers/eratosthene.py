import time
from math import*
# from os import chdir
# chdir("D:/0Tale S1/Python")
prem=[2]
tt1=time.time()
i,p,j=3,1,0
while len(prem)<1000000:
    while prem[j]<=sqrt(i):
        if i%prem[j]==0:
            p=0
            break
        j+=1
    if p==1:
        prem.append(i)
        # print(str(i), end='           ')
        # # print(len(prem))
        # if (10*len(prem))%1000000==0:
        #     print(100*len(prem)//1000000, end =' %\n')
    i,p,j=i+2,1,0
# print('enregistrement')


ob=open('listeprem.txt','w')

for i in range(0,len(prem)-1):
    ob.write(str(prem[i]))
    #ob.write('                ')
    #ob.write(str(i+1))
    ob.write('\n')
ob.write(' ')

ob.close()

tt2=time.time()
print(tt2-tt1, end=' secondes')