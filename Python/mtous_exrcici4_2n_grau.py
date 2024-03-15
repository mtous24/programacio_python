#mtous_exrcici4_2n_grau
from math import*

a = float(input("Introdueixi el coeficient del terem de segon grau:"))
b = float(input("Introdueixi el coeficient del terem de primer grau:"))
c = float(input("Introdueixi el coeficient del terem de grau 0:"))

d =(pow(b,2)-4*a*c)
if d < 0:
    print("Soloució imaginària")
else:
    e = sqrt(d)
    x1 = (-b + e)/2*a
    x2 = (-b - e)/2*a
    print(x1)
    print(x2)