#RO_PAG83_5_billets$
from math import*
print("quantitat dolars :",end =" ")
n_dolars = float(input())

billets100 = n_dolars//100
dolars_restants = n_dolars%100
billets50 = dolars_restants//50
dolars_restants2 = dolars_restants%50
billets20 = dolars_restants2//20
dolars_restants3 = dolars_restants2%20
billets10 = dolars_restants3//10
dolars_restants4 = dolars_restants3%10
billets5 = dolars_restants4//5
billets1 = dolars_restants4%5
print("Billets de 100:",billets100)
print("Billets de 50:",billets50)
print("Billets de 20:",billets20)
print("Billets de 10:",billets10)
print("Billets de 5:",billets5)
print("Billets de 1:",billets1)


