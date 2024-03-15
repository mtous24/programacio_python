#mtous_exercici3_obres cons

def distancia(n,dm,a):
    dcm = dm *100
    dcm = dcm *n
    dcm = dcm -2*a
    return dcm
n = int(input("Nombre de cons:"))
dm =float(input("Distancia entre cons en metres:"))#Entre 10 i 30 m
a = float(input("Amplada dels cons:")) #Entre 10 i 50 cm