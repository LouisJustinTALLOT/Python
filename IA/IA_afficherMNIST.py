from tkinter import*
from mnist import MNIST
from random import*
mndata = MNIST('D:\Downloads\AI')
images, labels = mndata.load_training()

numero=0#randrange(60000)

def raccourcirImage():
    for i in range(60000):
        lol=images[i]
        for j in range(56):
            del(lol[j])
        for j in range (56):
            del(lol[len(lol)-1])
raccourcirImage()
def afficherImage(numero):
    canvas1.delete("all")
    iko=images[numero]
    for i in range(24):
        for j in range(28):
            if iko[28*i+j]==0:
                'rien'
            else:
                couleur='#'+str(iko[28*i+j])*3
                canvas1.create_rectangle(24*j,24*i,24*(j+1),24*(i+1),fill=couleur)
    canvas1.grid(column=2, rowspan=5)

def aleatoire():
    global numero
    numero=randrange(60000)
    afficherImage(numero)
    canvas2.delete("all")
    canvas2.create_text(100,30,text='Numéro '+str(numero+1)+'  :  '+str(labels[numero]))
    canvas2.grid(column=1, row=0)
    
def avance():
    global numero
    if numero==59999:
        "rien"
    else:
        numero+=1
        afficherImage(numero)
        canvas2.delete("all")
        canvas2.create_text(100,30,text='Numéro '+str(numero+1)+'  :  '+str(labels[numero]))
        canvas2.grid(column=1, row=0)
    return

def recule():
    global numero
    if numero==0:
        "rien"
    else:
        numero-=1
        afficherImage(numero)
        canvas2.delete("all")
        canvas2.create_text(100,30,text='Numéro '+str(numero+1)+'  :  '+str(labels[numero]))
        canvas2.grid(column=1, row=0)
    return




fenetre1=Tk()
canvas1=Canvas(fenetre1, height=576, width=672, background='white')
canvas1.grid(column=2, rowspan=5)

canvas2=Canvas(fenetre1, height=75, width=200, background='light yellow')
canvas2.create_text(100,30,text='Numéro '+str(numero+1)+'  :  '+str(labels[numero]))
canvas2.grid(column=1, row=0)
        
buttonAvance=Button(fenetre1, text='Avancer', command=avance)
buttonAvance.grid(column=1, row=1)

buttonRecule=Button(fenetre1, text='Reculer', command=recule)
buttonRecule.grid(column=1, row=2)

buttonAléatoire=Button(fenetre1, text='Nombre\naléatoire', command=aleatoire)
buttonAléatoire.grid(column=1,row=3)

buttonQuit=Button(fenetre1, text='Quitter', command=fenetre1.destroy)
buttonQuit.grid(column=1, row=4)

# fenetre1.attributes('-fullscreen', 1)
afficherImage(numero)
fenetre1.mainloop()



# iko=images[0]
# 
# chaine=''
# liste=[]
# 
# for i in range(28):
#     for j in range(28):
#         if iko[28*i+j]==0:
#             chaine+=' '
#         else:
#             chaine+='o'
#     liste.append(chaine)
#     chaine=''
# for i in liste:
#     print(i)