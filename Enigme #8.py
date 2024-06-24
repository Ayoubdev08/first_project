# Définition de la fonction 'encode' qui prend en paramètre une chaîne de caractères 's'
def encode(s):
    # Retourne un entier formé par la concaténation des valeurs ASCII de chaque caractère de 's', formatées sur 3 chiffres
    return int(''.join(f"{ord(c):03}" for c in s))

# Définition de la fonction 'decode' qui prend en paramètre un entier 'x'
def decode(x):
    # Conversion de 'x' en chaîne de caractères, formatée sur 3 chiffres
    s = f"{x:03}"
    # Retourne une chaîne de caractères formée par la conversion en caractères des valeurs ASCII de chaque groupe de 3 chiffres de 's'
    return ''.join(chr(int(s[i:i+3])) for i in range(0, len(s), 3))

# Définition de la fonction 'rapide_exp' qui prend en paramètres trois entiers 'x', 'n' et 'p'
def rapide_exp(x, n, p):
    # Initialisation de 'result' à 1
    result = 1
    # Tant que 'n' est supérieur à 0
    while n > 0:
        # Si 'n' est impair
        if n % 2 == 1:
            # Multiplie 'result' par 'x' modulo 'p'
            result = (result * x) % p
        # Calcule le carré de 'x' modulo 'p'
        x = (x * x) % p
        # Divise 'n' par 2
        n //= 2
    # Retourne 'result'
    return result

# Définition de la fonction 'encrypte' qui prend en paramètres trois entiers 'e', 'n' et 'm'
def encrypte(e, n, m):
    # Retourne le résultat de l'appel à 'rapide_exp' avec 'm', 'e' et 'n' en paramètres
    return rapide_exp(m, e, n)

# Affectation de la paire (15213133, 881856821380357) aux variables 'e' et 'n'
(e, n) = (15213133, 881856821380357)
# Affichage du chiffrement de "OUI"
print("chiffrement de OUI : ", encrypte(e, n, encode("OUI")))
# Affichage du chiffrement de "NON"
print("chiffrement de NON : ", encrypte(e, n, encode("NON")))
# Affichage du chiffrement de "BLANC"
print("chiffrement de BLANC : ", encrypte(e, n, encode("BLANC")))
# Affectation de 229446820549265 à 'resultat'
resultat = 229446820549265
# Si le déchiffrement de 'resultat' est égal à "OUI", affiche "Alice a voté OUI", sinon affiche "Alice a voté NON"
print("Alice a voté OUI") if decode(rapide_exp(resultat, 17, 881856821380357)) == "OUI" else print("Alice a voté NON")