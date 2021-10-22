import csv 
header = ['Prenom', 'Nom', 'Fonction']
rows=[[]]
for i in range(2):
    prenom=input("prenom=?")
    nom=input("nom=?")
    fonction=input("fonction=?")
    row=[nom,prenom,fonction]
    rows.append(row)
with open('users.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerow(header) 
    write.writerows(rows) 
