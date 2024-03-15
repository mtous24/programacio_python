#RO_PAG148_24_daus
from random import*
n = int(input("Introdueix la quantitat de tirades:"))
diners = 0
h = 0
while h < n:
    h = h+1
    m = randint(1,6)
    if m ==1:
        diners = diners + 1
    elif m == 6:
        diners = diners +5
    else:
        diners = diners - 2
    print("tirada",h,"=",m, end=" ")
    print("dolars =",diners,"$")
print("Diners al acabar la partida:",diners,"$")
