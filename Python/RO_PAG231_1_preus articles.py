#RO_PAG231_1_preus articles
llista_preus = []
articles_comprar = []
articles = []
n = int(input("Quantitat d'articles que hi han:"))
q = float(input("Quantitat de diners disponibles(€):"))
p =q
for i in range(1,n+1):
    x = float(input("Preu de l'article següent(€):"))
    if q > x:
        q = q-x
        articles_comprar = articles_comprar +[i]
    llista_preus = llista_preus +[x]
    articles = articles + [i]
    
print("Articles",articles)    
print("El preu de cada article, respectivament:", llista_preus)
print("")
print("Articles que es poden comprar amb",p,"€:",articles_comprar)





    
    
