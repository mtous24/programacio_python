#RO_PAG81_3_bloc_rectangular
from math import*

print("Introdueix la amplada en m:", end=" ")
amplada = float(input())
print("Introdueix la profunditat en m:", end=" ")
profunditat = float(input())
print("Introdueix l'altura en m:", end=" ")
altura = float(input())

area = 2 *(amplada * altura) + 2*(altura *profunditat) + 2*(profunditat * amplada)
volum = amplada * profunditat * altura

print("Àrea bloc rectangular = ",area,"m2")
print("Vloum bloc ractangular = ",volum,"m3")