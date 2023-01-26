import pytest
from code_challenges.comparisons import sort_movies_by_year,sort_movies_by_title

def test_sort_movies_by_year(movies):
    actual = sort_movies_by_year(movies)
    expected = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]
    assert actual == expected

def test_sort_movie_by_title(movies):
    actual = sort_movies_by_title(movies)
    expected = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"]
    assert actual == expected


@pytest.fixture
def movies():
    movie_list = [
        {
            "title": "Beetlejuice",
            "year": 1988,
            "genres": ["Comedy", "Fantasy"],
        },
        {
            "title": "The Cotton Club",
            "year": 1984,
            "genres": ["Crime", "Drama", "Music"],
        },
        {
            "title": "The Shawshank Redemption",
            "year": 1994,
            "genres": ["Crime", "Drama"],
        },
        {
            "title": "Crocodile Dundee",
            "year": 1986,

            "genres": ["Adventure", "Comedy"],
        },
        {
            "title": "Valkyrie",
            "year": 2008,
            "genres": ["Drama", "History", "Thriller"],
        },
        {
            "title": "Ratatouille",
            "year": 2007,
            "genres": ["Animation", "Comedy", "Family"],
        },
        {
            "title": "City of God",
            "year": 2002,

            "genres": ["Crime", "Drama"],
        },
        {
            "title": "Memento",
            "year": 2000,

            "genres": ["Mystery", "Thriller"],
        },
        {
            "title": "The Intouchables",
            "year": 2011,

            "genres": ["Biography", "Comedy", "Drama"],
        },
        {
            "title": "Stardust",
            "year": 2007,
            "genres": ["Adventure", "Family", "Fantasy"],
        },
    ]
    return movie_list
