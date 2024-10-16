# 1. Création d'un application web Flask
# 2. Extration des données 
# 3. Prétraitement des données
# 4. Chargement des données

from flask import Flask
from api.api import api

app = Flask(__name__)

app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)
