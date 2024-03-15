#RO_PAG96_familia_kWh
from math import*
e= float(input("Introdueix la energia consumida en kWh:"))
preukWh = float(input("Introdueix el preu per kWh:"))

if e>=700:
    preukWh = preukWh +0.05*preukWh
else:
    preukWh = preukWh
print("Preu",preukWh,"€/kWh")    

preukWhfam = preukwh * e

print("Cost total conum de la familia =",preukWhfam,"€")