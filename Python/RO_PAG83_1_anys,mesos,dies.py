#RO_PAG83_1_anys,mesos,dies
from math import*
print("nombre de dies :",end =" ")
n_dies = float(input())

anys = n_dies//365
mesos = n_dies%365//30
dies =n_dies%365%30

print(n_dies,"dies són",anys,"anys,",mesos,"meosos i ",dies,"dies")



