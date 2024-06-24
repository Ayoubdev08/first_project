# Définition de la fonction 'shadok_to_decimal' qui prend en paramètre une chaîne de caractères 'shadok_number'
def shadok_to_decimal(shadok_number):
    # Création d'un dictionnaire 'shadok_digits' qui associe chaque chiffre Shadok à sa valeur décimale
    shadok_digits = {'GA': 0, 'BU': 1, 'ZO': 2, 'MEU': 3}

    # Retourne la somme des valeurs décimales de chaque chiffre Shadok dans 'shadok_number', multipliée par 4 à la puissance de sa position
    # 'enumerate(reversed(shadok_number.split()))' donne l'indice et la valeur de chaque chiffre Shadok dans 'shadok_number', en partant de la fin
    return sum(shadok_digits[symbol] * (4 ** i) for i, symbol in enumerate(reversed(shadok_number.split())))


# Création d'une chaîne de caractères 'shadok_number' représentant un nombre en Shadok
shadok_number = "BU MEU ZO MEU GA GA"

# Affichage du nombre Shadok 'shadok_number' converti en décimal
print(f"Le nombre Shadok '{shadok_number}' en décimal est : {shadok_to_decimal(shadok_number)}")
