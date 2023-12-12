'''affichage du nombre de chiffres et nombre de chiffres disticts dans un nombre'''
# Fonction pour compter et afficher le nombre de chiffres dans l'entier
def compter_chiffres(entier):
    nb_chiffres = 0
    temp = entier
    while temp != 0:
        temp //= 10
        nb_chiffres += 1
    print(f"Le nombre d'éléments dans l'entier est : {nb_chiffres}")

# Fonction pour compter et afficher le nombre de chiffres distincts dans l'entier
def compter_chiffres_distincts(entier):
    chiffres = set()
    temp = entier
    while temp != 0:
        chiffre = temp % 10
        chiffres.add(chiffre)
        temp //= 10
    nb_chiffres_distincts = len(chiffres)
    print(f"Le nombre de chiffres distincts dans l'entier est : {nb_chiffres_distincts}")

# Saisie de l'entier par l'utilisateur
while True:
    try:
        entier = int(input("Entrez un nombre entier : "))
        compter_chiffres(entier)
        compter_chiffres_distincts(entier)
        break
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")
