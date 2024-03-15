#OR_PAG146_PAQUETS
n_paquets= int(input("Introdueix nombre paquets:"))
e = 1
pes_max = 0
promig = 0
pes_min = 999999999
while n_paquets >= e:
    pes= float(input("Pes del paquet:"))
    e = e+1
    promig = promig +pes
    if pes > pes_max:
        pes_max = pes
    elif pes < pes_min:
        pes_min = pes
print("Pes mínim =",pes_min)
print("Pes màxim =",pes_max)

promig = promig/n_paquets
print("Promig pes paquets =",promig)