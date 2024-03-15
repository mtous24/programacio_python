#RO_PAG71_pla de penssions
from math import*
print("Introdueix valor de cada diposit en euros:", end=" ")
p = float(input())
print("Introdueix interès mensual:", end=" ")
i = float(input())
print("Introdueix numero diposits mensuals efectuats:", end=" ")
num_diposits  = float(input()) 
mes = p + i * p
print("capital mes1 =",mes)
for x in range (2,num_diposits+1):
    if i == num_diposits :