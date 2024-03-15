#RO_PAG147_22_3granotes
from random import*
x1 = 10
x2 = 10
x3 = 10
i1 = 0
i2 = 0
i3 = 0
while (0 < x1 and x1 < 20) or (0 < x2 and x2 < 20) or (0 < x3 and x3 <20):
    i1 = i1 +1
    d1 = randint(1,4)
    if d1 == 1:
        x1 = x1
    elif d1 == 2:
        x1 = x1+0.5
    elif d1 == 3:
        x1 = x1 +1
    elif d1 == 4:
        x1 = x1 - 0.5
    d2 = randint(1,4)
    i2 = i2+1
    elif d2 == 1:
        x2 = x2
    elif d2 == 2:
        x2 = x2+0.5
    elif d2 == 3:
        x2 = x2 +1
    elif d2 == 4:
        x2 = x2-0.5
    d3 = randint(1,4)
    i3 = i3+1
    elif d3 == 1:
        x3 = x3
    elif d3 == 2:
        x3 = x3+0.5
    elif d3 == 3:
        x3 = x3 +1
    elif d2 == 4:
        x3 = x3-0.5
        
    
print(x1)
print(x2)
print(x3)