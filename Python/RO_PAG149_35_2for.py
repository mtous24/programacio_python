#RO_PAG149_35_2for
#a= int(input("Introdueix un número entre 1 i 1000:"))
#b= int(input("Introdueix un número entre 1 i 1000:"))
for a in range(1,1000+1):
    for b in range (1,1000+1):
        x = 1000-a
        y = 1000-b
        suma =x+y
        resta = 1000-suma
        producte = resta *1000
        producte2 = x*y
        resultat = producte +producte2
        if resultat == a*b:
            print("El producte de(a,b):",a,"x",b,"=",resultat,"és correcte")