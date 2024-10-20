import unittest
from rental import Rental
from movie import Movie
from pricing import NEW_RELEASE, REGULAR, CHILDREN


class RentalTest(unittest.TestCase):
    def setUp(self):
        self.new_movie = Movie("Dune: Part Two", 2023, ["Action", "Sci-Fi"])
        self.regular_movie = Movie("Air", 2023, ["Drama"])
        self.childrens_movie = Movie("Frozen", 2013, ["Animation", "Family"])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("Air", 2023, ["Drama"])
        self.assertEqual("Air", m.title)
        self.assertEqual(2023, m.year)
        self.assertIn("Drama", m.genre)

    def test_rental_price(self):
        rental = Rental(self.regular_movie, 2, REGULAR)
        self.assertEqual(rental.get_price(), 2.0)
        rental = Rental(self.regular_movie, 3, REGULAR)
        self.assertEqual(rental.get_price(), 3.5)
        rental2 = Rental(self.new_movie, 1, NEW_RELEASE)
        self.assertEqual(rental2.get_price(), 3.0)
        rental2 = Rental(self.new_movie, 5, NEW_RELEASE)
        self.assertEqual(rental2.get_price(), 15.0)
        rental3 = Rental(self.childrens_movie, 3, CHILDREN)
        self.assertEqual(rental3.get_price(), 1.5)
        rental3 = Rental(self.childrens_movie, 4, CHILDREN)
        self.assertEqual(rental3.get_price(), 3.0)

    def test_rental_points(self):
        rental = Rental(self.new_movie, 3, NEW_RELEASE)
        self.assertEqual(rental.rental_points(), 3)
        rental2 = Rental(self.regular_movie, 3, REGULAR)
        self.assertEqual(rental2.rental_points(), 1)
