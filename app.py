# Importation des modules nécessaires depuis le framework Flask
from flask import Flask, render_template, request, jsonify

# Initialisation d'une application Flask
app = Flask(__name__)

# Définition d'une route pour l'URL racine '/'
@app.route('/')
def index():
    return render_template('index.html')  # Rend le modèle HTML nommé 'index.html'

# Définition d'une route pour '/calculate' qui accepte les requêtes POST
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Récupération des données JSON depuis la requête
        data = request.get_json()
        # Extraction de la valeur 'expression' depuis les données JSON
        expression = data['expression']
        # Évaluation de l'expression à l'aide de la fonction eval() de Python
        result = eval(expression)
        # Retourne le résultat sous forme de réponse JSON
        return jsonify({'result': result})
    except Exception as e:
        # Si une erreur se produit pendant l'évaluation, retourne le message d'erreur en JSON
        return jsonify({'error': str(e)})

# Exécute l'application Flask si ce script est lancé directement
if __name__ == '__main__':
    app.run(debug=True)
