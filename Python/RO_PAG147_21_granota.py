#RO_PAG147_21_granota
from random import*
x = 0
i = 0
while x > -20 and x < 20:
    d = randint(1,2)
    i = i +1
    if d ==1:
        x = x+1
    else:
        x = x-1
print("Quantitat de salts realitzats per arribar a un extrem:",i)
print(x)
