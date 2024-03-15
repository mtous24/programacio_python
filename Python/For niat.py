#For niat
fila = int(input("Nombre de files:"))
columna = 0
for fliles in range (0, fila):
    columna = columna +1
    for columnes in range (0,columna):
        print("*", end= " ")
    print(" ")
    
fila = int(input("Nombre de files:"))
columna = fila
for files in range(0,fila):
    columna = columna -1
    for columnes in range(0, columna+1):
        print("*", end= " ")
    print(" ")
    
espai = 0
fila = int(input("Nombre de files:"))
columna = fila
for files in range(0, fila):
    columna = columna -1
    espai = espai + 1
    for espais in range (0,espai):
        print( " ", end= " ")
    for columnes in range (0, columna+1):
        print( "*", end= " ")
    print(" ")
    

fila = int(input("Nombre de files:"))
columna = 0
espai = fila
for files in range(0, fila):
    espai = espai -1
    columna = columna +1
    for espais in range (0,espai):
        print(" ", end= " ")
    for columnes in range (0,columna):
        print( "*", end= " ")
    print(" ")
    
fila= int(input("Nombre de files:"))
columna = fila
for files in range(fila):
    columna -= 1
    for columnes in range(fila):
        if columnes>columna:
            print(("*"*2),end = "")
        elif columnes ==columna:
            print("*",end = "")  
        else:
            print(" ",end = "")
    print("")
    
fila = int(input("Nombre de files:"))    