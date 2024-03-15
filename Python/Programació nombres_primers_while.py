#Programació nombres_primers_while
n = int(input("Introdueix un nombre:"))
i = 2
if n ==2 or n==1:
        print("El nombre",n,"és primer")
while i < n:
    if n%i == 0:
        print("El nombre",n,"no és primer")
    elif n%i != n:
        i = i+1
        print("El nombre",n,"és primer")
        
        
    