#OR_PAG41_2_vots-1-0
num_vots = int(input("Número de vots = "))
sis = 0
nos = 0

for comptador in range(1,num_vots+1,1):
    print("Vot",comptador, "= ", end = " ")
    num_valor =float(input())
    if num_valor == 1:
        sis = sis +1
    else:
        nos = nos +1
print("Vots a favor = ",sis)
print("Vots en contra =", nos)
    