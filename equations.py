'''resolution d'une equation du second degré'''
import math

# Fonction pour calculer le discriminant
def calculer_discriminant(a, b, c):
    return b ** 2 - 4 * a * c

# Procédure pour calculer et afficher les solutions selon le discriminant
def calculer_et_afficher_solution(a, b, c):
    delta = calculer_discriminant(a, b, c)
    
    if delta > 0:
        racine_delta = math.sqrt(delta)
        x1 = (-b + racine_delta) / (2 * a)
        x2 = (-b - racine_delta) / (2 * a)
        print(f"Deux solutions réelles distinctes : x1 = {x1} et x2 = {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Une solution réelle double : x = {x}")
    else:
        racine_delta = math.sqrt(abs(delta))
        partie_reelle = -b / (2 * a)
        partie_imaginaire = racine_delta / (2 * a)
        print(f"Deux solutions complexes conjuguées : "
              f"x1 = {partie_reelle} + {partie_imaginaire}i et "
              f"x2 = {partie_reelle} - {partie_imaginaire}i")

# Saisie des coefficients de l'équation
while True:
    try:
        a = float(input("Entrez le coefficient a : "))
        b = float(input("Entrez le coefficient b : "))
        c = float(input("Entrez le coefficient c : "))
        
        if a == 0:
            print("Ce n'est pas une équation du second degré (a doit être différent de 0).")
        else:
            calculer_et_afficher_solution(a, b, c)
        break
    except ValueError:
        print("Veuillez entrer des coefficients valides (nombres réels).")
