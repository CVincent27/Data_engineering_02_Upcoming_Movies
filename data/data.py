import requests
from datetime import datetime

API_KEY = '0fffa6b984569317d8e03bc81fc79b07'
BASE_URL = 'https://api.themoviedb.org/3/movie/upcoming'
LANGUAGE = 'fr-FR'
MAX_PAGES = 5

def fetch_upcoming_movies():
    # Récupères les films via l'API sur 5 pages
    all_movies = []
    # stock uniq id
    seen_movie_ids = set() 
    page = 1  # Commence à la page 1
    
    while page <= MAX_PAGES:
        url = f'{BASE_URL}?api_key={API_KEY}&language={LANGUAGE}&page={page}'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            movies = data.get('results', [])
            
            if not movies:
                break 
            
            # Ajout des films à la liste si leur ID n'est pas déjà présent
            for movie in movies:
                if movie['id'] not in seen_movie_ids:
                    all_movies.append(movie)
                    seen_movie_ids.add(movie['id'])
            
            page += 1  
        else:
            break
    
    return all_movies

def process_movies_data(movies):
    """Traite les données des films et les trie par date de sortie."""
    upcoming_movies = []
    
    for movie in movies:
        release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')
        
        if release_date > datetime.now(): 
            upcoming_movies.append({
                'title': movie['title'],
                'release_date': release_date,  
                'overview': movie.get('overview', 'Aucune description disponible.')
            })
    
    # Trier les films par date de sortie
    upcoming_movies_sorted = sorted(upcoming_movies, key=lambda x: x['release_date'])

    # Convertir les dates de sortie en chaînes pour l'affichage final
    for movie in upcoming_movies_sorted:
        movie['release_date'] = movie['release_date'].strftime('%Y-%m-%d')

    return upcoming_movies_sorted
