#RO_PAG81_Area_triangle_coordenades_9
from math import*
print("P i Q son punts")
a = int(input("x de P(a)= "))
b =int(input("y de P(b)= "))
c =int(input("x de Q(c)= "))
d =int(input("y de Q(d)= "))

e = pow((c-a),2)
f= pow ((d-b),2)
g = e + f
x = sqrt(g)
print("costat triangle entre P i Q(x)=",x)
y = sqrt((pow(a,2))+(pow(b,2)))
print("costat triangle entre Origen i P(y) =",y)
z=sqrt((pow(c,2))+(pow(d,2)))
print("costat triangle entre Origen i Q(z) =",z)
t =(x+y+z)/2

area_triangle = sqrt(t*(t-x)*(t-y) *(t-z))
print("Àrea triangle = ",area_triangle)