#RO_PAG80_3_nombres perfectes
'''Escriba una función perfecto(n) que determine si un número entero dado n es un
número perfecto. Un número perfecto debe ser igual a la suma de todos sus divisores
enteros menores que el valor del número.
Ejemplo: 28 = 1 + 2 + 4 + 7 + 14
Escriba un programa de prueba que use la función escrita y encuentre los números
perfectos entre 1 y 1000
'''
def perfecto(n):
    suma = 1
    for i in range(2,n):
        if n%i ==0:
            print(i)
    if suma ==n:
        t = "És un nombre primer"
        
    else:
        t = "No nombre primer"
    return t
n = int(input("Introdueix un nombre:"))
print(n,perfecto(n))
