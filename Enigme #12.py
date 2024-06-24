# Définition de la fonction 'read_file' qui prend en paramètre un chemin de fichier 'file_path'
def read_file(file_path):
    # Ouverture du fichier en mode lecture ('r') et affectation à la variable 'file'
    with open(file_path, 'r') as file:
        # Retourne le contenu du fichier lu
        return file.read()

# Définition de la fonction 'format_text' qui prend en paramètres un texte 'text', une longueur de ligne 'line_length' et une taille de bâton 'stick_size'
def format_text(text, line_length, stick_size):
    # Retourne le texte formaté avec des retours à la ligne insérés à chaque 'stick_size' caractères
    return '\n'.join(text[i::stick_size] for i in range(stick_size))

# Définition de la fonction 'print_formatted_text' qui prend en paramètres un chemin de fichier 'file_path', une longueur de ligne 'line_length' et une taille de bâton 'stick_size'
def print_formatted_text(file_path, line_length, stick_size):
    # Lecture du fichier et affectation du contenu à la variable 'text'
    text = read_file(file_path)
    # Affichage de la taille du bâton
    print(f"Stick size: {stick_size}")
    # Affichage du texte formaté
    print(format_text(text, line_length, stick_size))

# Appel de la fonction 'print_formatted_text' avec le chemin du fichier, la longueur de ligne et la taille du bâton en paramètres
print_formatted_text('/home/abelaid/Téléchargements/Enigme12.txt', 90, 5)