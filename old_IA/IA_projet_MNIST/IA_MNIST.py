from tkinter import*
from mnist import MNIST
from random import*
from numpy import*
from math import*

# IMPORTATION DU MODULE MNIST ET DES DONNEES
mndata = MNIST("""D:\\Programmation\\0Ordinateur\\Python\\IA\\IA_projet_MNIST""")
images_train, labels_train = mndata.load_training()
images_test,labels_test=mndata.load_testing()

taille_de_backpropagation=0.1
train_oui_ou_non=1
numero=0

def diviser_pas_bckprop_par2():
    global taille_de_backpropagation
    taille_de_backpropagation/=2
    return

#CREATION D'UNE FONCTION DE REMPLISSAGE ALEATOIRE D'UNE MATRICE DE TAILLLE N,P
def remplissage_aleat_mat(n,p):
    "Fonction de création d'une matrice aléatoire de taille n*p"
    aa=[]
    for i in range(n*p):
        aa.append(random.random())
    aa=array(aa)
    aa=aa.reshape(n,p)
    return(aa)

# FONCTION SIGMOIDE
def sigmoide(matrice):
    """fonction permettant de prendre la sigmoide d'une matrice 
    pour ramener ses valeurs entre 0 et 1"""
    z=shape(matrice)
    for i in range(z[0]):
        for j in range(z[1]):
            matrice[i,j]=float((1/(1+exp(-matrice[i,j]))))
    return matrice

def diviser_par_255(liste):
    "cette fonction divise tous les éléments de la liste par 255"
    # (n,p)=shape(matrice)
    liste1=[]
    for i in range(len(liste)):
        # for j in range(p):
        liste1.append(float(liste[i]/255))
    return liste1

# def multiplier_par_255(matrice):
#     "cette fonction multiplie tous les coefficients de la matrice par 255"
#     (n,p)=shape(matrice)
#     for i in range(n):
#         for j in range(p):
#             matrice[i,j]*=255
#     return matrice    

def transformer_en_image(train_oui_ou_non,numero):
    """cette fonction retourne une matrice 28*28 
    contenant les valeurs de l'image entre 0 et 1"""
    if train_oui_ou_non:
        # on prend alors training
        liste_image=images_train[numero]
        matrice_image=array(diviser_par_255(liste_image))
        matrice_image=matrice_image.reshape(784,1)
        # matrice_image=diviser_par_255(matrice_image)
        return (matrice_image,labels_train[numero])
    else:
        # c'est donc testing
        liste_image=images_test[numero]
        matrice_image=array(diviser_par_255(liste_image))
        matrice_image=matrice_image.reshape(784,1)
        # matrice_image=diviser_par_255(matrice_image)
        return (matrice_image,labels_test[numero])
    
def creation_mat_resultat(nombre):
    """cette fonction renvoie une matrice 10*1 du résultat attendu"""
    liste=[0]*10
    liste[nombre]=1
    mat_res=array(liste)
    mat_res=mat_res.reshape(10,1)
    return mat_res

def moyenne_matrice(matrice):
    n,p=shape(matrice)
    somme=0
    for i in range(n):
        for j in range(p):
           somme+=matrice[i,j]
    somme/=(n*p)
    return somme
    
def afficherImage(train_oui_ou_non,numero):
    canvas1.delete("all")
    # for i in range(28):
    #     for j in range(28):
    #         if mat_image[i*28+j,0]==0:
    #             'rien'
    #         else:
    #             couleur='#'+str(mat_image[i*28+j,0]*255)*3
    #             canvas1.create_rectangle(24*j,24*i,24*(j+1),24*(i+1),fill=couleur)
    if train_oui_ou_non:
        iko=images_train[numero]
        for i in range(28):
            for j in range(28):
                if iko[28*i+j]==0:
                    'rien'
                else:
                    couleur='#'+str(iko[28*i+j])*3
                    canvas1.create_rectangle(24*j,24*i,24*(j+1),24*(i+1),fill=couleur)
    else:
        iko=images_test[numero]
        for i in range(28):
            for j in range(28):
                if iko[28*i+j]==0:
                    'rien'
                else:
                    couleur='#'+str(iko[28*i+j])*3
                    canvas1.create_rectangle(24*j,24*i,24*(j+1),24*(i+1),fill=couleur)
        
        
    canvas1.grid(column=1, rowspan=8)    
    
def trouver_nombre(mat_res):
    max=0
    indice_du_max=-1
    for i in range(10):
        if mat_res[i,0]>max:
            max=mat_res[i,0]
            indice_du_max=i
            
    return indice_du_max,max
    
# On arrive dans le vif du sujet : ma classe contenant le réseau de neurones
class Network(object):

    def __init__(self): #fonction d'initialisation
        # self.mat1=remplissage_aleat_mat(16,784)
        # self.biais1=remplissage_aleat_mat(16,1)        

        # self.mat2=remplissage_aleat_mat(16,16)
        # self.biais2=remplissage_aleat_mat(16,1)        

        # self.mat3=remplissage_aleat_mat(10,16)
        # self.biais3=remplissage_aleat_mat(10,1)
        self.mat1=remplissage_aleat_mat(8,784)
        self.biais1=remplissage_aleat_mat(8,1)        

        self.mat2=remplissage_aleat_mat(8,8)
        self.biais2=remplissage_aleat_mat(8,1)        

        self.mat3=remplissage_aleat_mat(10,8)
        self.biais3=remplissage_aleat_mat(10,1)
    def calcul(self,mat_image):
        # fonction effectuant le calcul proprement dit
        global mat_resultat
        matcouche1=sigmoide(dot(self.mat1,mat_image)+self.biais1)
        
        matcouche2=sigmoide(dot(self.mat2,matcouche1)+self.biais2)
        mat_resultat=sigmoide(dot(self.mat3,matcouche2)+self.biais3)
        return
            
    def cout_reseau(self,train_oui_ou_non,numero):
        global mat_image
        cout=0
        for i in range(1):#chiffre a changer pour le nb d'itérations
            mat_image,chiffre=transformer_en_image(train_oui_ou_non,randrange(60000))
            mat_attendu=creation_mat_resultat(chiffre)#création de la mat de résultat attendu
            self.calcul(mat_image)
            mat_cout=(mat_attendu-mat_resultat)**2
            cout+=moyenne_matrice(mat_cout)
        # cout/=5
        return cout
        
    def backpropagation(self,numero):
        global train_oui_ou_non,cout
        train_oui_ou_non=1
        liste_matrices=[self.mat1,self.biais1,self.mat2,self.biais2,self.mat3,self.biais3]
        cout1=self.cout_reseau(train_oui_ou_non,numero)
        for i in liste_matrices:
            n,p=shape(i)
            for j in range(n):
                for k in range(p):
                    i[j,k]+=taille_de_backpropagation
                    cout2=self.cout_reseau(train_oui_ou_non,numero)
                    if cout2>=cout1:
                        i[j,k]-=2*taille_de_backpropagation
                        cout2=self.cout_reseau(train_oui_ou_non,numero)
                        if cout2>=cout1:
                            i[j,k]+=taille_de_backpropagation
                    cout1=self.cout_reseau(train_oui_ou_non,numero)

def begin_or_stop_test():
    global train_oui_ou_non
    if train_oui_ou_non:
        train_oui_ou_non=0
    else:
        train_oui_ou_non=1
        
IA=Network()
la_boucle_tourne=1
def boucle_principale():
    global la_boucle_tourne,numero
    # while la_boucle_tourne:
    cout=IA.cout_reseau(train_oui_ou_non,numero)
    Label(fenetre1,text='Coût : '+str(cout)).grid(row=2,column=2)
    # afficherImage(train_oui_ou_non,numero)
    Label(fenetre1,text='Résultat à trouver : '+str(labels_train[numero])).grid(row=0,column=2)
    Label(fenetre1,text='Résultat trouvé : '+str(trouver_nombre(mat_resultat)[0])+'\n'+str(trouver_nombre(mat_resultat)[1]*100)+'% de certitude').grid(row=1,column=2)
    Label(fenetre1,text=str(numero)).grid(row=8,column=2)
    IA.backpropagation(numero)
    numero+=1
    numero%=60000
    
def change():
    global la_boucle_tourne
    if la_boucle_tourne:
        la_boucle_tourne=0
    else:
        la_boucle_tourne=1 

fenetre1=Tk()
# canvas1=Canvas(fenetre1, height=672, width=672, background='white')
# canvas1.grid(column=1, rowspan=8)

Button(fenetre1,text='Quitter',command=fenetre1.destroy).grid(row=7,column=2) #Bouton Quitter
Button(fenetre1,text='Diviser par 2 \ntaille_de_backpropagation',command=diviser_pas_bckprop_par2).grid(row=6,column=2)

Button(fenetre1,text='Lancer le test',command=begin_or_stop_test).grid(row=5,column=2)
Button(fenetre1,text="Démarrer \nl'entraînement",command=boucle_principale).grid(row=3,column=2)
Button(fenetre1,text="Pauser \nl'entraînement",command=change).grid(row=4,column=2)

fenetre1.mainloop()