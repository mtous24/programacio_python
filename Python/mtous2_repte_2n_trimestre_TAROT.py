# mtous2_execici2_TAROT

dia = int(input("Introdueix dia de neixement:"))
mes = int(input("Introdueix mes de neixement:"))
ANY = int(input("Introdueix any de neixement:"))

suma1 = dia + mes + ANY
print(suma1)
xifra1 = suma1//1000
print(xifra1)
residu1 = suma1%1000
xifra2 = residu1//100
print(xifra2)
residu2 = residu1%100
xifra3 =residu2//10
print(xifra3)
xifra4 = residu2%10
print(xifra4)
suma2 = xifra1 +xifra2 + xifra3 + xifra4
print(suma2)
xifra1_2 = suma2//10
xifra2_2 = suma2%10
num_tarot = xifra1_2 +xifra2_2
print("Aquest és el teu nombre del tarot:",num_tarot)