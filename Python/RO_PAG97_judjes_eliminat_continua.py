#RO_PAG97_judjes_eliminat_continua
from math import*
j1 = int(input("Introdueix vot del judje 1 (si(1) o no(0)):"))
j2 = int(input("Introdueix vot del judje 2 (si(1) o no(0)):"))
j3 = int(input("Introdueix vot del judje 3 (si(1) o no(0)):"))

if j1 == 0 and j2 ==1 and j3 ==1:
    print("Continua")
elif j1 ==1 and j2 == 0 and j3 ==1:
    print("Continua")
elif j1 ==1 and j2 == 1 and j3 ==0:
    print("Continua")
elif j1 == 1 and j2 ==1 and j3 ==1:
    print("Continua")
else:
    print("Eliminat")