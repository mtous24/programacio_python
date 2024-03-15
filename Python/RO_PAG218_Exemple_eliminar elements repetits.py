#RO_PAG218_Exemple_eliminar elements repetits

n = int(input("Quantitat d'elements:"))
v = []
for i in range(n):
    x = int(input("Introdueix l'element numèric següent:"))
    v = v+[x]
print("Llista original", v)
u =[]
for a in v:
    if a not in u:
        u = u+[a]
print("Llista depurada:",u)        