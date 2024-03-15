#RO_PAG83_3_suma_xifres_centrals
from math import*
nprimer = int(input("Introdueix pirmer nombre de tres xifres:"))
nsegon = int(input("Introdueix segon nombre de tres xifres:"))

xifra1_nprimer = nprimer//100
xifra2_nprimer = nprimer%100//10
xifra3_nprimer =nprimer%100%10

xifra1_nsegon = nsegon//100
xifra2_nsegon = nsegon%100//10
xifra3_nsegon =nsegon%100%10
print("Primera xifra del primer nombre:",xifra1_nprimer)
print("Segona xifra del primer nombre:",xifra2_nprimer)
print("Tercera xifra del primer nombre:",xifra3_nprimer)
print("Primera xifra del segon nombre:",xifra1_nsegon)
print("Segona xifra del psegon nombre:",xifra2_nsegon)
print("Tercera xifra del segon nombre:",xifra3_nsegon)


suma_xifres2 = xifra2_nprimer + xifra2_nsegon
print("Suma de les dues xifres centrals =",suma_xifres2)