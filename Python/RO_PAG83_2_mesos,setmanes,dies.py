#RO_PAG83_2_mesos,setmanes,dies
from math import*
print("nombre de dies :",end =" ")
n_dies = float(input())

mesos = n_dies//30
setmanes = n_dies%30//7
dies =n_dies%30%7

print(n_dies,"dies són",mesos,"mesos,",setmanes,"setmanes i ",dies,"dies")

