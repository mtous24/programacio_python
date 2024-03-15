#OR_pag32_mostra_area/cilindre_o_volum/cilindre

a = int(input("altura = "))
r = int(input("radi = "))

if a > r :
    v = (3.1416 * r**2)* a
    print("volum = ", v,"m3")
   
if r > a :
    area = 2 * (3.1416 * r**2) * (2 * 3.1416 * a)
    print("àrea = ",area, "m2")



