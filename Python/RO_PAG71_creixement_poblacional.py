#RO_PAG71_creixement_poblacional
from math import*
k = (50 -(2*exp(0.1*10)))/10
print(k)

print("temps en anys =",end=" ")
t = float(input())

f_t = k *t +2 *exp(0.1 *t)
print(f_t)
