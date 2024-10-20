from pricing import NEW_RELEASE, REGULAR, CHILDREN
from dataclasses import dataclass
from typing import Collection


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """

    title: str
    year: int
    genre: Collection[str]

    def is_genre(self, genre: str):
        return genre.lower() in [single_genre.lower() for single_genre in self.genre]
    
    def __str__(self):
        return f"{self.title} ({self.year})"
