# from math import*
i=t=c=choix=0
choix=int(input('Entrez 0 pour coder et 1 pour décoder :   '))
ch="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if choix:
    message=input('message à décoder:  ')
    message=message.lower()
    message=message.replace('é','e')
    message=message.replace('à','a')
    message=message.replace('è','e')
    message=message.replace('ù','u')
    message=message.replace('ç','c')
    message=message.replace(' ','')
    message=message.upper()
    for i in message:
        for t in range(26):
            if ch[t]==i:
                break
        # c=(11*t+8)%26 
        # c=(19*t-8*19)%26
        c=(19*t+4)%26
        print(ch[c], end='')
    
else:
    message=input('message à coder:  ')
    message=message.lower()
    message=message.replace('é','e')
    message=message.replace('à','a')
    message=message.replace('è','e')
    message=message.replace('ù','u')
    message=message.replace('ç','c')
    message=message.replace(' ','')
    message=message.upper()
    for i in message:
        for t in range(26):
            if ch[t]==i:
                break
        c=(11*t+8)%26
        # c=(19*t-8*1e9)%26
        print(ch[c], end='')