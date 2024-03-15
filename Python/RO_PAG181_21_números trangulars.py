#RO_PAG181_21_números trangulars
def triangular_for(n):
    f = 0
    for i in range(1,n+1):
        f = f + i
        print(i,f)
def triangular_while(n):
   f = 0
   i = 0
   while i < n:
        i = i + 1
        f = f + i
        print(i,f)
def suma_triangulars(n):
    f = 0
    k = f
    for i in range(1,n+1):
        f = f + i
        k = k + f
    return k
    
n = int(input("Introdueix un nombre n:"))
triangular_for(n)
print(" ")
triangular_while(n)
print(" ")
print("Suma de triangulars:",suma_triangulars(n))

q = int(input("Introdueix el nombre de vegades:"))
suma = 0
for e in range(1, q+1):
    suma = suma_triangulars(n) + suma
print("Sumade la suma de triangulars:",suma)