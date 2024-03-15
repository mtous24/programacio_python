#RO_PAG216_Exemple

n =int(input("Nombre de termes de la llista:"))
v=[]
for i in range(n):
    x = int(input("Introdueix el següent terme:"))
    v =v+[x]
s = 0
for a in v:
    if a%2 ==0:
        s = s+a
print("la suma és:",s)    