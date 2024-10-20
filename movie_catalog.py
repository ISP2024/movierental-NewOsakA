from typing import Optional
from movie import Movie

import csv


class MovieCatalog:
    """Singleton class responsible for managing and accessing movies."""
    _instance = None

    def __new__(cls, filename='movies.csv'):
        if not cls._instance:
            cls._instance = super(MovieCatalog, cls).__new__(cls)
            cls._instance._movies = []
            cls._instance.load_movies(filename)
        return cls._instance

    def load_movies(self, filename: str):
        """Fetches movie records from a CSV file and converts them into Movie objects."""
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=',')
                try:
                    next(reader)
                except StopIteration:
                    print("Warning: CSV file is empty.")
                    return

                for row in reader:
                    try:
                        title, year, genres = row[1], int(row[2]), row[3].split('|')
                        self._movies.append(Movie(title=title, year=year, genre=genres))
                    except (IndexError, ValueError):
                        continue
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_movie(self, title: str, year: Optional[int] = None) -> Optional[Movie]:
        """Search for a movie by title, with an optional year filter."""
        # Return the first matching movie by title (case-insensitive).
        for movie in self._movies:
            if movie.title.lower() == title.lower() and (year is None or movie.year == year):
                return movie
        return None
