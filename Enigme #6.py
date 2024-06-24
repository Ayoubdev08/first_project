# Importation des modules 'time' et 'random'
import time
import random


# Définition de la fonction 'generer_code_pin' qui génère un code PIN aléatoire de 6 chiffres
def generer_code_pin():
    return str(random.randint(0, 999999)).zfill(6)


# Définition de la fonction 'verifier_proposition' qui vérifie combien de chiffres dans la proposition correspondent au code PIN
def verifier_proposition(proposition, code_pin):
    return sum(p == c for p, c in zip(proposition, code_pin))


# Définition de la fonction 'verifier_longueur_code_pin' qui vérifie si le code PIN a une longueur de 6 et ne contient que des chiffres
def verifier_longueur_code_pin(code_pin):
    return len(code_pin) == 6 and code_pin.isdigit()


# Définition de la fonction 'deviner_code_pin_utilisateur' qui permet à l'utilisateur de deviner le code PIN
def deviner_code_pin_utilisateur(code_pin):
    start_time = time.time()
    timeout = 300

    while time.time() - start_time < timeout:
        remaining_time = int(timeout - (time.time() - start_time))
        proposition = input(
            f"Entrez votre proposition de code PIN (6 chiffres). Temps restant : {remaining_time} secondes : ")

        if verifier_longueur_code_pin(proposition):
            if proposition == code_pin:
                print(f"Bravo ! Vous avez trouvé le code PIN en {time.time() - start_time:.2f} secondes.")
                return
            else:
                print(f"{verifier_proposition(proposition, code_pin)} chiffre(s) correct(s). Essayez encore.")
        else:
            print("Erreur : Le code PIN doit contenir exactement 6 chiffres.")

    print("Temps écoulé ! Vous avez perdu.")


# Définition de la fonction 'deviner_code_pin_ordinateur' qui permet à l'ordinateur de deviner le code PIN
def deviner_code_pin_ordinateur(password):
    guess = "000000"
    start_time = time.time()

    for i in range(6):
        for n in range(10):
            temp_guess = guess[:i] + str(n) + guess[i + 1:]
            print(f"Essai #{n + 1} pour la position {i + 1} : {temp_guess}")

            if temp_guess[i] == password[i]:
                guess = temp_guess
                break

    print(f"L'ordinateur a trouvé le code PIN en {time.time() - start_time:.2f} secondes!")
    print("Le code PIN est : ", guess)


# Définition de la fonction 'main' qui gère le déroulement du jeu
def main():
    while True:
        mode = input("Choisissez le mode de jeu: (1) Vous devinez le code PIN généré par l'ordinateur "
                     "(2) L'ordinateur devine votre code PIN : ")

        if mode == '1':
            code_pin = generer_code_pin()
            print(
                "L'ordinateur a généré un code PIN à 6 chiffres. À vous de deviner et d'essayer d'être plus rapide que l'ordinate!")
            deviner_code_pin_utilisateur(code_pin)
        elif mode == '2':
            password = input("Entrez un code PIN de 6 chiffres que l'ordinateur doit deviner: ")
            if verifier_longueur_code_pin(password):
                deviner_code_pin_ordinateur(password)
            else:
                print("Erreur : Le code PIN doit contenir exactement 6 chiffres.")
        else:
            print("Mode de jeu invalide. Veuillez réessayer.")

        if input("Voulez-vous rejouer? (O/N) : ").lower() != "o":
            print("Merci d'avoir joué! À une prochaine fois 👋")
            break


# Exécution de la fonction 'main' si le script est exécuté directement
if __name__ == "__main__":
    main()
