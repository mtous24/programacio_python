#RO_PAG100_aleatoris
from random import*
x = 0
cl = 0
c1 =0
c2 = 0
c3=0
c4 =0
c5 =0
while x != 6:
    cl = cl +1
    x = randint(1, 6)
    print(x)
    if x ==1:
        c1 = c1+1
    elif x ==2:
        c2 =c2+1
    elif x ==3:
        c3 = c3+1
    elif x ==4:
        c4 = c4+1
    else:
        c5 = c5 +1
print("Quantitat de llençaments per tal de que sorti el número 6:",cl)
print ("Quantitat de vegades que ha sortit el número 1:",c1)
print ("Quantitat de vegades que ha sortit el número 2:",c2)
print("Quantitat de vegades que ha sortit el número 3:",c3)
print ("Quantitat de vegades que ha sortit el número 4:",c4)
print ("Quantitat de vegades que ha sortit el número 5:",c5)