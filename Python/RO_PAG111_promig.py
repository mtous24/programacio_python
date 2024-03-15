#RO_PAG111_promig
n = int(input("Introdueixi la quantitat de dades:"))
s = 0
for i in range (n):
    x = float(input("Introdueixi la següent dada:"))
    s = s+x
p = s/n
print("El promig d'aquest grup de dades és:",p)