#RO_PAG96_cualificacions_estudiants
from math import*
cual1_estud1 = float(input("Introdueix la cualificació 1 de l'estudiant 1:"))
cual2_estud1 = float(input("Introdueix la cualificació 2 de l'estudiant 1:"))
cual3_estud1 = float(input("Introdueix la cualificació 3 de l'estudiant 1:"))

cual1_estud2 = float(input("Introdueix la cualificació 1 de l'estudiant 2:"))    
cual2_estud2 = float(input("Introdueix la cualificació 2 de l'estudiant 2:"))
cual3_estud2 = float(input("Introdueix la cualificació 3 de l'estudiant 2:"))

if cual1_estud1 > cual2_estud1  and cual1_estud1 > cual3_estud1 :
    if cual2_estud1 > cual3_estud1:
        cf1 = (cual1_estud1 + cual2_estud1)
    elif cual3_estud1 >cual2_estud1:
        cuf1 = (cual1_estud1 + cual3_estud1)
    print("Cualificació Final estudiant 1 :",cf1)    
elif cual2_estud1 > cual1_estud1 and cual2_estud1 > cual3_estud1:
    if cual1_estud1 > cual3_estud1:
        cf1 = (cual1_estud1 + cual2_estud1)
    elif cual3_estud1 > cual1_estud1:
        cf1 = (cual3_estud1 + cual2_estud1)
    print("Cualificació Final estudiant 1 :",cf1)
elif cual3_estud1 > cual1_estud1 and cual3_estud1 >cual2_estud1:
    if cual1_estud1 > cual2_estud1:
        cf1 = (cual3_estud1 + cual2_estud1)
    else:
        cf1 = (cual3_estud1 + cual1_estud1)
elif cual1_estud1 == cual2_estud1 and cual1_estud1 != cual3_estud1:
    if cual1_estud1 > cual3_estud1:
        cf1 = (cual1_estud1 + cual2_estud1)
    elif cual1_estud1 < cual3_estud1:
        cf1 = (cual3_estud1 + cual2_estud1)
    print("Cualificació Final estudiant 1 :",cf1)
elif cual3_estud1 == cual1_estud1 and cual1_estud1 != cual2_estud1:
    if cual2_estud1 > cual1_estud1:
         cf1 = (cual1_estud1 + cual2_estud1)
    else:
         cf1 = (cual1_estud1 + cual3_estud1)
    print("Cualificació Final estudiant 1 :",cf1)     
elif cual3_estud1 == cual2_estud1 and cual1_estud1 != cual1_estud1:
    if cual1_estud1 > cual2_estud1:
         cf1 = (cual1_estud1 + cual3_estud1)
    else:
         cf1 = (cual1_estud1 + cual2_estud1)
    print("Cualificació Final estudiant 1 :",cf1)
elif cual1_estud1 == cual2_estud1 == cual3_estud1:
    cf1 = cual1_estud1 + cual3_estud1 
    print("Cualificació Final estudiant 1 :",cf1)
    
    
if cual1_estud2 > cual2_estud2  and cual1_estud2 > cual3_estud2 :
    if cual2_estud2 > cual3_estud2:
        cf2 = (cual1_estud2 + cual2_estud2)
    elif cual3_estud2 >cual2_estud2:
        cuf2 = (cual1_estud2 + cual3_estud2)
    print("Cualificació Final estudiant 2 :",cf2)    
elif cual2_estud2 > cual1_estud2 and cual2_estud2 > cual3_estud2:
    if cual1_estud2 > cual3_estud2:
        cf2 = (cual1_estud2 + cual2_estud2)
    elif cual3_estud2 > cual1_estud2:
        cf2 = (cual3_estud2 + cual2_estud2)
    print("Cualificació Final estudiant 2 :",cf2)
elif cual3_estud2 > cual1_estud2 and cual3_estud2 >cual2_estud2:
    if cual1_estud2 > cual2_estud2:
        cf2 = (cual3_estud2 + cual2_estud2)
    else:
        cf2 = (cual3_estud2 + cual1_estud2)
elif cual1_estud2 == cual2_estud2 and cual1_estud2 != cual3_estud2:
    if cual1_estud2 > cual3_estud2:
        cf2 = (cual1_estud2 + cual2_estud2)
    elif cual1_estud2 < cual3_estud2:
        cf2 = (cual3_estud2 + cual2_estud2)
    print("Cualificació Final estudiant 2 :",cf2)
elif cual3_estud2 == cual1_estud2 and cual1_estud2 != cual2_estud2:
    if cual2_estud2 > cual1_estud2:
         cf2 = (cual1_estud2 + cual2_estud2)
    else:
         cf2 = (cual1_estud1 + cual3_estud1)
    print("Cualificació Final estudiant 2 :",cf2)     
elif cual3_estud2 == cual2_estud2 and cual1_estud2 != cual1_estud2:
    if cual1_estud2 > cual2_estud2:
         cf2 = (cual1_estud2 + cual3_estud2)
    else:
         cf2 = (cual1_estud2 + cual2_estud2)
    print("Cualificació Final estudiant 2 :",cf2)
elif cual1_estud2 == cual2_estud2 == cual3_estud2:
    cf2 = (cual1_estud2 + cual3_estud2)
    
if cf1 > cf2:
    print("La cualificació més gran és la del estudiant 1")
else:
    print("La cualificació més gran és la del estudiant 2")