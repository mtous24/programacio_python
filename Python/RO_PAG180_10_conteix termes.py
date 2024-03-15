#RO_PAG180_10_conteix termes
from random import*

def conteix(x):
    terme = 0
    suma = 0
    quant_termes = 0
    i = 1
    e = 2
    o = 3
    while suma < x:
        i = i +1
        e = e+ 1
        o = o +1
        terme = i * e * o
        suma = suma + terme
        quant_termes = quant_termes + 1        
    return quant_termes

x = randint(1,1000)
print("El nombre a arribar és:", x)
print("La quantitat de termes de la sèrie que hem nesessitat per arribari és:",conteix(x))