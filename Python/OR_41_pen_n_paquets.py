#OR_PAG41_pes_n_paquet
num_paquets = 6
pes_max = 0 

for comptador in range(1, num_paquets +1, 1):
    print("Pes del paquet",comptador, "en kg =", end = " ")
    pes_paquet =float(input())
    if pes_paquet > pes_max:
        pes_max = pes_paquet
print("El pes del paquet més gran =", pes_max, "kg") 