from random import random
import matplotlib.pyplot as plt
import mplcursors
import pandas as pd


price =0.0
CASES_OPENED = 1000



def open_Case():
    global price
    color = ""
    price = price-3.02
    a=round(random()*10000)
    if(a>0 and a<26):
        color = "Yellow"
    elif(a>=26 and a<90):
        color = "Red"
    elif(a>=90 and a<410):
        color = "Pink"
    elif(a>=410 and a<2008):
        color = "Purple"
    elif(a>=2008):
        color = "Blue"

    return color
        


def GetStats( data2):
    global price
    global CASES_OPENED
    colorCount = [0,0,0,0,0]


    for x in range(CASES_OPENED):
        c = open_Case()
        if c == "Yellow":
            colorCount[4] = colorCount[4]+1
            #Knifes 100
            price=price+250
        if c == "Red":
            colorCount[3] = colorCount[3]+1
            #Asiimov $60.40, Chameleon 4.82
            r = random()*10
            if(r<=5):
                price=price+60.40
            else:
                price=price+4.82
        if c == "Pink":
            colorCount[2] = colorCount[2]+1
            r = random()*10
            if(r<=3.33):
                price=price+25.09
            elif(r>3.33 and r<=6.66):
                price=price+5.55
            else:
                price=price+5.61
            #AK-47 Redline 25.09, Nova Antique 5.55, P90 Trigon  5.61
        if c == "Purple":
            colorCount[1] = colorCount[1]+1
            r = random()*10
            if(r<=5):
                price=price+2
            else:
                price=price+1.01 
            #Guardian 2, Pulse 1.01
        if c == "Blue":
            colorCount[0] = colorCount[0]+1
            r = random()*10
            if(r<=1.66):
               price= price+1.50
            elif(r>1.66 and r<=3.33):
               price= price+1.30
            elif(r>3.33 and r<=5):
               price= price+.4
            elif(r>5 and r <=8.33):
               price= price+.2
            else:
               price= price+.15

            #Heat 1.50
            #Sergeant 1.30
            #Sandstorm .40
            #Corporal .2
            #HeavenGuard .2
            #Terrain .15
        data2[x] = price
    
    return colorCount


print("Open Pheonix Cases?")
answer = input("y/n: ")
t=0
num = int(input('How many 1000 cases do you want to open: ')) 
while(t<num):
    price = 0
    plt.style.use('ggplot')
    data2 =[None] * CASES_OPENED
    sd=GetStats( data2)
    plt.plot(range(CASES_OPENED),data2)
    plt.title("If Reese opens 1000 cases")
    plt.xlabel('Cases')
    plt.ylabel('Dollars Net')
    
    t+=1
plt.show()

