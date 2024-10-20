import unittest
from datetime import datetime
from movie import Movie
from rental import Rental
from pricing import NEW_RELEASE, REGULAR, CHILDREN


class PricingTest(unittest.TestCase):
    """Tests for Rental.price_code_for_movie."""

    def test_new_release(self):
        """Verify that a movie released in the current year is classified as a new release."""
        current_year = datetime.now().year
        movie = Movie("Challengers", current_year, ["Comedy", "Drama", "Romance"])
        self.assertEqual(Rental.price_code_for_movie(movie), NEW_RELEASE)

    def test_regular_movie(self):
        """Check that a movie with no 'Children' genre and not released this year is
        classified with a REGULAR price code."""
        movie = Movie("Spider Man: No Way Home", 2020, ["Action", "Adventure", "Fantasy"])
        self.assertEqual(Rental.price_code_for_movie(movie), REGULAR)

    def test_children_genre(self):
        """Ensure that a movie with the 'Children' genre is categorized with a CHILDREN price code."""
        movie = Movie("Turning Red", 2022, ["Animation", "Adventure", "Children", "Comedy"])
        self.assertEqual(Rental.price_code_for_movie(movie), CHILDREN)
