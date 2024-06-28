# Ligne 1: Importe les classes et fonctions nécessaires depuis le module Flask.
from flask import Flask, request, jsonify, render_template
# Ligne 2: Importe le module SQLite pour interagir avec la base de données.
import sqlite3

# Ligne 4: Initialise une instance de l'application Flask.
app = Flask(__name__)


# Ligne 6-13: Définit une fonction `init_db` pour initialiser la base de données SQLite.
def init_db():
    conn = sqlite3.connect('database.db')  # Établit une connexion à la base de données SQLite `database.db`.
    c = conn.cursor()  # Crée un curseur pour exécuter des requêtes SQL.
    c.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            expression TEXT NOT NULL,
            result TEXT NOT NULL
        )
    ''')  # Exécute une commande SQL pour créer une table `history` si elle n'existe pas déjà.
    conn.commit()  # Valide les modifications dans la base de données.
    conn.close()  # Ferme la connexion à la base de données.


# Ligne 17: Définit une route pour l'URL racine de l'application.
@app.route('/')
def index():
    return render_template('index.html')  # Renvoie un template HTML nommé `index.html`.


# Ligne 21-32: Définit une route pour gérer les requêtes POST vers `/calculate`.
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()  # Récupère les données JSON envoyées dans la requête POST.
    expression = data['expression']  # Extrait l'expression mathématique à évaluer depuis les données JSON reçues.
    try:
        result = str(eval(expression))  # Évalue l'expression à l'aide de la fonction `eval` de Python.
        save_to_history(expression, result)  # Enregistre l'expression et le résultat dans la base de données.
        return jsonify(result=result)  # Renvoie le résultat au format JSON.
    except Exception as e:
        return jsonify(result='Error')  # En cas d'erreur, renvoie un message d'erreur au format JSON.


# Ligne 36-41: Définit une route pour gérer les requêtes GET vers `/history`.
@app.route('/history', methods=['GET'])
def history():
    conn = sqlite3.connect('database.db')  # Établit une connexion à la base de données SQLite `database.db`.
    c = conn.cursor()  # Crée un curseur pour exécuter des requêtes SQL.
    c.execute(
        'SELECT expression, result FROM history ORDER BY id DESC')  # Exécute une requête SQL pour récupérer l'historique des calculs.
    rows = c.fetchall()  # Récupère toutes les lignes résultantes de la requête.
    conn.close()  # Ferme la connexion à la base de données.
    return jsonify(
        history=[{'expression': row[0], 'result': row[1]} for row in rows])  # Renvoie l'historique au format JSON.


# Ligne 45-49: Définit une fonction `save_to_history` pour enregistrer l'expression et le résultat dans la base de données.
def save_to_history(expression, result):
    conn = sqlite3.connect('database.db')  # Établit une connexion à la base de données SQLite `database.db`.
    c = conn.cursor()  # Crée un curseur pour exécuter des requêtes SQL.
    c.execute('INSERT INTO history (expression, result) VALUES (?, ?)',
              (expression, result))  # Exécute une requête SQL pour insérer les données dans la table `history`.
    conn.commit()  # Valide les modifications dans la base de données.
    conn.close()  # Ferme la connexion à la base de données.


# Ligne 52-54: Point d'entrée principal du script.
if __name__ == '__main__':
    init_db()  # Initialise la base de données.
    app.run(debug=True)  # Lance l'application Flask en mode débogage.