#A taper dans le terminal avant :
# pip install pandas
# pip install matplotlib

### import librairies

import pandas as ps #représenter tableaux données sous forme de dataframe
import matplotlib.pyplot as plt
# import numpy as np

############################## Importation donées ##############################
gares = ps.read_csv('referentiel-gares-voyageurs.csv', sep=";")
tarifs = ps.read_csv('tarifs-tgv-inoui-ouigo.csv', sep=";")
TER = ps.read_csv('tarifs-ter-par-od.csv', sep=";")

# Observation des jeux de données
print("Observation données")
print(tarifs["Profil tarifaire"].value_counts()) #2 modalités differentes
print(tarifs["Classe"].value_counts()) #2 modalités differentes

print("-----------------------------")


# Nettoyage des données
print("Nettoyage des données")

print("-----------------------------")
#jeu de données symétrique ?

# Nouveaux data selon Classe et Tarif du trajet
#tarifs_N1 = tarifs.groupby(['Classe', 'Profil tarifaire']).get_group((1, 'Tarif Normal'))
#tarifs_N2 = tarifs.groupby(['Classe', 'Profil tarifaire']).get_group((2, 'Tarif Normal'))
#tarifs_R1 = tarifs.groupby(['Classe', 'Profil tarifaire']).get_group((1, 'Tarif Réglementé'))
#tarifs_R2 = tarifs.groupby(['Classe', 'Profil tarifaire']).get_group((2, 'Tarif Réglementé'))

# Afficher les dataframes
"""
print(tarifs_N1)
print(tarifs_N2)
print(tarifs_R1)
print(tarifs_R2)
"""
### Demander quel tarif et classe à l'utilisateur pour séléctionner la bonne table
classe = input("En quelle classe voulez-vous voyager ?") # 1 ou 2
profil = input("A quel tarif pouvez-vous prétendre ?") #Réglementé ou Normal

if classe == 1 :
    if profil == "Normal" :
       tarif_app = tarifs.groupby(['Classe', 'Profil tarifaire']).get_group((1, 'Tarif Normal'))
    elif profil == "Réglementé" :
        tarif_app = tarifs.groupby(['Classe', 'Profil tarifaire']).get_group((1, 'Tarif Réglementé'))
    else :
        tarif_app = tarifs.groupby(['Classe']).get_group((1))
elif classe == 2 :
    if profil == "Normal" :
       tarif_app = tarifs.groupby(['Classe', 'Profil tarifaire']).get_group((2, 'Tarif Normal'))
    elif profil == "Réglementé" :
        tarif_app = tarifs.groupby(['Classe', 'Profil tarifaire']).get_group((2, 'Tarif Réglementé'))
    else :
        tarif_app = tarifs.groupby(['Classe']).get_group((2))
else :
    tarif_app = tarifs

#### Création dict depuis dataframe

# On selectionne les variables qui nous interessent pour créer le dictionnaire
test_app = tarif_app.iloc[:,[1,3,7]]
# regrouper les données par gare de départ
regroupement_garesOrigine = test_app.groupby('Gare origine')

# créer un dictionnaire avec une expression lambda appliquée à chaque groupe
graph = regroupement_garesOrigine.apply(lambda x: dict(zip(set(x['Destination']), x['Prix minimum'])))
# la fct set permet de retirer les doublons de gare d'arrivée (donc un trajet entre 2 gares = tjrs meme prix classe et tarif non prix en compte)
# la fct zip associe le prix minimum entre la gare d'arrivée et la clef (gare départ)
# la fct dict permet de mettre les resultats dans un dict

# transformer l'objet pandas Series obtenu en un dictionnaire
graph = graph.to_dict()
print(graph)
print("-----------------------------")