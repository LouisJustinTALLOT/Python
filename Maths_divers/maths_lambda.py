from math import*
from turtle import*
# reset()
# up()
# width(2)
# u=0
# for n in range(1,1000):
#     u=(1/n)*(gcd(20,n))
#     print(u)
#     up()
#     goto(n-500,300*u-250)
#     down()
#     forward(1)
#     up()
# 
# for i in range(10):
#     print(i*(i+1)//2,'     ',i)
#     
for x in range(11):
    for y in range(11):
        if x**2-8*y**2==1:
            print('(x= ',x,' ; y= ',y,')')
    