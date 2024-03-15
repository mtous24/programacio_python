#RO_PAG71_area_trangle-rectangle
from math import*
print("Introdueix el valor de la diagonal(cm):", end=" ")
d = float(input())
print("Introdueix el valor de l'angle en graus:", end=" ")
alfa = float(input())

alfa = alfa *(pi/180)# passar de graus a radiants
print(alfa,"radiants")
a = d *sin(alfa)
print(a,"cm" )
b = d *cos(alfa)
print(b,"cm")
area = (a*b)/2
print("Àrea triangle",area,"cm2")