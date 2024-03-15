#RO_PAG81_4_progressió_aritmètica
from math import*
print("Introdueix l'últim terme de la progressió aritmètica :", end=" ")
u = float(input())
print("Introdueix el primer terme de la progressió aritmètica :", end=" ")
a = float(input())
print("Introdueix la quantitat de termes de la progressió aritmètica:", end=" ")
n = float(input())

r = u/(a +(n-1))

print("Raò entre dos termes consecutius",r)