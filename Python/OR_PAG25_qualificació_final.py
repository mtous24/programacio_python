#OR_PAG25_nota_final

nota_examen = float(input("nota examen = "))
nota_llissons = float(input("nota llissons = "))
nota_tasca1 = float(input("nota tasca1 = "))
nota_tasca2 = float(input("nota tasca2 = "))
nota_tasca3 = float(input("nota tasca3 = "))

examen = nota_examen * 0.01
llissons = nota_llissons * 0.1
tasques = ((nota_tasca1, * 0.1 + nota_tasca2, * 0.1 + nota_tasca3, * 0.1)/3)
qf = (examen * 0.7 + llissons * 0.2 * tasques * 0.1) * 100

print("qualificació final = ",qf)

