import csv 
header = ['Prenom', 'Nom', 'Fonction']
rows=[[]]
for i in range(1):
    prenom=input("prenom=?")
    nom=input("nom=?")
    fonction=input("fonction=?")
    row=[prenom,nom,fonction]
    rows.append(row) #ajouter une ligne au tableau
with open('users.csv', 'w') as f:  #créer et écrire dans le CSV (filepath)
    write = csv.writer(f) #pointer sur le ficher (créer le fichier)
    write.writerow(header) 
    write.writerows(rows) 
