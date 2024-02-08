import numpy as np
import matplotlib.pyplot as plt

# Tableau de tableaux contenant des mots
tableau_de_tableaux = [
    ["le", "chat", "mange", "la", "souris"],
    ["la", "souris", "court", "vite"],
    ["le", "chien", "aboie"]
]

# Calcul du positionnement moyen de chaque mot
longueurs = [len(sous_tableau) for sous_tableau in tableau_de_tableaux]
mots_uniques = list(set([mot for sous_tableau in tableau_de_tableaux for mot in sous_tableau]))

positionnements_moyens = [np.mean([sous_tableau.index(mot) + 1 if mot in sous_tableau else 0 for sous_tableau in tableau_de_tableaux]) for mot in mots_uniques]

# Trier les mots et leurs positionnements moyens par ordre croissant de longueur
mots_positionnements_tries = sorted(zip(mots_uniques, positionnements_moyens), key=lambda x: x[1])

mots_tries = [mot[0] for mot in mots_positionnements_tries]
positionnements_moyens_tries = [mot[1] for mot in mots_positionnements_tries]

# Création du graphique
plt.bar(mots_tries, positionnements_moyens_tries)
plt.xlabel('Mots')
plt.ylabel('Positionnement moyen')
plt.title('Positionnement moyen de chaque mot dans les sous-tableaux (rangé par longueur de mot)')
plt.show()