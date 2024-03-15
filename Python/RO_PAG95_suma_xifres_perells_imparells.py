#RO_PAG95_suma_xifres_perells/imparells
from math import*
n = int(input("Introdueix un nombre de dos xifres:"))

xifra1 = n//10
xifra2 = n%10//1
print("Primera xifra del  nombre:",xifra1)
print("Segona xifra del nombre:",xifra2)

suma_xifres = xifra1 + xifra2
if suma_xifres%2==0:
    print("Nombre parell",suma_xifres)
else:
    print("Nombre imparell",suma_xifres)