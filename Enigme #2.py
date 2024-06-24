# Importe le module itertools qui fournit des fonctions créant des itérateurs pour des boucles efficaces
import itertools


# Définit une fonction nommée 'solve_cryptarithm'
def solve_cryptarithm():
    # Crée une chaîne de caractères contenant les lettres 'SENDMORY'
    letters = 'SENDMORY'

    # Pour chaque permutation possible des chiffres de 0 à 9 prises 7 à la fois (la longueur de 'letters')
    for perm in itertools.permutations(range(10), len(letters)):
        # Assigner chaque chiffre de la permutation aux variables s, e, n, d, m, o, r, y
        s, e, n, d, m, o, r, y = perm

        # Si 's' ou 'm' est égal à 0, passer à la prochaine permutation (car dans un nombre, le chiffre le plus à gauche ne peut pas être 0)
        if s == 0 or m == 0: continue

        # Calcule les valeurs numériques de 'send', 'more' et 'money' en utilisant les chiffres assignés aux lettres
        send, more, money = s * 1000 + e * 100 + n * 10 + d, m * 1000 + o * 100 + r * 10 + e, m * 10000 + o * 1000 + n * 100 + e * 10 + y

        # Si 'send' plus 'more' est égal à 'money'
        if send + more == money:
            # Affiche les valeurs de 'SEND', 'MORE' et 'MONEY'
            print(f"SEND: {send}\nMORE: {more}\nMONEY: {money}")

            # Affiche le 'Code secret (MONROE)'
            print(f"Code secret (MONROE): {m * 100000 + o * 10000 + n * 1000 + r * 100 + o * 10 + e}")

            # Retourne le 'Code secret (MONROE)'
            return m * 100000 + o * 10000 + n * 1000 + r * 100 + o * 10 + e


# Affiche le 'Code secret' qui est le résultat de la fonction 'solve_cryptarithm'
print(f"Le code secret est: {solve_cryptarithm()}")