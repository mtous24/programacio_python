#RO_PAG148_27_talula
n = int(input('Ingrese un dato: '))#25
r = 0
while n>0:
 d = n%2
 n = n//2
 r = 10*r + d
 print(d, n, r) 