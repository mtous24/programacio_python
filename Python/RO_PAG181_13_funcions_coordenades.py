#RO_PAG181_13_funcions_coordenades
from math import*

def polar(x,y):
    a = pow(x,2)
    b = pow(y,2)
    c = a + b
    r = sqrt(c)
    d = y/x
    e = atan(d)#en radiants
    fi = e * 180/pi
    print("Mòdul:",r)
    print("angle:",fi)
def cartesiana(r,fi):  #en radiants
        x = r * cos(fi)
        y = r * sin(fi)
        print("la coordenada x és:",x)
        print("la coordenada y és:",y)
print("1. convertir coordenades cardinals a polars")
print("2. convertir coordenades polars a cardinals")
print("3. Salir")
opcio = int(input("Tria l'opicó que vulguis:"))
if opcio == 1:
    x = float(input("Introdueix la coordenada x:"))
    y = float(input("Introdueix la coordenada y:"))
    polar(x,y)
elif opcio == 2:
    r = float(input("Introdueix el mòdul:"))
    h = float(input("Introdueix l'angle en graus:"))
    fi = h * pi/180
    cartesiana(r,fi)
elif opcio == 3:
   print("HA SORTIT DEL PROGRAMA")