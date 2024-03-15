#Progamació_nombres_primers_while
while True:
    n = int(input("Introdueix un nombre:"))
    i = 2
    while i < n:
        if n%i ==0:
            print("El nombre",n,"no és primer")
            break
        elif n%i !=n:
            i = i+1
            if i== n:
                print("El nombre",n,"és un nombre primer")
         elif n ==1:
            print("El nombre",n,"és un nombre primer")
         elif n == 2:
             print("El nombre",n,"és un nombre primer")

