# Définition de la fonction 'flip' qui prend en paramètres une liste 'arr' et un indice 'i'
def flip(arr, i):
    # Initialisation de la variable 'start' à 0
    start = 0
    # Tant que 'start' est inférieur à 'i'
    while start < i:
        # Stockage temporaire de la valeur de 'arr[start]' dans 'temp'
        temp = arr[start]
        # Remplacement de 'arr[start]' par 'arr[i]'
        arr[start] = arr[i]
        # Remplacement de 'arr[i]' par 'temp' (la valeur originale de 'arr[start]')
        arr[i] = temp
        # Incrémentation de 'start'
        start += 1
        # Décrémentation de 'i'
        i -= 1

# Définition de la fonction 'pancake_sort' qui prend en paramètre une liste 'arr'
def pancake_sort(arr):
    # Initialisation de la variable 'curr_size' à la longueur de 'arr'
    curr_size = len(arr)
    # Tant que 'curr_size' est supérieur à 1
    while curr_size > 1:
        # Trouver l'indice du maximum de 'arr' jusqu'à l'indice 'curr_size'
        mi = arr.index(max(arr[0:curr_size]))
        # Appel de la fonction 'flip' sur 'arr' et 'mi'
        flip(arr, mi)
        # Appel de la fonction 'flip' sur 'arr' et 'curr_size - 1'
        flip(arr, curr_size-1)
        # Décrémentation de 'curr_size'
        curr_size -= 1

# Initialisation de la liste 'pile'
pile = [6, 4, 9, 2, 1, 8, 3, 7, 5]
# Affichage de 'pile'
print(pile)
# Appel de la fonction 'pancake_sort' sur 'pile'
pancake_sort(pile)
# Affichage de 'pile' après le tri
print(pile)