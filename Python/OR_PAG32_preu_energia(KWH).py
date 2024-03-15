#OR_pag32_energia

e = float(input("energia mensual consumida(kWh) = "))
p = float(input("preu (€/kWh) = "))

if e > 700 :
    p = p + (p * 0.05/(e - 700))    
pt = p * e
 
print("preu total = ",pt,"€/kWh")