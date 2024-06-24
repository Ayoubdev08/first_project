# Importation de la bibliothèque PIL (Python Imaging Library) pour manipuler des images
from PIL import Image

# Définition de la fonction 'b2d' qui convertit une chaîne binaire en un nombre décimal
def b2d(binaire):
    return int(binaire, 2)

# Définition de la fonction 'extract_bits_from_pixels' qui extrait le bit le moins significatif de chaque canal de couleur de chaque pixel
def extract_bits_from_pixels(pixels):
    return [rgb[i] % 2 for rgb in pixels for i in range(4)]

# Définition de la fonction 'write_to_file' qui écrit les bits décodés dans un fichier
def write_to_file(bits, filename):
    with open(filename, 'w') as f:
        for i in range(0, len(bits), 8):
            f.write(chr(b2d(''.join(map(str, bits[i:i+8])))))

# Ouverture de l'image PNG et affectation à la variable 'png'
png = Image.open('/home/abelaid/Téléchargements/Enigme5.png')
# Récupération des pixels de l'image et affectation à la variable 'pixels'
pixels = png.getdata()

# Extraction des bits des pixels et affectation à la variable 'ListeBits'
ListeBits = extract_bits_from_pixels(pixels)

# Écriture des bits dans le fichier 'Enigme_5_Reponse.txt'
write_to_file(ListeBits, 'Enigme_5_Reponse.txt')

# Affichage du message indiquant que le fichier 'Enigme_5_Reponse.txt' a été créé
print('Fichier Enigme_5_Reponse.txt créé')
# Affichage du message 'La Enigme_5_Reponse.txt:'
print('La Enigme_5_Reponse.txt:')