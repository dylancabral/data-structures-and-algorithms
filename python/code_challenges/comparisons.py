from typing import List


def sort_movies_by_year(movies):
    sorted_movies = sorted(movies, key=lambda x: (x['year'], x['title']), reverse=True)
    return [movie['title'] for movie in sorted_movies]

def sort_movies_by_title(movies: List[dict]):
    def get_sort_key(movie):
        title = movie['title']
        if title.startswith(('A','An','The')):
            # split the title into words, get the second word and return it
            return title.split()[1]
        else:
            # split the title into words, get the first word and return it
            return title.split()[0]

    # use the sorted function and pass the get_sort_key function as the key
    sorted_movies = sorted(movies, key=get_sort_key)
    # create a list of movie titles
    movie_titles = [movie['title'] for movie in sorted_movies]
    return movie_titles

# def sort_movies_by_title(movies: List[dict]):
#   return [movie['title'] for movie in sorted(movies, key=lambda x: x['title'].split()[1] if x['title'].startswith(('A','An','The')) else x['title'].split()[0])]



