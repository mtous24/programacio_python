#RO_PAG83_4_numero al revès
from math import*
nprimer = int(input("Introdueix un nombre de tres xifres:"))

xifra1 = nprimer//100
xifra2 = nprimer%100//10
xifra3 =nprimer%100%10

print("Primera xifra del nombre:",xifra1)
print("Segona xifra del nombre:",xifra2)
print("Tercera xifra del nombre:",xifra3)

a = xifra1
xifra1 = xifra3
xifra3 = a
print("Primera xifra del nombre al revès:",xifra1)
print("Segona xifra del nombre al revès:",xifra2)
print("Tercera xifra del nombre al revès:",xifra3)

nreves = xifra1 *100 + xifra2 *10 + xifra3
print("Nombre al revès:",nreves)