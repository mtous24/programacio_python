#RO_PAG95_volum_Error_cilindre_if
from math import*

r = float(input("Introdueix el radi del cilindre(cm):"))
a = float(input("Introdueix l'altura del cilindre(cm):"))

if a>r:
   volum = (pi * pow(r,2)) * a
   print("Volum cilindre = ",volum,"cm3")
else:    
    print("Error")