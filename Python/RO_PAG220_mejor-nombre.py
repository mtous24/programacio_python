#RO_PAG220_mejor-nombre
def thebest(n):
    v=[]
    r=0
    p=0
    for i in range(0,n):
        x=int(input("Nombre: "))
        v=v+[x]
    for t in v:
        if t>r:
            r=t
            p= p+1
    return r,p-1
n= int(input("Introdueix el nombre de termes de la llista original:"))
print(thebest(n))