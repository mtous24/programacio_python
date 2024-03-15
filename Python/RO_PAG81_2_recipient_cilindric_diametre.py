#RO_PAG81_recipient_cilindric_diametre
from math import*
a = float(input("altura(en metres) = "))
v = float(input("volum (en litres)= "))

v = v /1000
print(v,"m3")
r = sqrt(v/(pi *a))
d = 2*r
print("Diàmetre recipient =", d,"m")