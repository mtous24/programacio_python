#RO_PAG96_sous
from math import*
hores_joan = float(input("Hores setmanals treballades pel Joan:"))
hores_pere = float(input("Hores setmanals treballades pel Pere:"))
hores_josep = float(input("Hores setmanals treballades pel Josep:"))
salarih_joan = float(input("Salri per hora d'en Joan:"))
salarih_pere = float(input("Salari per hora d'en Pere:"))
salarih_josep = float(input("Salari per hora d'en Josep:"))
descontes_joan = float(input("Descontes d'en Joan."))
descontes_pere = float(input("Descontes d'en Pere:"))
descontes_josep = float(input("Descontes d'el Josep:"))

salarib_joan = salarih_joan * hores_joan
salarib_pere = salarih_pere * hores_pere
salarib_josep = salarih_josep * hores_josep
print("Salari brut d'en Joan:",salarib_joan)
print("Salari brut d'en Josep:",salarib_josep)
print("Salari brut d'en Pere:",salarib_pere)
salarin_joan = salarib_joan * descontes_joan
salarin_pere = salarib_pere * descontes_pere
salarin_josep = salarib_josep * descontes_josep
print("Salari net d'en Joan:",salarin_joan)
print("Salari net d'en Josep:",salarin_josep)
print("Salari net d'en Pere:",salarin_pere)

if salarin_joan == salarin_josep and salarin_joan == salarin_pere:
    print("Els tres cobren el mateix, el màxim sou,",salarin_pere,"€ setmanals")
elif salarin_joan == salarin_josep and salarin_josep != salarin_pere:
    if salarin_pere > salarin_josep:
         print("El Pere cobra el màxim sou,",salarin_pere,"€ setmanals")
    else:
        print("El Joan i el Jopep cobren el mateix, el màxim sou,",salarin_joan,"€ setmanals")
elif salarin_joan == salarin_pere and salarin_joan != salarin_josep:
    if salarin_josep >salarin_pere:
        print("El Josep cobra el màxim sou,",salarin_josep,"€ setmanals")
    else:
        print("El Pere i el Joan cobre el mateix, el màxim sou,",salarin_joan,"€ setmanals")
elif salarin_pere == salarin_josep and salarin_pere != salarin_joan:
    if salarin_joan > salarin_pere:
        print("El Joan cobra el sou màxim,",salarin_joan,"€ setmanals")
    else:
        print("El Pere i el Josep cobre el mateix, el màxim sou,",salarin_josep,"€ setmanals")
elif salarin_josep != salarin_joan and salarin_pere != salarin_joan and salarin_josep != salarin_pere:
    if salarin_josep > salarin_joan and salarin_josep > salarin_pere:
        print("El Jossep cobra el sou màxim,",salari_josep,"€ setmanals")
    elif: salarin_pere > salarin_joan and salarin_pere > salarin_josep:
        print("El Pere cobra el sou màxim,",salarin_pere,"€ setmanals")
     else:
         print("El Joan cobra el sou màxim,"salarin_joan,"€ setamanals")