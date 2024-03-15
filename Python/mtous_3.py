#mtous_3
preu_gelat_avellana = 2.25
preu_pastis_ametlla = 1.75
n = int(input("Nombre gelats d'avellana:"))
m = int(input("Nombre pastisos d'ametlla:"))
def comprar(n,m):  # n = nombre de gelats d'avellana i m = nombre pastisos d'ametlla que vulguis comprar
    preu_compra = n * preu_gelat_avellana + m * preu_pastis_ametlla
    return preu_compra
   
print(comprar(n,m))
euros_donats = float(input("Introdueix els euros per pagar:"))
canvi = comprar(n,m) - euros_donats    
monedes2eu = canvi//2
monedes2_2eu = monedes2eu%2
monedes1eu = monedes2_2eu//1
monedes1_1eu = monedes1eu%1
monedes50cent = monedes1_1eu//0.5
monedes50cent_1 = monedes50cent%0.5
monedes20cent = monedes50cent_1//0.2
monedes20cent_1 = monedes20cent%0.2
monedes5cent = monedes20cent_1//0.05
print("Canvi:", monedes2eu,"monedes 2€,", monedes1eu,"monedes 1€,", monedes50cent ,"monedes 50 cent,", monedes20cent,"monedes 20 cent,", monedes5cent,"monedes 5 cent")