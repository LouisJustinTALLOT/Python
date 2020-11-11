listex=[0,42]
for i in range (1,100000):
    xi  =   listex[i]
    listex.append((1337*xi+404)%1000000)
print(listex[1:])
print(42 in listex[2:])

print(sum(listex)/len(listex))

