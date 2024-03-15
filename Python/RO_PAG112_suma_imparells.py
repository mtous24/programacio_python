#RO_PAG112_suma_imparells
n=int(input('Ingrese la cantidad de impares: '))
s=0
imp=1
for i in range(n):
 s=s+imp
 imp=imp+2
if s==n**2:
 print('Verdadero')
else:
 print('Falso')
