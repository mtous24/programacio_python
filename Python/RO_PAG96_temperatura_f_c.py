#RO_PAG96_temperatura_f_c
from math import*

p = int(input("Introdueix codi (1 o 2):"))
if p ==1:
    print("Introdueix temperatura en Farenheits:",end =" ")
    t = float(input())
    c = 5/9(t-32)
    print("Temperatura en graus centigrads",c,)
elif p==2:
     print("Introdueix temperatura en graus centigrads:",end =" ")
     t = float(input())
     f = 32 + (9*t)/5
     print("Temperatura en graus Farenheits",f,)