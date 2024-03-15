#RO_PAG147_14_articles
articles = [454,768,1000,2347]
diners = 1000
articles_comprats = 0
a = 0
for n in range (4):
    if articles[n] <= diners:
       a = diners//articles[n]
       articles_comprats = articles_comprats +1
       print("Podem comprar",a,"unitat de l'article",n)
    if n ==len(articles)-1:
        print("articles que podem comprar =",articles_comprats)
        
#articles = [454,768,1000,2347]
# diners = 1000
articles_comprats = 0

k = 1
for n in articles:
    if articles[n] <= diners:
       a = diners//articles[n]
       articles_comprats = articles_comprats +1
       print("Podem comprar",a,"unitat de l'article",n)
    if n ==len(articles)-1:
        print("articles que podem comprar =",articles_comprats)
    
#articles = [454,768,1000,2347]
# diners = 1000
articles_comprats = 0    