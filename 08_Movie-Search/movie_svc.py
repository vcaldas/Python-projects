import requests
import collections

MovieResult = collections.namedtuple('MovieResult',
                                     'imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres')


def find_movies(search_text):
    url = 'http://movie_service.talkpython.fm/api/search/{}'.format (search_text)

    if not search_text or not search_text.strip ():
        raise ValueError ("Search text is required")

    resp = requests.get(url)
    resp.raise_for_status()

    movie_data = resp.json()
    moves_list = movie_data.get('hits')

    movies = [
        MovieResult(**md)
        for md in moves_list
    ]

    movies.sort(key=lambda x: -x.year)

    return movies


