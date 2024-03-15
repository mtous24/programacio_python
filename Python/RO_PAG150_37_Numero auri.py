#RO_PAG150_37_Numero auri
n = int(input(" n = "))
print("Parelles de númerus (a,b) entre 1 i n, que no satisfasin el número auri")
for a in range (1,n+1):
    for b in range (1, n+1):
        if not a/b == (a+b)/a:
            print("(a,b) =",(a,b))
print("Les parelles de números no satisfan al número auri")