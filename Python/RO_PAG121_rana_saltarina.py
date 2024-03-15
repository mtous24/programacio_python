#RO_PAG121_rana_saltarina
from random import*
x = 0 #Cordenada x de les caselles
y = 0 #Cordenada y de les caselles
i = 0 #Intents

while (-5 < x and x < 5) and (-5 < y and y < 5):
    d =randint(1,4)
    i = i +1
    if d ==1:
        x = x +1
    elif d == 2:
        x = x-1
    elif d == 3:
        y = y +1
    else:
        y = y-1
    print("Casella on es pot trobar la granota:",x,y)
print("Cantitat d'intents:",i)    