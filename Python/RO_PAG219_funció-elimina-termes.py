#RO_PAG219_funció-elimina-termes

def elimina_termes(v):
    u=[]
    for e in v:
        if e not in u:
            u = u +[e]
    return u

v =[]
n = int(input("Quantitat termes llista original:"))
for i in range(n):
    x = int(input("Termes de la llista original:"))
    v = v + [x]
print("Llista original:",v)
elimina_termes(v)
print("Llista depurada",elimina_termes(v))