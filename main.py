# 1. Création d'un application web Flask
# 2. Extration des données 
# 3. Prétraitement des données
# 4. Chargement des données

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Test API"})

if __name__ == '__main__':
    app.run(debug=True)
