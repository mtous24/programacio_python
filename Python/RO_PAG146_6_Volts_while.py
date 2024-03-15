#RO_PAG146_6_Volts_while
vots = int(input("Introdueix el nombre de vots:"))
candidat_1 = 0
candidat_2 = 0
candidat_3 = 0
vots_blancs = 0
vots_nuls = 0
i = 0
while i < vots:
    i = i +1
    vot = int(input("Vot ="))
    if vot == 0:
        vots_blancs = vots_blancs +1
    elif vot ==1:
        candidat_1 = candidat_1 +1
    elif vot ==2:
        candidat_2 = candidat_2 +1
    elif vot == 3:
        candidat_3 = candidat_3 + 1
    else:
        vots_nuls = vots_nuls +1
        
print("Vots en blanc =",vots_blancs)
print("Vots pel candidat 1 =",candidat_1)
print("Vots pel candidat 2 =",candidat_2)
print("Vots pel candidat 3 =",candidat_3)
print("Vots nuls =",vots_nuls)