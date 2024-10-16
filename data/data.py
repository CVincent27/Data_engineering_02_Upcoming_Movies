import requests
from datetime import datetime

API_KEY = '0fffa6b984569317d8e03bc81fc79b07'
BASE_URL = 'https://api.themoviedb.org/3/movie/upcoming'
LANGUAGE = 'fr-FR'

def get_upcoming_movies():
    # Récupération des films à venir
    url = f'{BASE_URL}?api_key={API_KEY}&language={LANGUAGE}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get('results', [])
    else:
        return []
    
def 