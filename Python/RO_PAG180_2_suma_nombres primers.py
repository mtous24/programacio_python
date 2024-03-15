#RO_PAG180_2_suma_nombres primers
'''Escriba un programa de prueba que use la función primo y encuentre dos números
enteros aleatorios menores que 100 tales que su suma sea también un número primo.
'''
from random import*
def primer(suma):
    for i in range(1, suma+1):
        a = suma%i
        if a ==  0:
            if i == suma or i ==1:
                return(suma)
        
m = randint(1,100)
n = randint(1,100)        
suma = m + n
print(primer(suma))




     
        