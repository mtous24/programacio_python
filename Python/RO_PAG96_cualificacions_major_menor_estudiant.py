#RO_PAG96_cualificacions_major_menor_estudiant
from math import*
cual1 = float(input("Introdueix la cualificació 1 de l'estudiant:"))
cual2 = float(input("Introdueix la cualificació 2 de l'estudiant:"))
cual3 = float(input("Introdueix la cualificació 3 de l'estudiant:"))

if cual1 == cual2 and caul3 == cual2:
    print("Totes les cualificacions són iguals")
elif cual1 ==cual2 and cual1 != cual3:
    if cual3 > cual1:
        print("Cualificaió més gran:",cual1,"cualificació 1 i cualificació 2")
        print("Cualificació més petita:",cual3,"cualificació 3")
    else:
        print("Cualificaió més gran:",cual3,"cualificació 3")
        print("Cualificació més petita:",cual2,"cualificacions 1 i 2")
elif cual2 == cual3 and cual1 !=cual2:
    if cual1> cual3:
        print("Cualificaió més gran:",cual1,"cualificació 1")
        print("Cualificació més petita:",cual2,"cualificaciosn 2 i 3")
    else:
        print("Cualificaió més gran:",cual3,"cualificacions 2 i 3")
        print("Cualificació més petita:",cual2,"cualificació 1")
elif cual1 == cual3 and cual1 != cual2:
   if cual2> cual3:
       print("Cualificaió més gran:",cual2,"cualificació 2")
       print("Cualificació més petita:",cual1,"cualificacions 1 i 3")
   else:
       print("Cualificaió més gran:",cual3,"cualificacions 1 i 3")
       print("Cualificació més petita:",cual2,"cualificació 2")
elif cual1 != cual2 and cual3 != cual2 and cual1 != cual3:
    if cual1 > cual2 and cual1 >cual3:
        if cual2 > cual3:
            print("Cualificació més petita:",cual3,"cualificació 3")
        else:
             print("Cualificació més petita:",cual2,"cualificació 2")
        print("Cualificaió més gran:",cual1,"cualificació")
    elif cual2 > cual1 and cual1 > cual3:     
          if cual1 > cual3:
              print("Cualificació més petita:",cual3,"cualificació 3")
          else:
             print("Cualificació més petita:",cual1,"cualificació 1")
          print("Cualificaió més gran:",cual2,"cualificació 2")
    elif cual3 > cual2 and cual3 > cual1:
        if cual2 > cual1:
            print("Cualificació més petita:",cual1,"cualificació 1")
        else:
            print("Cualificació més petita:",cual2,"cualificació 2")
        print("Cualificaió més gran:",cual3,"cualificació 3")
           