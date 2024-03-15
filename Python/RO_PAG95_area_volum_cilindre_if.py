#RO_PAG95_area_volum_cilindre_if
from math import*

r = float(input("Introdueix el radi del cilindre(cm):"))
a = float(input("Introdueix l'altura del cilindre(cm):"))

if a>r:
   volum = (pi * pow(r,2)) * a
   print("Volum cilindre = ",volum,"cm3")
else:    
    area = (2 * pi * pow(r,2)) + (2 * pi * a)
    print("Àrea cilindre = ",area,"cm2")
