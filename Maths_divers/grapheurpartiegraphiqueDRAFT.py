        #PARTIE GRAPHIQUE AVEC TURTLE
        up()
        width(2)
        for i in range(len(u)):
            goto(i*1200/maxi-600,((u[i]-min(u))/(max(u)-min(u)))*600-300)
            down()
            if hhh:
                "rien"
            else:
                forward(2)
                up()
        up()
        title(suite)
        width(1)
        color('grey')
        goto(-650,300)
        write(str(round(max(u),2)))
        goto(-650,-300)
        write(str(round(min(u),2)))
        goto(-650,0)
        write(str(round((max(u)+min(u))/2,2)))
        goto(-620,350)
        down()
        right(90)
        forward(700)
        up()
        goto(-620,0)
        left(90)
        down()
        forward(1400)
        
        goto(700,400)
        
        
        
        ##########################
        up()
        width(2)
        for i in range(len(f)):
            if f[i]==1e300:
                up()
            else:
                goto(i*1200/2200-600,((f[i]-min(f))/(max(f)-min(f)))*600-300)
                down()
        up()
        title(fonction)
        width(1)
        color('grey')
        goto(-650,300)
        write(str(round(max(f),2)))
        goto(-650,-300)
        write(str(round(min(f),2)))
        goto(-650,0)
        write(str(round((max(f)+min(f))/2,2)))
        goto(-620,350)
        down()
        right(90)
        forward(700)
        up()
        goto(-620,0)
        left(90)
        down()
        forward(1400)
        goto(700,400)