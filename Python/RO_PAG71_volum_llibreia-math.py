#RO_PAG71_volum
from math import*
print("Introdueix el radi en m:", end=" ")
r = float(input())
print("Introdueix l'altura en m:", end=" ")
h = float(input())

v = pi * pow(r,2) *h
print("Volum =",v,"m3")

a = 2*pi*r*h + 2 *pi *pow(r,2)
print("Àrea =",a,"m2")

