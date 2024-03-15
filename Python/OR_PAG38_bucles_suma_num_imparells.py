#OR_PAG38_bucles_suma_imparell

n = int(input("nombre de números imparells = "))
#k = int(input("cada número imparell = "))
#s = int(input("suma números imparells = "))

s = 0
for i in range(1,n+1):
    k = 2*i -1
    s = s + k
if (s == n*n):
    print("verdadero")
    print("suma números imparells = ",s)
else:
    print("falso")
    
