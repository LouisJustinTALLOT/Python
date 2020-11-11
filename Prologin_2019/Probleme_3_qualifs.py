# LePetitCodeur14 - Prologin qualifications - problème 3

def manhattan_maboul0(m, jours, n):
    dict_passages = {}
    for i in jours:                 #
        try :                       #
            dict_passages[i] += 1   # On initialise le dictionnaire contenant
        except :                    # le nb d'amis de passage
           dict_passages[i] = 1     #
   #                                #
    # dict_passages est de la forme : 
    #   {jour : nb amis, jour : nb amis}   
    
    # Code de la première solution:
    # 
    # res = 0                                   #
    # for i in range(1 , max(dict_passages)+1): #
    #     temp = 0                              #
    #     for j in range(m+1):                  #
    #         try:                              # Code de la première solution
    #             temp += dict_passages[i + j]  # 
    #                                           # marche mais trop long
    #         except :                          # --> on va améliorer la 
    #             " " # on ne fait rien         # complexité pour passer 
    #                                           # les tests de performance
    #     if temp > res:                        #
    #         res = temp                        #

    # code de la deuxième solution :

    res = 0
    temp = 0
    for j in range(m+1):                        #
        try:                                    # On initialise notre variable
            temp += dict_passages[1+j]          # temporaire avec les 
    #                                           # m+1 premières valeurs
        except :                                #
            " " # on ne fait rien               #
    res = temp                                  #
    for i in range(1 , max(dict_passages)+1):   #
        try:                                    #
            temp -= dict_passages[i]            #
        except:                                 #
            ""                                  #
        try:                                    #
            temp += dict_passages[i+m+1]        #
        except :                                #
            ""                                  #
        if temp > res:                          #
            res = temp                          #
    #                                           #
    print(res)                                  #
    return res                                  #

(n, m) = list(map(int, input().split()))
jours = list(map(int, input().split()))

manhattan_maboul0(m, jours, n)
