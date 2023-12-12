'''tri par colonne d'une matrice carrée en ordre décroissant'''
# Fonction pour saisir une matrice de taille 6x6
def saisie_matrice():
    matrice = []
    for i in range(6):
        ligne = []
        for j in range(6):
            while True:
                try:
                    valeur = int(input(f"Saisissez l'élément [{i}][{j}]: "))
                    if valeur < 0:
                        print("Veuillez entrer un entier positif.")
                    else:
                        ligne.append(valeur)
                        break
                except ValueError:
                    print("Veuillez entrer un entier valide.")
        matrice.append(ligne)
    return matrice

# Fonction pour afficher la matrice
def afficher_matrice(matrice):
    for ligne in matrice:
        print(" ".join(map(str, ligne)))
    print()

# Fonction pour trier les colonnes en ordre décroissant
def tri_colonnes(matrice):
    for j in range(6):
        colonne = [matrice[i][j] for i in range(6)]
        colonne.sort(reverse=True)
        for i in range(6):
            matrice[i][j] = colonne[i]

# Saisie de la matrice
print("Saisie de la matrice :")
matrice = saisie_matrice()

if matrice:
    # Affichage de la matrice non triée
    print("\nMatrice non triée :")
    afficher_matrice(matrice)

    # Tri des colonnes en ordre décroissant
    tri_colonnes(matrice)

    # Affichage de la matrice triée
    print("Matrice triée par colonnes en ordre décroissant :")
    afficher_matrice(matrice)
