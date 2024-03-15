#mtous_exrcici4_2n_grau
from math import*
a = float(input("Introdueixi el coeficient del terem de segon grau(x^2):"))
b = float(input("Introdueixi el coeficient del terem de primer grau(x):"))
c = float(input("Introdueixi el coeficient del terem de grau 0(nombre):"))
d = sqrt(pow(b,2)-4*a*c)
x1 = (-b + d)/2*a
x2 = (-b - d)/2*a
if d < 0:
    print("Soloució imaginària")