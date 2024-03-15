#RO_PAG104_bacteries
n = int(input("Introdueixi la quantitat inicial de bactèries:"))
m = int(input("Introdueixi la quantitat màxima de bactèries:"))
d = 0
while n <= m:
    n = 2*n
    d = d+1
print("Dies en que les bactèries arriben a la quantitat màxima:",d)    