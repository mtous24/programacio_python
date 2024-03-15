#RO_PAG180_1_divisors
n = int(input("Introdueix el nombre:"))
def conteo(n):
    count = 0
    for i in range(1, n+1):
        a = n%i
        if a == 0:
            count = count + 1
    return count
print(conteo(n))

        
    