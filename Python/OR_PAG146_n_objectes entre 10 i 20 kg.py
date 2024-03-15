#RO_PAG146_n_objectes entre 10 i 20 kg
n =int(input("Introdueix el nombre d'objectes de la bodega: "))
i = 0
obj_menys10kg = 0
obj_entre_10i20kg = 0
obj_mes20kg = 0

while i < n:
    i = i +1
    pes = float(input("Introdueix el pes  del paquet (kg): "))
    if pes < 10:
        obj_menys10kg = obj_menys10kg +1
    elif pes > 20:
        obj_mes20kg = obj_mes20kg + 1
    elif pes > 10 and pes < 20:
        obj_entre_10i20kg = obj_entre_10i20kg + 1
print("Objectes de menys de 10 kg:", obj_menys10kg)
print("Objectes d'entre 10 i 20 kg:", obj_entre_10i20kg)
print("Objectes de més de 20 kg:", obj_mes20kg)