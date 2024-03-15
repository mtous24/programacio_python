#RO_PAG159_Llibreia geometria_figures_planes_i_en_volum
from math import*
def quadrat:
    A = a**2
    P = 4*a
    print("Àrea =",A)
    print("Perímetre =",P)
def triangle:
   A = (b*h)/2
   P = a + c +b
   print("Àrea =",A)
   print("Perímetre =",P)
def rectangle:
    A = a*b
    P = 2*a+2*b
    print("Àrea =",A)
    print("Perímetre =",P)
def paralelogram:
    A = b *h
    P = 2 *(a+b)
    print("Àrea =",A)
    print("Perímetre =",P)
def rombe:
    A = (D*d)/2
    P = 4*a
    print("Àrea =",A)
    print("Perímetre =",P)
def estel:
    A = (D*d)/2
    P = 2*(b+a)
    print("Àrea =",A)
    print("Perímetre =",P)
def trapeci:
    A = (B+b)*h/2
    P = B +b+a+c
    print("Àrea =",A)
    print("Perímetre =",P)
def cercle:
    A = pi*r**2
    P = 2*pi*r
    print("Àrea =",A)
    print("Perímetre =",P)
def poligon_regular:
    P = n*b
    A = (P*a)/2
    print("Àrea =",A)
    print("Perímetre =",P)
def corona_circular:
    A = pi *(R**2-r**2)
    print("Àrea =",A)
def sector_circular:
    A = (pi * r**2 *n)/360
    print("Àrea =",A)
def cub:
    A = 6*a
    V = a**3
    print("Àrea =",A)
    print("Volum =",V)
def cilindre:
    A = 2*pi*r*(h+r)
    V = pi*r**2*h
    print("Àrea =",A)
    print("Volum =",V)
def bolc_rectangular:
    A = 2*(a*b+a*c+b*c)
    V = a*b*c
    print("Àrea =",A)
    print("Volum =",V)
def prinsma:
    A = P*(h+a)#a = apotema base, P = perímetre base
    V = Ab*h # Ab=area base
    print("Àrea =",A)
    print("Volum =",V)
def con:
    A = pi*r*(r+g) # g = geneeratriu
    V = (pi *r**2*h)/3
    print("Àrea =",A)
    print("Volum =",V)
def tronc_con:
    A = pi*(g*(r+R)+r**2+R**2)
    V = (pi*h*(R**2+r**2+R*r))/3
    print("Àrea =",A)
    print("Volum =",V)
def esfera:
    A = 4*pi*r**2
    V = (4*pi*r**2)/3
    print("Àrea =",A)
    print("Volum =",V)
def piramide:
    A = (P*(a+a2))/2#P = perimetre base
    V = (Ab*h)/3 # Ab=aera base
    print("Àrea =",A)
    print("Volum =",V)
def tetraedre_regular:
    A = sqrt(3)*a**2
    V = (sqrt(2)*a**3)/12
    print("Àrea =",A)
    print("Volum =",V)
def octaedre_regular:
    A = 2*sqrt(3)*a**2
    V = (sqrt(2)*a**3)/3
    print("Àrea =",A)
    print("Volum =",V)
 def tronc_piramide:
    A = ((P+P2)/2)*a+Ab+Ab2 # P2=P= perímertre de la base  Ab =Ab2=areas base
    V = ((Ab + Ab2+sqrt(Ab*Ab2))*h)/3
    print("Àrea =",A)
    print("Volum =",V)
def Casquet_esfèric:
    A = 2*pi*r*h
    V = (pi*pow(h,2)*(3*r-h))/3
    print("Àrea =",A)
    print("Volum =",V)
def cunya_esfèrica:
    A = (4*pi*pow(r,2)*n)/360
    V = (4*pi*pow(r,3)*n)/3*360
    print("Àrea =",A)
    print("Volum =",V)
def segment_esfèric:
    A = 2*pi*r*h
    V = (pi*h*(pow(h,2)+3*pow(r,3)+r2))/6
    print("Àrea =",A)
    print("Volum =",V)
#programa peincipal menu
sortida = False
while not sortida:
    print(" ")
    print("1.quadrat")
    print("2.triangle")
    print("3.rectangle")
    print("4.paral·lelogram")
    print("5.rombe")
    print("6.estel")
    print("7.trapeci")
    print("8.cercle")
    print("9.poligon regular")
    print("10.corona circular")
    print("11.sector circular")
    print("12.cub")
    print("13.cilindre")
    print("14.bolc rectangular")
    print("15.prisma")
    print("16.con")
    print("17.tronc del con")
    print("18.esfera")
    print("19.piràmide")
    print("20.octoedre regular")
    print("21.tetraedre regular")
    print("22.tronc de la piràmide")
    print("23.casquet esfèric")
    print("24.cunya esfèrica")
    print("25.segment esfèric")
    print("26. sortir")
    opcio = int(input("Tria l'opció que vulguis:"))
    if opcio == 1:
        a = float(input("Introcueix el valor d'un costat:"))
        quadrat(a)
    elif opcio == 2:
        a = float(input("Costat:"))
        b = float(input("Base:"))
        c = float(input("Costat:"))
        h = float(input("Altura triangle:"))
        triangle(a,b,c,h)
     elif opcio == 3:
         a = float(input("Costat: "))
         b = float(input("Base: "))
         rectangle(a,b)
     elif  opcio == 4:
         a = float(input("Costat: "))
         b = float(input("Base: "))
         h = float(input("Altura del paralelogram: "))
         paralelogram(a,b,h)
     elif opcio == 5:
         D = float(input("Diagonal gran:"))
         d = float(input("Diagonal petita:"))
         a = float(input("Costat:"))
         rombe(D,d,a)
         
         