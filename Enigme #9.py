import hashlib

# Définition des constantes fournies
x, y, m, p, target = "A", "B", "5", "42", 2**250

def double_sha256(s):
    """Fonction pour calculer le double SHA-256 d'une chaîne de caractères"""
    # Calcul du premier hachage SHA-256 et conversion en hexadécimal
    first_hash = hashlib.sha256(s.encode()).hexdigest()
    # Calcul du deuxième hachage SHA-256 à partir du premier hachage, converti en hexadécimal
    second_hash = hashlib.sha256(first_hash.encode()).hexdigest()
    return second_hash

n = 0
# Tant que le résultat du double hachage est supérieur ou égal à la cible, incrémenter n
while int(double_sha256(x + y + m + p + str(n)), 16) >= target:
    n += 1

print(f"Le plus petit entier n permettant la validation de la transaction est: {n}")
