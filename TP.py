#Ex1
#Q1
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
ventes = [125000, 98000, 143500, 87000, 210000, 176500]


Total = sum(ventes)
Moyenne = Total / len(ventes)

print(f"La total de ventes est égal :{Total} MRU")
print(f"La moyenne de ventes est égal : {Moyenne} MRU")
#Q2
vente_max = 0
index_max = 0
for i in range (len(ventes)):
    if vente_max < ventes[i]:
        vente_max = ventes[i]
        index_max = i

print(vente_max)
print(index_max)
print(jours[index_max])

#Q3
jour_vente_max = []
for i in range (len(ventes)):
    if Moyenne < ventes[i]:
        print(jours[i])
        jour_vente_max.append(jours[i])
print(jour_vente_max)

#Q4
jours_tries = list(jours)
ventes_tries = list(ventes)

for i in range (len(jours_tries)):
    for j in range (i + 1, len(ventes_tries)):
        if ventes_tries[j] > ventes_tries[i]:
            ventes_tries[i] , ventes_tries[j]= ventes_tries[j], ventes_tries[i]
            jours_tries[i], jours_tries[j] = jours_tries[j], jours_tries[i]

print(jours_tries)
print(ventes_tries)
for i in range(len(jours_tries)):
    print(f"- {jours_tries[i]} : {ventes_tries[i]} MRU")

#Ex3
catalogue = {
"P01": {"nom": "Ordinateur portable", "categorie": "Informatique",
"prix": 45000},
"P02": {"nom": "Imprimante", "categorie": "Informatique",
"prix": 12000},
"P03": {"nom": "Chaise de bureau", "categorie": "Mobilier",
"prix": 6500},
"P04": {"nom": "Ramette papier", "categorie": "Fournitures",
"prix": 350},
}
print(catalogue)
#Q1
catalogue["P05"] = {"nom": "Bureau", "categorie": "Mobilier", "prix": 18000}
print(catalogue)
#Q2
for produit in catalogue.values():
    if produit["categorie"] == "Informatique":
        produit["prix"] = round(produit["prix"] * 1.05)

print(catalogue)

#Q3
del catalogue["P04"]
print(catalogue)