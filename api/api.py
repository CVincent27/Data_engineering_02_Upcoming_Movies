from flask import Blueprint, jsonify
from data.data import fetch_upcoming_movies, process_movies_data

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def get_upcoming_movies():
    # Route de l'api qui renvoie les film
    movies = fetch_upcoming_movies()
    processed_movies = process_movies_data(movies)
    return jsonify(processed_movies)