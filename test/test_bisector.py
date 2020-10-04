import unittest
from random import seed

from bisector import Bisector


class TestBisector(unittest.TestCase):

    def test_find_minimum_population_size(self):
        seed(1)
        expected_minimum_population_size = 8
        minimum_population_size = Bisector.find_minimum_population_size(20)
        self.assertEqual(expected_minimum_population_size, minimum_population_size)

        expected_minimum_population_size = 14
        minimum_population_size = Bisector.find_minimum_population_size(50)
        self.assertEqual(expected_minimum_population_size, minimum_population_size)


if __name__ == '__main__':
    unittest.main()
