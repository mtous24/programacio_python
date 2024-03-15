#RO_PAG95_dimensions_bloc
from math import*

x = float(input("Introdueix el radi del bolc regular(x) en cm:"))
y = float(input("Introdueix l'altura del bloc regular(y) en cm:"))
z = float(input("Introdueix la profunditat del bloc regular(z) en cm:"))

diagonal1 = sqrt(pow(x,2) + pow(y,2))
diagonal2 = sqrt(pow(x,2) + pow(z,2))
diagonal3 = sqrt(pow(y,2) + pow(z,2))

if diagonal1 == diagonal2 and diagonal3 == diagonal1:
    print("Totes les diagonals són iguals i fan",diagonal1,"cm de llarg")
elif diagonal == diagonal2 and diagonal3 != diagonal1:
    if diagonal3>diagonal1:
        print("La diagonal 3 és la més gran  i fa",diagonal3,"cm de llarg")
    else:
        print("Les diagonals 1 i 2 són les més grans i fan",diagonal1,"cm de llarg")
elif diagonal2 == diagonal3 and diagonal1 != diagonal3:
    if diagonal1>diagonal3:
        print("Les diagonals 1 i 2 són les més grans i fan",diagonal1,"cm de llarg")
    else:
        print("La diagonal 3 és la més gran i fa",diagonal3,"cm de llarg")
elif diagonal1 == diagonal3 and diagonal2 != diagonal1:
    if diagonal2>diagonal1:
        print("La diagonal 2 és la més gran i fa",diagonal2,"cm de llarg")
    else:
        print("Les diagonals 1 i 3 són les més grans i fan",diagonal1,"cm de llarg")
else:
    if diagonal1>diagonal2 and diagonal1>diagonal3:
        print("La diagonal 1 és la més gran i fa",diagonal1,"cm de llarg")
    elif diagonal2>diagonal1 and diagonal2>diagonal3:
        print("La diagonal 2 és la més gran fa",diagonal2,"cm de llarg")
    elif diagonal3>diagonal1 and diagonal3>diagonal1:
        print("La diagonal 3 és la més gran i fa",diagonal3,"cm de llarg")
    
