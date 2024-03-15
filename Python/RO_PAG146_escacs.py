#RO_PAG146_escacs
ncaselles = 64
i = 0
while i < ncaselles:
    granscasella = pow(2,i)
    granscasellaant = granscasella
    print("Grans en cada casella:",granscasella)
    i = i+1
    ngrans = granscasella +granscasellaant
    ngransant = ngrans
ngranstotal = ngrans +ngransant
print("Nombre de grams total:",ngranstotal)
kg = ngranstotal / 20000
t = kg/1000
print("Tones dels grans demanats pel creador d'escacs:",t)
    

    
    