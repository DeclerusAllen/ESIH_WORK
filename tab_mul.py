'''Mardi 12/12/2023'''
'''la multiplication de deux matrices.'''
import numpy as np

# Fonction pour vérifier si un nombre est premier
def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Saisie des valeurs pour la matrice A
print("Remplissage de la matrice A (5x3) avec des entiers positifs non nuls :")
matrice_A = []
for i in range(5):
    ligne = []
    for j in range(3):
        while True:
            try:
                valeur = int(input(f"Saisissez l'élément [{i}][{j}] de la matrice A : "))
                if valeur <= 0:
                    print("Veuillez entrer un entier positif non nul.")
                else:
                    ligne.append(valeur)
                    break
            except ValueError:
                print("Veuillez entrer un entier valide.")

    matrice_A.append(ligne)

# Saisie des valeurs pour la matrice B (nombres premiers)
print("\nRemplissage de la matrice B (3x2) avec des nombres premiers :")
matrice_B = []
for i in range(3):
    ligne = []
    for j in range(2):
        while True:
            try:
                nombre = int(input(f"Saisissez le nombre premier [{i}][{j}] : "))
                if est_premier(nombre):
                    ligne.append(nombre)
                    break
                else:
                    print("Veuillez entrer un nombre premier.")
            except ValueError:
                print("Veuillez entrer un nombre valide.")
    matrice_B.append(ligne)

# A*B
try:
    matrice_A = np.array(matrice_A)
    matrice_B = np.array(matrice_B)
    matrice_C = np.dot(matrice_A, matrice_B)

    # Matrice
    print("\nLe produit des matrices A et B (matrice C) est :")
    print(matrice_C)
except ValueError:
    print("Assurez-vous que les dimensions des matrices sont correctes pour effectuer le produit.")
    

