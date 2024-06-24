with open('/home/abelaid/Téléchargements/Enigme1.txt') as fichier:

    # Pour chaque ligne dans le fichier, divise la ligne en mots, convertit chaque mot en un entier, puis en un caractère, et les joint tous dans une chaîne de caractères
    # Le résultat final est stocké dans la variable 'final_result'
    final_result = ''.join(chr(int(word)) for line in fichier for word in line.split())

    # Affiche le résultat final à l'écran
    print(final_result)