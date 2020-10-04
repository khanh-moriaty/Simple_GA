import unittest
from random import seed

from creator.individual import Individual
from creator.selector import Selector


class TestSelector(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        population = [Individual('10101'), Individual('11000'), Individual('01111')]
        cls._selector = Selector(population)

    def test_fitness(self):
        self.assertEqual(3, self._selector._fitness('01101'))
        self.assertEqual(5, self._selector._fitness('11111'))
        self.assertEqual(1, self._selector._fitness('00001'))

    def test_select_random_individual(self):
        seed(1)
        random_individual = self._selector._select_random_individual()
        self.assertEqual(Individual('10101'), random_individual)

    def test_select_two_random_individuals(self):
        seed(1)
        first, second = self._selector._select_two_random_individuals()
        self.assertEqual(Individual('10101'), first)
        self.assertEqual(Individual('01111'), second)

    def test_select_parent(self):
        seed(1)
        expected_parent = Individual('01111')
        parent = self._selector._select_parent()
        self.assertEqual(expected_parent, parent)

    def test_select_parents(self):
        seed(1)
        first_parent, second_parent = self._selector.select_parents()
        expected_first_parent = Individual('01111')
        expected_second_parent = Individual('10101')
        self.assertEqual(expected_first_parent, first_parent)
        self.assertEqual(expected_second_parent, second_parent)

    def test_select_best_individual(self):
        seed(1)
        expected_best_individual = Individual('01111')
        best_individual = self._selector.select_best_individual()
        self.assertEqual(expected_best_individual, best_individual)

    def test_select_best_individuals(self):
        seed(1)
        expected_best_individuals = [Individual('10101'), Individual('01111')]
        best_individuals = self._selector.select_best_individuals(2)
        self.assertEqual(expected_best_individuals, best_individuals)

    def test_select_pairs_of_parents(self):
        seed(1)
        expected_pairs_of_parents = [(Individual('01111'), Individual('10101')),
                                     (Individual('10101'), Individual('11000')),
                                     (Individual('01111'), Individual('10101'))]
        pairs_of_parents = self._selector.select_pairs_of_parents(3)
        self.assertEqual(expected_pairs_of_parents, pairs_of_parents)


if __name__ == '__main__':
    unittest.main()
