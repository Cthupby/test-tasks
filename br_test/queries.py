from base import Session
from client_movie import Client, Movie


# Create a new session
session = Session()

# extract all movies
movies = session.query(Movie).all()

# 2 - print movies' details
print('\n### All movies:')
for movie in movies:
    print(f'{movie.title} was released on {movie.year} in {movie.genre} genre')
print('')
